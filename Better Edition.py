from sense_hat import SenseHat
from random import randint
sense = SenseHat()
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
gray = (125, 125, 125)
brown = (150, 50, 0)
black = (0, 0, 0)
class Chunk:
  def __init__(self, x, y):
    self.position = [x, y]
    self.contents = [[],[],[],[],[],[],[],[]]
  
  def generate_chunk(self):
    level = 4 + randint(-2, 2)
    for x in range(0,8):
      for y in range(0,8):
        if y >= level:
          col = gray
        elif y > level - 2:
          col = brown
        elif y == level - 2:
          col = green
        else:
          col = black
        self.contents[y].append(col)

def create_chunk(chunks, direction):
  if direction == "r":
    new_chunk = Chunk(chunks[len(chunks)-1].position[0] + 1, 0)
    new_chunk.generate_chunk()
    chunks.append(new_chunk)
  else:
    new_chunk = Chunk(chunks[0].position[0] - 1, 0)
    new_chunk.generate_chunk()
    chunks.insert(0,new_chunk)
  return chunks

def create_check(chunks, pos):
  if chunks[len(chunks) - 1] == chunks[pos[0]]:
    d = "r"
    chunks = create_chunk(chunks, d)
  if chunks[0] == chunks[pos[0]]:
    d = "l"
    chunks = create_chunk(chunks, d)
  return chunks
    
def update_display():
  loaded_area = []
  for x in range(0, 8):
    loaded_row = []
    for y in range(0, 8):
      loaded_row.append(chunks[chunk_pos[0] - 1].contents[x][y])
    for y in range(0, 8):
      loaded_row.append(chunks[chunk_pos[0]].contents[x][y])
    for y in range(0, 8):
      loaded_row.append(chunks[chunk_pos[0] + 1].contents[x][y])
    loaded_area.append(loaded_row)
  display = []
  for x in range(0, 8):
    for y in range(0, 8):
      display.append(loaded_area[x][13+y])
  for x in range(0, 8):
    for y in range(0, 8):
      sense.set_pixels(display)
  
chunk1 = Chunk(0, 0)
chunks = [chunk1]
chunk1.generate_chunk()
chunk_pos = [0,0]
pos = [10, 10]
while True:
  create_check(chunks, chunk_pos)
  update_display()
  wasd = input()
  if wasd == "d" and chunk_pos[0] == 0:
    chunk_pos[0] += 2
  elif wasd == "d":
    chunk_pos[0] += 1
  elif wasd == "a":
    chunk_pos[0] -= 1
  if chunk_pos[0] == -1:
    chunk_pos[0] +=1
  print(chunk_pos)
  

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
    

chunk1 = Chunk(0, 0)
chunks = [chunk1]
chunk1.generate_chunk()
pos = [0,0]
while True:
  display = []
  for x in range(0, 8):
    for y in range(0, 8):
      display.append(chunks[pos[0]].contents[x][y])
  sense.set_pixels(display)
  create_check(chunks, pos)
  wasd = input()
  if wasd == "d":
    pos[0] += 1
  elif wasd == "a":
    pos[0] -= 1
  if pos[0] == -1:
    pos[0] +=1
  print(pos)
  

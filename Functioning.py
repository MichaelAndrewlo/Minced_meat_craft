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
  def __init__(self, x, y, level):
    self.position = [x, y]
    self.contents = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    self.s_level = level
    self.e_level = self.s_level
  
  def generate_chunk_right(self): 
    for x in range(0,16):
      if randint(0, 5) > 2:
        self.e_level += randint(-1, 1)
      for y in range(0,16):
        if y >= self.e_level:
          col = gray
        elif y > self.e_level - 3:
          col = brown
        elif y == self.e_level - 3:
          col = green
        else:
          col = black
        self.contents[y].append(col)

  def generate_chunk_left(self): 
    for x in range(0, 16):
      if randint(0, 5) > 2:
        self.e_level += randint(-1, 1)
      for y in range(0,16):
        if y >= self.e_level:
          col = gray
        elif y > self.e_level - 3:
          col = brown
        elif y == self.e_level - 3:
          col = green
        else:
          col = black
        self.contents[y].insert(0, col)

class Player:
  def __init__(self, x, y):
    self.pos = [x, y]
    self.chunk_pos = [0, 0]
  
  def move(self): 
    wasd = input()
    if wasd == "d":
      self.pos[0] += 1
    elif wasd == "a":
      self.pos[0] -= 1
    elif wasd == "w":
      self.pos[1] -= 1
    elif wasd == "s":
      self.pos[1] += 1
    if self.pos[0] == 40:
      self.chunk_pos[0] += 1
      self.pos[0] = 24
    if self.pos[0] == 7:
      self.chunk_pos[0] -= 1
      self.pos[0] = 24

def create_chunk(chunks, direction): 
  if direction == "r":
    new_chunk = Chunk(chunks[len(chunks)-1].position[0] + 1, 0, chunks[len(chunks)-1].e_level )
    new_chunk.generate_chunk_right()
    chunks.append(new_chunk)
  else:
    new_chunk = Chunk(chunks[0].position[0] - 1, 0, chunks[0].e_level)
    new_chunk.generate_chunk_left()
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
  for x in range(0, 16):
    loaded_row = []
    for y in range(0, 16):
      loaded_row.append(chunks[player1.chunk_pos[0] - 1].contents[x][y])
    for y in range(0, 16):
      loaded_row.append(chunks[player1.chunk_pos[0]].contents[x][y])
    for y in range(0, 16):
      loaded_row.append(chunks[player1.chunk_pos[0] + 1].contents[x][y])
    loaded_area.append(loaded_row)
  display = []
  for x in range(0, 8):
    for y in range(0, 8):
      display.append(loaded_area[player1.pos[1] + x][player1.pos[0] + y])
  sense.set_pixels(display)
  
chunk1 = Chunk(0, 0, 9)
chunks = [chunk1]
chunk1.generate_chunk_right()
player1 = Player(16, 0)
while True:
  create_check(chunks, player1.chunk_pos)
  if player1.chunk_pos[0] == 0:
    player1.chunk_pos[0] += 1
  update_display()
  player1.move()
  if player1.chunk_pos[0] == -1:
    player1.chunk_pos[0] += 1

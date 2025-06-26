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
    self.level = level
  
  def generate_chunk_right(self): 
    for x in range(0,16):
      if randint(0, 5) == 5 + (self.level - 9):
        self.level += 1
      elif randint(0, 5) == 5 - (self.level - 9):
        self.level -= 1
      for y in range(0,16):
        if y >= self.level:
          col = gray
        elif y > self.level - 3:
          col = brown
        elif y == self.level - 3:
          col = green
        else:
          col = black
        self.contents[y].append(col)

  def generate_chunk_left(self): 
    for x in range(0, 16):
      if randint(0, 5) == 5 + (self.level - 9):
        self.level += 1
      elif randint(0, 5) == 5 - (self.level - 9):
        self.level -= 1
      for y in range(0,16):
        if y >= self.level:
          col = gray
        elif y > self.level - 3:
          col = brown
        elif y == self.level - 3:
          col = green
        else:
          col = black
        self.contents[y].insert(0, col)


class Player:
  def __init__(self, x, y):
    self.pos = [x, y]
    self.chunk_pos = [0, 0]
  
  def move(self): 
    for event in sense.stick.get_events():
      if event.action == "pressed":
        if event.direction == "right":
          self.pos[0] += 1
        elif event.direction == "left":
          self.pos[0] -= 1
        elif event.direction == "up":
          self.pos[1] -= 1
        elif event.direction == "down":
          self.pos[1] += 1
    if self.pos[0] == 40:
      self.chunk_pos[0] += 1
      self.pos[0] = 24
    if self.pos[0] == 7:
      self.chunk_pos[0] -= 1
      self.pos[0] = 24

def get_dist(x1, y1, x2, y2):
  x_change = x1 - x2
  y_change = y1 - y2
  x_sqr = x_change ** 2
  y_sqr = y_change ** 2
  dist = (x_sqr + y_sqr) ** (1/2)
  return dist


def create_chunk(chunks, direction): 
  if direction == "r":
    new_chunk = Chunk(chunks[len(chunks)-1].position[0] + 1, 0, chunks[len(chunks)-1].level )
    new_chunk.generate_chunk_right()
    chunks.append(new_chunk)
  else:
    new_chunk = Chunk(chunks[0].position[0] - 1, 0, chunks[0].level)
    new_chunk.generate_chunk_left()
    chunks.insert(0,new_chunk)
  return chunks

def create_check(chunks, pos): 
  if chunks[len(chunks) - 1] == chunks[player1.chunk_pos[0]]:
    d = "r"
    chunks = create_chunk(chunks, d)
  if chunks[0] == chunks[player1.chunk_pos[0]]:
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

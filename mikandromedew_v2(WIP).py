from random import randint
from sense_hat import SenseHat
sense = SenseHat()
white = (255,255,255)
black = (0,0,0)
green = (0, 255, 0)
gray = (125, 125, 125)
baige = (255, 255, 125)
red_brown = (125, 25, 0)
display = []
class Chunk:
  def __init__(self, x, y, level):
    self.position = [x, y]
    self.contents = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    self.biome = "no"
    self.start_level = level
    
  def generate_chunk(self):
    for i in range(0,16):
      for z in range(0,16):
        if i > self.start_level:
          add = gray
        elif i > self.start_level - 2:
          add = red_brown
        elif i == self.start_level - 2 :
           add = green 
        elif i < self.start_level - 2:
          add = black
        self.contents[i].append(add)

class Player:
  def __init__(self, x, y, chunk_x, chunk_y):
    self.position = [x, y]
    self.chunk_pos = [chunk_x, chunk_y]
    
  def move(self, direction):
    if direction == "d":
        self.position[0] += 1
    elif direction == "a":
        self.position[0] -= 1
    elif direction == "w":
        self.position[1] -= 1
    elif direction == "s":
        self.position[1] += 1
  
def create_chunk(chunk_pos, chunks):
  level = 7 + randint(-4, 4)
  new_chunk = Chunk(chunk_pos[0], chunk_pos[1], level)
  new_chunk.generate_chunk()
  chunks.append(new_chunk)
    
  return chunks

def create_check(player1, chunks):
  for y in range(-1, 2):
      for x in range(-1,2):
        existing = []
      
        chunk_pos = []
        direction = ""
        chunk_pos.append(x + player1.chunk_pos[0])
        chunk_pos.append(y + player1.chunk_pos[1])
        if chunk_pos[1] == -1:
          pass
        else:
          for chunk in chunks:
            if chunk.position == chunk_pos:
              existing.append("T")
              break
            else:
              existing.append("F")
        if "F" in existing:
          chunks = create_chunk(chunk_pos, chunks)

def update_display():
  display = []
  pos = player1.position
  chunk_pos = player1.chunk_pos
  for t in range(-3,5):
    for z in range(-3,5):
      if pos[1]+t < 0:
        think = True
      
      display.append(chunks[0].contents[pos[1]+t][pos[0]+z])
  print(player1.position)
  sense.set_pixels(display)
  sense.set_pixel(4, 4, (255, 255, 255))
  return player1
      
  
chunks = []
player1 = Player(4, 4, 0, 0)
chunks = create_chunk([0,0], chunks)
while True:
    create_check(player1, chunks)
    player1 = update_display()
    direction = input()
    player1.move(direction)

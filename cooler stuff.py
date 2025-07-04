from sense_hat import SenseHat
from random import randint
from random import choice
sense = SenseHat()
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
gray = (125, 125, 125)
brown = (150, 50, 0)
black = (0, 0, 0)
yellow = (255, 255, 0)
dark_gray = (50, 50, 50)
dark_blue = (50, 100, 200)
dark_yellow = (125, 125, 0)
light_blue = (175, 175, 255)
biomes = {
0: {"avg_level" : 16, "colours": [brown, green], "change" : 1, "chance" : 5, "levels" : [3, 3]},
1: {"avg_level" : 17, "colours": [dark_yellow, yellow], "change" : 1, "chance" : 5, "levels" : [3, 3]},
2: {"avg_level" : 8, "colours": [gray, white], "change" : 2, "chance" : 3, "levels" : [3, 4]},
"mountain_end": {"avg_level" : 16, "colours": [gray, white], "change" : 2, "chance" : 3, "levels" : [3, 4]},
3: {"avg_level" : 26, "colours": [dark_yellow, blue], "change" : 2 , "chance" : 4, "levels" : [3, 7]},
"shore" : {"avg_level" : 17, "colours": [dark_yellow, blue], "change" : 2 , "chance" : 4, "levels" : [3, 7]}
}
class Chunk:
  def __init__(self, x, y, level, biome):
    self.position = [x, y]
    self.contents = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[], [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    self.level = level
    self.biome = biome
  
  def generate_chunk_right(self, d): 
    for x in range(0, 32):
      if randint(0, 5) >= self.biome["chance"] + (self.level - self.biome["avg_level"]):
        self.level += randint(1, self.biome["change"])
      elif randint(0, 5) >= self.biome["chance"] - (self.level - self.biome["avg_level"]):
        self.level -= randint(1, self.biome["change"])
      for y in range(0, 32):
        col = black
        if self.biome == biomes[3] or self.biome == biomes["shore"]:
          if y >= 14:
            col = self.biome["colours"][1]
        elif y >= self.level - self.biome["levels"][1]:
          col = self.biome["colours"][1]
        if y > self.level - self.biome["levels"][0]:
          col = self.biome["colours"][0]
        if y >= self.level:
          col = gray
        if y == len(self.contents) - 1:
          col = dark_gray
        if d == "l":
          self.contents[y].insert(0, col)
        else:
          self.contents[y].append(col)

  def generate_chunk_left(self): 
    for x in range(0, 32):
      if randint(0, 5) >= self.biome["chance"] + (self.level - self.biome["avg_level"]):
        self.level += randint(1, self.biome["change"])
      elif randint(0, 5) >= self.biome["chance"] - (self.level - self.biome["avg_level"]):
        self.level -= randint(1, self.biome["change"])
      for y in range(0,32):
        col = black
        if self.biome == biomes[3]:
          if y >= 14:
            col = self.biome["colours"][1]
        elif y >= self.level - self.biome["levels"][1]:
          col = self.biome["colours"][1]
        if y > self.level - self.biome["levels"][0]:
          col = self.biome["colours"][0]
        if y >= self.level:
          col = gray
        if y == len(self.contents) - 1:
          col = dark_gray
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
    if self.pos[0] == 64:
      self.chunk_pos[0] += 1
      self.pos[0] = 32
    if self.pos[0] == 24:
      self.chunk_pos[0] -= 1
      self.pos[0] = 56

def get_dist(x1, y1, x2, y2):
  x_change = x1 - x2
  y_change = y1 - y2
  x_sqr = x_change ** 2
  y_sqr = y_change ** 2
  dist = (x_sqr + y_sqr) ** (1/2)
  return dist


def create_chunk(chunks, direction): 
  choice = randint(0,3)
  if direction == "r":
    if chunks[len(chunks)-1].biome == biomes[2]:
      choice = "mountain_end"
    new_chunk = Chunk(chunks[len(chunks)-1].position[0] + 1, 0, chunks[len(chunks)-1].level, biomes[choice])
    new_chunk.generate_chunk_right()
    chunks.append(new_chunk)
  else:
    if chunks[0].biome == biomes[2] and choice != 2:
      choice = "mountain_end"
    new_chunk = Chunk(chunks[0].position[0] - 1, 0, chunks[0].level, biomes[choice])
    new_chunk.generate_chunk_left()
    chunks.insert(0,new_chunk)
  return chunks

def create_check(chunks, pos): 
  choice = randint(0,3)
  if chunks[len(chunks) - 1] == chunks[player1.chunk_pos[0]]:
    d = "r"
    if chunks[len(chunks)-1].biome == biomes[2] and choice != biomes[2]:
      choice = "mountain_end"
    elif chunks[len(chunks)-1].biome == biomes[3]:
      choice = "shore"
    new_chunk = Chunk(chunks[len(chunks)-1].position[0] + 1, 0, chunks[len(chunks)-1].level, biomes[choice])
    new_chunk.generate_chunk_right(d)
    chunks.append(new_chunk)
  if chunks[0] == chunks[player1.chunk_pos[0]]:
    d = "l"
    if chunks[0].biome == biomes[2] and choice != biomes[2]:
      choice = "mountain_end"
    elif chunks[0].biome == biomes[3]:
      choice = "shore"
    new_chunk = Chunk(chunks[0].position[0] - 1, 0, chunks[0].level, biomes[choice])
    new_chunk.generate_chunk_right(d)
    chunks.insert(0,new_chunk)
  return chunks
    
def update_display(): 
  loaded_area = []
  for x in range(0, 32):
    loaded_row = []
    for y in range(0, 32):
      loaded_row.append(chunks[player1.chunk_pos[0] - 1].contents[x][y])
    for y in range(0, 32):
      loaded_row.append(chunks[player1.chunk_pos[0]].contents[x][y])
    for y in range(0, 32):
      loaded_row.append(chunks[player1.chunk_pos[0] + 1].contents[x][y])
    loaded_area.append(loaded_row)
  display = []
  for x in range(0, 8):
    for y in range(0, 8):
      display.append(loaded_area[player1.pos[1] + x][player1.pos[0] + y])
  sense.set_pixels(display)
  
chunk1 = Chunk(0, 0, 16, biomes[0])
chunks = [chunk1]
chunk1.generate_chunk_right("r")
player1 = Player(32, 8)
while True:
  create_check(chunks, player1.chunk_pos)
  if player1.chunk_pos[0] == 0:
    player1.chunk_pos[0] += 1
  update_display()
  player1.move()
  if player1.chunk_pos[0] == -1:
    player1.chunk_pos[0] += 1

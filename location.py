from myjson import MyJson
from door import Door
from konsola import Konsola
from square import Square
from mob import Mob
from hero import Hero
class Location:
  def __init__(self, filePath):
      self.name = "Nigdzie"
      self.x = 0
      self.y = 0
      self.size_x = 1
      self.size_y = 1
      self.size_z = 1
      self.ground_level = 0
      self.s = None
      self.doors = []
      self.items = []
      self.mobs = []

      data = MyJson.read_json(filePath)
      self.name = data['name']
      self.x = data['x']
      self.y = data['y']
      self.size_x = data['size_x']
      self.size_y = data['size_y']
      self.size_z = data['size_z']
      self.ground_level = data['ground_level']
      square_list = data['square']
      door_list = data['door']
      item_list = data['items']
      mob_list = data['mobs']
      
      self.add_squares(square_list)

      self.add_doors(door_list)
      self.add_doors_to_squares()

      self.add_items(item_list)
      self.add_mobs(mob_list)

      

      
  def add_squares(self, square_list):
    self.s = [[[Square(i, j, k, 5, "Pustka", "Nic tu nie ma", [], n=1,ne=1,e=1,se=1,s=1,sw=1,w=1,nw=1,u=1,d=1) for k in range(self.size_z)] for j in range(self.size_y)] for i in range(self.size_x)]
    for s in range(len(square_list)):
      x = square_list[s]["coord"]["x"]
      y = square_list[s]["coord"]["y"]
      z = square_list[s]["coord"]["z"]
      self.s[x][y][z] = Square(x, y, z, square_list[s]["surface"], square_list[s]["name"], square_list[s]["description"], square_list[s]["items"],
                  n=bool(square_list[s]["exit"][0]), ne=bool(square_list[s]["exit"][1]), 
                  e=bool(square_list[s]["exit"][2]), se=bool(square_list[s]["exit"][3]), 
                  s=bool(square_list[s]["exit"][4]), sw=bool(square_list[s]["exit"][5]), 
                  w=bool(square_list[s]["exit"][6]), nw=bool(square_list[s]["exit"][7]), 
                  u=bool(square_list[s]["exit"][8]), d=bool(square_list[s]["exit"][9]))

  def add_doors(self, door_list):
    for d in door_list:
      newDoor = Door(d['id'], d['coord']['x'], d['coord']['y'], d['coord']['z'], d['direction'], d['key'], bool(d['open']))
      self.doors.append(newDoor)
  
  def add_doors_to_squares(self):
    for d in self.doors:
      x = d.x
      y = d.y
      z = d.z
      # print(f"{x} + {y} + {z} - {d.direction} ({d.open})")
      if d.direction == 8:
        self.s[x][y][z].door_n = d
        self.s[x][y-1][z].door_s = d
      elif d.direction == 4:
        self.s[x][y][z].door_w = d
        self.s[x-1][y][z].door_e = d
      elif d.direction == 0:
        self.s[x][y][z].door_d = d
        self.s[x][y][z-1].door_u = d
      
  def add_items(self, item_list):
    pass


  def add_mobs(self, mob_list):
    for m in mob_list:
      keywords = m["keywords"]
      if m['id'] == 0:
          newMob = Hero(m['id'], m['x'], m['y'], m['z'], m['name'], m['alias'], m['description'], m['species'], m['lift'], m['equip'], **keywords)
      else:
        newMob = Mob(m['id'], m['x'], m['y'], m['z'], m['name'], m['alias'], m['description'], m['species'], m['lift'], m['equip'], **keywords)
      newMob.current_location = self
      self.mobs.append(newMob)



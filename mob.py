
class Mob:
  id = 0
  @classmethod
  def increment_ID(cls):
    cls.id += 1 
    return cls.id
  def __init__(self, mobId, xx, yy, zz, n, a, d, sp, lft, itId, **kwargs):
    if mobId == -1:
      self.id=Mob.increment_ID()
    else:
      Mob.increment_ID()
      self.id = mobId
    self.current_location = None
    self.x = xx
    self.y = yy
    self.z = zz
    self.name = n
    self.dead_body = "Zwłoki " + self.name
    self.alias = a
    self.description = d
    self.species = sp
    self.param = {
      "hp" : kwargs.get("hp", 50),
      "hp_max" : kwargs.get("hp_max", 5),
      "stamina" : kwargs.get("st", 100),
      "stamina_aviable" : kwargs.get("st_av", 100),
      "stamina_max" : kwargs.get("st_max", 100),
      "mana" : kwargs.get("mn", 0),
      "mana_max" : kwargs.get("mn_max", 0),
      "nourish" : kwargs.get("nou", 50),
      "nourish_max" : kwargs.get("nou_max", 50),
    }
    self.stat = {
      "strength" : kwargs.get("str", 5),
      "dexterity" : kwargs.get("dxt", 5),
      "speed" : kwargs.get("spd", 5),
      "defence" : kwargs.get("dfc", 5),
      "perceptivity" : kwargs.get("per", 5),
      "visibility" : kwargs.get("vis", 5)
    }
    self.weapons = {
      "sword" : kwargs.get("sword", 5),
      "axe" : kwargs.get("axe", 5),
      "spear" : kwargs.get("spear", 5),
      "cudgel" : kwargs.get("cudgel", 5),
      "bow" : kwargs.get("bow", 2)
    }
    self.defence = {
      "cut" : kwargs.get("dfc_cut", self.stat["defence"]),
      "stab" : kwargs.get("dfc_stab", self.stat["defence"]),
      "crush" : kwargs.get("dfc_crush", self.stat["defence"]),
      "fire" : kwargs.get("dfc_fire", self.stat["defence"]),
      "ice" : kwargs.get("dfc_ice", self.stat["defence"]),
      "magic" : kwargs.get("dfc_magic", 0)
    }
    self.bodyPart = {
      "right_hand" : None,
      "left_hand" : None,
      "head" : None,
      "torso1" : None,
      "torso2" : None,
      "hands" : None,
      "legs" : None,
      "boots" : None,
      "finger1" : None,
      "finger2" : None,
      "neck" : None
    }
    self.active_bonus = []
    self.lift = lft
    self.item_ids = []
    self.item_ids = itId
    self.equip = []
    self.fainted = False
    self.dead = False

  def whereami(self):
    print("{} - X: {} Y: {} Z: {}".format(self.name, self.x, self.y, self.z))
    print(self.current_location.name)
    
  def whoami(self):
    print(self.name)
    print(self.description)
    print(self.species)
  
  def travel(self, direction):
    if self.current_location.s[self.x][self.y][self.z].check_exit(direction):
      self.move(direction)
      #self.weaking(0.1, -0.05)
      return True
  def move(self, direction):
    match direction:
      case 0:
        self.z-=1
      case 1:
        self.y+=1
        self.x-=1
      case 2:
        self.y+=1
      case 3:
        self.y+=1
        self.x+=1
      case 4:
        self.x-=1
      case 5:
        self.z+=1
      case 6:
        self.x+=1
      case 7:
        self.y-=1
        self.x-=1
      case 8:
        self.y-=1
      case 9:
        self.y-=1
        self.x+=1

    
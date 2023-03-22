from konsola import Konsola

class Square:
	def __init__(self, x, y, z, surf, name, desc, ids, **kwargs):
		self.x = x
		self.y = y
		self.z = z
		self.surface = surf
		#self.surfColor = self.surfColor(self.surface)
		self.name = name
		self.description = desc
		self.north = kwargs['n']
		self.northeast = kwargs['ne']
		self.east = kwargs['e']
		self.southeast = kwargs['se'] 
		self.south = kwargs['s']
		self.southwest = kwargs['sw']
		self.west = kwargs['w']
		self.northwest = kwargs['nw']
		self.up = kwargs['u']
		self.down = kwargs['d']
		self.door_n = None
		self.door_e = None
		self.door_s = None
		self.door_w = None
		self.door_u = None
		self.door_d = None
		self.item_ids = []
		self.item_ids = ids
		self.items = []

	def check_exit(self, direction):
		exits = {
			0: self.down,
			1: self.southwest,
			2: self.south,
			3: self.southeast,
			4: self.west,
			5: self.up,
			6: self.east,
			7: self.northwest,
			8: self.north,
			9: self.northeast
		}
		
		doors = self.set_doors_list()
			
		if direction in exits: 
			if exits[direction] == False:
				print("Nie da się tam przejść")
			elif exits[direction] and doors[direction] == False:
				komunikat = ["Drzwi nie dają się otworzyć", "Drzwi ani drgną", "Drzwi są zamknięte"]
				Konsola.printRandom(komunikat)
			return exits[direction]*doors[direction] #zwraca true w przypadku gdy oba są true, w pozostałych zwraca false
		else: 
			print("Nie da się tam przejść")
			return False
	
	def set_doors_list(self):
		doors = {
			0: True,
			1: True,
			2: True,
			3: True,
			4: True,
			5: True,
			6: True,
			7: True,
			8: True,
			9: True
		}
		try: doors[0] = self.door_d.open
		except: pass
		try: doors[2] = self.door_s.open
		except: pass
		try: doors[4] = self.door_w.open
		except: pass
		try: doors[5] = self.door_u.open
		except: pass
		try: doors[6] = self.door_e.open
		except: pass
		try: doors[8] = self.door_n.open
		except: pass

		return doors

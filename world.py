from location import Location
from konsola import Konsola

class World:
	def __init__(self, maps):
		self.x = 0
		self.y = 0
		self.location = []
		self.size_x= 1
		self.size_y = 1
		self.size_z = 1
		self.ground_level = 0
		self.s = []
		for i in range(len(maps)):
			temp_location = Location(maps[i])
			self.location.append(temp_location)
		
		self.set_world_size()
		self.populate_global_squares()

	def set_world_size(self):
		for loc in self.location:
			if (loc.x + loc.size_x) > self.size_x:
				self.size_x= loc.x + loc.size_x
			if (loc.y + loc.size_y) > self.size_y:
				self.size_y = loc.y + loc.size_y
			if (self.size_z + loc.size_z - loc.ground_level - 1) > self.size_z:
				self.size_z = self.size_z + loc.size_z - loc.ground_level - 1 #kiedy nowa kratka wystaje w górę
			if loc.ground_level > self.ground_level:
				self.size_z += loc.ground_level - self.ground_level #kiedy nowa kratka wystaje w dół
				self.ground_level = loc.ground_level

	def populate_global_squares(self):
		self.s = [[[5 for k in range(self.size_z)] for j in range(self.size_y)] for i in range(self.size_x)]
		
		for loc in self.location:
			for x in range(loc.size_x):
				for y in range(loc.size_y):
					for z in range(loc.size_z):
						self.s[loc.x + x][loc.y + y][self.ground_level - loc.ground_level + z] = loc.s[x][y][z]

	def show_square(self, hero):
		hero_x = hero.x + hero.current_location.x
		hero_y = hero.y + hero.current_location.y
		hero_z = hero.z + (self.ground_level - hero.current_location.ground_level)
		s = self.s[hero_x][hero_y][hero_z]

		Konsola.print(s.name, "lyellow")
		Konsola.wrap(s.description, "lwhite")
		Konsola.compas(self, hero_x, hero_y, hero_z)
		for i in s.items:
			Konsola.print(i.name, "lcyan")
		
		for m in hero.current_location.mobs:
			if m.x == hero.x and m.y == hero.y and m.z == hero.z and m.id != 0:
				print("  ", end="")
				Konsola.print(m.name, "lmagenta")
	
	def move_mob_in_direction(self, mob, direction):
		did_move = False
		if direction in (7,8,9) and mob.y == 0:
			did_move = self.move_to_location(mob, direction)
		elif direction in (7,4,1) and mob.x == 0:
			did_move = self.move_to_location(mob, direction)
		elif direction in (9,6,3) and mob.x == mob.current_location.size_x-1:
			did_move = self.move_to_location(mob, direction)
		elif direction in (1,2,3) and mob.y == mob.current_location.size_y-1:
			did_move = self.move_to_location(mob, direction)
		else:
			did_move = mob.travel(direction)
		
		return did_move
	
	def move_to_location(self, mob, direction):
		if mob.current_location.s[mob.x][mob.y][mob.z].check_exit(direction):
			mobX = mob.x + mob.current_location.x
			mobY = mob.y + mob.current_location.y
			mobZ = mob.z + (self.world.ground_level - mob.current_location.ground_level)

			match direction:
				case 8:
					for loc in self.world.location:
					#sprawdzam, czy obecnie(!) hero znajduje się dokładnie jedną kratkę na południe od lokacji
						if loc.y + loc.size_y == mobY and loc.x <= mobX <= loc.x+loc.size_x: 
							mob.x = mobX - loc.x
							mob.y = mobY - loc.y - 1
							mob.z = mobZ - (self.world.ground_level - loc.ground_level)
							mob.current_location = loc
							return True
				case 6:
					for loc in self.world.location:
						if loc.x - 1 == mobX and loc.y <= mobY <= loc.y+loc.size_y:
							mob.x = 0
							mob.y = mobY - loc.y 
							mob.z = mobZ - (self.world.ground_level - loc.ground_level)
							mob.current_location = loc
							return True
				case 2:
					for loc in self.world.location:
						if loc.y - 1 == mobY and loc.x <= mobX <= loc.x+loc.size_x:
							mob.x = mobX - loc.x
							mob.y = 0
							mob.z = mobZ - (self.world.ground_level - loc.ground_level)
							mob.current_location = loc
							return True
				case 4:
					for loc in self.world.location:
						if loc.x + loc.size_x == mobX and loc.y <= mobY <= loc.y+loc.size_y:
							mob.x = mobX - loc.x -1
							mob.y = mobY - loc.y 
							mob.z = mobZ - (self.world.ground_level - loc.ground_level)
							mob.current_location = loc
							return True
				case 9:
					for loc in self.world.location:
						#spr, czy hero.x + 1 i hero y - 1 jest na obszarze lokacji
						if loc.y <= mobY - 1 <= loc.y + loc.size_y - 1 and loc.x <= mobX + 1 <= loc.x + loc.size_x -1:
							mob.x = mobX - loc.x + 1
							mob.y = mobY - loc.y - 1
							mob.z = mobZ - (self.world.ground_level - loc.ground_level)
							mob.current_location = loc
							return True
				case 3:
					for loc in self.world.location:
						#spr, czy hero.x + 1 i hero y + 1 jest na obszarze lokacji
						if loc.y <= mobY + 1 <= loc.y + loc.size_y - 1 and loc.x <= mobX + 1 <= loc.x + loc.size_x -1:
							mob.x = mobX - loc.x + 1
							mob.y = mobY - loc.y + 1
							mob.z = mobZ - (self.world.ground_level - loc.ground_level)
							mob.current_location = loc
							return True
				case 1:
					for loc in self.world.location:
						#spr, czy hero.x - 1 i hero y + 1 jest na obszarze lokacji
						if loc.y <= mobY + 1 <= loc.y + loc.size_y - 1 and loc.x <= mobX - 1 <= loc.x + loc.size_x -1:
							mob.x = mobX - loc.x - 1
							mob.y = mobY - loc.y + 1
							mob.z = mobZ - (self.world.ground_level - loc.ground_level)
							mob.current_location = loc
							return True
				case 7:
					for loc in self.world.location:
						#spr, czy hero.x - 1 i hero y - 1 jest na obszarze lokacji
						if loc.y <= mobY - 1 <= loc.y + loc.size_y - 1 and loc.x <= mobX - 1 <= loc.x + loc.size_x -1:
							mob.x = mobX - loc.x - 1
							mob.y = mobY - loc.y - 1
							mob.z = mobZ - (self.world.ground_level - loc.ground_level)
							mob.current_location = loc
							return True
		return False
	

from konsola import Konsola
from world import World
from myjson import MyJson

class Game:
	def __init__(self):
		self.gameplay_number = 0
		self.god_mode = True
		self.world = None
		self.hero = None
		self.is_playing = False
		self.time_in_sec = 0
	
	def choose_game(self):
		Konsola.landing()
		while True:
			choice = input()
			match choice:
				case "1":
					self.new_game()
					break
				case "2":
					if self.load_save():
						break
				case "3":
					if self.tutorial():
						break
				case "4":
					self.arena()
					break
				case "5":
					self.end_game()
				case _:
					Konsola.print("Wprowadź poprawny wybór", "red", "green")
	
	def new_game(self):
		maps = ["initial/tantar.json", "initial/czarny_las.json"]
		self.game_setter(maps, "Nowa gra", 0)

		saves = self.open_saves()
		try:
			self.gameplay_numer = saves[-1]["save_number"]+1
		except IndexError:
			self.gameplay_numer = 0
	
	def load_save():
		Konsola.print("Section in development", "red", "green")
		return False
	
	def tutorial():
		Konsola.print("Section in development", "red", "green")
		return False

	def arena(self):
		self.game_setter(['arena/arena.json'], "Arena reningowa", 0)
		
	
	def game_setter(self, maps, message, time):
		Konsola.clear()
		Konsola.print(message, "lwhite")
		Konsola.hr()
		self.world = World(maps)
		self.hero = self.world.location[0].mobs[0]
		self.world.show_square(self.hero)
		self.time_in_sec = time
		self.is_playing = True
	
	def endGame(self):
		self.is_playing = False
		Konsola.print("Czy na pewno chcesz wyjść? Upewnij się, że zapisałeś grę (Y/N)", "lyellow", "red")
		#is_it_ok = input()
		is_it_ok = "Y"
		if is_it_ok in ("Y", "y"):
			exit()
	
	def open_saves(self):
		savesPath = "save/saves.json"
		saves = []
		data = MyJson.read_json(savesPath)
		for i in data:
			nrSave = i['save_number']
			locName = i['loc_name']
			time = i['time']
			hero = i['hero']
			locPaths = i['loc_paths']
			save = {"save_number" : nrSave, "loc_paths" : locPaths, "loc_name" : locName, "time" : time, "hero" : hero}
			saves.append(save)
		return saves
	
	def move_mob_in_direction(self, mob, direction):
		did_move = self.world.move_mob_in_direction(mob, direction)
		
		if mob == self.hero and did_move:
			self.time_in_sec+=15
			self.world.show_square(self.hero)

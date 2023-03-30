from game import Game
from konsola import Konsola

game = Game()

game.choose_game()
world = game.world
hero = game.hero


commands = {
  
}

while game.is_playing:
  command = Konsola.prompt(game.hero)
  command_name = command[0]
  command_args = command[1:]




  if len(command) == 0:
    print("Co chcesz zrobić?")
  elif command[0] in ("north", "n", "8"):
    game.move_mob_in_direction(game.hero, 8)
  elif command[0] in ("northeast", "ne", "9"):
    game.move_mob_in_direction(game.hero, 9)
  elif command[0] in ("east", "e", "6"):
    game.move_mob_in_direction(game.hero, 6)
  elif command[0] in ("southeast", "se", "3"):
    game.move_mob_in_direction(game.hero, 3)
  elif command[0] in ("south", "s", "2"):
    game.move_mob_in_direction(game.hero, 2)
  elif command[0] in ("southwest", "sw", "1"):
    game.move_mob_in_direction(game.hero, 1)
  elif command[0] in ("west", "w", "4"):
    game.move_mob_in_direction(game.hero, 4)
  elif command[0] in ("northwest", "nw", "7"):
    game.move_mob_in_direction(game.hero, 7)
  elif command[0] in ("up", "u", "5"):
    game.move_mob_in_direction(game.hero, 5)
  elif command[0] in ("down", "d", "0"):
    game.move_mob_in_direction(game.hero, 0)
  elif command[0] in ("exit", "end", "quit", "q"):
    game.endGame()
  elif command[0] in ("whereami"):
    game.hero.whereami()
  elif command[0] in ("whoami"):
    game.hero.whoami()
  elif command[0] in ("help", "pomoc"):
    Konsola.help()

  


  ## GODMODE STUFF ##
  elif command[0] in ("map", "mapa"):
    Konsola.map(hero)
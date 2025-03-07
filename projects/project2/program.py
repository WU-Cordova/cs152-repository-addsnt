from projects.project2.kbhit import KBHit
from projects.project2.grid import Grid
from projects.project2.gamecontroller import GameController

def main():
    grid = Grid(10,10)
    game_controller = GameController(grid)
    #game_controller.run()

if __name__ == '__main__':
    main()


# from projects.project2 import KBHit
from projects.project2.grid import Grid
from projects.project2.gamecontroller import GameController

def main():

    grid = Grid(10,10)

    game_controller = GameController(grid)

    kbhit = KBHit() # need to import KBHit (download file)
    


if __name__ == '__main__':
    main()

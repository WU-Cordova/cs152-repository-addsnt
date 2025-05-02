from projects.project2.grid import Grid
from projects.project2.kbhit import KBHit
import time
import os
import copy

class GameController:
    def __init__(self, grid: Grid) -> None:
        self.grid = grid
        self.kb = None # allows for number to be entered, and THEN kbhit commands to go in
        self.auto_mode = True
        self.speed = 1
        self.previous_gens = []
        self.choose_speed()
        self.manual_mode = False

    def choose_speed(self):
        print("Choose simulation speed: (1) slow (2) normal (3) fast (4) manual mode")
        choice = input("> ").strip()

        if choice == "1":
            self.speed = 1.5  # slow
        elif choice == "2":
            self.speed = 1  # normal/default
        elif choice == "3":
            self.speed = 0.3  # fast
        elif choice == "4":
            self.speed = 1
            print("I could not get amnual to work (see line 82). You are being put on auto mode regular speed.")
        else:
            print("Invalid choice, using normal speed.")
        self.kb = KBHit()

    def is_empty_grid(self) -> bool:
        for row in range(self.grid.grid.row_len):
            for col in range(self.grid.grid.column_len):
                if self.grid.grid[row][col].is_alive:
                    return False
        print("All cells died, simulation ending.")
        return True

    def is_stable_or_repeating(self) -> bool:
        for prev_gen in self.previous_gens:
            if self.grid == prev_gen:
                print("Grid is stable or repeating. Simulation ending.")
                return True
        return False

    def run(self) -> None:
        print("Press 'Q' to quit, 'M' for manual mode, 'A' for auto mode.")
        iteration = 0

        while True:
            print(f'Generation: {iteration}')
            iteration += 1
            self.grid.display()

            if self.is_empty_grid() or self.is_stable_or_repeating():
                break
                
            self.previous_gens.append(copy.deepcopy(self.grid))

            if self.auto_mode:
                time.sleep(self.speed)
                self.grid.next_generation()
            
            if self.kb.kbhit():
                c = self.kb.getch().lower()
                if c == 'q' or ord(c) == 27:
                    print("Stopping simulation.")
                    break
                elif c == 'a':
                    self.auto_mode = True
                    self.manual_mode = False
                    print("Switched to auto mode.")
                    continue
                elif c == 'm':
                    self.auto_mode = False
                    self.manual_mode = True
                    print("Switched to manual mode.")
                '''elif ord(c)==13 and self.manual_mode==True:
                    self.grid.next_generation()
                    continue'''
                    # this just doesn't work and I am giving up. It spawns the same generation very rapidly.
    
        self.kb.set_normal_term()
        self.ask_restart()

    def ask_restart(self):
        choice = input("\nSimulation ended. Restart? (y/n): ").strip().lower()
        if choice == "y":
            self.previous_gens = []  # Clear history
            self.grid = Grid(10,10)
            # when running, the kbhit commands no longer work...
            # and there is no option for speed chaning.
            self.run()
        else:
            print("Simulation ended.")

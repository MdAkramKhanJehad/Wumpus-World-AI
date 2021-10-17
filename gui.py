from tkinter import *
from agent import Agent
from world import World
from grid_label import Grid_Label
import time


def solve_wumpus_world(master, world_file):
    world = World()
    world.generate_world(world_file)
    label_grid = [[Grid_Label(master, i, j) for j in range(world.num_cols)] for i in range(world.num_rows)]
    agent = Agent(world, label_grid)

    while not agent.exited:
        agent.explore()
        if agent.found_gold:
            agent.leave_cave()
        break
    agent.repaint_world()
    agent.world_knowledge[agent.world.agent_row][agent.world.agent_col].remove('A')
    time.sleep(1.5)
    agent.repaint_world()


master = Tk()
master.title("Wumpus World")
# master.iconbitmap("icon.ico")

world = World()
world.generate_world("world_1.txt")
label_grid = [[Grid_Label(master, i, j) for j in range(world.num_cols)] for i in range(world.num_rows)]

world_1 = Button(master, text="World 1", command=lambda: solve_wumpus_world(master, "world_1.txt"), width=8,
                 font="Helvetica 14 bold", bg="gray80", fg="blue", borderwidth=0, activeforeground="white",
                 activebackground="gray40")

world_1.grid(row=0, column=len(label_grid[0]))

mainloop()

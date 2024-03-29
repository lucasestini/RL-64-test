import numpy as np
from plotMap import plotmap 
from keras.models import model_from_json 
from environment import Maze
from models import *
import pickle




def play(map_index):
    map_npy = 'mappe_test/map_'+map_index+'.npy'
    plt.grid(True)
    maze = np.load(map_npy)
    exit_cell = (30,5)    #(37_27) 80_1 (30,5) 80_2 ....
    model_name = 'NN double augm prior 8 rays +  delta location '+map_index
    while True:

        plt.imshow(maze, cmap="binary")
        plt.plot(exit_cell[0], exit_cell[1], "gs", markersize=5)  # exit is a big green square
        plt.title(map_npy)
        plt.show()
        start_cell = tuple(int(x) for x in input('start cell: ').split()) #(20,28) (20,25) (14,5) (22,21) 80_1// (38,16) 80_2
        game = Maze(maze, start_cell=start_cell, exit_cell=exit_cell, close_reward = -0.5)
        model = QReplayDoubleAugmPrior8(game, name = model_name, load = True)
        status, trajectory, time_elapsed = game.play(model, start_cell = start_cell) 
        game.render("moves")
        game.play(model, start_cell = start_cell) 
        print('*******************************************')
        print('status = {}'.format(status))
        print('trajectory = {}'.format(trajectory))
        print('time elapsed = {} seconds'.format(time_elapsed))
        repeat = input('Type True to repeat: ')
        if repeat != "True":
            break
if __name__ == '__main__':
    map_index = input('type map index: ')
    play(map_index)
              
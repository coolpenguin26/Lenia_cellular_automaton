'''Conway's Game of Life'''


#import functions
from GoL import GameOfLifeAnimation

def main():
    animation = GameOfLifeAnimation(size=64)
    animation.animate() #simuilation

if __name__ == "__main__":
    main()




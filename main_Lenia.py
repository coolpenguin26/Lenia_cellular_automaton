'''Lenia'''


#import functions
from Lenia import LeniaAnimation

def main():
    animation = LeniaAnimation(size=64)
    animation.animate() #simulation
    animation.plot() #kernel/growth plots

if __name__ == "__main__":
    main()

'''object oriented Lenia animation'''

#import useful libraries
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation
import scipy

from update import update
from kernels import Kernel
from creatures import pattern
from visuals import plots

#set default parameters
size = 64 #size of grid
R = 1 #kernel radius
np.random.seed(0)


        
class LeniaAnimation:
    def __init__(self, size=64, R=13):
        '''define the world and figure'''
        
        self.size = size
        self.R = R
        
        #random world
        #self.A = np.random.rand(size,size)
        
        #specific world with loaded creature
        self.A = self.initialise_world()
        
        #create the kernel
        self.kernel = Kernel(size, kernel_type='circular', smooth=True, R=self.R, end=True)
        self.convolution_FFT = True
        self.fK = np.fft.fft2(np.fft.fftshift(self.kernel.K / np.sum(self.kernel.K)))
        
        #create the figure for visualisation
        self.fig, self.ax = plt.subplots() #figure serves as a container
        self.img = self.ax.imshow(self.A, cmap='PuRd', interpolation='nearest',vmin=0,vmax=1)
        self.ax.set_title('System')
        self.colorbar = self.fig.colorbar(self.img, ax=self.ax, orientation='vertical')
        self.colorbar.set_label('Cell status')
        self.colorbar.set_ticks([0, 1])
        self.colorbar.set_ticklabels(['Dead', 'Live'])
        
        
    def initialise_world(self, size=64, scale=1, cx=20, cy=20):
        '''load specific creatures'''
        scale = 1
        cx, cy = 20, 20
        
        pattern_data = pattern.get("orbium", {})
        cells = pattern_data.get("cells", [])
        
        globals().update(pattern_data)
        C = np.asarray(cells)
        A = np.zeros([self.size, self.size])
        C = scipy.ndimage.zoom(C, scale, order=0)
        A[cx:cx+C.shape[0], cy:cy+C.shape[1]] = C
        return A
        
    def update(self, i):
        '''update frame'''
        self.A = update(self.A,self.kernel,self.convolution_FFT,self.fK)
        self.img.set_array(self.A)
        return self.img,
    
    def animate(self):
        '''simulation as animation'''
        ani = matplotlib.animation.FuncAnimation(self.fig, self.update, frames=200, interval=20, blit=True)
        ani.save('lenia_animation.gif', writer='pillow')

    def plot(self):
        '''kernel and growth function plots'''
        plots(self.kernel,self.R,save=True)
        
        

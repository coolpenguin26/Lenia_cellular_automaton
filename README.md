# Lenia_cellular_automaton
Lenia is a recently introduced cellular automaton (2018) which is an extension of Conway’s Game of Life with continuous variables. States, time, and space are made continuous and definition of a kernel and growth function is required. I produced an implementation of Lenia with one active convolution channel and one active kernel.


A simple code following some guidance by Bert Chan’s tutorial, was implemented in Jupyter notebook (Lenia.ipynb). This is readable and the cells run in order; it was used to easily visualise the animations/plots with changing parameters for experiment. Multiple produced plots and
commentary are included in the notebook.


In python, I implemented a more sophisticated object oriented approach to Lenia. Functions and classes are defined in individual files and called to the main program. Details of the folder structure:

**main_Lenia.py** Main program that runs Lenia simulation - saves the simulation as a gif and also
saves several plots of the kernel and growth function. The default set-up is Orbium with a
ring kernel, translating across the world.

**main_GoL.py** Program that runs Game of Life simulation - saves the simulation as a gif.
Lenia.py Object oriented programming implementation of Lenia animation.

**GoL.py** Object oriented programming implementation of Game of Life animation.

**update.py** Contains the functions for both Lenia and GoL that define how to advance one
frame in the animation. This is effectively the convolution, growth function, and integration
step.

**kernels.py** Contains definition of kernel class including associated growth function. This is
imported for instantiating various kernel shapes.

**visuals.py** Contains definition of function that plots the kernel shape, kernel cross section,
and growth function.

**creatures.py** Contains a library of lifeforms/patterns of interest that can be placed in Lenia
world simulation.

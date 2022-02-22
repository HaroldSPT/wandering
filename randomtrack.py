import imp
from turtle import title
from wandering import CommonWandering
from track import Track
from location import Location

from bokeh.plotting import figure, output_file, show

def walking(location, wandering, steps):
    beggining = location.get_loction(wandering)

    for _ in range(steps):
        location.move_wandering(wandering)

    return beggining.distance(location.get_location(wandering))

def simulate_walk(steps, number_attemps, wandering_type):
    wandering = wandering_type(name='Alirio')
    origin = Location(0, 0)
    distance = []

    for _ in range(number_attemps):
        track = Track()
        track.add_wandering(wandering, origin)
        simulation_walk = walking(track, wandering, steps)
        distance.append(round(simulation_walk, 1))

def graph(x, y):
    graphics = figure(title='Camino del Errante', x_axis_label='Pasos', y_axis_label='Distancia')
    graphics.line(x, y, legend='Distancia')
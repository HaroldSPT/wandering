import imp
from turtle import distance, title
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
    distances = []

    for _ in range(number_attemps):
        track = Track()
        track.add_wandering(wandering, origin)
        simulation_walk = walking(track, wandering, steps)
        distances.append(round(simulation_walk, 1))

def graph(x, y):
    graphics = figure(title='Camino del Errante', x_axis_label='Pasos', y_axis_label='Distancia')
    graphics.line(x, y, legend='Distancia')

def main(distances_walk, number_attemps, wandering_type):
    average_walking_distance = []

    for steps in distances_walk:
        distances = simulate_walk(steps, number_attemps, wandering_type)
        middle_distance = round(sum(distances) / len(distances), 4)
        max_distances = max/(distances)
        min_distances = min/(distances)
        average_walking_distance.append(middle_distance)
        print(f'{wandering_type.__name__} Caminata aleatoria de {steps} pasos')
        print(f'Media = {middle_distance}')
        print(f'Max = {max_distances}')
        print(f'Min = {min_distances}')
    graph(distances_walk, average_walking_distance)

    if __name__ == '__main__':
        distances_walk = [10, 100, 1000, 10000]
        number_attemps = 100
        main(distances_walk, number_attemps, CommonWandering)
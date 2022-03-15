from turtle import title
from Wandering import CommonWandering
from Wandering import LeftWandering
from Wandering import RightWandering
from track import Track
from location import Location

from bokeh.plotting import figure, output_file, show

def know_wandering_type(wandering_type):
    if wandering_type.__name__ == "CommonWandering":
        return "Errante Común"
    elif wandering_type.__name__ == "RightWandering":
        return "Errante de Derecha"
    else:
        return "Errrante de Izquierda"

def walking(wandering, steps, wandering_type):
    beggining = [wandering.position()]

    x_graph = [0]
    y_graph = [0]

    for _ in range(steps -1):
        wandering.walk()
        x, y = wandering.position()
        x_graph.append(x)
        y_graph.append(y)

    know_type = know_wandering_type(wandering_type)
    graph_steps(x_graph, y_graph, know_type, steps)
    return wandering.distance_origin()

def simulate_walk(steps, number_attemps, wandering_type):

    wandering = []
    distances = []

    for i in range(number_attemps):
        wandering.append(wandering_type(name=f'Alirio {i}'))
        simulations_walk = walking(wandering[i], steps, wandering_type)
        distances.append(round(simulations_walk, 1))
    return distances

    
def graph_steps(x_graph, y_graph, wandering_type, steps):
    graphics = figure(title='Camino del Errante', x_axis_label='Pasos', y_axis_label='Distancia')
    graphics.line(x_graph, y_graph, legend_label=str(steps)+' Pasos')
    final_x = x_graph[-1]
    final_y = y_graph[-1]
    graphics.diamond_cross(0, 0, fill_color = "green", line_color = "green", size = 18)
    graphics.diamond_cross(final_x, final_y, fill_color = "red", line_color = "red", size = 18)
    final_straight_x = [0, final_x]
    final_straight_y = [0, final_y]
    graphics.line(final_straight_x, final_straight_y, line_width = 2, color = "yellow")
    show (graphics)

def main(distances_walk, number_attemps, wandering_type):


    for steps in distances_walk:
        distances = simulate_walk(steps, number_attemps, wandering_type)
        middle_distance = round(sum(distances) / len(distances), 4)
        max_distances = max(distances)
        min_distances = min(distances)
        
        print(f'{wandering_type.__name__} Caminata aleatoria de {steps} pasos')
        print(f'Media = {middle_distance}')
        print(f'Max = {max_distances}')
        print(f'Min = {min_distances}')

if __name__ == '__main__':
    distances_walk = [10000]
    number_attemps = 1
    main(distances_walk, number_attemps, CommonWandering)
import imp
from wandering import CommonWandering
from track import Track
from location import Location

from bokeh.plotting import figure, output_file, show

def walking(location, wandering, steps):
    beggining = location.get_loction(wandering)

    for _ in range(steps):
        location.move_wandering(wandering)

    return beggining.distance(location.get_location(wandering))
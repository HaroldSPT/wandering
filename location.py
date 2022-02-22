class Location:
    def __init__(self):
        self.wandering_location =  {}

    def add_wandering(self, wardering, track):
        self.wandering_location[wardering] = track

    def move_wandering(self, wandering):
        delta_x, delta_y = wandering.walk()
        actual_location = self.wandering_location[wandering]
        new_location = actual_location.move(delta_x, delta_y)

        self.wandering_location[wandering] = new_location

    def get_location(self, wandering):
            return self.wandering_location[wandering]
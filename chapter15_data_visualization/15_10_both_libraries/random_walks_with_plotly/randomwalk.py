from random import choice
import matplotlib.pyplot as plt

class RandomWalk:
    # class to generate random walks
    def __init__(self, num_points=5000):
        self.num_points = num_points

        self.x_values = [0]
        self.y_values = [0]

    # method to calculate all the points
    def fill_walk(self):
        # keep taking steps until the walk reaches the desired length
        while len(self.x_values) < self.num_points:

            x_step = self.get_step()
            y_step = self.get_step()

            # if going nowhere, restart loop
            if x_step == 0 and y_step == 0:
                continue

            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)
    
    # method to get steps
    def get_step(self):
        step_direction = choice([1, -1])
        step_distance = choice([0, 1, 2, 3, 4])
        step = step_direction*step_distance
        return step
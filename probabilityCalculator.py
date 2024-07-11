import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color, count in kwargs.items():
            self.contents.extend([color] * count)
    
    def draw(self, draw):
        draws = []
        if draw > len(self.contents):
            all_draw = self.contents[:]
            self.contents.clear()
            return all_draw
        for i in range(draw):
            randomIndex = random.randint(0, len(self.contents)-1)
            draws.append(self.contents.pop(randomIndex))
        return draws

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    num_successful = 0
    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)
        
        # Check if drawn balls match expected counts
        success = True
        for color, count in expected_balls.items():
            if drawn_balls.count(color) < count:
                success = False
                break
        
        if success:
            num_successful += 1
    
    return num_successful / num_experiments

# Example usage
hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                         expected_balls={'red': 2, 'green': 1},
                         num_balls_drawn=5,
                         num_experiments=2000)


hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={'red':2,'green':1},
                  num_balls_drawn=5,
                  num_experiments=2000)
print(probability)
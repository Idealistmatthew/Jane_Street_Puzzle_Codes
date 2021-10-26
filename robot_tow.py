import random

class Marker(object):
    def __init__(self, position):
        self.position = position

    def get_position(self):
        return self.position

    def check_rob1_win(self):
        if self.position > 0.5:
            return True
        else:
            return False

    def check_rob2_win(self):
        if self.position < -0.5:
            return True
        else:
            return False

    def rob1_pull(self):
        dist = random.random()
        self.position += dist

    def rob2_pull(self):
        dist = random.random()
        self.position -= dist

def run_trial(position):
    point = Marker(position)
    while point.check_rob1_win() != True or point.check_rob2_win() != True:
        point.rob1_pull()
        if point.check_rob1_win():
            return True
        point.rob2_pull()
        if point.check_rob2_win():
            return False

def find_prob(num_trials, position):
    num_1wins = 0
    for i in range(num_trials):
        if run_trial(position):
            num_1wins += 1
    return num_1wins/num_trials

def find_root(lower, upper):
    mid = (lower+upper)/2
    res = find_prob(1000000,-mid)
    epsilon = 10**(-6)
    while abs(res-0.5) > epsilon:
        if res-0.5 > 0:
            lower = mid
            mid = (lower + upper)/2
            res = find_prob(1000000,-mid)
            print("Current: " + str(res))
        else:
            upper = mid
            mid = (lower+upper)/2
            res = find_prob(1000000,-mid)
            print("Current: " + str(res))
    print(mid)
    print(res)

# find_root(0.2847,0.2853)
print(find_prob(10000000,0))

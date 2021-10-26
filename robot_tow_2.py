import numpy
import math

# adapted from https://mail.scipy.org/pipermail/scipy-user/2013-June/034744.html
def halton(dim: int, nbpts: int):
    h = numpy.full(nbpts * dim, numpy.nan)
    p = numpy.full(nbpts, numpy.nan)
    P = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
    lognbpts = math.log(nbpts + 1)
    for i in range(dim):
        b = P[i]
        n = int(math.ceil(lognbpts / math.log(b)))
        for t in range(n):
            p[t] = pow(b, -(t + 1))

        for j in range(nbpts):
            d = j + 1
            sum_ = math.fmod(d, b) * p[0]
            for t in range(1, n):
                d = math.floor(d / b)
                sum_ += math.fmod(d, b) * p[t]

            h[j*dim + i] = sum_
    return h.reshape(nbpts, dim)

seq = halton(1,10000)
cnt = 0


# def prandom(seq, ctr):
#     ans = seq[]
#     seq = seq[:-1]
#     # print(seq)
#     # print(ans)
#     return ans
#
#
# for i in range(10):
#     print(prandom(seq))


class Randomizer(object):
    def __init__(self, seq):
        self.seq = seq
        self.counter = 0

    def prandom(self):
        ans = seq[self.counter]
        self.counter += 1
        return ans



class Marker(object):
    def __init__(self, position,uwu):
        self.position = position
        self.uwu = uwu

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
        print("Yo")
        dist = self.uwu.prandom()
        self.position += dist

    def rob2_pull(self):
        dist = self.uwu.prandom()
        self.position -= dist

def run_trial(position,uwu):
    point = Marker(position,uwu)
    while point.check_rob1_win() != True or point.check_rob2_win() != True:
        point.rob1_pull()
        if point.check_rob1_win():
            return True
        point.rob2_pull()
        if point.check_rob2_win():
            return False

def find_prob(num_trials, position):
    uwu = Randomizer(seq)
    num_1wins = 0
    for i in range(num_trials):
        if run_trial(position,uwu):
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



print(seq)
# find_root(0.2847,0.2853)
print(find_prob(100,0))

import random
import numpy as np


class Individuo:
    x: np.ndarray
    y: float

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Populacao:
    p: np.array
    best: Individuo
    popsize: int

    def __init__(self, func, dim, popsize, bounds=(0, 1)):
        self.func = func
        self.popsize = popsize
        self.p = np.empty(popsize, dtype=Individuo)

        for i in range(popsize):
            x = bounds[1] * np.random.rand(dim)
            self.p[i] = Individuo(x, func(*x))

        self.best = self.p[0]
        self.find_best()

    def find_best(self):
        for i in range(self.popsize):
            self.p[i].y = self.func(*(self.p[i].x))
            if self.p[i].y < self.best.y:
                self.best = self.p[i]

        return self.best


def funcao(x1, x2, x3):
    return np.abs(x1 - 10) + np.abs(x2 - 20) + np.abs(x3 - 30)


pop = Populacao(funcao, 3, 10000, bounds=(0, 100))
best = pop.find_best()

print(best.x)
print(best.y)

# Mutacao
for _ in range(10000):
    for i in range(pop.popsize):
        index_rand1 = random.randint(0, pop.popsize - 1)
        x_rand1 = pop.p[index_rand1].x

        index_rand2 = random.randint(0, pop.popsize - 1)
        x_rand2 = pop.p[index_rand2].x

        if random.uniform(0, 1) < 0.7:
            pop.p[i].x = pop.best.x + 0.1 * (x_rand1 - x_rand2)

    best = pop.find_best()

    print(best.x)
    print(best.y)

    if best.y < 1e-5:
        break

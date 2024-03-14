import random
import matplotlib.pyplot as plt

START = 1000
STOP = 10
P = 0.5
WIN = 0.1
LOSS = 0.05
EPOCH = 10000


def k():
    f = P*WIN-(1-P)*LOSS
    print(f)
    return f / (WIN*LOSS)


def cal():
    # ratio = 1.0
    ratio = k()
    print(ratio)
    all = START
    rs = [all]
    i = 0
    while all > STOP and i < EPOCH:
        r = random.random()
        if r <= P:
            rs.append(WIN*all*ratio+(1-ratio)*all)
        else:
            rs.append(LOSS*all*ratio+(1-ratio)*all)

        all = rs[-1]
        i += 1

    print(rs)
    print(len(rs))
    return rs


def draw(rs: list):
    plt.figure(figsize=(8, 6))
    plt.plot(rs, '*-')
    plt.show()


if __name__ == '__main__':
    rs = cal()
    draw(rs)

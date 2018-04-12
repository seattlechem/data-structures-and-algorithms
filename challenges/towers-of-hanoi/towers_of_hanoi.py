class Tower:

    def __init__(self):
        self.counter = 0

    def towers_of_hanoi(self, n, a='A', c='B', b='C'):
        if n == 1:
            self.counter += 1
            print('Disk {} moved from {} to {}'.format(self.counter, a, b))
        else:
            self.towers_of_hanoi(n - 1, a, b, c)
            n = n - 1
            self.towers_of_hanoi(1, a, c, b)
            self.towers_of_hanoi(n - 1, b, c, a)

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw

def nomalize(a):
    amax = np.amax(a)
    amin = np.amin(a)
    p = (amax+amin) / 2.0
    q = (amax-amin) / 2.0
    return ( np.amin(a)-p ) / q

class DynSys:

    def __init__(self, n_state, dt):
        self.n_state = n_state
        self.state = np.empty(n_state)
        self.dt = dt

    def f(self, u):
        return np.zeros(self.n_state)

    def next_state(self, u):
        self.state += self.dt * self.f(u)
        return self.state

    def plot(self, u):
        record = np.empty((len(u)+1, self.n_state))
        record[0,:] = self.state
        for i in range(len(u)):
            record[i+1,:] = self.next_state(u[i])
        for i in range(self.n_state):
            record[:,i] = normalize(record[:,i])
            plt.plot(record[:,i])
        plt.show()

    def img(self):
        return np.zeros((1,1))


class Pendulum(DynSys):

    def __init__(self, dt):

        self.L = 1
        self.m = 1
        self.Q = 10
        self.img_size = 64

        DynSys.__init__(self, 2, dt)
        self.g = 9.81
        self.A = self.g/self.L
        self.B = np.sqrt(self.A) / self.Q
        self.C = 1.0 / (self.m * self.L ** 2)


    def f(self, u):
        s = self.state
        return np.array([ s[1], -self.A*np.sin(s[0]) - self.B*s[1] + self.C*u ])

    def img(self):
        l = self.img_size
        x = l*(0.5 + 0.4*np.sin(self.state[0]))
        y = l*(0.5 + 0.4*np.cos(self.state[0]))
        R = l/10.0
        l_width = int(l/30.0)
        img = Image.new('L', (l,l) )
        draw = ImageDraw.Draw(img)
        draw.ellipse((x-R, y-R, x+R, y+R), fill=255)
        draw.line( (0.5*l, 0.5*l, x, y), fill=255, width=l_width )
        del draw
        return np.array(img)

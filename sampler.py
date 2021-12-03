import numpy as np
from scipy.stats import norm, uniform
from matplotlib.pyplot import scatter, show, plot

class Problem:
    def __init__(self):
        self.name = 'problem'
    
    def eval(self, x):
        return np.exp(-x**2) / (np.pi**0.5)
        # return x**2
        # return np.exp((-1*(x - 0)**2) / (2 * 1**2))
        
        
class Sampler:
    def __init__(self):
        pass
    
    def generate(self):
        pass
    
class Importance_Sampling(Sampler):
    def __init__(self):
        self.name = 'importance sampling'
        
        self.dimension = 1
        self.min_val, self.max_val = 0, 1
        self.mean = np.random.uniform(self.min_val, self.max_val, self.dimension)
        self.std = np.random.uniform(self.max_val-1, self.max_val, self.dimension)
        self.size = 100

    def generate(self):
        
        # X = np.random.normal(self.mean, self.std, self.size)
        q = np.random.uniform(self.min_val, self.max_val, self.size)
        
        q_x = norm(self.mean, self.std).pdf(q)
        p_x = norm(self.min_val, self.max_val).pdf(q)
        weights = p_x / q_x
        
        return weights, q_x

class Rejection_Sampling(Sampler):
    def __init__(self):
        self.name = 'Rejection sampling'
        self.dimension = 1
        self.min_val, self.max_val = 0, 1
        self.mean = np.random.uniform(self.min_val, self.max_val, self.dimension)
        self.std = np.random.uniform(self.max_val-1, self.max_val, self.dimension)
        self.size = 100
        # self.X = np.random.uniform(self.min_val, self.max_val, self.size)
        self.c = 1.0
        # self.c = 
    
    def _p_x(self, x):
        return norm.pdf(x, self.mean, self.std)
    
    def _q_x(self, x):
        return norm.pdf(x, self.min_val, self.max_val) 
    
    def generate(self):
        
        i = 0
        samples = []
        while i< self.size:
            x_i = np.random.normal(self.min_val, self.max_val)
            if(self._p_x(x_i) <= self.c * self._q_x(x_i)):
                
            # p_x = norm(self.min_val, self.max_val).pdf(x_i)
            # q_x = norm(self.min_val - 1, self.max_val).pdf(x_i)
                u = np.random.uniform(self.min_val- 1, self.c * self._q_x(x_i))
            # n = p_x /(self.c*q_x)
            # n = (self._p_x(x_i) / (self.c * self._q_x(x_i)))
                if (u < self._p_x(x_i)):
                    samples.append(x_i)
                    i = i + 1
                else:
                    i = i + 1
        return samples
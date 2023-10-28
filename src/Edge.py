from Landmark import Landmark
from Feature import Feature
class Edge():
    def __init__(self, lm: Landmark, ft: Feature, time:float = 0.0):
        self.lm = lm
        self.ft = ft
        self.time = time

    
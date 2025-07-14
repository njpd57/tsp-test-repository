class Point:
    def __init__(self, x, y):
        self.x      = x
        self.y      = y
        self.radius = 1
        self.alpha  = 150

    def GetTuple(self):
        return (self.x, self.y)

    def __repr__(self):
        return f"({self.x}, {self.y})"

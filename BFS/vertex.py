class vertex():
    def __init__(self, label):
        self.label = label
        self.parent = None
        self.neighbors = []
        self.distance = None
        self.color = None

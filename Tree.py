class Tree(object):
    def __init__(self, children, jumpDistance, row, col):
        self.upChild = None
        self.downChild = None
        self.rightChild = None
        self.leftChild = None
        self.jumpDistance = None
        self.row = None
        self.col = None
class Node:
    def __init__(self, upChild, downChild, rightChild, leftChild, jumpDistance, row, col, depth):
        self.upChild = upChild
        self.downChild = downChild
        self.rightChild = rightChild
        self.leftChild = leftChild
        self.jumpDistance = jumpDistance
        self.row = row
        self.col = col
        self.depth = depth
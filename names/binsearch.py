class BinarySearchTree:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if self.value is None:
            self.value = value
        elif self.value > value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)

    def contains(self, target):
        if self.value == target:
            return True
        if target < self.value:
            if self.left != None:
                return self.left.contains(target)
            return False
        if self.right != None:
            return self.right.contains(target)
        return False

    def get_max(self):
        if self.right:
            max_value = self.right.get_max()
        else:
            return self.value
        return max_value

    def for_each(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

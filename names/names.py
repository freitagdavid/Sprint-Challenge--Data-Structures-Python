import time
from binsearch import BinarySearchTree

start_time = time.time()

duplicates = []


def bin_tree_from_file(file_name):
    with open(file_name, 'r') as f:
        working = f.read().split('\n')
        bin_tree = BinarySearchTree()
        for i in working:
            bin_tree.insert(i)
        return bin_tree


names_1 = bin_tree_from_file('names_1.txt')
names_2 = bin_tree_from_file('names_2.txt')

print(len(names_1))


def is_equal(x):
    if names_2.contains(x):
        duplicates.append(x)


names_1.for_each(is_equal)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

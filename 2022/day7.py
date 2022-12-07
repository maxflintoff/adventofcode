from utils import getInput

class File:
    def __init__(self, name, size=0):
        self.size = size
        self.name = name
        self.parent = None
        self.children = []

def day7():

    input = getInput('day7')

    root = File('/')
    current = root
    for command in input.split('\n'):
        if command.startswith('$'):
            command = command.split()
            if command[1] == 'cd':
                if command[2] == '..':
                    current = current.parent
                else:
                    directory = File(command[2])
                    directory.parent = current
                    current.children.append(directory)
                    current = directory

        else:
            size, name = command.split()
            if size != 'dir':
                file = File(name, int(size))
                current.children.append(file)
    
    allSizes = []

    def calculate_size(file: File):
        size = 0
        if len(file.children) > 0:
            for child in file.children:
                childSize = calculate_size(child)
                size += childSize
        else:
            return file.size
        file.size = size
        allSizes.append(size)
        return size
    
    calculate_size(root)

    print('Star 1:', sum(s for s in allSizes if s <= 100000))

    # Star 2
    UnusedSize = 70000000 - root.size
    for size in sorted(allSizes):
        if size + UnusedSize >= 30000000:
            star2 = size
            break

    print('Star 2:', str(star2))

if __name__ == "__main__":
    day7()
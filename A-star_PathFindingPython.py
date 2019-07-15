

# node class for path finding

class Node():
   
# initiating Values (self works like ' this. ' instance of an object)

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

 # Returns a list of tuples as a path from the given start to the given end in the given maze

def astar(maze, start, end):

# Creating starting and ending node

    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

 # Initializing open and closed list

    open_list = []
    closed_list = []

# Appending the starting node to open_list that we initialized above

    open_list.append(start_node)

# Looping till we find the ending node

    while len(open_list) > 0:

# Get the current node

        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

# Pop current index from open list, and append current node to closed list

        open_list.pop(current_index)
        closed_list.append(current_node)

# checking condition if we find the goal

        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] # Return reversed path

# Generating childs

        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: # Adjacent squares

            # Geting node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Condition 
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue

         
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            # Create new node if above conditions are satisfied

            new_node = Node(current_node, node_position)

            # Append new node to children 

            children.append(new_node)

        # Loop through children

        for child in children:

            # Nested Loop if child is on the closed list

            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Create the f, g, and h values

            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # else if child is already in the open list

            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list

            open_list.append(child)


def main():

    maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    start = (0, 0)
    end = (7, 6)

    path = astar(maze, start, end)
    print(path)

# ' __name__ ' is a built-in variable which evaluates to the name of the current module

if __name__ == '__main__':
    main()
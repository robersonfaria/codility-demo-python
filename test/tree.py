############
#  FINISH  #
############


class Tree:
    def __init__(self, x, l=None, r=None):
        self.x = x
        self.l = l
        self.r = r


def solution(T):
    paths = find_paths(T, [[]])
    print(paths)
    longest = max(paths)
    return calc_changes(T, longest)


def find_paths(T, paths):
    l = len(paths)
    if T:
        if T.l and T.r:
            paths[l - 1].append(T.x)
            p = paths[l - 1].copy()
            paths = find_paths(T.l, paths)
            paths.append(p)
            paths = find_paths(T.r, paths)
            return paths
        if T.l:
            paths[l - 1].append(T.x)
            return find_paths(T.l, paths)
        if T.r:
            paths[l - 1].append(T.x)
            return find_paths(T.r, paths)
    paths[len(paths) - 1].append(T.x)
    return paths


def calc_changes(node, path):
    direction = ''
    changes = 0
    for value in path:
        if node:
            if node.l and node.l.x == value:
                node = node.l
                if direction != 'l':
                    changes += 1
                    direction = 'l'
            if node.r and node.r.x == value:
                node = node.r
                if direction != 'r':
                    changes += 1
                    direction = 'r'
    return changes - 1


X = Tree(5, Tree(3, Tree(2, Tree(6, None, None), Tree(4, None, None)), None),
         Tree(7, Tree(1, None, None), Tree(11, Tree(30, None, Tree(9, None, None)), Tree(8, None, None))))
print(solution(X))

#####################
#         5         #
#       /   \       #
#      3     7      #
#     /     / \     #
#    2     1  11    #
#   / \      /  \   #
#  6   4    30   8  #
#             \     #
#              9    #
#####################

X = Tree(5, Tree(3, Tree(20, Tree(6, None, None), Tree(50, None, None)), None),
         Tree(10, Tree(1, None, None),
              Tree(15, Tree(30, None, Tree(9, Tree(3, None, None), None)), Tree(8, None, None))))
print(solution(X))
####################
#         5        #
#       /   \      #
#      3    10     #
#     /    /  \    #
#    20   1   15   #
#   /  \     /  \  #
#  6   50   30   8 #
#            \     #
#             9    #
#            /     #
#           3      #
####################

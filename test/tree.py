######################################
# not finished, I'll finish tomorrow #
######################################


class Tree:
    def __init__(self, x, l=None, r=None):
        self.x = x
        self.l = l
        self.r = r


def solution(T):
    subtree(T, 0, 'l', [0], [0])


def subtree(T, path, direction, changes, delphi):
    print(T.x, path, direction, changes, delphi)
    delphi[path] += 1
    if T.l:
        if direction == 'r':
            changes[path] += 1
        subtree(T.l, path, 'l', changes, delphi)
    if T.l and T.r:
        path += 1
        delphi.append(0)
        changes.append(0)
    if T.r:
        if direction == 'r':
            changes[path] += 1
        subtree(T.r, path, 'r', changes, delphi)


X = Tree(5, Tree(3, Tree(20, Tree(6, None, None), None), None),
         Tree(10, Tree(1, None, None), Tree(15, Tree(30, None, Tree(9, None, None)), Tree(8, None, None))))
print(solution(X))

#         5
#       /   \
#      3     10
#     /     /  \
#    20    1   15
#   /         /  \
#  6         30   8
#             \
#              9

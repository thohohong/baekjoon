nodeNum, waterQuantity = map(int, input().split(" "))

tree = [[] for i in range(nodeNum + 1)]

for i in range(nodeNum - 1) :
    U, V = map(int, input().split(" "))
    tree[U].append(V)
    tree[V].append(U)

stack = []
stack.append((1, -1)) # (a, b) : a is current node, b is parent node of a

leafNodeCount = 0
while not len(stack) == 0 :
    cur, parent = stack.pop()

    if len(tree[cur]) == 1 :
        if tree[cur][0] == parent :
            leafNodeCount += 1
            continue

    for elem in tree[cur] :
        if elem != parent :
            stack.append((elem, cur))

print(waterQuantity / leafNodeCount)
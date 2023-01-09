path = [('s', 'a'), ('s', 'b'), ('b', 'g')]
startState = 's'
finalState = 'g'
curr = path.pop()[0]
finalPath = [finalState, curr]
while curr != startState:
    for i in path:
        if i[1] == curr:
            curr = i[0]
            finalPath.append(curr)
            break

print(finalPath)

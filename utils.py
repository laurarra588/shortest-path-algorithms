def reconstruct_path(pred, target):
    path = []
    current = target

    if pred[current] == -1:
        return []

    while current != -1:
        path.append(current)
        current = pred[current]

    path.reverse()
    return path

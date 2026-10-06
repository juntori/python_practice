image = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 255, 255, 255, 0],
    [0, 255, 255, 255, 0, 0],
    [0, 0, 255, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
]
xs = []
ys = []

for y, row in enumerate(image):
    for x, value in enumerate(row):
        if value >= 128:
            xs.append(x)
            ys.append(y)
box = (min(xs), min(ys), max(xs), max(ys))
print(f"박스: {box}")
print(f"폭: {box[2] - box[0] + 1}, 높이: {box[3] - box[1] + 1}")

def mean_brightness(image):
  total = 0
  count = 0
  for b in image:
    for b2 in b:
      count += 1
      total += b2
  return total / count

def binarize_image(image, threshold):
  result = []
  for row in image:
    new_row = []
    for value in row:
      if value >= threshold:
        new_row.append(255)
      else:
        new_row.append(0)
    result.append(new_row)
  return result

image = [
  [10, 200, 90],
  [160, 40, 250],
]
avg = mean_brightness(image)
print(f"평균: {avg:.1f}")
print(binarize_image(image, avg))

def area(box):
  x1, y1, x2, y2 = box
  return (x2-x1) * (y2-y1)

def iou(a,b):
  ix1 = max(a[0], b[0])
  iy1 = max(a[1], b[1])
  ix2 = min(a[2], b[2])
  iy2 = min(a[3], b[3])
  inter = max(0, ix2 - ix1) * max(0, iy2 - iy1)
  union = area(a) + area(b) - inter
  return inter / union

print(area((100, 50, 300, 250)))
print(f"{iou((0, 0, 4, 4), (2, 2, 6, 6)):.2f}")
print(iou((0, 0, 2, 2), (5, 5, 8, 8)))

zone = (400, 200, 640, 480)
detections = [
  {"class": "person", "conf": 0.91, "box": (450, 250, 520, 420)},
  {"class": "forklift", "conf": 0.84, "box": (100, 180, 300, 400)},
  {"class": "person", "conf": 0.38, "box": (420, 300, 470, 460)},
  {"class": "person", "conf": 0.77, "box": (150, 100, 210, 260)},
  {"class": "robot", "conf": 0.62, "box": (380, 50, 460, 190)},
]

def filter_by_conf(detections, min_conf):
  result = []
  for det in detections:
    if det["conf"] >= min_conf:
      result.append(det)
    return result

def count_by_class(detections):
  counts = {}
  for det in detections:
    name = det["class"]
    counts[name] = counts.get(name, 0) + 1
  return counts

valid = filter_by_conf(detections, 0.5)
print(f"유효 탐지: {len(valid)}개")
for name, n in count_by_class(valid).items():
  print(f"{name}: {n}")
for det in valid:
  if det["class"] == "person" and iou(det["box"], zone) > 0:
    print(f"경고: person({det['conf']})이 위험 구역에 있습니다")
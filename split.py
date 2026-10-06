lines = [
    "2026-09-01,A100,10.3,OK",
    "2026-09-01,A100,10.9,NG",
    "2026-09-01,B200,25.1,OK",
    "2026-09-02,A100,9.8,OK",
    "2026-09-02,B200,26.2,NG",
    "2026-09-02,B200,24.1,NG",
    "2026-09-02,C300,5.0,OK",
]
totals = {}
ngs = {}

for line in lines:
  date, product, value, result = line.split(",")
  totals[product] = totals.get(product, 0) + 1
  if result == "NG":
    ngs[product] = ngs.get(product, 0) + 1

for product, n in totals.items():
  print(f"{product}: {n}건, 불량 {ngs.get(product, 0)}건")
rate = sum(ngs.values()) / len(lines) * 100
print(f"전체 불량률: {rate:.1f}%")
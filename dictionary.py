specs = {
    "A100": (9.5, 10.5),
    "B200": (24.5, 25.5),
    "C300": (4.8, 5.2),
}

code = input("제품 코드: ")
if code not in specs:
    print("등록되지 않은 제품")
else:
    n = float(input("측정 값: "))
    x, y = specs[code]
    if x <= n <= y:
        print(f"OK (기준 {x} ~ {y})")
    else:
        print(f"NG (기준 {x} ~ {y})")
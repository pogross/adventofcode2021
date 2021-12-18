def count_increasing(measurements: list[int], stepsize: int = 1) -> int:
    count = 0
    for idx in range(len(measurements) - stepsize):
        if measurements[idx] < measurements[idx + stepsize]:
            count += 1

    return count


if __name__ == "__main__":
    with open("input.txt") as f:
        raw = f.read()

    measurements = [int(x) for x in raw.split("\n")]
    print(f"First answer is {count_increasing(measurements)}")
    print(f"Second answer is {count_increasing(measurements, 3)}")

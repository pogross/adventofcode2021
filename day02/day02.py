def execute_command(command: str) -> (int):
    direction, magnitude = command.split(" ")

    horizontal, depth = 0, 0
    if direction == "forward":
        horizontal += int(magnitude)
    elif direction == "up":
        depth -= int(magnitude)
    elif direction == "down":
        depth += int(magnitude)

    return horizontal, depth


def chain_commands(commands: list[str]) -> (int):

    horizontal, depth = 0, 0
    for command in commands:
        horizontal_change, depth_change = execute_command(command)
        horizontal += horizontal_change
        depth += depth_change

    return horizontal, depth


if __name__ == "__main__":
    with open("input.txt") as f:
        raw = f.read()

    commands = [x for x in raw.split("\n")]
    horizontal, depth = chain_commands(commands)
    print(f"First answer is {horizontal*depth}")
    # print(f"Second answer is {count_increasing(measurements, 3)}")

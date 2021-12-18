"""
forward 5
down 5
forward 8
up 3
down 8
forward 2
After following these instructions, you would have a horizontal position of 15 and a depth of 10. (Multiplying these together produces 150.)
"""
import pytest

from day02 import chain_commands, execute_command


@pytest.mark.parametrize(
    "command, expected", [("forward 2", (2, 0)), ("down 5", (0, 5))]
)
def test_execute_command(command, expected):
    actual = execute_command(command)
    assert actual == expected


@pytest.mark.parametrize(
    "commands, expected",
    [(["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"], (15, 10))],
)
def test_chain_commands(commands, expected):
    actual = chain_commands(commands)
    assert actual == expected

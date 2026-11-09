"""Check published examples and local links with Python's standard library."""

from __future__ import annotations

import contextlib
from fractions import Fraction
import io
import itertools
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]


def check_links() -> int:
    count = 0
    for document in ROOT.rglob("*.md"):
        contents = document.read_text(encoding="utf-8")
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", contents):
            parsed = urlsplit(target)
            if parsed.scheme or target.startswith("#"):
                continue
            destination = (document.parent / unquote(parsed.path)).resolve()
            assert destination.is_relative_to(ROOT), (document, target)
            assert destination.is_file(), (document, target)
            count += 1
    return count


def check_binary_search() -> int:
    lesson = (ROOT / "examples" / "binary-search-lesson.md").read_text(
        encoding="utf-8"
    )
    blocks = re.findall(r"```python\n(.*?)\n```", lesson, flags=re.DOTALL)
    assert len(blocks) == 1, "Expected one complete Python example."
    namespace = {"__name__": "__main__"}
    output = io.StringIO()
    with contextlib.redirect_stdout(output):
        exec(compile(blocks[0], "binary-search-lesson.md", "exec"), namespace)
    assert output.getvalue().strip() == "None"

    search = namespace["binary_search"]
    count = 0
    for length in range(7):
        for values in itertools.combinations_with_replacement(range(4), length):
            for target in range(-1, 5):
                numbers = list(values)
                result = search(numbers, target)
                assert numbers == list(values), "Input was unexpectedly changed."
                if target in numbers:
                    assert isinstance(result, int)
                    assert 0 <= result < len(numbers)
                    assert numbers[result] == target
                else:
                    assert result is None
                count += 1
    return count


def check_cache_example() -> None:
    lesson = (ROOT / "examples" / "cache-lesson.md").read_text(encoding="utf-8")
    row = next(line for line in lesson.splitlines() if line.startswith("| 是否命中 |"))
    outcomes = [cell.strip() for cell in row.split("|")[2:-1]]
    assert len(outcomes) == 10
    assert set(outcomes) <= {"是", "否"}
    rate = Fraction(outcomes.count("是"), len(outcomes))
    assert rate == Fraction(7, 10)
    assert Fraction(15, 20) == Fraction(3, 4)


def check_probability_example() -> None:
    # The six non-blue cards were not specified. Vary their numbers instead
    # of inventing values and treating the reverse conditional as known.
    blue_cards = [("blue", 1), ("blue", 1), ("blue", 1), ("blue", 0)]
    reverse_probabilities = set()
    for outside_ones in range(7):
        cards = blue_cards + [("other", 1)] * outside_ones
        cards += [("other", 0)] * (6 - outside_ones)
        blue_numbers = [number for color, number in cards if color == "blue"]
        assert Fraction(blue_numbers.count(1), len(blue_numbers)) == Fraction(3, 4)
        one_cards = [(color, number) for color, number in cards if number == 1]
        reverse_probabilities.add(Fraction(3, len(one_cards)))
    assert len(reverse_probabilities) > 1
    assert Fraction(2, 4) == Fraction(1, 2)


def main() -> None:
    if not __debug__:
        raise SystemExit("Run without -O: these checks use assertions.")
    link_count = check_links()
    case_count = check_binary_search()
    check_cache_example()
    check_probability_example()
    print(f"PASS: {link_count} local document links.")
    print(f"PASS: actual lesson code and {case_count} binary-search cases.")
    print("PASS: cache table arithmetic and conditional-probability assumptions.")
    print("Teaching quality and terminology still require human or agent review.")


if __name__ == "__main__":
    main()

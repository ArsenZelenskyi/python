import sys
from typing import List, Tuple

PARING_BRACKETS = {
    ')': '(',
    '}': '{',
    ']': '[',
    '>': '<'
}

OPENING_BRACKETS = set(PARING_BRACKETS.values())
CLOSING_BRACKETS = set(PARING_BRACKETS.keys())


def analyze_bracket_positions(input_text: str) -> Tuple[bool, List[int]]:
    bracket_stack: List[Tuple[str, int]] = []
    invalid_char_indices: List[int] = []

    for current_index, current_char in enumerate(input_text):
        if current_char in OPENING_BRACKETS:
            bracket_stack.append((current_char, current_index))
        elif current_char in CLOSING_BRACKETS:
            if bracket_stack and bracket_stack[-1][0] == PARING_BRACKETS[current_char]:
                bracket_stack.pop()
            else:
                invalid_char_indices.append(current_index)

    for _, remaining_index in bracket_stack:
        invalid_char_indices.append(remaining_index)

    invalid_char_indices.sort()

    is_balanced = len(invalid_char_indices) == 0
    return is_balanced, invalid_char_indices


def generate_error_pointer_line(input_text: str, error_indices: List[int]) -> str:
    pointer_symbols = [" "] * len(input_text)
    for index in error_indices:
        if 0 <= index < len(pointer_symbols):
            pointer_symbols[index] = "^"
    return "".join(pointer_symbols)


def validate_text_brackets(input_text: str) -> bool:
    is_valid, error_indices = analyze_bracket_positions(input_text)

    if not is_valid:
        human_readable_positions = ", ".join(str(idx + 1) for idx in error_indices)
        visual_pointers = generate_error_pointer_line(input_text, error_indices)

        raise ValueError(
            f"Дужки незбалансовані на позиціях: {human_readable_positions}\n"
            f"{input_text}\n"
            f"{visual_pointers}"
        )
    return True


def main():
    try:
        user_text = input("Введіть рядок: ")

        if validate_text_brackets(user_text):
            print("Рядок валідний")

    except ValueError as err:
        print(f"\nПомилка валідації:\n{err}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
def get_mask_card_number(card_number: str) -> str:
    """Принимает на вход номер карты
    и возвращает ее маску"""

    first_6 = card_number[:6]
    last_4 = card_number[-4:]

    masked_length = len(card_number) - 10
    masked_middle = "*" * masked_length

    full_masked_string = first_6 + masked_middle + last_4

    part1 = full_masked_string[0:4]
    part2 = full_masked_string[4:8]
    part3 = full_masked_string[8:12]
    part4 = full_masked_string[12:16]

    return f"{part1} {part2} {part3} {part4}"
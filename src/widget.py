import masks

account_card = input()
date = input()

def mask_account_card(account_card: str) -> str:

    """Функция принимает в качестве аргумента строку,
    содержащую тип и номер карты или счета, и возвращает строку с замаскированным номером"""

    account_card_info = account_card.rsplit(" ", 1)
    if "Счет" in account_card:
        return f"{account_card_info[0]} {masks.get_mask_account(account_card_info[1])}"
    else:
        return f"{account_card_info[0]} {masks.get_mask_card_number(account_card_info[1])}"


def get_date(date: str) -> str:

    '''Принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407"
    и возвращает строку с датой в формате "ДД.ММ.ГГГГ" ("11.03.2024").'''

    return f'{date[8:10]}.{date[5:7]}.{date[:4]}'
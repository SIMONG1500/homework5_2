def filter_by_state(state_list: list, state_default='EXECUTED') -> list:
    '''Принимает на вход список словарей
    и значение ключа state.
    Возвращает список словарей,
    содержащий только те словари,
    у которых ключ state соответствует
    указанному значению.'''

    filtered_list = []

    for i in state_list:
        if i['state'] == state_default:
            filtered_list.append(i)
        else:
            continue

    return filtered_list


def sort_by_date(state_list: list, decreasing=True) -> list:
    '''Принимает список словарей
    и параметр, задающий порядок сортировки.
    возвращает новый список, отсортированный по дате'''

    sorted_list = state_list.copy()

    sorted_list.sort(key= lambda state_list: state_list.get('date'),
    reverse = decreasing)
    return sorted_list



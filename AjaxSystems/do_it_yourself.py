def bad_device():  # Перевірка на браковані девайси
    bad_lst = []
    file_one = open("app_2.log", "r")
    for text in file_one:
        if 'DD' in text:
            bad_lst.append(text[44:50])
    file_one.close()
    return set(bad_lst)


def good_device():  # Перевірка на добрі девайси
    good_lst = []
    file_one = open("app_2.log", "r")
    for text in file_one:
        if 'BIG' in text:
            good_lst.append(text[44:50])
    file_one.close()
    return set(good_lst)


def set_device():  # Множинна перевірка на браковані/ добрі
    diff_set = set(good_device()).difference(set(bad_device()))
    return diff_set


def final_dict():  # Створення словника
    file_one = open("app_2.log", "r")
    dict_lst = []
    for text in file_one:
        if 'BIG' in text:
            dict_lst.append(text[44:50])

    f_dict = {}
    for el in set_device():
        if el in dict_lst:
            f_dict[el] = dict_lst.count(el)
        else:
            f_dict[el] = 0
    file_one.close()
    return f_dict


def final_text():  # Презентація текста

    print(f"{'_'*13}Failed test {len(bad_device())} devices{'_'*13}")  # Failed test
    for dev_id in sorted(bad_device()):
        print(f'Device {dev_id} was removed')

    print(f"{'_'*13}Success test {len(set_device())} devices{'_'*13}")  # Success test
    for key, value in sorted(final_dict().items()):
        print(f'Device {key} sent {value} statues')


final_text()

def is_on_list(list, day):
    return day in list


def add_x(list, day):
    list.append(day)


def get_x(list, index):
    return list[index]


def remove_x(list, day):
    list.remove(day)


days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

print("Is Wed on 'days' list?", is_on_list(days, "Wed"))

print("The fourth item in 'days' is:", get_x(days, 3))

add_x(days, "Sat")
print(days)

remove_x(days, "Mon")
print(days)
import calendar

print(dict((index, month) for index, month in enumerate(calendar.month_abbr) if month))


def my_month(month):
    return dict((index, month) for index, month in enumerate(calendar.month_abbr) if month)[month]


print(my_month(1))

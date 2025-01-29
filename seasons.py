"""leap year = 366 days

INPUT: YYYY - MM - DD
OUTPUT: how old in: Minutes - rounded to integer, English, no "and"

year
month
day
--->> return minutes

assume user was born at midnight (00:00:00)
assume the current time is midnight (00:00:00)

TYPE ERROR: Exit via sys.exit if the user does not input a date in YYYY-MM-DD format.

Test file:

// Five hundred twenty-five thousand, six hundred minutes //

Tính số ngày = tổng số ngày hiện tại - tổng số ngày của birthday + nếu là leap year thì thêm ngày


"""

import sys
from datetime import date


class Time_Calculator:
    def __init__(self, year, month, day):
        self.year = int(year)
        self.month = int(month)
        self.day = int(day)

    def day_Calculator(self):
        return (self.year - 1) * 365 + self.month_Count() + self.day + self.leep_Day()

    def month_Count(self):
        # Days in each month (index 0 is January, index 11 is December)
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        # Sum up days from all months before the current month
        return sum(month_days[: self.month - 1])

    def leep_Day(self):
        leep = 0
        for i in range(1, self.year + 1):
            if (i % 4 == 0 and i % 100 != 0) or (i % 400 == 0):
                leep += 1
        return leep


def main():
    # input
    birthday = input("Birthday: ").strip()
    birthday = birthday.split("-")
    #! Check valid
    if (len(birthday[0]) != 4) or (len(birthday[1]) != 2) or (len(birthday[2]) != 2):
        sys.exit("Invalid Date")
    else:
        birthday1 = Time_Calculator(birthday[0], birthday[1], birthday[2])
        print(birthday1.day_Calculator())

    current_date = date.today()
    current_date = str(current_date)
    current_date1 = current_date.split("-")
    current_date1 = Time_Calculator(
        current_date1[0], current_date1[1], current_date1[2]
    )


if __name__ == "__main__":
    main()

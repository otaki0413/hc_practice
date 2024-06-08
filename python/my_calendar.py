import datetime


def get_first_date(year, month):
    """
    月初日を取得する
    :param year:年
    :param month:月
    :return:月初日
    """
    return datetime.date(year, month, 1)


def get_last_date(year, month):
    """
    月末日を取得する
    :param year:年
    :param month:月
    :return:月末日
    """
    # 翌月の月初日を取得
    if month == 12:
        next_month_first_date = datetime.date(year+1, 1, 1)
    else:
        next_month_first_date = datetime.date(year, month+1, 1)

    # 翌月の月初日から1日引く
    last_date = next_month_first_date - datetime.timedelta(days=1)
    return last_date


# 現在日付(yyyy-mm-dd)
d_today = datetime.date.today()

# 曜日用のリスト
day_of_week = ["月", "火", "水", "木", "金", "土", "日"]

# 月初日と月末日
d_first = get_first_date(d_today.year, d_today.month)
d_last = get_last_date(d_today.year, d_today.month)

# 日付格納用のリスト
calendar_list = []

# 最初の週の空白を追加
for _ in range(d_first.weekday()):
    calendar_list.append("   ")

# 日付を追加
for day in range(1, d_last.day+1):
    if day <= 9:
        calendar_list.append(f" {day} ")
    else:
        calendar_list.append(f"{day} ")

# カレンダー出力
print(f"       {d_today.month}月 {d_today.year}")
print(" ".join(day_of_week))
for i in range(0, len(calendar_list), 7):
    print("".join(calendar_list[i:i+7]))

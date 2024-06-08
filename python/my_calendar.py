import datetime
import sys


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


def main():
    # 現在日付(yyyy-mm-dd)
    d_today = datetime.date.today()

    # コマンドライン引数のチェック
    args = sys.argv
    if len(args) == 1:
        pass
    elif len(args) == 3:
        if args[1] != "-m":
            sys.exit("第1引数は -m を入力してください。")
        try:
            month = int(args[2])
            if month not in range(1, 13):
                raise ValueError
        except ValueError:
            sys.exit(f"{int(args[2])} is neither a month number (1..12) nor a name")

        d_today = datetime.date(year=d_today.year, month=int(args[2]), day=1)
    else:
        sys.exit("月を指定する場合は、コマンドライン引数を2つ入力してください。\n第1引数は -m 、第2引数は1〜12までの数値です。")

    # 曜日表示用のリスト
    days_of_week = ["月", "火", "水", "木", "金", "土", "日"]

    # 月初日と月末日
    d_first = get_first_date(d_today.year, d_today.month)
    d_last = get_last_date(d_today.year, d_today.month)

    # 日付格納用のリスト
    calendar_list = []

    # 最初の週の空白を追加
    for _ in range(d_first.weekday()):
        calendar_list.append("   ")

    # 日付を追加（1桁か2桁かで空白を考慮する）
    for day in range(1, d_last.day+1):
        if day <= 9:
            calendar_list.append(f" {day} ")
        else:
            calendar_list.append(f"{day} ")

    # カレンダー出力
    print(f"       {d_today.month}月 {d_today.year}")
    print(" ".join(days_of_week))
    for i in range(0, len(calendar_list), 7):
        print("".join(calendar_list[i:i+7]))


if __name__ == "__main__":
    main()

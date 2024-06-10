import sys


score_mapping = {
    "-4": "コンドル",
    "-3": "アルバトロス",
    "-2": "イーグル",
    "-1": "バーディ",
    "0": "パー",
    "1": "ボギー",
}


def get_score(x, y):
    if x < 3 or x > 5:
        raise ValueError(f"規定打数の値に{x}を検出しました。3以上5以下にしてください。")
    if y < 1:
        raise ValueError(
            f"プレイヤーの打数の値に{y}を検出しました。1以上にしてください。"
        )

    if x < 5 and y == 1:
        return "ホールインワン"

    if y - x > 1:
        return f"{y - x}ボギー"

    result = str(y - x)
    return score_mapping.get(result, "スコア未定義")


lines = sys.stdin.readlines()

line1 = list(map(int, lines[0].strip().split(",")))
line2 = list(map(int, lines[1].strip().split(",")))

nested_list = [[line1[i], line2[i]] for i in range(len(line1))]

output = []
for x, y in nested_list:
    try:
        score = get_score(x, y)
    except ValueError as error:
        print(error)
        sys.exit(1)
    else:
        output.append(score)

print(",".join(output))

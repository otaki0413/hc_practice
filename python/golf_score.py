import sys


def get_score(x, y):
  if x < 3 or x > 5:
    raise ValueError(f"規定打数の値に{x}を検出しました。3以上5以下にしてください。")
  if y < 1:
    raise ValueError(f"プレイヤーの打数の値に{y}を検出しました。1以上にしてください。")

  if y == 1:
    if x == 4:
      return "ホールインワン"
    elif x == 5:
      return "コンドル"
    else:
      return "ホールインワン"
  elif x-y == 0:
    return "パー"
  elif x-y == 1:
    return "バーディ"
  elif x-y == 2:
    return "イーグル"
  elif x-y == 3:
    return "アルバトロス"
  elif x-y == -1:
    return "ボギー"
  elif x-y < -1:
    return f"{-(x-y)}ボギー"
  else:
    return "スコア未定義"


lines = sys.stdin.readlines()

line1 = list(map(int, lines[0].strip().split(",")))
line2 = list(map(int, lines[1].strip().split(',')))

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

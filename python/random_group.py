import random

members = ["A", "B", "C", "D", "E", "F"]

# リストをシャッフルする
random.shuffle(members)

# 2または3をランダムに取得してグループ化する
number = random.choice([2, 3])
group1 = members[:number]
group2 = members[number:]

# 各リストをアルファベット順にソートする
group1.sort()
group2.sort()

print(group1)
print(group2)

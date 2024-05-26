import random

members = ["A", "B", "C", "D", "E", "F"]

# リストをシャッフルする
random.shuffle(members)

# ランダムに3:3か2:4のリストに分ける
if random.choice([True, False]):
    group1 = members[:3]
    group2 = members[3:]
else:
    group1 = members[:2]
    group2 = members[2:]

# 各リストをアルファベット順にソートする
group1.sort()
group2.sort()

print(group1)
print(group2)

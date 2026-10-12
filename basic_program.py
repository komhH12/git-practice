# basic_program.py —— 学生成绩小工具（Git 分支练习的道具文件）
# 运行： python3 basic_program.py
# 想练手可以随便改：换分数、加等级、加功能，都行。


def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 60:
        return "C"
    else:
        return "F"


scores = [95, 82, 67, 50]

for s in scores:
    print(s, "分 →", get_grade(s))

print("平均分：", sum(scores) / len(scores))

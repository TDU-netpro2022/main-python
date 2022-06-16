# 入力すべき行数を取得
print("何行入力するか数字をまず入力してください。")
num_lines = int(input())
print("入力を開始してください。")

# 1行ずつ取り出し
for i in range(num_lines):
    line = input()
    print(i + 1, "行目:" + line)


def greet(to):
    print('hello, ' + to)

print("main.py")
print(__name__)

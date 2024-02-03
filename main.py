import sys


def main(lines):
    for i, v in enumerate(lines):
        # print("line[{0}]: {1}".format(i, v))
        if i == 0:  # 1行目は数字の要素数 n
            n = v
        elif i == 1:
            a = list(
                map(int, v.split(" "))
            )  # 1行目じゃない(2行目)の時は数字のリストを取得
    print(n)
    print(a)


if __name__ == "__main__":
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip("\r\n"))
    main(lines)

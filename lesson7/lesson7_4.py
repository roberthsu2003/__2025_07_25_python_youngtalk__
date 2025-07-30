import argparse

parser = argparse.ArgumentParser(description="讓使用輸入姓名")
parser.add_argument("-n","--name",type=str,help="這裏要放姓名")
args = parser.parse_args()

if not args.name:
    name = input("請輸入您的姓名:")
else:
    name = args.name

print(name)


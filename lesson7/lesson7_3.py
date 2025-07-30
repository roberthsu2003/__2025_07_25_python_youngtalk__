import argparse

parser = argparse.ArgumentParser(description="讓使用輸入姓名")
parser.add_argument("-n","--name",type=str,help="姓名",default="無名氏")
args = parser.parse_args()

print(f"您的姓名是{args.name}")
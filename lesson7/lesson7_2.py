import argparse

parser = argparse.ArgumentParser(description="要求使用者輸入姓名")
parser.add_argument("name", help="請輸入姓名")
args = parser.parse_args()

print(f"您的姓名是:{args.name}")
import argparse
import random

parser = argparse.ArgumentParser(description="猜數字遊戲")
parser.add_argument("-n","--name",type=str,help="姓名")
parser.add_argument("-f","--frequency",type=int,help="玩的次數",default=1)
args = parser.parse_args()

if not args.name:
    name = input("請輸入您的姓名:")
else:
    name = args.name

frequency = args.frequency

for i in range(frequency):
    print(f"========猜數字遊戲第{i+1}次=========\n\n")
    min = 1
    max = 100
    count = 0
    target = random.randint(min,max)
    print(target)
    while(True):
        keyin = int(input(f"猜數字範圍{min}~{max}:"))
        count += 1
        if(keyin>=min and keyin<=max):
            if target == keyin:
                print(f"賓果!猜對了, 答案是:{target}")
                print(f"{name}共猜了{count}次\n")
                break
            elif(keyin > target):
                print(f"猜錯了!再小一點")
                max = keyin - 1
            else:
                print(f"猜錯了!再大一點")
                min = keyin + 1
            print(f"{name}已經猜{count}次\n")
        else:
            print("請輸入提示範圍內的數字\n")

print(f"遊戲結束,{name}共玩了{frequency}次")


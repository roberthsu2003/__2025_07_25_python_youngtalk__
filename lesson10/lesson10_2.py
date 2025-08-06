import argparse
import random

def input_names(players:list[dict]):
    parser = argparse.ArgumentParser(description="猜數字遊戲")
    parser.add_argument("-m", "--master",type=str, help = "保持者")
    parser.add_argument("-c", "--challenger",type=str, help = '挑單者')
    args = parser.parse_args()

    if not (args.master):
        hostname = input("請輸入保持者姓名:")
    else:
        hostname = args.master
    
    if not (args.challenger):
        challenger_name = input("請輸入挑單者姓名:")
    else:
        challenger_name = args.challenger
    
    players[0]["name"] = hostname
    players[0]['roler'] = 'host'

    players[1]['name'] = challenger_name
    players[1]['roler'] = 'challenger'

       
def play_games(players:list[dict]):
    for player in players:        
        print(f"========{player['name']:}猜數字遊戲=========\n\n")
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
                    print(f"你共猜了{count}次\n")
                    break
                elif(keyin > target):
                    print(f"猜錯了!再小一點")
                    max = keyin - 1
                else:
                    print(f"猜錯了!再大一點")
                    min = keyin + 1
                    print(f"您已經猜{count}次\n")
            else:
                print("請輸入提示範圍內的數字\n")
        player['play_times'] = count
        print(f"{player['name']},猜了{player['play_times']}")

    

def main():
    players = [
        {"name":"","play_times":0,"roler":""},
        {"name":"","play_times":0,"roler":""}
    ]
    print("1.player初始化完成")

    input_names(players)
    print(players)
    print("2.取得資訊完成")

    play_games(players)
    print("3.遊戲結束")


#todo:輸出比賽結果


if __name__ == "__main__":
    main()
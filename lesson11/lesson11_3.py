import random
from typing import Literal

class GuessGesture():
    @staticmethod
    def input_gesture() -> Literal[0 ,1 ,2 ,'q']:
        while True:
            gesture = input("輸入0:剪刀/1:石頭/2:布(輸入q退出):")
            if gesture == "0":
                return 0
            elif gesture == "1":
                return 1
            elif gesture == "2":
                return 2
            elif gesture == "q":
                return "q"
            else:
                print("請輸入正確選項")

    @staticmethod
    def compare(player_gesture: int, opponent_gesture: int, record: dict):
        #0:剪刀
        #1:石頭
        #2:布
        if (player_gesture == 0 and opponent_gesture == 2)\
            or (player_gesture == 1 and opponent_gesture == 0)\
            or (player_gesture == 2 and opponent_gesture == 1):
            print("你贏了!")
            record["勝"] += 1
        elif player_gesture == opponent_gesture:
            print("平手!")
            record["平"] += 1
        else:
            print("你輸了!")
            record["敗"] += 1

def main():
    gestures = ["剪刀","石頭","布"]
    record = {"勝":0,"敗":0,"平":0}
    print("\n=======猜拳遊戲=======\n")

    while True:
        player_gesture = GuessGesture.input_gesture()
        if player_gesture == "q":
            print(f"遊戲結束,你的成績是:{record['勝']}勝,{record['敗']}敗,{record['平']}平")
            break

        computer_gesture = random.randint(0,2)
        print(f"你出了{gestures[player_gesture]}")
        print(f"電腦出了{gestures[computer_gesture]}")
        GuessGesture.compare(player_gesture,computer_gesture,record)
        print(f"目前成績:{record['勝']}勝,{record['敗']}敗,{record['平']}平\n")
        
            

if __name__ == "__main__":
    main()
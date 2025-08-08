import random
from typing import Literal

def input_gesture():
    """
    提示用戶輸入剪刀、石頭或布，並將其轉換為對應的整數值。
    剪刀=0，石頭=1，布=2。輸入'q'則退出。
    若輸入無效，會提示重新輸入。
    
    Returns:
        int or str: 用戶選擇的手勢（0, 1, 2）或'q'（退出）。
    """

def compare(player_gesture, opponent_gesture, record):
    """
    比較玩家和電腦的手勢，並根據結果更新戰績紀錄。
    
    Args:
        player_gesture (int): 玩家選擇的手勢（0, 1, 2）。
        opponent_gesture (int): 電腦隨機選擇的手勢（0, 1, 2）。
        record (dict): 用於記錄勝、敗、平次數的字典。
    """


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
        player_gesture = input_gesture()
        if player_gesture == "q":
            print(f"遊戲結束,你的成績是:{record['勝']}勝,{record['敗']}敗,{record['平']}平")
            break

        computer_gesture = random.randint(0,2)
        print(f"你出了{gestures[player_gesture]}")
        print(f"電腦出了{gestures[computer_gesture]}")
        compare(player_gesture,computer_gesture,record)
        print(f"目前成績:{record['勝']}勝,{record['敗']}敗,{record['平']}平\n")
        
            

if __name__ == "__main__":
    main()
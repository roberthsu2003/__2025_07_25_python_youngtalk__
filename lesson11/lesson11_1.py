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

    """
    猜拳遊戲主流程函數。
    控制遊戲流程、顯示結果並統計玩家戰績。
    """

def input_gesture()->Literal[0, 1, 2, 'q'] :
    while True:
        gesture = input("輸入0:剪刀/1:石頭/2:布(輸入q退出):")
        if gesture == "0":
            gesture = 0
            break
        elif gesture == "1":
            gesture = 1
            break
        elif gesture == "2":
            gesture = 2
            break
        elif gesture == "q":
            break
        else:
            print("請輸入正確選項")
    return gesture

def compare(player_gesture,opponent_gesture,record):
    if player_gesture - 1 == opponent_gesture or opponent_gesture - 2 == player_gesture:
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

        opponent_gesture = random.randint(0,2)
        print(f"你出了{gestures[player_gesture]}")
        print(f"電腦出了{gestures[opponent_gesture]}")
        compare(player_gesture,opponent_gesture,record)
        print(f"目前成績:{record['勝']}勝,{record['敗']}敗,{record['平']}平\n")
        
            

if __name__ == "__main__":
    main()
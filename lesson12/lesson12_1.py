import random
from tools import GuessGesture

def main():    
    print("\n=======猜拳遊戲=======\n")

    while True:
        player_gesture = GuessGesture.input_gesture()
        if player_gesture == "q":
            print(f"遊戲結束,你的成績是:{GuessGesture.record['勝']}勝,{GuessGesture.record['敗']}敗,{GuessGesture.record['平']}平")
            break

        computer_gesture = random.randint(0,2)
        print(f"你出了{GuessGesture.gestures[player_gesture]}")
        print(f"電腦出了{GuessGesture.gestures[computer_gesture]}")
        GuessGesture.compare(player_gesture,computer_gesture)
        print(f"目前成績:{GuessGesture.record['勝']}勝,{GuessGesture.record['敗']}敗,{GuessGesture.record['平']}平\n")
        
            

if __name__ == "__main__":
    main()
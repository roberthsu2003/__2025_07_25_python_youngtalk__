import argparse
import game
def parse_name()->str:
    parser = argparse.ArgumentParser(description="猜數字遊戲")
    parser.add_argument("-n", "--name",type=str, help = "姓名")
    args = parser.parse_args()

    if not args.name:
        name = input("請輸入姓名:")
    else:
        name = args.name
    
    return name

def main():    
    name:str = parse_name()
    playCount:int = 0
    while(True):
        game.play_game()
        playCount += 1
        play_again:str = input("您還要繼續嗎(y,n):")
        if play_again == 'n':
            break
    print(f"{name}:遊戲結束,您共玩{playCount}次")

if __name__ == '__main__':
    main()
    
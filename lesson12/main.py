import random
from collections import Counter

class DiceGame:
    def __init__(self):
        self.total_score = 0
        self.round_count = 0
    
    def roll_dice(self):
        """擲出4個骰子，每個骰子點數1-6"""
        return [random.randint(1, 6) for _ in range(4)]
    
    def calculate_score(self, dice):
        """根據PRD規則計算分數"""
        # 統計每個點數出現的次數
        counter = Counter(dice)
        
        # 檢查是否有4個相同
        if 4 in counter.values():
            same_number = [num for num, count in counter.items() if count == 4][0]
            if same_number == 6:
                return 18
            elif same_number == 5:
                return 17
            elif same_number == 4:
                return 16
            elif same_number == 3:
                return 15
            elif same_number == 2:
                return 14
            elif same_number == 1:
                return 13
        
        # 檢查是否有3個相同（不算分，需要重新擲）
        if 3 in counter.values():
            return None  # 需要重新擲
        
        # 檢查是否有2個相同
        pairs = [num for num, count in counter.items() if count == 2]
        
        if len(pairs) == 2:
            # 兩對的情況，計算比較大的分數
            pair1_score = pairs[0] * 2
            pair2_score = pairs[1] * 2
            return max(pair1_score, pair2_score)
        elif len(pairs) == 1:
            # 一對的情況，另外兩個骰子相加
            pair_number = pairs[0]
            other_dice = [num for num in dice if num != pair_number]
            return sum(other_dice)
        else:
            # 沒有相同，需要重新擲
            return None
    
    def display_dice(self, dice):
        """顯示骰子結果"""
        print(f"骰子結果: {dice[0]}, {dice[1]}, {dice[2]}, {dice[3]}")
    
    def play_round(self):
        """進行一輪遊戲"""
        self.round_count += 1
        print(f"\n=== 第 {self.round_count} 輪 ===")
        
        while True:
            dice = self.roll_dice()
            self.display_dice(dice)
            
            score = self.calculate_score(dice)
            
            if score is None:
                print("沒有符合計分條件，重新擲骰子！")
                input("按 Enter 繼續...")
                continue
            else:
                print(f"本輪得分: {score} 分")
                self.total_score += score
                print(f"總分: {self.total_score} 分")
                break
    
    def play_game(self):
        """主遊戲循環"""
        print("歡迎來到擲骰子遊戲！")
        print("\n遊戲規則:")
        print("- 每次擲出4個骰子")
        print("- 4個相同數字有特殊分數 (6:18分, 5:17分, 4:16分, 3:15分, 2:14分, 1:13分)")
        print("- 2個相同數字: 另外2個骰子相加為分數")
        print("- 兩對相同: 計算較大的對子分數")
        print("- 3個相同或沒有相同: 重新擲骰")
        
        while True:
            print("\n選擇操作:")
            print("1. 擲骰子")
            print("2. 查看總分")
            print("3. 重新開始")
            print("4. 退出遊戲")
            
            choice = input("請輸入選項 (1-4): ").strip()
            
            if choice == "1":
                self.play_round()
            elif choice == "2":
                print(f"目前總分: {self.total_score} 分")
                print(f"已進行輪數: {self.round_count} 輪")
            elif choice == "3":
                self.total_score = 0
                self.round_count = 0
                print("遊戲重新開始！")
            elif choice == "4":
                print(f"遊戲結束！最終得分: {self.total_score} 分")
                print("謝謝遊玩！")
                break
            else:
                print("請輸入正確的選項 (1-4)")

if __name__ == "__main__":
    game = DiceGame()
    game.play_game()

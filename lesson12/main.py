import random
from collections import Counter

class Player:
    def __init__(self, name):
        self.name = name
        self.total_score = 0
        self.rounds_won = 0

class DiceGame:
    def __init__(self):
        self.player1 = Player("玩家1")
        self.player2 = Player("玩家2")
        self.round_count = 0
        self.target_score = 50  # 目標分數，可以調整
    
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
    
    def display_dice(self, dice, player_name):
        """顯示骰子結果"""
        print(f"{player_name} 的骰子結果: {dice[0]}, {dice[1]}, {dice[2]}, {dice[3]}")
    
    def player_turn(self, player):
        """單個玩家的回合"""
        print(f"\n--- {player.name} 的回合 ---")
        input(f"{player.name} 按 Enter 擲骰子...")
        
        while True:
            dice = self.roll_dice()
            self.display_dice(dice, player.name)
            
            score = self.calculate_score(dice)
            
            if score is None:
                print("沒有符合計分條件，重新擲骰子！")
                input("按 Enter 繼續...")
                continue
            else:
                print(f"{player.name} 本輪得分: {score} 分")
                player.total_score += score
                print(f"{player.name} 總分: {player.total_score} 分")
                return score
    
    def play_round(self):
        """進行一輪比賽，兩個玩家輪流擲骰"""
        self.round_count += 1
        print(f"\n{'='*50}")
        print(f"第 {self.round_count} 輪比賽開始！")
        print(f"{'='*50}")
        
        # 玩家1的回合
        score1 = self.player_turn(self.player1)
        
        # 玩家2的回合
        score2 = self.player_turn(self.player2)
        
        # 判定本輪勝負
        print(f"\n--- 第 {self.round_count} 輪結果 ---")
        if score1 > score2:
            print(f"🎉 {self.player1.name} 獲勝！({score1} vs {score2})")
            self.player1.rounds_won += 1
        elif score2 > score1:
            print(f"🎉 {self.player2.name} 獲勝！({score2} vs {score1})")
            self.player2.rounds_won += 1
        else:
            print(f"🤝 平手！({score1} vs {score2})")
        
        # 顯示目前比分
        self.display_scores()
    
    def display_scores(self):
        """顯示目前比分"""
        print(f"\n--- 目前比分 ---")
        print(f"{self.player1.name}: {self.player1.total_score} 分 (贏了 {self.player1.rounds_won} 輪)")
        print(f"{self.player2.name}: {self.player2.total_score} 分 (贏了 {self.player2.rounds_won} 輪)")
    
    def check_winner(self):
        """檢查是否有玩家達到目標分數"""
        if self.player1.total_score >= self.target_score:
            return self.player1
        elif self.player2.total_score >= self.target_score:
            return self.player2
        return None
    
    def reset_game(self):
        """重設遊戲"""
        self.player1.total_score = 0
        self.player1.rounds_won = 0
        self.player2.total_score = 0
        self.player2.rounds_won = 0
        self.round_count = 0
    def play_game(self):
        """主遊戲循環"""
        print("🎲 歡迎來到雙人擲骰子競賽遊戲！🎲")
        print("\n遊戲規則:")
        print("- 每次擲出4個骰子")
        print("- 4個相同數字有特殊分數 (6:18分, 5:17分, 4:16分, 3:15分, 2:14分, 1:13分)")
        print("- 2個相同數字: 另外2個骰子相加為分數")
        print("- 兩對相同: 計算較大的對子分數")
        print("- 3個相同或沒有相同: 重新擲骰")
        print(f"- 🏆 先達到 {self.target_score} 分的玩家獲勝！")
        
        # 讓玩家設定名稱
        player1_name = input("\n請輸入玩家1的名稱 (按Enter使用預設): ").strip()
        if player1_name:
            self.player1.name = player1_name
            
        player2_name = input("請輸入玩家2的名稱 (按Enter使用預設): ").strip()
        if player2_name:
            self.player2.name = player2_name
        
        while True:
            print(f"\n{'='*50}")
            print("選擇操作:")
            print("1. 開始新一輪比賽")
            print("2. 查看目前比分")
            print("3. 設定目標分數")
            print("4. 重新開始遊戲")
            print("5. 退出遊戲")
            print(f"{'='*50}")
            
            choice = input("請輸入選項 (1-5): ").strip()
            
            if choice == "1":
                self.play_round()
                
                # 檢查是否有獲勝者
                winner = self.check_winner()
                if winner:
                    print(f"\n🎊 恭喜 {winner.name} 獲得最終勝利！🎊")
                    print(f"最終分數: {winner.total_score} 分")
                    print("遊戲結束！")
                    
                    restart = input("是否要重新開始？(y/n): ").strip().lower()
                    if restart == 'y':
                        self.reset_game()
                        print("遊戲重新開始！")
                    else:
                        break
                        
            elif choice == "2":
                self.display_scores()
                
            elif choice == "3":
                try:
                    new_target = int(input(f"請輸入新的目標分數 (目前: {self.target_score}): "))
                    if new_target > 0:
                        self.target_score = new_target
                        print(f"目標分數已設定為 {self.target_score} 分")
                    else:
                        print("目標分數必須大於0")
                except ValueError:
                    print("請輸入有效的數字")
                    
            elif choice == "4":
                self.reset_game()
                print("遊戲重新開始！")
                
            elif choice == "5":
                print("\n遊戲結束！")
                self.display_scores()
                print("謝謝遊玩！")
                break
            else:
                print("請輸入正確的選項 (1-5)")
    
if __name__ == "__main__":
    game = DiceGame()
    game.play_game()

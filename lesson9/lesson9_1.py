def calculate_bmi(weight:float, height:float) -> float:
    if weight <= 0 or height <= 0:
        raise ValueError("輸入的體重與身高需為大於 0")
    bmi = weight / ((height / 100) ** 2)
    return  bmi

def classify_bmi(bmi:float)->str:
    if bmi < 18.5:
        return "體重過輕"
    elif bmi < 24:
        return  "體重正常"
    elif bmi < 27:
        return  "過重"
    elif bmi < 30:
        return  "輕度肥胖"
    elif bmi < 35:
        return  "中度肥胖"
    else:
        return  "重度肥胖"

def suggest_weight_range(height:float)->tuple[float]:
    min_bmi = 18.5
    max_bmi = 24
    min_weight = min_bmi * ((height / 100) ** 2)
    max_weight = max_bmi * ((height / 100) ** 2)
    return min_weight, max_weight

def main():
    print("✷" * 7, "計算BMI", "✷" * 7)
    try:
        weight:float = float(input("輸入體重 (kg): "))
        height:float = float(input("輸入身高 (cm): "))
        bmi:float = calculate_bmi(weight, height)

        print("\n======= 結果 =======")
        print(f"體重: {weight:.1f} kg")
        print(f"身高: {height:.1f} cm")
        print(f"BMI: {bmi:.2f}")

        status:str = classify_bmi(bmi)
        print(f"判定: {status}")

        if not (18.5 <= bmi < 24):
            min_w, max_w = suggest_weight_range(height)
            print(f"建議健康體重範圍: {min_w:.1f}kg ~ {max_w:.1f}kg")

    except ValueError as ve:
        print(f"錯誤: {ve}")
        
if __name__ == "__main__":
     main()
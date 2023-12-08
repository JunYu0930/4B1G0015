class Fruit:
  def __init__(self, name, weight, value):
    self._name = name
    self._weight = weight
    self._value = value

  def Calculate(self):
    return self._weight*self._value
  
obj_apple_1 = Fruit ("Apple", 300, 0.05)
obj_banana_2 = Fruit ("Banana", 200, 0.02)
obj_watermelin_3 = Fruit ("Watermelin", 1300, 0.015)
print(obj_apple_1._name)
print("weight=",obj_apple_1._weight * obj_apple_1._value)
print(obj_banana_2._name)
print("weight=",obj_banana_2._weight * obj_banana_2._value)
print(obj_watermelin_3._name)
print("weight=",obj_watermelin_3._weight * obj_watermelin_3._value)
 
class 每日運動量:
    def __init__(self, 輸入的運動名稱, 輸入的運動時間分鐘, 輸入的單位時間消耗的卡數):
        self._運動名稱 = 輸入的運動名稱
        self._運動時間分鐘 = 輸入的運動時間分鐘
        self._單位時間消耗的卡數 = 輸入的單位時間消耗的卡數

    def 計算運動時間內所消耗總卡路里數(self):
        return self._運動時間分鐘*self._單位時間消耗的卡數

daily_exercise_1 = 每日運動量("跑步", 30, 10)
daily_exercise_2 = 每日運動量("游泳", 50, 20)
total_kcal = daily_exercise_1.計算運動時間內所消耗總卡路里數()+daily_exercise_2.計算運動時間內所消耗總卡路里數()
print(f'每日運動量統計: {daily_exercise_1._運動名稱}+{daily_exercise_2._運動名稱} 消耗總卡路里數= {total_kcal}')
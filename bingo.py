import random

random_list = random.sample(range(1, 76), 75)

rireki = []


for i in range(75):
    input("エンターキーを押すと数字を表示")  
    selected_number = random_list[i]
    rireki.append(selected_number)
    
    
    print(f"今回の数字: {selected_number}")
    print(f"これまでの履歴: {rireki}")


print(f"すべての数字: {random_list}")




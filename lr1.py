#Задано одновимірний масив з 20 елементів. Для ініціалізації використайте функцію random().
#Перетворіть його у двовимірний. Кожен елемент масиву збільшити на 10. Результат виведіть у
#файл та на екран. 

#з використанням бібліотеки numpy
import numpy as np
import random 
import time

start_time1 = time.perf_counter()

array1 = np.random.randint(1, 10, size = 20)
array2 = array1.reshape(4,5)

print(f"Одновимірний масив = {array1}")
print(f"Двовимірний масив = {array2}")
print(f"Двовимірний масив збільшений на 10 = {array2 + 10}")

end_time1 = time.perf_counter()
print("--------------------------")

#без використання бібліотеки numpy
start_time2 = time.perf_counter()

array3 = [random.randint(1,10) for _ in range(20)]
print(f"Одновимірний масив без numpy = {array3}")

array_copy = array3[:]
res = [[array_copy.pop(0) for _ in range(5)] for _ in range(4)]

increment = 10

for i in range(len(res)):
    for j in range(len(res[i])):
        res[i][j] += increment

print("Двовимірний масив збільшений на 10 без numpy:")
for row in res:
        print(row)

end_time2 = time.perf_counter()

print(f"Час з використанням бібліотеки numpy = {end_time1 - start_time1}")
print(f"Час без використанням бібліотеки numpy ={end_time2 - start_time2}")

with open('result.txt', 'w') as file1:
    file1.write(f"Одновимірний масив = {array1}\n")
    file1.write(f"Двовимірний масив = {array2}\n")
    file1.write(f"Двовимірний масив збільшений на 10 = {array2 + 10}\n")
    file1.write(f"Одновимірний масив без numpy= {array3}\n")
    file1.write("Двовимірний масив без numpy:\n")
    for row in res:
        file1.write('[' + '\t'.join(map(str, row)) + ']\n')
    file1.write(f"Час з використанням бібліотеки numpy = {end_time1 - start_time1}\n")
    file1.write(f"Час без використанням бібліотеки numpy ={end_time2 - start_time2}\n")
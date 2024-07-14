grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = list(students) #Преобразуем множество в список
students_alphabet = sorted(students) #Отсортируем имена по алфавиту
average_1 = (float(sum(grades[0])/len(grades[0]))) #Среднее оценки
average_2 = (float(sum(grades[1])/len(grades[1])))
average_3 = (float(sum(grades[2])/len(grades[2])))
average_4 = (float(sum(grades[3])/len(grades[3])))
average_5 = (float(sum(grades[4])/len(grades[4])))
marks_list = [average_1, average_2, average_3, average_4, average_5] #Формирование списка
results = dict(zip(students_alphabet, marks_list)) #Преобразование в словарь
print(results)
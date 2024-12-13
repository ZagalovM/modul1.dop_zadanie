#Задание "Средний балл"
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = ({'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'})
average_rating = {} #пустой словарь
names = list(students) #изменил множество в список(ТОТ САМЫЙ ДРУГОЙ "ТИП")
names.sort() #отсортировал список
average_rating.update({names[0]:sum(grades[0])/len(grades[0])})
average_rating.update({names[1]:sum(grades[1])/len(grades[1])})
average_rating.update({names[2]:sum(grades[2])/len(grades[2])})
average_rating.update({names[3]:sum(grades[3])/len(grades[3])})
average_rating.update({names[4]:sum(grades[3])/len(grades[4])})
print(average_rating)

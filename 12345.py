grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
sort = sorted(list(students))
a = {sort[0]: sum(grades[0]) / len(grades[0]), sort[1]: sum(grades[1]) / len(grades[1])}



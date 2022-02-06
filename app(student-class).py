from student import student

student1 = student("Fulgent", "Computer Science", 1.7611, False)
# >>> Access the datas from datatypes
print(student1.GPA)
"""
... object is the data itself while class is what describes the datatype
"""
student2 = student("Catherine", "Business Management", None, False)
print(student2.is_on_suspension)


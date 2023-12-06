number = int(input('Enter the student quantity: '));
students = [];
genders = [];

for i in range(number):
    name = input(f'Enter the student name: ');
    gender = input(f'Enter the student gender (M/F): ').upper();
    grades = []
    
    for n in range(4):
        grade = float(input(f'Enter {n}° grade: '));
        grades.append(grade)
    
    students.append({"Name": name, "Grades": grades, "Gender": gender })
    genders.append(gender);
    
avgs = [] ;
avg_gender = {"M": [], "F": []};
    
for student in students:
    name = student["Name"];
    grade = student["Grades"];
    gender = student["Gender"];
    
    avg = sum(grade) / len(grade);
    avgs.append(avg);
    avg_gender[gender].append(avg);
    
    print(f"Student's number: {i+1}");
    print(f'Name: {name}');
    print(f'Gender: {gender}');
    
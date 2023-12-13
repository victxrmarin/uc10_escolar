import matplotlib.pyplot as plt;

number = int(input('Enter the student quantity: '));
students = [];
genders = [];

for i in range(number):
    name = input(f'Enter the student name: ');
    gender = input(f'Enter the student gender (M/F): ').upper();
    grades = []
    
    for n in range(4):
        grade = float(input(f'Enter {n + 1}° grade: '));
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
    
    plt.figure(figsize=(8,4));
    plt.bar(range(number), avgs, tick_label=[student["Name"] for student in students]);
    plt.xlabel("Students");
    plt.ylabel("Average");
    plt.title("Students Averages");
    plt.savefig("students_avg.png");
    plt.show();
    
    genders = list(avg_gender.keys());
    avg_per_gender = [sum(avg_gender[gender]) / len(avg_gender[gender]) for gender in genders];
    
    plt.figure(figsize=(4, 4));
    plt.bar(genders, avg_per_gender);
    plt.xlabel('Gender');
    plt.ylabel('Average grades');
    plt.title("Gender Averages");
    plt.savefig("genders_avg.png");
    plt.show();
    
    
    
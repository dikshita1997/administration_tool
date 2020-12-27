import csv

def write_into_csv(info_list):
    with open('student_info.csv','a',newline='') as csv_file:
        writer = csv.writer(csv_file)
        if csv_file.tell() == 0:
            writer.writerow({"Name","Age","Contact","Email"})
        writer.writerow(info_list)

condition = True
if __name__ == '__main__':
    while condition:
        student_info = input("Enter student information in the format(Name Age Contact Email)")
        print("Entered Info",student_info)

        student_info_list = student_info.split(' ')
        print("Entered information is", student_info_list)
        write_into_csv(student_info_list)
        condition_check = input("Enter yes or no if you want to enter information")
        if condition_check=="yes":
            condition = True
        elif condition_check == "no":
            condition = False

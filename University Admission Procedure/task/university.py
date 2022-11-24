dep_list = ["Biotech", "Chemistry", "Engineering", "Mathematics", "Physics"]  # dep list in correct order
# GPA position in string for each  in str posit
dep_post_dict = {'Biotech': [2, 3], 'Chemistry': 3, 'Engineering': [4, 5], 'Mathematics': 4, 'Physics': [2, 4]}

result_list = [[], [], [], [], []]


def internal_sorting(elem):
    """Function for a deep sorting, return keys for soring depend on departament, and GPA vs spec exam comparsion"""
    if type(dep_post_dict[sel_departament]) == list:
        # here if departament has two GPA values for evaluate
        if ((int(elem[dep_post_dict[sel_departament][0]]) + int(elem[dep_post_dict[sel_departament][1]])) / 2) > int(elem[6]):
            # here if student FirstGPA+SecondGPA > SpecialExam score
            return (-(int(elem[dep_post_dict[sel_departament][0]]) + int(elem[dep_post_dict[sel_departament][1]])) / 2, elem[0], elem[1])
    else:
        # here if departament has only one GPA value
        if int(elem[dep_post_dict[sel_departament]]) > float(elem[6]):
            # here if
            return (-int(elem[dep_post_dict[sel_departament]])), elem[0], elem[1]
    # if student has special exam priority, return
    return -float(elem[6]), elem[0], elem[1]


def student_sorting(departament, d_priority, vacant_places_left):
    """Function for sorting students resume's / (str, int, int)"""
    global students_list

    temp_list = [line for line in sorted(students_list, key=internal_sorting) if line[d_priority] == departament]

    # short list to vacant places number
    temp_list = temp_list[:vacant_places_left]

    # delete successful resumes from students resume list
    students_list = [item for item in students_list if item not in temp_list]
    return temp_list


def results_output():
    """Results output function"""
    for n in range(0, 5):
        # print to file
        with open(dep_list[n].lower()+".txt", "w") as r_file:
            for item in result_list[n]:
                if type(dep_post_dict[dep_list[n]]) == list:
                    mean_value = (int(item[dep_post_dict[dep_list[n]][0]]) +
                                  int(item[dep_post_dict[dep_list[n]][1]])) / 2
                    if mean_value < float(item[6]):
                        mean_value = item[6]
                else:
                    mean_value = int(item[dep_post_dict[dep_list[n]]])
                    if mean_value < float(item[6]):
                        mean_value = item[6]
                r_file.write(f"{item[0]} {item[1]} {mean_value}\n")
            r_file.close()


# User input - max number of students for each Depart
max_stud_in_depart = int(input())

# full list of students
students_list = [line.split() for line in open("applicant_list.txt")]

# main cycle, that go through three rows of departaments in students resumes
for m in range(7, 10):
    # cycle go through 5 departaments student list and add into each dep list students
    for n in range(len(dep_list)):
        places_left = max_stud_in_depart - len(result_list[n])
        if places_left > 0:
            sel_departament = dep_list[n]
            result_list[n] += student_sorting(dep_list[n], m, places_left)
            result_list[n].sort(key=internal_sorting)


# final result output
results_output()

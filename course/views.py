from django.shortcuts import render
from datetime import datetime

# Create your views here.
def learn_django(request):
    django_details = {
        'Course_name': 'Django is a Python framework', 
        'Duration': 'Six Months', 
        'Fees': 'Five Thousands', 
        'Seats': False
    }
    return render(request, 'course/courseone.html', django_details)

def know_date_time(request):
    # Return the current date time
    current_dare_time = datetime.now()
    datetime_dict = {'cdt': current_dare_time}
    return render(request, 'course/date_time.html', datetime_dict)

# Floatformat of value
def value_format(request):
    num_dict = {'n1': 56.24321, 'n2': 56.00000, 'n3': 56.37000}
    return render(request, 'course/value_format.html', num_dict)

# Practice Conditional statement - if, else, for etc
def learn_condition(request):
    info = {
        'Name': 'Kazi Mushfiqur Rahman', 
        'Institute': 'MIU', 
        'Subject': 'CSE', 
        'CGPA': 3.80,
        'Hobby': 'Programming',
        'Designation': True,
        'Award': False
    }
    return render(request, 'course/condition.html', info)


def learn_forloop(request):
    students = { 'Names': ['Masum', 'Ashiq', 'Nasim', 'Hasan']}
    return render(request, 'course/forloop.html', students)
    # For empty block
    # return render(request, 'course/forloop.html')


def learn_student_info(request):
    students_info = {
        'student1': {'Name': 'Mushfiq', 'Dept': 'CSE', 'Institute': 'MIU'},
        'student2': {'Name': 'Nasim', 'Dept': 'CSE', 'Institute': 'MIU'},
        'student3': {'Name': 'Minhaz', 'Dept': 'CSE', 'Institute': 'MIU'}
    }
    return render(request, 'course/stuinfo.html', {'students_info': students_info})


def learn_nested_loop(request):
    stuinfo = {
        'student1': {'Name': 'Mushfiq', 'Dept': 'CSE', 'Institute': 'MIU'},
        'student2': {'Name': 'Nasim', 'Dept': 'CSE', 'Institute': 'MIU'},
        'student3': {'Name': 'Minhaz', 'Dept': 'CSE', 'Institute': 'MIU'}
    }
    return render(request, 'course/nestedloop.html', {'stuinfo': stuinfo})
    
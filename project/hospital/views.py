from django.shortcuts import render
from .models import EmployeeData
def index(request):
    return render(request, 'index.html')
 
def apponimant(request):
    return render(request, 'apponimant.html')

def login(request):
    global adminemail
    global adminpass
    global adminName
    adminemail = "pooja0294@gmail.com"
    adminpass = "Pooja@123"
    adminName = "Pooja"
    
    if request.method == 'POST':
        emp_email = request.POST.get('email')
        emp_pass = request.POST.get('password')
        user = EmployeeData.objects.filter(emp_email=emp_email)

        if emp_email == adminemail and emp_pass == adminpass:
            print(emp_email)
            
            return render(request,'admindashboard.html', {'admin_email':adminemail, 'admin_pass':adminpass, 'admin_name': adminName})

        if user.exists():
            user1 = EmployeeData.objects.get(employe_email=emp_email)
            pass1 = user1.emp_password

            if pass1 == emp_pass:
                user= {
                        'name': user1.emp_name,
                        'email': user1.emp_email,
                        'department': user1.emp_dep,
                        'contact': user1.emp_contact,
                        'work': user1.emp_work,
                        'user_id': user1.id   # Ensure user.id exists
                    }
                return render(request, 'userdashboard.html', {'data':user})
            else:
                message = "Email and password do not match"
                return render(request, 'login.html', {'message': message})
        else:
            message2 = "Email ID does not exist"
            return render(request, 'login.html', {'message2': message2})

    return render(request, 'login.html')

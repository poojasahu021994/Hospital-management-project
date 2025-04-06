from django.shortcuts import render
from .models import DoctorData

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
        doc_email = request.POST.get('email')
        doc_pass = request.POST.get('password')
        user = DoctorData.objects.filter(doc_email=doc_email)

        if doc_email == adminemail and doc_pass == adminpass:
            print(doc_email)
            
            return render(request,'admindashboard.html', {'admin_email':adminemail, 'admin_pass':adminpass, 'admin_name': adminName})

        if user.exists():
            user1 = DoctorData.objects.get(employe_email=doc_email)
            pass1 = user1.doc_password

            if pass1 == doc_pass:
                user= {
                        'name': user1.doc_name,
                        'email': user1.doc_email,
                        'department': user1.doc_dep,
                        'contact': user1.doc_contact,
                        'work': user1.doc_work,
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

def home(request):
    return render(request, 'home.html')

def registration(request):
    if request.method=='POST':
           name=request.POST.get('name')
           Email=request.POST.get('email')
           Number=request.POST.get('contact')
           Specialty=request.POST.get('specialty')
           joining=request.POST.get('DOJ')
           department=request.POST.get('department')
           password=request.POST.get('password')
           cpassword=request.POST.get('cpassword')
           print(name,Email,joining,Number,password,cpassword,Specialty,department)
        
           user=DoctorData.objects.filter(doc_email=Email)
           if user:
                x="Email already exist"
                return render(request,'registration.html',{'msg':x})
           else:
                if password==cpassword:
                    DoctorData.objects.create(employe_name=name,employe_email=Email,contact_number=Number,date_of_joining=joining,department=department, employe_password=password)
                    x="Registration Sucessfully"
                    return render(request,'registration.html',{'msg':x})
                else:
                    x="password and confirm password not match"
                    return render(request,'registration.html',{'msg':x,'name':name,'customer_Email':Email,'customer_Number':Number,'password':password})
    else:      
       return render(request, 'registration.html')
    
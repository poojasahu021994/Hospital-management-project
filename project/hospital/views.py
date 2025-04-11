from django.shortcuts import render
from .models import DoctorData
from .models import Department

def index(request):
    return render(request, 'index.html')
 
def apponimant(request):
    return render(request, 'apponimant.html')

def admindeshboard(request):
    return render(request, 'admindeshboard.html' )


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
            return render(request,'admindeshboard.html')

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
           Qualif=request.POST.get('qualification')
           joining=request.POST.get('DOJ')
           department=request.POST.get('department')
           dep = Department.objects.get(dep_description=department)
           dep_id =dep.id
           password=request.POST.get('password')
           cpassword=request.POST.get('cpassword')
           print(name,Email,joining,Number,password,cpassword,Qualif,department,type(dep_id))
        
           user=DoctorData.objects.filter(doc_email=Email)
           if user:
                x="Email already exist"
                return render(request,'registration.html',{'msg':x})
           else:
                if password==cpassword:
                    DoctorData.objects.create(doc_name=name,doc_email=Email,doc_contact=Number,doc_Que=Qualif,doc_DOJ=joining,doc_dep=dep,doc_password=password)
                    x="Registration Sucessfully"
                    return render(request,'registration.html',{'msg':x})
                else:
                    x="password and confirm password not match"

                    return render(request,'registration.html',{'msg':x,'name':name,'customer_Email':Email,'customer_Number':Number,'password':password})
    else:  
       dep_data = Department.objects.all()   
       return render(request, 'registration.html',{'data':dep_data})
# def department(request):
#     return render(request,'department.html')

def department(request):
    if request.method=="POST":
        dep_name=request.POST.get('dep_name')
        dep_description=request.POST.get('dep_description')
        dep_HOD=request.POST.get('dep_HOD')
        depdata=Department.objects.create(dep_name=dep_name,dep_description=dep_description,dep_Hod=dep_HOD)
        depdata1=Department.objects.all()
        # if depdata1:
        #     user={
        #         'name':depdata1.dep_name,
        #         'desc':depdata1.dep_description,
        #         'hod':depdata1.dep_Hod
        #     }
        # print(user)
        # print(depdata1)
        return render(request,'department.html', {'data':depdata1.values})
    depdata1=Department.objects.all() 
    return render(request,'department.html',{'data':depdata1.values})

def doctorReports(request):
    mydata=DoctorData.objects.all()
    doc_count=mydata.count()
    print(doc_count)
    return render(request,'doctorReports.html', {'data':mydata, 'count':doc_count})
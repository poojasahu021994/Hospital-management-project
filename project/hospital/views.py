from django.shortcuts import render
from .models import DoctorData
from .models import Department
from .models import PatientData
from django.contrib.auth.hashers import check_password

def index(request):
    return render(request, 'index.html')
 
def appointments(request):
    dep_data = Department.objects.all()
    doc_name=DoctorData.objects.all()
    return render(request, 'appointments.html',{'data':dep_data, 'data1':doc_name})

def admindeshboard(request):
    return render(request, 'admindeshboard.html' )

# def login_view(request):
#     if request.method == 'POST':
        # patient_email = request.POST.get('patientemail')
        # patient_password = request.POST.get('password')

        # try:
        #     patient = PatientData.objects.get(patient_email=patient_email)
            
        #     # Check hashed password securely
        #     # if check_password(patient_password, patient.patient_password):
        #     pass1 = patient.patient_password

        #     if pass1 == patient_password:
        #         user = {
        #             'name': patient.patient_name,
        #             'email': patient.patient_email,
        #             'dob': patient.patient_DOB,
        #             'contact': patient.patient_contact,
        #             'address': patient.patient_add,
        #             'user_id': patient.id
        #         }
        #         return render(request, 'appointments.html', {'data': user})
        #     else:
        #         # Wrong password
        #         return render(request, 'login.html', {'error': 'Invalid credentials'})
        
        # except PatientData.DoesNotExist:
        #     # User not found
        #     return render(request, 'login.html', {'error': 'User does not exist'})



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
        patient_email = request.POST.get('patientemail')
        patient_password = request.POST.get('password')

        try:
            patient = PatientData.objects.get(patient_email=patient_email)
            
            # Check hashed password securely
            # if check_password(patient_password, patient.patient_password):
            pass1 = patient.patient_password

            if pass1 == patient_password:
                user = {
                    'name': patient.patient_name,
                    'email': patient.patient_email,
                    'dob': patient.patient_DOB,
                    'contact': patient.patient_contact,
                    'address': patient.patient_add,
                    'user_id': patient.id
                }
                return render(request, 'appointments.html', {'data': user})
            else:
                # Wrong password
                return render(request, 'login.html', {'error': 'Invalid credentials'})
        
        except PatientData.DoesNotExist:
            # User not found
            return render(request, 'login.html', {'error': 'User does not exist'})

        # patient login
        # patient_email=request.POST.get('patientemail')
        # patient_password=request.POST.get('password')
        # patient=PatientData.objects.filter(patient_email=patient_email)
        # if patient.exists():
        #     patient1 = PatientData.objects.get(patient_email=patient_email)
        #     pass1 = patient1.patient_password

        #     if pass1 == patient_password:
        #         user= {
        #                 'name': patient1.patient_name,
        #                 'email': patient1.patient_email,
        #                 'dob': patient1.patient_DOB,
        #                 'contact': patient1.patient_contact,
        #                 'address': patient1.patient_add,
        #                 'user_id': patient1.id   # Ensure user.id exists
        #             }
        #         return render(request, 'appointments.html', {'data':user})

        if doc_email == adminemail and doc_pass == adminpass:
            return render(request,'admindeshboard.html')

        if user.exists():
            user1 = DoctorData.objects.get(doc_email=doc_email)
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
                return render(request, 'doctordeshboard.html', {'data':user})
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


def department(request):
    if request.method=="POST":
        dep_name=request.POST.get('dep_name')
        dep_description=request.POST.get('dep_description')
        dep_HOD=request.POST.get('dep_HOD')
        depdata=Department.objects.create(dep_name=dep_name,dep_description=dep_description,dep_Hod=dep_HOD)
        depdata1=Department.objects.all()
        return render(request,'department.html', {'data':depdata1.values})
    depdata1=Department.objects.all() 
    return render(request,'department.html',{'data':depdata1.values})

# Doctor deshboard
def doctordeshboard(request):
    return render(request,'doctordeshboard.html')

# doctore reports
def doctorReports(request):
    mydata=DoctorData.objects.all()
    doc_count=mydata.count()
    print(doc_count)
    return render(request,'doctorReports.html', {'data':mydata, 'count':doc_count})

# Logout function
def Logout(request):
    return render(request,'login.html')

# profile function
def doctorprofile(request, pk):  
    user = DoctorData.objects.filter(id=pk).first()   # Get the user by primary key  
    print(user)  # Debugging to see if user exists
    
    if user:  
         user= {
            'name': user.doc_name,
            'email': user.doc_email,
            'department': user.doc_dep,
            'contact': user.doc_contact,
            'Qualification': user.doc_Que,
            'user_id': user.id   # Ensure user.id exists
        }
         return render(request, 'doctorprofile.html', {'data': user})
    
    return render(request, 'doctorprofile.html', {'error': 'User not found'}) 

# delete function
def removedoctor(request,pk):
    print(pk)
    data=DoctorData.objects.get(id=pk)
    data.delete()
    stu=DoctorData.objects.all()
    
    return render(request,'admindeshboard.html',{'data':stu.values})

# patient resigtration
def patientRegister(request):
    if request.method=='POST':
        patient_name=request.POST.get('patientname')
        patient_email=request.POST.get('patientemail')
        patient_add=request.POST.get('address')
        patient_DOB=request.POST.get('patientdob')
        patient_contact=request.POST.get('patientphone')
        patient_password=request.POST.get('password')
        patient_cpassword=request.POST.get('cpassword')
        print("Hi........")
        print(patient_name,patient_email,patient_add,patient_DOB,patient_contact,patient_password,patient_cpassword)
        user=PatientData.objects.filter(patient_email=patient_email)
        if user.exists():
            x="Email already exist"
            return render(request,'patientregister.html',{'msg':x})
        else:
            if patient_password==patient_cpassword:
                print(patient_cpassword,patient_password)
                PatientData.objects.create(patient_name=patient_name,patient_email=patient_email,patient_add=patient_add,patient_DOB=patient_DOB,patient_contact=patient_contact,patient_password=patient_password)
                x="Registration Sucessfully"
                return render(request,'patientregister.html',{'msg':x})
            else:
                x="password and confirm password not match"

                return render(request,'patientregister.html',{'msg':x,'name':patient_name,'customer_Email':patient_email,'customer_Number':patient_contact,'password':patient_password})
    else:
        return render(request, 'patientregister.html')        

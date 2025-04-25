from django.shortcuts import render
from .models import DoctorData
from .models import Department
from .models import PatientData
from .models import BookingData


def index(request):
    return render(request, 'index.html')
 
def appointments(request):
    dep_data = Department.objects.all()
    doc_name = DoctorData.objects.all()
    if request.method == 'POST':
        P_name=request.POST.get('pname')
        P_email=request.POST.get('pemail')
        P_address=request.POST.get('paddress')
        P_DOB=request.POST.get('pdob')
        P_contact=request.POST.get('pphone')
        P_details=request.POST.get('details')
        select_dep=request.POST.get('department')
        print(select_dep)
        dep = Department.objects.get(dep_description=select_dep)
        print(dep)
        dep_id=dep.id
        print(dep_id)
        select_doc=request.POST.get('select_doc')
        print(select_doc)
        s_doc=DoctorData.objects.get(id=select_doc)
        print(s_doc)
        booking=BookingData.objects.create(P_name=P_name,P_email=P_email,P_address=P_address,P_DOB=P_DOB,P_contact=P_contact,P_details=P_details,select_dep=dep)
        booking.select_doc.set([s_doc])
        x="Booking Suceussfully done"
        return render(request, 'appointments.html', {'msg':x})
    return render(request, 'appointments.html',{'data':dep_data, 'data':doc_name})


def admindeshboard(request):
    return render(request, 'admindeshboard.html' )

def contact(request):
    return render(request, 'Contact.html' )

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
        # patient login
        patient_email=request.POST.get('email')
        patient_password=request.POST.get('password')
        print(patient_email,patient_password)
        patient=PatientData.objects.filter(patient_email=patient_email)
        print(patient)
        if patient.exists():
            patient1 = PatientData.objects.get(patient_email=patient_email)
            print(patient1)
            pass1 = patient1.patient_password
            print(pass1,patient_password)

            if pass1 == patient_password:
                user= {
                        'name': patient1.patient_name,
                        'email': patient1.patient_email,
                        'dob': patient1.patient_DOB,
                        'contact': patient1.patient_contact,
                        'address': patient1.patient_add,
                        'user_id': patient1.id   # Ensure user.id exists
                    }
                return render(request, 'appointments.html', {'data':user})

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

#search bar
# from django.db.models import Q

# def search(request):
#     if request.method=="POST":
#         name=request.POST.get("search")
#     searchdata=DoctorData.objects.filter(Q(doc_name__icontains=name) | Q(doc_email__icontains=name) | Q(doc_dep__icontains=name) | Q(doc_Que__icontains=name) | Q(doc_work__icontains=name))
#     print(searchdata)
#     return render(request,'doctorReports.html',{"Sdata":searchdata})

from django.db.models import Q
from django.shortcuts import render
from .models import DoctorData

def search(request):
    if request.method == "POST":
        name = request.POST.get("searchname", "").strip()
        q_filter = Q(doc_name__icontains=name) | Q(doc_email__icontains=name) | Q(doc_dep__icontains=name) | Q(doc_Que__icontains=name) | Q(doc_work__icontains=name)

        # Only add contact if it's numeric
        if name.isdigit():
            q_filter |= Q(doc_contact=name)

        # Only add DOJ filter if it's a date
        from datetime import datetime
        try:
            date_val = datetime.strptime(name, "%Y-%m-%d").date()
            q_filter |= Q(doc_DOJ=date_val)
        except ValueError:
            pass  # Not a date

        searchdata = DoctorData.objects.filter(q_filter)

        return render(request, 'doctorReports.html', {'data': searchdata, 'count': searchdata.count()})


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


def homeData(request,pk):
    hpatient = PatientData.objects.get(id=pk)
    print(pk)
    user= {
            'name': hpatient.patient_name,
            'email': hpatient.patient_email,
            'dob': hpatient.patient_DOB,
            'contact': hpatient.patient_contact,
            'address': hpatient.patient_add,
            'user_id': hpatient.id   # Ensure user.id exists
        }
    print(id)
    return render(request, 'home.html',{'data':user})

def contactData(request,pk):
    cpatient = PatientData.objects.get(id=pk)
    user= {
            'name': cpatient.patient_name,
            'email': cpatient.patient_email,
            'dob': cpatient.patient_DOB,
            'contact': cpatient.patient_contact,
            'address': cpatient.patient_add,
            'user_id': cpatient.id   # Ensure user.id exists
        }
    return render(request, 'Contact.html',{'data':user})

def appointData(request,pk):
    cpatient = PatientData.objects.get(id=pk)
    user= {
            'name': cpatient.patient_name,
            'email': cpatient.patient_email,
            'dob': cpatient.patient_DOB,
            'contact': cpatient.patient_contact,
            'address': cpatient.patient_add,
            'user_id': cpatient.id   # Ensure user.id exists
        }
    return render(request, 'appointments.html',{'data':user})

# appointReport function
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
# def doctor_appointments(request,pk):
#     # 🧠 Assuming doctor is already logged in and stored in session
#     doctor_id = DoctorData.objects.filter(id=pk)
#     # doctor_id = request.session.get('doctor_id')  # or from request.user if using auth

#     if doctor_id:
#         # Doctor ko DB se lo
#         doctor = DoctorData.objects.get(pk=doctor_id)
#         doctor_data= {
#             'name': doctor.doc_name,
#             'email': doctor.doc_email,
#             'department': doctor.doc_dep,
#             'contact': doctor.doc_contact,
#             'Qualification': doctor.doc_Que,
#             'user_id': doctor.id   # Ensure user.id exists
#         }

#         # Us doctor ke appointments filter karo
#         appointments = BookingData.objects.filter(select_doc=doctor)

#         return render(request, 'doctor_appointment.html', {
#             'appointments': appointments,
#             'data': doctor_data
#         })
#     else:
#         return render("Please login first.")
# def doctor_appointments(request, pk):
#     doctor_id = BookingData.objects.filter(select_doc=pk)
#     print(doctor_id)
    # doctor_id = PatientData.objects.filter(se=pk)
    # if doctor_id:
    #     doctor = DoctorData.objects.get(pk=doctor_id)
    #     doctor_data= {
    #         'user_id': doctor.id   
    #     }
   
    # appointData=BookingData.objects.get(select_doc=doctor)
    # booking_data={
    #         'name': appointData.P_name,
    #         'email': appointData.P_email,
    #         'address': appointData.P_address,
    #         'department': appointData.select_dep ,
    #         'contact': appointData.P_contact,
    #         'DOB': appointData.P_DOB,
    #         'details': appointData.P_details,
    #         'user_id': appointData.id
    # }

    # return render(request, 'doctor_appointment.html', {
    #     'bookings': booking_data,
    #     'data': doctor_data
    # })
from django.shortcuts import render, get_object_or_404
from .models import BookingData, DoctorData

def doctor_appointments(request, pk):
    # Get the doctor instance
    doctor = get_object_or_404(DoctorData, pk=pk)

    # Fetch all bookings for this doctor
    bookings = BookingData.objects.filter(select_doc=doctor)

    # Optionally prepare booking data in a list of dicts
    booking_data = []
    for appoint in bookings:
        booking_data.append({
            'name': appoint.P_name,
            'email': appoint.P_email,
            'address': appoint.P_address,
            'department': appoint.select_dep,
            'contact': appoint.P_contact,
            'DOB': appoint.P_DOB,
            'details': appoint.P_details,
            'user_id': appoint.id
        })

    # Doctor data context (optional)
    doctor_data = {
        'user_id': doctor.id,
        # 'name': doctor.doc_name  # Assuming `DoctorData` has a name field
    }

    return render(request, 'doctor_appointment.html', {
        'bookings': booking_data,
        'data': doctor_data
    })

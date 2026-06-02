from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Job, Application , Company
from .forms import JobForm


def home(request):
    return render(request, 'open_page.html')

def home_redirect(request):

    if 'student_id' in request.session:
        return redirect('student_dashboard')

    elif 'company_id' in request.session:
        return redirect('company_dashboard')

    else:
        return redirect('home')   # your public homepage
    

def student_login_required(request):
    if 'student_id' not in request.session:
        return False
    return True

def get_logged_in_student(request):
    student_id = request.session.get('student_id')
    if not student_id:
        return None
    return Student.objects.filter(id=student_id).first()

# STUDENT REGISTRATION
def student_register(request):
    if request.method == "POST":
        Student.objects.create(
            name=request.POST.get('name').strip(),
            email=request.POST.get('email').strip(),
            branch=request.POST.get('branch').strip(),
            password=request.POST.get('password').strip()
        )
        return redirect('student_login')

    return render(request, 'students/student_register.html')

# STUDENT LOGIN
def student_login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        try:
            student = Student.objects.get(email=email, password=password)

            # STORE SESSION
            request.session['student_id'] = student.id

            return redirect('student_dashboard')

        except Student.DoesNotExist:
            return render(request, "students/student_login.html", {"error": "Invalid login"})

    return render(request, "students/student_login.html")

# STUDENT DASHBOARD
def student_dashboard(request):
    student_id = request.session.get('student_id')
    if not student_id:
        return redirect('student_login')

    student = Student.objects.get(id=student_id)
    return render(request, 'students/student_dashboard.html', {'student': student})

# SEARCH JOBS
def student_search_jobs(request):

    student_id = request.session.get('student_id')
    if not student_id:
        return redirect('student_login')

    student = Student.objects.get(id=student_id)

    applications = Application.objects.filter(student=student)
    applied_jobs = applications.values_list('job_id', flat=True)

    jobs = Job.objects.all()

    context = {
        "jobs": jobs,
        "applied_jobs": applied_jobs
    }

    return render(request, "students/student_search_jobs.html", context)

# APPLY JOB
def apply_job(request, job_id):

    student_id = request.session.get('student_id')
    if not student_id:
        return redirect('student_login')

    student = Student.objects.get(id=student_id)
    job = Job.objects.get(id=job_id)

    if not Application.objects.filter(student=student, job=job).exists():
        Application.objects.create(
            student=student,
            job=job,
            status="Pending"
        )

    return redirect("student_search_jobs")

# APPLICATION STATUS
def student_application_status(request):
    student = get_logged_in_student(request)
    if not student:
        return redirect('student_login')

    applications = (
        Application.objects
        .filter(student=student)
        .select_related('job')
        .order_by('-id')
    )

    return render(
        request,
        'students/student_application_status.html',
        {'applications': applications}
    )

# STUDENT PROFILE
def student_profile(request):
    student = get_logged_in_student(request)
    if not student:
        return redirect('student_login')

    if request.method == "POST":
        student.name = request.POST.get('name')
        student.branch = request.POST.get('branch')
        student.mobile = request.POST.get('mobile')
        student.course = request.POST.get('course')
        student.skills = request.POST.get('skills')

        cgpa = request.POST.get('cgpa')
        student.cgpa = float(cgpa) if cgpa else None

        student.save()
        return redirect('student_profile')

    return render(request, 'students/student_profile.html', {'student': student})

def applied_jobs(request):

    student_id = request.session.get('student_id')
    if not student_id:
        return redirect('student_login')

    student = Student.objects.get(id=student_id)

    applications = Application.objects.filter(student=student).select_related('job', 'job__company')

    return render(request, "students/applied_jobs.html", {"applications": applications})

# LOGOUT
def student_logout(request):
    request.session.flush()
    return redirect('home')
#=============================================company view======================
#COMPANY REGISTRATION
def company_register(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']

        Company.objects.create(
            name=name,
            email=email,
            password=password
        )

        return redirect('company_login')

    return render(request, 'company/company_register.html')

#COMPANY LOGIN
def company_login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        try:
            company = Company.objects.get(email=email, password=password)

            request.session['company_id'] = company.id
            return redirect('company_dashboard')

        except Company.DoesNotExist:
            return render(request, 'company/company_login.html', {'error': 'Invalid credentials'})

    return render(request, 'company/company_login.html')

#COMPANY DASHBOARD
def company_dashboard(request):
    company_id = request.session.get('company_id')

    if not company_id:
        return redirect('company_login')

    company = Company.objects.get(id=company_id)
    jobs = Job.objects.filter(company=company)

    context = {
        'company': company,
        'jobs': jobs
    }
    return render(request, 'company/company_dashboard.html', context)

#POST JOB

def post_job(request):
    company_id = request.session.get('company_id')
    if not company_id:
        return redirect('company_login')

    company = Company.objects.get(id=company_id)
    if request.method == 'POST':
        form = JobForm(request.POST)

        if form.is_valid():
            job = form.save(commit=False)
            job.company = company
            job.save()

            return redirect('company_dashboard')
    else:
        form = JobForm()

    return render(request, 'company/post_job.html', {'form': form})

#VIEW APPLICATIONS FOR A JOB
def view_applicants(request, job_id):

    company_id = request.session.get('company_id')

    if not company_id:
        return redirect('company_login')

    job = Job.objects.get(id=job_id)

    applications = Application.objects.filter(job=job).select_related('student')

    context = {
        'job': job,
        'applications': applications
    }

    return render(request, 'company/view_applicants.html', context)
#COMPANY LOGOUT
def company_logout(request):
    request.session.flush()
    return redirect('home')

def confirm_application(request, id):
    application = get_object_or_404(Application, id=id)
    application.status = "Confirmed"
    application.save()
    return redirect(request.META.get('HTTP_REFERER'))


def reject_application(request, id):
    application = get_object_or_404(Application, id=id)
    application.status = "Rejected"
    application.save()
    return redirect(request.META.get('HTTP_REFERER'))

def update_application_status(request, application_id):
    if request.method == "POST":
        application = get_object_or_404(Application, id=application_id)
        status = request.POST.get("status")

        if status in ["Confirmed", "Rejected"]:
            application.status = status
            application.save()

    return redirect(request.META.get('HTTP_REFERER'))
#=============================================admin view======================

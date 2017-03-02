from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect

from MyApp.models import Employee 
from MyApp.forms import EmployeeForm

# Create your views here.

class WelcomeView(View):
	def get(self, request, *args, **kwargs):
		return render(request, 'login.html')

class LoginView(View):
	def get(self, request):
		try:
			if request.user.is_authenticated():
				return HttpResponseRedirect('/home/')
			else:
				return HttpResponseRedirect('/load/')
		except:
			return HttpResponseRedirect('/load/')

	def post(self, request, *args, **kwargs):
		user = authenticate(username=request.POST.get('user'), 
							password=request.POST.get('password'))
		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/home/')
			else:
				return HttpResponseRedirect('/load/')

		else:
			return HttpResponseRedirect('/load/')


class HomePageView(View):
	def get(self, request, *args, **kwargs):
		try:
			if request.user.is_authenticated():
				emps = Employee.objects.all()
				data = []
				for emp in emps:
					data.append({'name': emp.name,
								 'number': emp.employee_number,
								 'age': emp.age,
								 'email': emp.email,
								 'phone': emp.phone_number,
								 'photo': str(emp.photo.url.split('/')[-1])})
				return render_to_response('home.html',
										  {'user': str(request.user),
										   'data': data})
			else:
				return HttpResponseRedirect('/load/')
		except:
			return HttpResponseRedirect('/load/')

class UpdateView(View):
	def get(self, request, emp_num=None):
		if emp_num and request.user.is_authenticated():
			try:
				emp = Employee.objects.get(employee_number=int(emp_num))
				data = [{'name': emp.name,
						 'number': emp.employee_number,
						 'age': emp.age,
						 'email': emp.email,
						 'phone': emp.phone_number,
						 'photo': str(emp.photo.url.split('/')[-1])}
						]
				return render(request, 'update.html',
							  {'user': str(request.user),
							   'data': data})
			except:
				return HttpResponseRedirect('/home/')
		else:
			return HttpResponseRedirect('/load/') 

class UpdateDataView(View):
	# @csrf_protect
	def post(self, request, *args, **kwargs):
		import pdb
		pdb.set_trace()
		if request.user.is_authenticated():
			try:
				data = request.POST
				obj = Employee.objects.get(employee_number=int(data.get('emp_id')))
				obj.employee_number = data.get('number')
				obj.age = int(data.get('age'))
				obj.name = str(data.get('name'))
				obj.email = str(data.get('email'))
				obj.phone_number = str(data.get('phone'))
				obj.save()
				emps = Employee.objects.all()
				data = []
				for emp in emps:
					data.append({'name': emp.name,
								 'number': emp.employee_number,
								 'age': emp.age,
								 'email': emp.email,
								 'phone': emp.phone_number,
								 'photo': str(emp.photo.url.split('/')[-1])})
				return render('home.html',
							  {'user': str(request.user),
							   'data': data})
			except:
				return HttpResponseRedirect('/home/')
		else:
			return HttpResponseRedirect('/load/')

class DeleteView(View):
	def get(self, request, emp_num=None):
		if emp_num and request.user.is_authenticated():
			try:
				emp = Employee.objects.get(employee_number=int(emp_num))
				emp.delete()
				return HttpResponseRedirect('/home/')
			except:
				return HttpResponseRedirect('/home/')
		else:
			return HttpResponseRedirect('/load/')

class AddEmployee(View):
	def get(self, request, *args, **kwargs):
		if request.user.is_authenticated():
			form = EmployeeForm()
			return render(request, 'add_emp.html', {'form': form})

class AddEmpView(View):
	def post(self, request, *args, **kwargs):
		import pdb
		pdb.set_trace()
		if request.user.is_authenticated():
			form = EmployeeForm(request.POST, request.FILES)
			if form.is_valid():
				form.save()
			return HttpResponseRedirect('/home/')
		else:
			return HttpResponseRedirect('/load/')
		

class LogoutView(View):
	def get(self, request, *args, **kwargs):
		if request.user.is_authenticated():
			logout(request)
			return HttpResponseRedirect('/load/')
		else:
			return HttpResponseRedirect('/load/')
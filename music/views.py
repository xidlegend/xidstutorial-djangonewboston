from django.views import generic  # Generic views make common functions easier like 'list' and 'details'
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy  # Delete album
from django.shortcuts import render, redirect  # redirect module redirects them to a page after they login
from django.contrib.auth import authenticate, login  # authenticate - takes a username and password and verifies that they are a user in the database, login gives them a session id while they are on the site
from django.views.generic import View
from .models import Album
from .forms import UserForm


class IndexView(generic.ListView):
	template_name = 'music/index.html'
	context_object_name = 'albums'  # By default the variable used is object_list you can change that like this

	def get_queryset(self):
		return Album.objects.all()  # Generi List view automatically queries this function to get the list of objects


class DetailView(generic.DetailView):
	model = Album
	template_name = 'music/details.html'


class AlbumCreate(CreateView):
	model = Album
	fields = ['artist', 'album_title', 'genre', 'album_logo']


class AlbumUpdate(UpdateView):
	model = Album
	fields = ['artist', 'album_title', 'genre', 'album_logo']


class AlbumDelete(DeleteView):
	model = Album
	success_url = reverse_lazy('music:index')


class UserFormView(View):
	form_class = UserForm
	template_name = 'music/registration_form.html'

	# display blank form
	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form': form})  # render calls the form template along with the entered information

	# process form data
	def post(self, request):
		form = self.form_class(request.POST)

		if form.is_valid():

			user = form.save(commit=False)  # creates an object from the form but doesent save it into the database

			#clean (normalized data - formated properly, for eg dates)
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.set_password(password)  # function to change the password, this function converts their password to hash and saves them to the database
			user.save()  # thats the line that saves them to the database

			# returns User objects if the credentials are correct, (authenticates)
			user = authenticate(username=username, password=password)

			if user is not None:

				if user.is_active:  # the user is not inactive i.e. banned

					login(request, user)
					return redirect('music:index')

		return render(request, self.template_name, {'form': form})  # render calls the form template along with the entered information



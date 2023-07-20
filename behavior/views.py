import csv
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Student, StudentNote
from .forms import CSVUploadForm, StudentNoteForm


class StudentListView(ListView):
    model = Student
    template_name = 'student_list.html'


class StudentCreateView(CreateView):
    model = Student
    fields = ['first_name', 'last_name']
    template_name = 'student_create.html'
    success_url = reverse_lazy('student_list')


class StudentUpdateView(UpdateView):
    model = Student
    fields = ['first_name', 'last_name']
    template_name = 'student_update.html'
    success_url = reverse_lazy('student_list')


class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'student_delete.html'
    success_url = reverse_lazy('student_list')


class StudentDetailView(DetailView):
    model = Student
    template_name = 'student_detail.html'


class CSVUploadView(View):
    def get(self, request):
        form = CSVUploadForm()
        return render(request, 'csv_upload.html', {'form': form})

    def post(self, request):
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = form.cleaned_data['csv_file']
            decoded_file = csv_file.read().decode('utf-8')
            csv_data = csv.reader(decoded_file.splitlines(), delimiter=',')
            for row in csv_data:
                first_name = row[0]
                last_name = row[1]
                Student.objects.create(first_name=first_name, last_name=last_name)
            return redirect('student_list')
        return render(request, 'csv_upload.html', {'form': form})


class StudentNoteView(View):
    def get(self, request, student_id):
        form = StudentNoteForm()
        student = Student.objects.get(id=student_id)
        notes = StudentNote.objects.filter(student=student).order_by('-created_at')
        return render(request, 'student_note.html', {'form': form, 'student': student, 'notes': notes})

    def post(self, request, student_id):
        form = StudentNoteForm(request.POST)
        student = Student.objects.get(id=student_id)
        if form.is_valid():
            note = form.cleaned_data['note']
            StudentNote.objects.create(student=student, note=note)
            return redirect('student_note', student_id=student_id)
        notes = StudentNote.objects.filter(student=student).order_by('-created_at')
        return render(request, 'student_note.html', {'form': form, 'student': student, 'notes': notes})


class NoteUpdateView(UpdateView):
    model = StudentNote
    fields = ['note']
    template_name = 'note_update.html'
    success_url = reverse_lazy('student_list')


from django.shortcuts import render

# Create your views here.

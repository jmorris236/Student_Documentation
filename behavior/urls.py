from django.urls import path
from .views import (
    StudentListView,
    StudentCreateView,
    StudentUpdateView,
    StudentDeleteView,
    StudentDetailView,
    CSVUploadView,
    StudentNoteView,
    NoteUpdateView,
)

urlpatterns = [
    path('', StudentListView.as_view(), name='student_list'),
    path('students/create/', StudentCreateView.as_view(), name='student_create'),
    path('students/<int:pk>/update/', StudentUpdateView.as_view(), name='student_update'),
    path('students/<int:pk>/delete/', StudentDeleteView.as_view(), name='student_delete'),
    path('students/<int:pk>/', StudentDetailView.as_view(), name='student_detail'),
    path('students/upload-csv/', CSVUploadView.as_view(), name='csv_upload'),
    path('students/<int:student_id>/note/', StudentNoteView.as_view(), name='student_note'),
    path('notes/<int:pk>/update/', NoteUpdateView.as_view(), name='edit_note'),
]

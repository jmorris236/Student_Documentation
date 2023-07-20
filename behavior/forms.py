from django import forms


class CSVUploadForm(forms.Form):
    csv_file = forms.FileField()


class StudentNoteForm(forms.Form):
    note = forms.CharField(widget=forms.Textarea)

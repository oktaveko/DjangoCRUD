from django import forms
from .models import Karyawan

class FormKaryawan(forms.ModelForm):

    class Meta:
        model =  Karyawan
        fields = ('fullname', 'mobile', 'emp_code', 'position')
        labels = {
            'fullname' : 'Nama Lengkap',
            'emp_code' : 'Kode Karyawan',
            'mobile' : 'Nomor Telp.',
            'position' : "Posisi"
        }

    def __init__(self, *args, **kwargs):
        super(FormKaryawan, self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "Select"
        self.fields['emp_code'].required = False
import dashboard.models
from django.forms import ModelForm
from . models import DriverFiles


class MyBusinessForm(ModelForm):
    class Meta:
        model = dashboard.models.businessForm
        exclude = ('timeStamp', 'id')


class MyDriver(ModelForm):
    class Meta:
        model = DriverFiles
        exclude = ('driver_id','all_files_flag','accept_flag')


#Driver File Upload Form One
class Form1(ModelForm):
    class Meta:
        model = DriverFiles
        fields = ['profile_photo', 'DVLA_Driving_Licence', 'DVLA_Check_Code', 'Private_Hire_Driver_Badge', 'Private_Hire_Driver_Licence']


# Driver File Upload Form Two

class Form2(ModelForm):
    class Meta:
        model = DriverFiles
        fields = ['Private_Hire_Vehicla_Licence', 'MOT_Test_Certificate', 'Vehicle_Insurance_Certificate',
                  'V5C_LogBook_or_New_Keeper_Slip_or_E_LogBook',
                   'Bank_Statement' ]
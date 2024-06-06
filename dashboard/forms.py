from django.forms import ModelForm
from . models import Fleet, Airports, City, Rates, SchoolContract, Schedule
import users.models


class MyAirport(ModelForm):
    class Meta:
        model = Airports
        fields = '__all__'

class MyCity(ModelForm):
    class Meta:
        model = City
        fields = '__all__'


class MyFleets(ModelForm):
    class Meta:
        model = Fleet
        fields = '__all__'

# Form for Reply
class MyReply(ModelForm):
    class Meta:
        model = users.models.Reply
        exclude = ('id',)

# Form for Airport Rates
class MyRates(ModelForm):
    class Meta:
        model = Rates
        exclude = ('who_created','airport_name', 'city_name')


# Form for School Contract
class MySchoolContract(ModelForm):
    class Meta:
        model = SchoolContract
        exclude = ('id',)



# Form for Schedule
        
class ScheduleForm(ModelForm):
    class Meta:
        model = Schedule
        exclude = ('id', 'school', 'timestamp')
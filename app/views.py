
import requests
from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.utils import timezone
from .models import SmokeData,HumanData,ObjectData

from .utils import get_blynk_data
from datetime import datetime
import pytz

# Create your views here.
BLYNK_AUTH_TOKEN = "RHqPlMuKI8Q-61aEhkWXf320vtYLe-ra"
# SM_VPIN = "V0"
# H_VPIN = "V1"

# Create your views here.
def index(request):
    return render(request,"sensor_data/index.html")
    
def logout_view(request):
    logout(request)
    return redirect('home')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pswd')

        # Check hard-coded username and password
        if username == 'admin' and password == 'admin':
            # Here you can create a user session or simply redirect
            print(username)
            print(password)
            return redirect('sensor-data')  # Redirect to the home page
        else:
            error_message = 'Invalid username or password'
            return render(request, 'sensor_data/index.html', {'error_message': error_message})
    
    return render(request, 'sensor_data/index.html')


def display_sensor_data(request):
    
    # Fetch data from V6 and V7 pins
    v6_data = get_blynk_data('V6')  # Now returns a dictionary with parsed values
    v7_data = get_blynk_data('V7')  # Similarly returns a dictionary
    
    # Example: Accessing 'H' value from V6 if it exists
    h_value = v6_data.get('H', 'N/A') if v6_data else 'N/A'
    print(h_value)
    ir_value=v6_data.get('IR1', 'N/A') if v6_data else 'N/A'
    print(ir_value)
    sm_value=v7_data.get('MQ2', 'N/A') if v7_data else 'N/A'
    print(sm_value)
    # Prepare context to pass to the template
    
    
    if h_value == '1':
       
        current_time = timezone.now() # Get current date and time
        ist_timezone = pytz.timezone('Asia/Kolkata')

        current_time_ist = timezone.now().astimezone(ist_timezone) # Get the current time in IST
        
        naive_current_time_ist = current_time_ist.replace(tzinfo=None) # Convert current_time_ist to naive datetime (remove timezone info)
        
        print(current_time_ist)
        # Create an instance of MyModel with IST time
       # my_instance = SmokeData.objects.create(time_in_ist=current_time_ist)
        # Store in database
        HumanData.objects.create(human_value=h_value, timestamp=naive_current_time_ist)

        detection_message = "Detected"
        
    else:
        detection_message = "Not Detected" 
        
    
    
    
   
    if ir_value == '1': 
        current_time = timezone.now() # Get current date and time
        ist_timezone = pytz.timezone('Asia/Kolkata')

        current_time_ist = timezone.now().astimezone(ist_timezone) # Get the current time in IST
        
        naive_current_time_ist = current_time_ist.replace(tzinfo=None) # Convert current_time_ist to naive datetime (remove timezone info)
        
        print(current_time_ist)
        # Create an instance of MyModel with IST time
       # my_instance = SmokeData.objects.create(time_in_ist=current_time_ist)
        # Store in database
        ObjectData.objects.create(object_value=ir_value, timestamp=naive_current_time_ist)
        detection_message1 = "Detected"
    else: 
        detection_message1 = "Not Detected" 
    
    
    current_time = timezone.now() # Get current date and time
    ist_timezone = pytz.timezone('Asia/Kolkata')

    current_time_ist = timezone.now().astimezone(ist_timezone) # Get the current time in IST
        
    naive_current_time_ist = current_time_ist.replace(tzinfo=None) # Convert current_time_ist to naive datetime (remove timezone info)
        
    print(current_time_ist)
        # Create an instance of MyModel with IST time
       # my_instance = SmokeData.objects.create(time_in_ist=current_time_ist)
        # Store in database
    SmokeData.objects.create(smoke_value=sm_value, timestamp=naive_current_time_ist)
     
    context = {
        'v6_data': v6_data or {'Error': 'Error retrieving data'},
        'v7_data': v7_data or {'Error': 'Error retrieving data'},
        'h_value': h_value,
        'ir_value':ir_value,
        'sm_value':sm_value,
        'dm':detection_message,
        'dm1':detection_message1

    }
    
    # Render the data in the template
    return render(request, 'sensor_data/view.html', context)


def smoke_data_report(request):
    # Fetch all records of SmokeData from the database
    smoke_data_list = SmokeData.objects.all().order_by('-timestamp')  # Order by timestamp descending

    # Pass the smoke data to the template
    context = {
        'smoke_data_list': smoke_data_list
    }
    return render(request, 'report/smoke_data_report.html', context)


def human_data_report(request):
    # Fetch all records of SmokeData from the database
    human_data_list = HumanData.objects.all().order_by('-timestamp')  # Order by timestamp descending

    # Pass the smoke data to the template
    context = {
        'human_data_list': human_data_list
    }
    return render(request, 'report/human_data_report.html', context)

def object_data_report(request):
    # Fetch all records of SmokeData from the database
    object_data_list = ObjectData.objects.all().order_by('-timestamp')  # Order by timestamp descending

    # Pass the smoke data to the template
    context = {
        'object_data_list': object_data_list
    }
    return render(request, 'report/object_data_report.html', context)
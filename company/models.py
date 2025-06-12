from django.db import models

from django.db.models import UniqueConstraint # Constraints fields to unique values

# Model representing Department
class Department(models.Model):
    #fields
    name = models.CharField(max_length = 100, help_text='Enter department name', unique=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.name
    
    '''class Meta:
        indexes = [
            models.Index(fields=['deartment_name']),
        ]
    '''

# Model representing Employee
class Employee(models.Model):
    #fields
    name = models.CharField(max_length = 100, help_text='Enter employee name')
    email = models.EmailField(max_length = 255, help_text='Enter email', unique=True)
    phone_number = models.IntegerField(help_text='Enter phone number', unique=True)
    address = models.CharField(max_length = 255, help_text='Enter address')
    date_of_joining = models.DateField(help_text='Enter date of joining')
    department = models.ForeignKey(Department,on_delete= models.CASCADE, help_text='Enter department')

    def __str__(self):
        """String for representing the Model object."""
        return self.name

    '''class Meta:
        indexes = [
            models.Index(fields=['name','email','phone_number','address','date_of_join','department']),
        ]
        '''


# Model representing Attendance
class Attendance(models.Model):
    #For CHOICES, the first element in each tuple is the value that will be stored in the database. 
    # The second element is displayed by the field’s form widget.
    CHOICES= [
        ('Present', 'Present'),
        ('Absent', 'Absent'),
        ('Late', 'Late'),
    ]

    #fields
    employee = models.ForeignKey(Employee, on_delete= models.CASCADE, help_text='Enter employee(FK)')
    date = models.DateField(help_text='Enter date')
    status = models.CharField(max_length = 7, choices = CHOICES , help_text='Enter status(Present/Absent/Late)')

    def __str__(self):
        """String for representing the Model object."""
        return f"{self.employee.name} - {self.date} - {self.status}"
    
    '''class Meta:
        unique_together = ('employee', 'date')  # Prevent duplicate attendance records per day
        #indexes = [
         #   models.Index(fields=['employee','date','status']), ]
    '''
    
# Model representing Performance
class Performance(models.Model):
    #fields
    employee = models.ForeignKey(Employee,on_delete= models.CASCADE, help_text='Enter employee(FK)')
    rating = models.IntegerField(help_text='Enter performance rating(1-5)')
    review_date = models.DateField( help_text='Enter review date', choices=[(i, str(i)) for i in range(1, 6)])

    def __str__(self):
        """String for representing the Model object."""
        return f"{self.employee.name} - {self.rating} - Rating: {self.review_date}"
    
    '''class Meta:
        indexes = [
            models.Index(fields=['employee_fk','rating','review_date']); 
        ]'''








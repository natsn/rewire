from django.db import models

# Create your models here.
class GreenSheet(models.Model):
    """
        The green sheet contains information regarding the 
        following actions:

            - Add an employee to a project
            - Payroll Change for Current Employee
            - Projects to Charge
            - Employee Seperation

    """
    # EMPLOYEE INFORMATION -------------------------------------
    full_name = models.CharField(max_length = 255)
    position = models.CharField(max_length = 255)
    supervisor_name = models.CharField(max_length = 255)
    ee_num = models.CharField(max_length = 255)

    # ADD AN EMPLOYEE TO A PROJECT -----------------------------
    STATUS_CHOICES = ((1, 'Regular'),
                      (2, 'On Call'),
                      (3, 'Temp (six months'),
                      (4, 'Work Study'),
                      (5, 'Intern'))
    aep_status_type = models.IntegerField(choices=STATUS_CHOICES)
    
    PERIOD_CHOICES = ((1, 'Monthly'),
                      (2, 'Hourly'))
    aep_period_type = models.IntegerField(choices=PERIOD_CHOICES)
    
    HIRE_CHOICES = ((1, 'New Hire'),
                    (2, 'Rehire'))
    aep_hire_type = models.IntegerField(choices=HIRE_CHOICES)

    # FTE (0.0, 1.0] or hours [1.0, 160.0]
    aep_amount_time = models.FloatField()

    # example: $12.50
    aep_pay_rate = models.FloatField()
    aep_start_date = models.DateField()

    # PAYROLL CHANGE FOR CURRENT EMPLOYEE ----------------------
    

    PAYROLL_CHANGE_CHOICES = ((1, 'Increase'),
                              (2, 'Promotion'),
                              (3, 'Change of Status'),
                              (4, 'Change of FTE / # Hours'),
                              (5, 'Change of Supervisor'))
    prc_payroll_change_type = models.IntegerField(choices=PAYROLL_CHANGE_CHOICES)
    
    # Examples? Is this a position?
    prc_change_from = models.CharField(max_length = 255)
    prc_change_to = models.CharField(max_length = 255)
    prc_effective_date = models.DateField()
    prc_comments = models.CharField(max_length = 1024)

    # PROJECTS TO CHARGE ---------------------------------------
    projects_to_charge = models.ManyToManyField(Project)

    # EMPLOYEE SEPERATION --------------------------------------
    es_effective_date = models.DateField()
    VOLUNTARY_CHOICES = ((1, 'Voluntary Seperation'),
                         (2, 'Involuntary Seperation'))
    es_voluntary_type = models.IntegerField(choices=VOLUNTARY_CHOICES)
    FROM_CHOICES = ((1, 'From ORI'),
                    (2, 'From Project'))
    es_from_type = models.IntegerField(choices=VOLUNTARY_CHOICES)

    # All done.
    general_comments = models.CharField(max_length = 1024)
    approved = models.BooleanField(default=False)
    # for app use
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Profile(models.Model):
    # TODO: Extra info pulled in from Hiline,
    # TODO: Lookup or Create Profile object if successful authentication through LDAP
    pass

class Project(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    phase = models.CharField(max_length=255)
from django.apps import AppConfig #In this line we import Appconfig class from django.apps module.


class DashboardConfig(AppConfig):#we declare name of the class as a DashboardConfig that inherits from the Appconfig
    default_FE_field = 'django.db.models.BigAutoField' #This line sets the default_auto_field attribute of the DashboardConfig class.
    name = 'dashboard' #Name attribute of dashboardconfig class to dashboard.

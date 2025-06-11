from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DepartmentViewSet, EmployeeViewSet, AttendanceViewSet, PerformanceViewSet
from .views import EmployeesPerDepartmentChart, MonthlyAttendanceOverviewChart
from .views import charts_view
from django.views.generic import RedirectView



# company/urls.py
router = DefaultRouter()
router.register('departments', DepartmentViewSet)
router.register('employees', EmployeeViewSet)
router.register('attendance', AttendanceViewSet)
router.register('performance', PerformanceViewSet)

urlpatterns = [
    # Redirect root URL to charts page
    path('', RedirectView.as_view(url='/charts/', permanent=False)),


    path('charts/', charts_view, name='charts_view'),
  
    path('charts/employees-per-department/', EmployeesPerDepartmentChart.as_view(), name='employees_per_department_chart'),
    path('charts/monthly-attendance/', MonthlyAttendanceOverviewChart.as_view(), name='monthly_attendance_chart'),
    path('api/', include(router.urls)),
]

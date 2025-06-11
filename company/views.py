from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Department, Employee, Attendance, Performance
from .serializers import DepartmentSerializer, EmployeeSerializer, AttendanceSerializer, PerformanceSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count
from django.db.models.functions import ExtractMonth
from collections import OrderedDict

from django.shortcuts import render

def charts_view(request):
    return render(request, 'charts.html')


class EmployeesPerDepartmentChart(APIView):
    def get(self, request):
        # Aggregate employees count by department
        data = Employee.objects.values('department__name').annotate(count=Count('id'))
        labels = [item['department__name'] for item in data]
        counts = [item['count'] for item in data]
        return Response({'labels': labels, 'counts': counts})

class MonthlyAttendanceOverviewChart(APIView):
    def get(self, request):
        # Aggregate attendance count per month (for the current year)
        data = (Attendance.objects
                .annotate(month=ExtractMonth('date'))
                .values('month')
                .annotate(count=Count('id'))
                .order_by('month'))

        # Ensure all months 1-12 are represented (0 if no data)
        month_counts = OrderedDict((i, 0) for i in range(1, 13))
        for item in data:
            month_counts[item['month']] = item['count']

        labels = [f'Month {m}' for m in month_counts.keys()]
        counts = list(month_counts.values())

        return Response({'labels': labels, 'counts': counts})



class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['department', 'date_of_joining']
    ordering_fields = ['name', 'date_of_joining']

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['employee', 'date']

class PerformanceViewSet(viewsets.ModelViewSet):
    queryset = Performance.objects.all()
    serializer_class = PerformanceSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['employee', 'review_date', 'rating']

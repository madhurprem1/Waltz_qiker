# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Employee
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import timedelta
from django.utils import timezone
from rest_framework.views import APIView


# Create your views here.
def index(request):
    return render(request, 'index.html')

@api_view(['GET', 'POST'])
def emp_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    employee_list_upadate = []
    counter = 0

    if request.method == 'GET':
        # to count million no of records
        count = Employee.objects.all().count()  # 1 million
        chunk_size = 1000
        # find date of 14 days before
        some_day_last_week = timezone.now().date() - timedelta(days=15)
        next_day = timezone.now().date() + timedelta(days=1)# This is next day

        for i in range(0, count, chunk_size):
            '''
            This is for if file to date wise but now not using because data is not coming because all is created with in 14 days
            # posts = Employee.objects.all().exclude(department='Waltzz').exclude(date_created__gte=some_day_last_week,
            #                                                                     date_created__lt=next_day).order_by(
            #     '-score')[i:i + chunk_size]
            '''
            posts = Employee.objects.all().exclude(department='Waltzz').order_by('-score')[i:i + chunk_size]
            posts_waltz = Employee.objects.filter(department='Waltzz').order_by('-date_created')[i:i + chunk_size]
            fourteen_qset = Employee.objects.filter(date_created__gte=some_day_last_week, date_created__lt=next_day)[i:i + chunk_size]

            waltz_length = len(posts_waltz)
            counter_waltz=0
            counter_foutreen=0

            for post in posts:
                counter+=1
                employee_dict_upadate={'employee_code':post.employee_code,'department':post.department, 'score':post.score}
                employee_list_upadate.append(employee_dict_upadate)
                if counter%4==0:
                    for waltz in range(waltz_length):

                        employee_dict_upadate = {'employee_code': posts_waltz[counter_waltz].employee_code, 'department': posts_waltz[counter_waltz].department,
                                                 'score': posts_waltz[counter_waltz].score}
                        counter_waltz += 1
                        employee_list_upadate.append(employee_dict_upadate)
                        if counter_waltz%2==0:

                            for fourteen in fourteen_qset:
                                employee_dict_upadate = {'employee_code': posts_waltz[counter_foutreen].employee_code,
                                                         'department': posts_waltz[counter_foutreen].department,
                                                         'score': posts_waltz[counter_foutreen].score}
                                counter_foutreen += 1
                                employee_list_upadate.append(employee_dict_upadate)
                                if counter_foutreen%2 == 0:
                                   break
                        break

        new_update_dict={"employee":employee_list_upadate}
        return Response(new_update_dict)


# class based view
class ParmList(APIView):

    def get(get, request):
        """
            Retrieve, update or delete a Employee.
        """
        employee_dict={}
        if request.method == 'GET':
            try:
                temp = request.query_params.get('chunk', None)
                count = Employee.objects.all().count()  # 1 million
                chunk_size = 1000
                emp_list=[]
                counter=1
                x = temp
                employee_dict={}
                if x.isdigit():
                    x=int(temp)

                for i in range(x, count, chunk_size):
                    posts = Employee.objects.all().order_by('-score')[i:i + chunk_size]
                    for post in posts:
                        counter+=1
                        emp_list.append(post.employee_code)
                        # count 20 beacaue need 20 records in list
                        if counter==20:
                            break
                employee_dict={'employee':emp_list}

                return Response(employee_dict)

            except Employee.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

        else:
            error_message = "Method is not GET"
            return Response(error_message)
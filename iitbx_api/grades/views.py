from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import mysql.connector
import os

# Create your views here.
labels = ['module_type','module_id','course_id','student_id','grade','max_grade']

mydb = mysql.connector.connect(
  host="10.129.103.92",
  user="root",
  passwd=os.environ.get('mysql_iitbx'),
  database="edxapp"
)

mycursor = mydb.cursor()

class AllStudentsAllCourses(APIView):

    def get(self, request, format=None):
        #obtain json data from database
        lst=[]
        mycursor.execute("SELECT  module_type,module_id,course_id,student_id,grade,max_grade FROM courseware_studentmodule ")
        myresult = mycursor.fetchall()
        for x in myresult :
            data = dict(zip(labels[::1],x[::1]))
            lst.append(data)
        if(len(lst)==0) :
            raise Http404
        return Response(lst)

class AllStudentsOneCourse(APIView):

    def get_course_data(self, pk):
        lst=[]
        try:
            #retrieving from databases
            pk = (pk,)
            print(pk)
            mycursor.execute("SELECT  module_type,module_id,course_id,student_id,grade,max_grade FROM courseware_studentmodule WHERE course_id=%s limit 5",pk)
            myresult = mycursor.fetchall()
            # print(type(myresult))
            for x in myresult :
                data = dict(zip(labels[::1],x[::1]))
                lst.append(data)
            if(len(lst)==0) :
                raise Http404
            return lst
        except :
            raise Http404

    def get(self, request, pk, format=None):
        data = self.get_course_data(pk)
        return Response(data)

class OneStudentOneCourse(APIView):

    def get_course_data_of_student(self, pk, pk1):
        lst=[]
        try:
            #retrieving from database
            print(pk1)
            pk = (pk,pk1)
            print(type(pk1))
            pk1=(pk1,)
            mycursor.execute("SELECT  module_type,module_id,course_id,student_id,grade,max_grade FROM courseware_studentmodule WHERE course_id=%s and student_id=%s limit 5",pk)
            myresult = mycursor.fetchall()
            for x in myresult :
                data = dict(zip(labels[::1],x[::1]))
                lst.append(data)
            if(len(lst)==0) :
                raise Http404
            return lst
        except :
            raise Http404

    def get(self, request, pk, pk1, format=None):
        data = self.get_course_data_of_student(pk,pk1)
        return Response(data)

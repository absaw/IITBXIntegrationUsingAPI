from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import mysql.connector
import os



from sshtunnel import SSHTunnelForwarder
import pymongo
import pprint
from pymongo import MongoClient
import bson

MONGO_HOST = "10.129.103.92"
MONGO_DB = "edxapp"
MONGO_USER = "admin"




# print(password1)
# print(os.environ.get('mysql_iitbx'))
# print("--------------------")



# Create your views here.
labels = ['module_type','module_id','course_id','student_id','grade','max_grade']

platforms=["10.129.103.92",]

# while not password1:
#     continue

# print(os.environ.get('mongo_pass'))
# print(os.environ.get('mysql_iitbx'))

# from pymongo import MongoClient



def fill_data(course,dictionary,db):
    chapterIds=[]
    chapters=[]
    chapterName=[]
    sequentialIds=[]
    sequentials=[]
    sequentialName=[]
    verticalIds=[]
    verticals=[]
    verticalName=[]
    courseName=""
    results = db.modulestore.active_versions.find({"course":course})
    for result in results :
        try :
            pub_id = result["versions"]["published-branch"]
        except:
            continue
        res = db.modulestore.structures.find({"_id":pub_id})
        for r in res:
            arr = r['blocks']
    	# for r in res:
    	# 	arr = r['blocks']
            for block in arr:
                if block['block_type'] == "course" :
                    courseName = block['fields']['display_name']
                    if course == "ARQ101":
                        print(courseName+"!")
                if block['block_type'] == "chapter" :
                    chapterName.append(block['fields']['display_name'])
                    chapters.append(block['fields']['children'])
                    chapterIds.append(block['block_id'])
                if block['block_type'] == "sequential" :
                    sequentialName.append(block['fields']['display_name'])
                    sequentials.append(block['fields']['children'])
                    sequentialIds.append(block['block_id'])
                if block['block_type'] == "vertical" :
                    verticalIds.append(block['block_id'])
                    verticalName.append(block['fields']['display_name'])
                    verticals.append(block['fields']['children'])
    if course == "ARQ101":
        print(courseName+"!!")
        print(len(chapterIds))

    for i in range(len(chapterIds)):
        if course == "ARQ101":
            print(len(chapters[i]))
        for var in chapters[i]:
            if len(var) == 0:
                continue
            if var[0] != "sequential":
                continue
            dictionary[course+var[1]]=[]
            if course == "ARQ101":
                print(courseName+"!!!")
            dictionary[course+var[1]].append(courseName)
            dictionary[course+var[1]].append(chapterName[i])
    for i in range(len(sequentialIds)):
        for var in sequentials[i]:
            if len(var) == 0:
                continue
    		# print(var)
            if var[0] != "vertical":
                continue
            dictionary[course+var[1]] = dictionary[course+sequentialIds[i]]
            dictionary[course+var[1]].append(sequentialName[i])
    for i in range(len(verticalIds)):
        for var in verticals[i]:
            if len(var) == 0:
                continue
            if var[0] != "problem":
                continue
            if course == "TEST_D_101.1x" and var[1]=="3ebcb45ccc7d4b91b3b13d6bfcdd0885":
                print("-----------------------------------------------------------")
            dictionary[course+var[1]]=dictionary[course+verticalIds[i]]
            dictionary[course+var[1]].append(verticalName[i])
            if course == "ARQ101":
                print(var[1])




class AllPlatforms(APIView):

    def get(self, request, format=None):
        #obtain json data from database
        lst1=[]
        for platform in platforms:
            mydb = mysql.connector.connect(
              host=platform,
              user="root",
              passwd=os.environ.get('mysql_iitbx'),
              database="edxapp"
            )
            client = MongoClient("mongodb://admin:"+os.getenv('mongo_pass')+"@"+platform+":27017")
            db = client.edxapp
            dictionary = dict()
            results = db.modulestore.active_versions.find({},{"course":1,"_id":0})
            for result in results :
                fill_data(result['course'],dictionary,db)
            mycursor = mydb.cursor()
            lst=[]
            var = ("problem",)
            mycursor.execute("SELECT  module_type,module_id,course_id,student_id,grade,max_grade FROM courseware_studentmodule WHERE module_type='problem' ")
            myresult = mycursor.fetchall()
            cnt = 0
            for x in myresult :
                data = dict(zip(labels[::1],x[::1]))
                string = data['module_id']
                string = string.split('@')
                pro_id = string[2]
                course = data['course_id'].split('+')[1]
                # print(data['course_id'])
                # print(pro_id)
                if not data['max_grade']:
                    continue
                if course+pro_id not in dictionary:
                    cnt = cnt + 1
                    continue
                data['courseName'] = dictionary[course+pro_id][0]
                data['sectionName'] = dictionary[course+pro_id][1]
                data['subSectionName'] = dictionary[course+pro_id][2]
                data['unitName'] = dictionary[course+pro_id][3]
                if data['max_grade'] :
                    lst.append(data)
            print(cnt)
            print(len(lst))
            lst1.append(lst)
        if(len(lst1)==0) :
            raise Http404
        return Response(lst1)




class AllCourses(APIView):

    def get(self, request, pk, format=None):
        #obtain json data from database
        mydb = mysql.connector.connect(
          host=pk,
          user="root",
          passwd=os.environ.get('mysql_iitbx'),
          database="edxapp"
        )
        client = MongoClient("mongodb://admin:"+os.getenv('mongo_pass')+"@"+pk+":27017")
        db = client.edxapp
        dictionary = dict()
        results = db.modulestore.active_versions.find({},{"course":1,"_id":0})
        for result in results :
            fill_data(result['course'],dictionary,db)
        mycursor = mydb.cursor()
        lst=[]
        var = ("problem",)
        mycursor.execute("SELECT  module_type,module_id,course_id,student_id,grade,max_grade FROM courseware_studentmodule WHERE module_type='problem' ")
        myresult = mycursor.fetchall()
        cnt = 0
        for x in myresult :
            data = dict(zip(labels[::1],x[::1]))
            string = data['module_id']
            string = string.split('@')
            pro_id = string[2]
            course = data['course_id'].split('+')[1]
            # print(data['course_id'])
            # print(pro_id)
            if not data['max_grade']:
                continue
            if course+pro_id not in dictionary:
                cnt = cnt + 1
                continue
            data['courseName'] = dictionary[course+pro_id][0]
            data['sectionName'] = dictionary[course+pro_id][1]
            data['subSectionName'] = dictionary[course+pro_id][2]
            data['unitName'] = dictionary[course+pro_id][3]
            if data['max_grade'] :
                lst.append(data)
        print(cnt)
        print(len(lst))
        if(len(lst)==0) :
            raise Http404
        return Response(lst)

class AllStudents(APIView):

    def get_course_data(self, pk, pk1):
        lst=[]
        try:
            #retrieving from databases
            mydb = mysql.connector.connect(
              host=pk,
              user="root",
              passwd=os.environ.get('mysql_iitbx'),
              database="edxapp"
            )
            client = MongoClient("mongodb://admin:"+os.getenv('mongo_pass')+"@"+pk+":27017")
            db = client.edxapp
            dictionary = dict()
            results = db.modulestore.active_versions.find({},{"course":1,"_id":0})
            for result in results :
                fill_data(result['course'],dictionary,db)
            mycursor = mydb.cursor()
            pk1 = (pk1,)
            print(pk1)
            mycursor.execute("SELECT  module_type,module_id,course_id,student_id,grade,max_grade FROM courseware_studentmodule WHERE module_type='problem' and course_id=%s ",pk1)
            myresult = mycursor.fetchall()
            # print(type(myresult))
            for x in myresult :
                data = dict(zip(labels[::1],x[::1]))
                # print(data['module_id'])
                string = data['module_id']
                string = string.split('@')
                pro_id = string[2]
                print(pro_id)
                # print(dictionary[pro_id])
                course = data['course_id'].split('+')[1]
                print(course)
                if not data['max_grade']:
                    continue
                if course+pro_id not in dictionary:
                    continue
                data['courseName'] = dictionary[course+pro_id][0]
                data['sectionName'] = dictionary[course+pro_id][1]
                data['subSectionName'] = dictionary[course+pro_id][2]
                data['unitName'] = dictionary[course+pro_id][3]
                print("!!!")
                if data['max_grade']:
                    lst.append(data)
            # print(len(lst))
            if(len(lst)==0) :
                raise Http404
            return lst
        except :
            raise Http404

    def get(self, request, pk, pk1, format=None):
        data = self.get_course_data(pk,pk1)
        return Response(data)

class OneStudent(APIView):

    def get_course_data_of_student(self, pk, pk1, pk2):
        lst=[]
        try:
            #retrieving from database
            mydb = mysql.connector.connect(
              host=pk,
              user="root",
              passwd=os.environ.get('mysql_iitbx'),
              database="edxapp"
            )
            client = MongoClient("mongodb://admin:"+os.getenv('mongo_pass')+"@"+pk+":27017")
            db = client.edxapp
            dictionary = dict()
            results = db.modulestore.active_versions.find({},{"course":1,"_id":0})
            for result in results :
                fill_data(result['course'],dictionary,db)
            mycursor = mydb.cursor()
            print(pk2)
            pk1 = (pk1,pk2)
            print(type(pk1))
            pk1=(pk1,)
            mycursor.execute("SELECT  module_type,module_id,course_id,student_id,grade,max_grade FROM courseware_studentmodule WHERE module_type='problem' and course_id=%s and student_id=%s ",pk1)
            myresult = mycursor.fetchall()
            for x in myresult :
                data = dict(zip(labels[::1],x[::1]))
                string = data['module_id']
                string = string.split('@')
                pro_id = string[2]
                course = data['course_id'].split('+')[1]
                data['courseName'] = dictionary[course+pro_id][0]
                data['sectionName'] = dictionary[course+pro_id][1]
                data['subSectionName'] = dictionary[course+pro_id][2]
                data['unitName'] = dictionary[course+pro_id][3]
                if data['max_grade']:
                    lst.append(data)
            if(len(lst)==0) :
                raise Http404
            return lst
        except :
            raise Http404

    def get(self, request, pk, pk1, pk2, format=None):
        data = self.get_course_data_of_student(pk,pk1,pk2)
        return Response(data)

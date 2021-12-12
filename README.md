# Developement of microservice architecture of inter-networked APIs functioning in the IIT BombayX ecosystem

The aim of this project was to develop four application programming interfaces(APIs) respectively for grades, course, platform and course import and to integrate the APIs with the IITBombayX server. The grade API fetches the grades of the students depending upon the query being made by the user. The course API is used to display a list of all courses, or the remote platforms on which a course is available and also manages database entries for new course creation. The platform API displays a list of all platforms or of courses on those platforms and can also be used for platform creation. The course and platform APIs are linked by a many-to-many relationship such that one platform may support numerous courses and vice versa. When a new course is created in the IITBX server, Course Import API is used to import that course on remote server’s machine..
<p>
<h1>Prerequisites:</h1>
<ul>
<li>The security keys have been wiped to make the project public. Insert newly generated keys before trying out the project
<li>pip install gitpython
<li>apt install mysql
<li>apt libmysqlclient-dev
<li>pip install mysql-connector-python-rf
<li>pip install mysqlclient
<li>create a user which has access to iitbxapi database
</ul>

<h1>Adding Environment Variable</h1>
-go to ~/.bashrc and add export "var_name"="value" and in the file import os and use os.environ.get("var_name")

<h3>IITBX BACKEND APIs</h3> <h5>get_course , get_platform, grades, Clone</h5>
<h3>IITBX Contol Django Project</h3> <h5>controlSection</h5>


  <h1>Screenshots</h1>
  
  <h3>Control Section Course Creation</h3>
  <img src="https://github.com/absaw/Integration-using-APIs-with-IITBX-platform/tree/master/Screenshots/controlSection/courseForm.png">
  
   <h3>Control Section Platform Creation</h3>
  <img src="https://github.com/absaw/Integration-using-APIs-with-IITBX-platform/tree/master/Screenshots/controlSection/platformForm.png">
  
  <h2>Course API - various functionalities</h3>
  
  <h3>One Course</h3>
  <img src = "https://github.com/absaw/Integration-using-APIs-with-IITBX-platform/tree/master/Screenshots/iitbxApi/oneCourse.png">
  <h3>All Courses</h3>
  <img src = "https://github.com/absaw/Integration-using-APIs-with-IITBX-platform/tree/master/Screenshots/iitbxApi/allcourse.png">
  <h3>Platforms on one course</h3>
  <img src = "https://github.com/absaw/Integration-using-APIs-with-IITBX-platform/tree/master/Screenshots/iitbxApi/oneCourseAllPlatforms.png">
  
  <h2>Platform API - various functionalites</h2>
  
  <h3>One Platform</h3>
  <img src = "https://github.com/absaw/Integration-using-APIs-with-IITBX-platform/tree/master/Screenshots/iitbxApi/platform-iitb.png">
  <h3>All Platforms</h3>
  <img src = "https://github.com/absaw/Integration-using-APIs-with-IITBX-platform/tree/master/Screenshots/iitbxApi/platform.png">
  <h3>Courses on one platform</h3>
  <img src = "https://github.com/absaw/Integration-using-APIs-with-IITBX-platform/tree/master/Screenshots/iitbxApi/onePlatformAllCourses.png">

</p>


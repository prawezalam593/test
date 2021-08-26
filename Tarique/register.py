#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
print "Student Register Form!!!"
print """
<html>
<head>
<script type="text/javaScript"spc="validate.js"></script>
</head>
<body>
<form action="#"name="studentRegistration"onsubmit="return(validate());">
<table cellpadding="2"width="90%"bgcolor="99FFFF"align="center"cellspacing="2">
<tr>
<td colspan=2>
<center><fontsize="6"><b>Student Registration Form</b></font></center>
</td>
</tr>
<tr>
<td>Name</td>
<td><input type="text"name=textname id="textname"size="30"></td>
</tr>
<tr>
<td>Father Name</td>
<td><input type="text"name="fathername"id="fathername"size="30"></td>
</tr>
<tr>
<td>Mother Name</td>
<td><input type="text"name="mothername"id="mothername"size="30"></td>
</tr>
<tr>
<td>Sex</td>
<td><input type="radio"name="sex"=value="male"size="10">Male<input type="radio"name="sex"value="Female"size="10">Female</td>
</tr>
<tr>
<td>Marital Status</td>
<td><input type="radio"name="maritalstatus"=value="married"size="10">Married<input type="radio"name="maritalstatus"value="unmaried"size="10">Unmaried</td>
</tr>
<tr>
<td>Permanent Address</td>
<td><input type="text"name="permanentaddress"id="permanentaddress"size="30"></td>
</tr>
<tr>
<td>Corresspondence Address</td>
<td><input type="text"name="corresspondenceaddress"id="corresspondenceaddress"siz="30"></td>
</tr>
<tr>
<td>Course</td>
<td><select name="Course">
<option value="-1"selected>select..</option>
<option value="B.Tech">B.TECH</option>
<option value="MCA">MCA</option>
<option value="B.Pharma">B.Pharma</option>
</select></td>
</tr>
<tr>
<td>Year</td>
<td><select name="year">
<option value="-1"selected>select..</option>
<option value="1st">1st</option>
<option value="2nd">2nd</option>
<option value="3rd">3rd</option>
<option value="4th">4th</option>
</tr>
<tr>
<td>Qualification Detail</td>
<td><input type="text"name="Qualification Detail"size="40"></td>
<tr>
<td>Matriculation</td>
<td><input type="text"name="matriculation"size"="20"></td>
<td>E-mailid</td>
<td><input type="text"name="e-mailid"id="e-mailid"size="30"></td>
</tr>
<tr>
<td>DOB</td>
<td><input type="text"name="dob"id="dob"size="30"></td>
</tr>
<tr>
<td>Mobile No.</td>
<td><input type="text"name="mobileno"id="mobile no."size="30"></td>
</tr>
<tr>
<td><input type="reset"></td>
<td colspan\"2"><input type="submit"value="Submit Form"/></td>
</tr>
</table>
</form>
</body>
</html>
"""
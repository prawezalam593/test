#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
print "Student login !!!"
print """
	<html>
	<head><title>Student Login</title> 
	<script> 
	function valid() 
	{ 
	var x=document.getElementById("mail").value; 
	if(x.indexOf("@")==-1) 
	{ 
	alert("Kindly check user email id") 
	return false; 
	} 
	else if(x.indexOf(".")==-1) 
	{ 
	alert("Please insert "."") 
	return false; 
	} 
	else 
	{ 
	alert("Good"); 
	} 
	} 
	</script></head> 
	<body> 
	<form action="a.html" method="post" onsubmit="return valid();"> 
	<center><h2> Student Login</h2></center> 
	<center>User Id:<input type="text" id="mail"></center><br> 
	<center>Password:<input type="password" id="pwd"></center><br> 
	<center><input type="submit" value="Submit" name="sub"> 
	<input type="reset" value="Reset" name="rst"></center> 
	</form> 
	</body> 
	</html>
	"""

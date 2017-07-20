<?php
$host='localhost';
$database='registration';
$user='root';
$pass='';
$username = $_GET['username'];
		$password = $_GET['password'];
		$phonenumber = $_GET['phonenumber'];

$con=mysqli_connect($host,$user,$pass,$database);
if($con)
 echo 'Connected successfully to mydb database';
        
		
		if($username == '' || $password == '' || $phonenumber == ''){
			echo 'please fill all values';
		}else{
			$sql = "SELECT * FROM userdetails WHERE username='$username'";
			
			$check = mysqli_fetch_array(mysqli_query($con,$sql));
if(isset($check)){
				echo 'username or email already exist';
			}else{			
                $sql="insert into userdetails values ('$username','$password','$phonenumber')";
                $query=mysqli_query($con,$sql);
if($query)
 echo 'Inserted in to table';
			}
		}
			mysqli_close($con);

?>
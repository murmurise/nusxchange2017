<?php
error_reporting(0);
require "dbConnect.php";

$username = $_GET['username'];
		$password = $_GET['password'];

		
		if($username == '' || $password == ''){
			echo 'please fill all values';
		}else{
			
			$sql = "SELECT * FROM Register WHERE username='$username' AND password='$password'";
			
			$check = mysqli_fetch_array(mysqli_query($con,$sql));
			
			if(isset($check)){
				echo 'Welcome';
			}else{				
				
					echo 'oops! Please try again! Incorrect details';
				
			}

			mysqli_close($con);
}

?>
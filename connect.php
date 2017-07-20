<?php
$host='localhost';
$database='mydb';
$user='root';
$pass='';
$sno=$_POST['sno'];
$name=$_POST['name'];

$con=mysqli_connect($host,$user,$pass,$database);
if($con)
 echo 'Connected successfully to mydb database';
 
$sql="insert into mytable values ('$sno','$name')";
$query=mysqli_query($con,$sql);
if($query)
 echo 'Inserted into table';

?>
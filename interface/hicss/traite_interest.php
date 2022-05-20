<?php 

	
	//si tout va bien
	{
	session_start ();
        $_SESSION['number'] = $_POST['number'];
	$_SESSION['alerte']=false;
        header('Location: csp.php'); 
		
	}
?>


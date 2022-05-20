<?php

session_start();
for($i = 1;$i <= $_SESSION['number']; $i ++){


if ($_POST['num_p'.$i]==null or $_POST['num_dis'.$i]==null or $_POST['danger_p'.$i]==null or $_POST['adress'.$i]==null or $_POST['acc'.$i]==null) {
	//empeche le participant de quitter la page sans cocher des cases
	$_SESSION['alerte']=true;
	header('Location: csp.php');
}

else {

$_SESSION['num_p'.$i] = $_POST['num_p'.$i];
$_SESSION['num_dis'.$i] = $_POST['num_dis'.$i];
$_SESSION['danger_p'.$i] = $_POST['danger_p'.$i];
$_SESSION['adress'.$i] = $_POST['adress'.$i];
$_SESSION['acc'.$i] = $_POST['acc'.$i];
	
	header('Location: avant.php');
}



}




?>



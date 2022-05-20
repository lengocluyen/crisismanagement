<?php
session_start ();
//determine le numero de l'etape en fonction de l'ordre


if ($_SESSION['alerte']==true){
	echo "<script>alert(\"Please answer the questions\")</script>"; 
}
else { 

$images_repas ="<form method='post' action='traite_csp.php'>";

for($i = 1;$i <= $_SESSION['number']; $i ++){
$images_repas .="
		<b>The information of place $i</b>
<br></br>
Adress: <input type = 'text' name='adress".$i."'>		
<br></br>
The number of people to be evacuated in this place: <input type = 'number' min = 1 name='num_p".$i."'>		
<br></br>
The number of people disabled in this place: <input type = 'number' min = 0 name='num_dis".$i."'>		
<br></br>

Please specify the level of danger: <input type = 'number' min = 1 name='danger_p".$i."'>		
<br></br>
Is the place accessible by ground vehicle?
<input type='radio' class='form-radio'  name='acc".$i."' value='2'>Yes
<input type='radio' class='form-radio'  name='acc".$i."' value='1'>No
<br></br>

";}
	

	$images_repas .="
					<p class='submit'>	
					<input type='submit' value='Next'/>
					</p>
					</form>
					</center>";	
	}


?> 

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" dir="ltr" lang="fr" xml:lang="fr">
<head>
	<title>Vehicle recommender systems</title>
	<meta http-equiv="content-Language" content="fr" />
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<link rel="stylesheet" href="style_sheet.css">
</head>
<div class="div-body">
<body>
	<h1>Now: </h1>
        <h2>Please give more infomration related to each place: </h2>
	<br />
	<?php echo ($images_repas); ?>	
</div>
</body>
</html>

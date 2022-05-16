<?php session_start() ; 
if ($_SESSION['alerte']==true){
	echo "<script>alert(\"Merci de répondre à toutes les questions.\")</script>"; 
}?>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" dir="ltr" lang="fr" xml:lang="fr">
<link rel="stylesheet" href="style_sheet.css">
<body>
<div class="div-body">
	<h1>Etape 1/4:</h1>
        <h2>Quelques questions sur vous...</h2>
	<h3>Les réponses seront traitées de manière anonyme.</h3> 

<?php

$serveur = "localhost";
$base = "Recsys";
$user = "root";
$pass = "110119zjf";
$mysqli = new mysqli($serveur, $user, $pass, $base);
$mysqli->set_charset("utf8");
if ($mysqli->connect_error) {
    die('Erreur de connexion ('.$mysqli->connect_errno.')'. $mysqli->connect_error);
}

//selection des genres
$_SESSION['t3'] = date('d/m/Y G:i:s');
$select = 'SELECT id_gender,gender_text FROM Gender where id_gender != 4';
$result = mysqli_query($mysqli,$select) or die('Erreur de connexion ('.$mysqli->connect_errno.')'. $mysqli->connect_error);

echo '<b>Votre sexe : </b>';
echo '<form method="POST" action="traite_csp.php">';
while($row = mysqli_fetch_array($result)) {	
	echo '<input type="radio" class="form-radio" name="gender" value="'.$row['id_gender'].'">'.$row['gender_text'].'<br>';
}

// selection des tranches d age
$select = 'SELECT id_age,age_text FROM Age where id_age != 10';
$result = mysqli_query($mysqli,$select) or die('Erreur de connexion ('.$mysqli->connect_errno.')'. $mysqli->connect_error);
$total = mysqli_num_rows($result);
//checkbox
echo '<br>';
echo '<b>Votre âge :</b>';
echo '<br>';
while($row = mysqli_fetch_array($result)) {	
	echo '<input type="radio" class="form-radio" name="age" value="'.$row['id_age'].'">'.$row['age_text'].'<br>';
}
//echo '</form>';


// selection de l education
$select = 'SELECT id_education,education_text FROM Education where id_education != 10';
$result = mysqli_query($mysqli,$select) or die('Erreur de connexion ('.$mysqli->connect_errno.')'. $mysqli->connect_error);
$total = mysqli_num_rows($result);
//checkbox
echo '<br>';
echo '<b>Votre niveau scolaire : </b>';
echo '<br>';
while($row = mysqli_fetch_array($result)) {	
	echo '<input type="radio" class="form-radio" name="education" value="'.$row['id_education'].'">'.$row['education_text'].'<br>';
}



// selection des CSP
$select = 'SELECT id_csp,text_csp FROM Categorie_social where id_csp != 10';
$result = mysqli_query($mysqli,$select) or die('Erreur de connexion ('.$mysqli->connect_errno.')'. $mysqli->connect_error);
$total = mysqli_num_rows($result);
//checkbox
echo '<br>';
echo '<b>Votre profession : </b>';
echo '<br>';
while($row = mysqli_fetch_array($result)) {	
	echo '<input type="radio" class="form-radio" name="csp" value="'.$row['id_csp'].'">'.$row['text_csp'].'<br>';
}


echo '<br>';
echo '<center><input type="submit" value="Valider"><center>';
echo '</form>';

$mysqli->close();
?>
</div>
</body>
</html>


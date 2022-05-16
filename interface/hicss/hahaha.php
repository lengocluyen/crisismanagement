<?php session_start() ; 
if ($_SESSION['alerte']==true){
	echo "<script>alert(\"Merci de répondre à toutes les questions.\")</script>"; 
}?>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" dir="ltr" lang="fr" xml:lang="fr">
<link rel="stylesheet" href="style_sheet.css">
<body>
<div class="div-body">
	<h1>Etape 3/4:</h1>
        <h2>Pour vous donner des recommandations personnalisées</h2>
	<h3>Veuillez indiquer la situation dans la quelle vous êtes</h3> 

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

$select = 'SELECT id_context1,Physical_text FROM Context_Physical';
$result = mysqli_query($mysqli,$select) or die('Erreur de connexion ('.$mysqli->connect_errno.')'. $mysqli->connect_error);

echo '<b>Quel votre état physique? </b>';
echo '<form method="POST" action="traite_hahaha.php">';
echo '<br>';
while($row = mysqli_fetch_array($result)) {	
	echo '<input type="radio" class="form-radio" name="physical" value="'.$row['id_context1'].'">vous êtes '.$row['Physical_text'].'<br>';
}


$select = 'SELECT id_context2,Mood_text FROM Context_Mood';
$result = mysqli_query($mysqli,$select) or die('Erreur de connexion ('.$mysqli->connect_errno.')'. $mysqli->connect_error);
$total = mysqli_num_rows($result);
//checkbox
echo '<br>';
echo '<b>Quel votre état désprit?</b>';

echo '<br>';
while($row = mysqli_fetch_array($result)) {	
	echo '<input type="radio" class="form-radio" name="mood" value="'.$row['id_context2'].'">vous '.$row['Mood_text'].'<br>';
}
//echo '</form>';



$select = 'SELECT id_context3,Location_text FROM Context_Location';
$result = mysqli_query($mysqli,$select) or die('Erreur de connexion ('.$mysqli->connect_errno.')'. $mysqli->connect_error);
$total = mysqli_num_rows($result);
//checkbox
echo '<br>';
echo '<b>Vous êtes où?</b>';
echo '<br>';
while($row = mysqli_fetch_array($result)) {	
	echo '<input type="radio" class="form-radio" name="location" value="'.$row['id_context3'].'">vous êtes '.$row['Location_text'].'<br>';
}




$select = 'SELECT id_context4,Companion_text FROM Context_Companion';
$result = mysqli_query($mysqli,$select) or die('Erreur de connexion ('.$mysqli->connect_errno.')'. $mysqli->connect_error);
$total = mysqli_num_rows($result);
//checkbox
echo '<br>';
echo '<b>Quel temps fait-il ? </b>';
echo '<br>';
while($row = mysqli_fetch_array($result)) {	
	echo '<input type="radio" class="form-radio" name="weather" value="'.$row['id_context4'].'">il '.$row['Companion_text'].'<br>';
}


echo '<br>';

echo '<center><input type="submit" value="Valider"><center>';

echo '</form>';

$mysqli->close();
?>
</div>
</body>
</html>


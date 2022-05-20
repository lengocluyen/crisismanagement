<?php
// On démarre la session
session_start ();

// On détruit les variables de notre session
session_unset ();

//On détruit notre session
session_destroy ();

?>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" dir="ltr" lang="fr" xml:lang="fr">   
<head>
<link rel="stylesheet" href="style_sheet.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
</head>
<body>
                                 
<div class="div-body"> 
 <a href="https://www.lamsade.dauphine.fr/" target=_blank>
		<a href="https://www.utc.fr/" target=_blank>
		<img src='../img/download.jpeg'  height='80px' style="position: relative;top: -40px;left:-40px;"></a>
                <a href="https://dauphine.psl.eu/" target=_blank>
                <img src='../img/dauphine.png'  height='80px' style="position: relative;top: -40px;left:700px;"></a>

		<h1 align="center"> Thanks for using this system  </h1>
		<center>~ ~ ~</center>
        

<?php


echo $_SESSION['adress2'];
?>
</div>
</body>
</html>


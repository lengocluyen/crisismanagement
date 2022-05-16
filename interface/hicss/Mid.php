<?php
// On démarre la session
session_start ();

?>


<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" dir="ltr" lang="fr" xml:lang="fr"> 
<link rel="stylesheet" href="style_sheet.css">
<div class="div-body">   
    <body>
		<a href="https://www.lamsade.dauphine.fr/" target=_blank>
		<img src='../img/lamsade.jpeg'  height='80px' style="position: relative;top: -40px;left:-40px;"></a>
                <a href="https://dauphine.psl.eu/" target=_blank>
                <img src='../img/dauphine.png'  height='80px' style="position: relative;top: -40px;left:600px;"></a>

	
        <h1 align="center"> Pour mieux connaitre vos préférences à propos des films. </h1><br />
        
        <h2 align="center">
            Nous allons vous proposer des films dans différentes situations. Imaginez les notes que vous allez donner &agrave; chaque film (bien que vous n'ayez peut-être pas vu les films). Il est à noter que les titres des films sont en anglais. <br /><br />
        </h2>
				
		<?php
		{ echo
		'<form name="page suivante" action="note1.php" method="post">
		<center><input type="submit" value="Suivant"></center>
		</form>';
		}
		?>
          
    </body>
</div>
</html>



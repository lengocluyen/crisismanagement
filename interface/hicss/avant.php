<?php
// On démarre la session
session_start ();
//determine le numero de l'etape en fonction de l'ordre




?>


<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" dir="ltr" lang="fr" xml:lang="fr"> 
<link rel="stylesheet" href="style_sheet.css">
<div class="div-body">   
    <body>
		<a href="https://www.utc.fr/" target=_blank>
		<img src='../img/download.jpeg'  height='80px' style="position: relative;top: -40px;left:-40px;"></a>
                <a href="https://dauphine.psl.eu/" target=_blank>
                <img src='../img/dauphine.png'  height='80px' style="position: relative;top: -40px;left:700px;"></a>

	<h2 align="center"> The system is calculating the most appropriate vehicle for each place.</h2><br />

				
		<?php
		{ echo
		'<form name="page suivante" action="avant1.php" method="post">
		<center><input type="submit" value="Next"></center>
		</form>';

		}
		?>
    </body>
</div>
</html>



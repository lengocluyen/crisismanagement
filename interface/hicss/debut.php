<?php
session_start ();

$requete = "SELECT `id_movie` FROM Movies";
$movies = mysqli_query($mysqli,$requete);

$_SESSION['film1']= rand(0,100);
$_SESSION['film2']=rand(101,201);
$_SESSION['film3']=rand(202,302);
$_SESSION['film4']=rand(303,403);
$_SESSION['film5']=rand(404,504);
$_SESSION['film6']=rand(505,605);
$_SESSION['film7']=rand(606,706);
$_SESSION['film8']=rand(707,807);
$_SESSION['film9']=rand(808,908);
$_SESSION['film10']=rand(909,1009);
$_SESSION['film11']=rand(1010,1110);
$_SESSION['film12']=rand(1111,1230);
$_SESSION['id_explanation1'] = 1;
$_SESSION['id_explanation2'] = 2;
$_SESSION['id_explanation3'] = 3;
$_SESSION['id_explanation4'] = 4;
$_SESSION['id_explanation5'] = 5;
$_SESSION['id_explanation6'] = 6;
$_SESSION['id_explanation7'] = 1;
$_SESSION['id_explanation8'] = 2;
$_SESSION['id_explanation9'] = 3;
$_SESSION['id_explanation10'] = 4;
$_SESSION['id_explanation11'] = 5;
$_SESSION['id_explanation12'] = 6;

$_SESSION['context_physical1']=rand(1,2);
$_SESSION['context_physical2']=rand(1,2);
$_SESSION['context_physical3']=rand(1,2);
$_SESSION['context_physical4']=rand(1,2);
$_SESSION['context_physical5']=rand(1,2);
$_SESSION['context_physical6']=rand(1,2);
$_SESSION['context_physical7']=rand(1,2);
$_SESSION['context_physical8']=rand(1,2);
$_SESSION['context_physical9']=rand(1,2);
$_SESSION['context_physical10']=rand(1,2);
$_SESSION['context_physical11']=rand(1,2);
$_SESSION['context_physical12']=rand(1,2);

$_SESSION['context_companion1']=rand(1,5);
$_SESSION['context_companion2']=rand(1,5);
$_SESSION['context_companion3']=rand(1,5);
$_SESSION['context_companion4']=rand(1,5);
$_SESSION['context_companion5']=rand(1,5);
$_SESSION['context_companion6']=rand(1,5);
$_SESSION['context_companion7']=rand(1,5);
$_SESSION['context_companion8']=rand(1,5);
$_SESSION['context_companion9']=rand(1,5);
$_SESSION['context_companion10']=rand(1,5);
$_SESSION['context_companion11']=rand(1,5);
$_SESSION['context_companion12']=rand(1,5);


$_SESSION['context_location1']=rand(1,3);
$_SESSION['context_location2']=rand(1,3);
$_SESSION['context_location3']=rand(1,3);
$_SESSION['context_location4']=rand(1,3);
$_SESSION['context_location5']=rand(1,3);
$_SESSION['context_location6']=rand(1,3);
$_SESSION['context_location7']=rand(1,3);
$_SESSION['context_location8']=rand(1,3);
$_SESSION['context_location9']=rand(1,3);
$_SESSION['context_location10']=rand(1,3);
$_SESSION['context_location11']=rand(1,3);
$_SESSION['context_location12']=rand(1,3);

$_SESSION['context_mood1']=rand(1,3);
$_SESSION['context_mood2']=rand(1,3);
$_SESSION['context_mood3']=rand(1,3);
$_SESSION['context_mood4']=rand(1,3);
$_SESSION['context_mood5']=rand(1,3);
$_SESSION['context_mood6']=rand(1,3);
$_SESSION['context_mood7']=rand(1,3);
$_SESSION['context_mood8']=rand(1,3);
$_SESSION['context_mood9']=rand(1,3);
$_SESSION['context_mood10']=rand(1,3);
$_SESSION['context_mood11']=rand(1,3);
$_SESSION['context_mood12']=rand(1,3);



//variables qui permettront de savoir à quel moment l'utilisateur abandonne (s'il abandonne)
$_SESSION['verif']['incr_interest']=0;
$_SESSION['verif']['incr_csp']=0;
$_SESSION['verif']['incr_note1']=0;
$_SESSION['verif']['incr_note2']=0;
$_SESSION['verif']['incr_note3']=0;
$_SESSION['verif']['incr_note4']=0;
$_SESSION['verif']['incr_explanation1']=0;
$_SESSION['verif']['incr_explanation2']=0;
$_SESSION['verif']['incr_explanation3']=0;
$_SESSION['verif']['incr_explanation4']=0;
$_SESSION['verif']['incr_explanation5']=0;
$_SESSION['verif']['incr_explanation6']=0;
$_SESSION['verif']['incr_explanation7']=0;
$_SESSION['verif']['incr_explanation8']=0;
$_SESSION['verif']['incr_explanation9']=0;
$_SESSION['verif']['incr_explanation10']=0;
$_SESSION['verif']['incr_noexp1']=0;
$_SESSION['verif']['incr_noexp2']=0;
$_SESSION['verif']['incr_noexp3']=0;
$_SESSION['verif']['incr_noexp4']=0;
$_SESSION['verif']['incr_noexp5']=0;
$_SESSION['verif']['incr_noexp6']=0;
$_SESSION['verif']['incr_noexp7']=0;
$_SESSION['verif']['incr_noexp8']=0;
$_SESSION['verif']['incr_noexp9']=0;
$_SESSION['verif']['incr_noexp10']=0;
$_SESSION['verif']['incr_question']=0;
$_SESSION['interest'] = 1;

$_SESSION['verif']['decr_interest']=0;
$_SESSION['verif']['decr_csp']=0;
$_SESSION['verif']['decr_note1']=0;
$_SESSION['verif']['decr_note2']=0;
$_SESSION['verif']['decr_note3']=0;
$_SESSION['verif']['decr_note4']=0;
$_SESSION['verif']['decr_explanation1']=0;
$_SESSION['verif']['decr_explanation2']=0;
$_SESSION['verif']['decr_explanation3']=0;
$_SESSION['verif']['decr_explanation4']=0;
$_SESSION['verif']['decr_explanation5']=0;
$_SESSION['verif']['decr_explanation6']=0;
$_SESSION['verif']['decr_explanation7']=0;
$_SESSION['verif']['decr_explanation8']=0;
$_SESSION['verif']['decr_explanation9']=0;
$_SESSION['verif']['decr_explanation10']=0;
$_SESSION['verif']['decr_noexp1']=0;
$_SESSION['verif']['decr_noexp2']=0;
$_SESSION['verif']['decr_noexp3']=0;
$_SESSION['verif']['decr_noexp4']=0;
$_SESSION['verif']['decr_noexp5']=0;
$_SESSION['verif']['decr_noexp6']=0;
$_SESSION['verif']['decr_noexp7']=0;
$_SESSION['verif']['decr_noexp8']=0;
$_SESSION['verif']['decr_noexp9']=0;
$_SESSION['verif']['decr_noexp10']=0;
$_SESSION['verif']['decr_question']=0;

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
		<h1 align="center" style="position: relative;top: -40px;"> Vehicle recommendation during an evacuation  </h1>

	
        <h2 align="center"> Hello !</h2><br />
        
        <h3 align="center"> 
             This recommender system helps to manage civil vehicle resources during en evacuation, it can recommend you the most appropriate civile vehicle resources 
        </h3>
				
		<?php
		{ echo
		'<form name="page suivante" action="interest.php" method="post">
		<center><input type="submit" value="Suivant"></center>
		</form>';
		}
		?>
          
    </body>
</div>
</html>



<?php
// On démarre la session
session_start ();

$images_repas ="<form method='post' action='fin.php'>";

$hehe ="

Is this recommendation acceptable?
<input type='radio' class='form-radio'  name='accp1' value='2'>Yes
<input type='radio' class='form-radio'  name='accp1' value='1'>No
<br></br>

If you do not accept this recommendation please specify more precisely your requirements
<br></br>
<input type='checkbox' id='r1' name='r1 value=1>
<label for='r1'> Less repesponse time</label><br>
<input type='checkbox' id='r2' name='r2' value=2>
<label for='r3'> To another shelter</label><br>
<input type='checkbox' id='r3' name='r3' value=3>
<label for='r3'> Vehicles with more space</label><br>



";

$images_repas .="




Is this recommendation acceptable?
<input type='radio' class='form-radio'  name='accp1' value='2'>Yes
<input type='radio' class='form-radio'  name='accp1' value='1'>No
<br></br>

If you do not accept this recommendation please specify more precisely your requirements
<br></br>
<input type='checkbox' id='r1' name='r1 value=1>
<label for='r1'> Less repesponse time</label><br>
<input type='checkbox' id='r2' name='r2' value=2>
<label for='r3'> To another shelter</label><br>
<input type='checkbox' id='r3' name='r3' value=3>
<label for='r3'> Vehicles with more space</label><br>



";


$images_repas .="
					<p class='submit'>	
					<input type='submit' value='Next'/>
					</p>
					</form>
					</center>";
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

        <h2 align="center"> Here are the vehicles recommende to each place </h2><br />






<h3 align="left"> The recommendations for the 46 Rue de l'Oise, 60200 Compiegne: </h3><br /> 
<table width="100%" border="1 solid" rules="all" align="center" cellpadding="5">
  <tr>
<th>Information of the the vehicle</th>
<th>Location of the vehicle</th>
<th>Driver</th>
<th>Places available</th>
<th>Time for ariving at this place</th>
<th>Destination-Shelter</th>
  </tr>
 <tr>
  <th>Audi Q3 </th>
  <th> 24 TER Rue du Bataillon de France, 60200 Compiegne</th>
  <th> Octave Viens </th>
  <th>  5</th>
  <th> 10min</th>
  <th> Gymnasium Des Rose, 60200 Compiegne</th>

</tr>

 <tr>
  <th> Renault Captur 2</th>
  <th> 2 Pl. du 14 Juillet, 60200 Compiegne</th>
  <th> Adrien Theberge </th>
  <th>  5</th>
  <th> 11min</th>
  <th>Gymnasium Des Rose, 60200 Compiegne</th>

</tr>

 <tr>
  <th> Citroen C3 Aircross</th>
  <th> 21T Rue Saint-Germain, 60200 Compiegne</th>
  <th> Joseph Brault </th>
  <th>  5 </th>
  <th> 9min </th>
  <th>Gymnasium Des Rose, 60200 Compiegne</th>
</tr>

 
  </table>



<?php
		echo ($hehe);
		?>




<h3 align="left"> The recommendations for 35-39 Quai du Clos des Roses, 60200 Compiegne: </h3><br /> 
<table width="100%" border="1 solid" rules="all" align="center" cellpadding="5">
  <tr>
<th>Information of the the vehicle</th>

<th>Location of the vehicle</th>
<th>Driver</th>
<th>Places available</th>
<th>Time for ariving at this place</th>
<th>Destination-Shelter</th>
  </tr>
 <tr>
  <th> Citroen Jumpy Combi </th>
  <th> 25 Rue Fournier Sarloveze, 60200 Compiegne</th>
  <th> Jerome Marleau </th>
  <th>  9</th>
  <th> 15min</th>
  <th>30 Rue Saint-Joseph, 60200 Compiegne</th>

</tr>

 <tr>
  <th> Minibus Renault Master</th>
  <th> 2 Pl. du 14 Juillet, 60200 Compiegne</th>
  <th> Algernon Casgrain </th>
  <th>  17 </th>
  <th> 11 min</th>
  <th>30 Rue Saint-Joseph, 60200 Compiegne</th>

</tr>

 <tr>
  <th> Renault Trafic 3 Combi</th>
  <th> 4 Sq. Camille Saint-Saens, 60200 Compiegne</th>
  <th> Leal Gauthier </th>
  <th>  9 </th>
  <th> 13min </th>
  <th>30 Rue Saint-Joseph, 60200 Compiegne</th>

</tr>

 
  </table>

				
		<?php
		echo ($images_repas);
		?>
    </body>
</div>
</html>



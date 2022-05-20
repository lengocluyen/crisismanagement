<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" dir="ltr" lang="fr" xml:lang="fr">

<script>
function validateForm()
{
var x=document.forms["my_form"]["number"].value;
if (x==null || x=="")
  {
  alert("Please specify the number");
  return false;
  }
}
</script>

<link rel="stylesheet" href="style_sheet.css">

<body>
<div class="div-body">

		<a href="https://www.lamsade.dauphine.fr/" target=_blank>
		<img src='../img/download.jpeg'  height='80px' style="position: relative;top: -40px;left:-40px;"></a>
                <a href="https://dauphine.psl.eu/" target=_blank>
                <img src='../img/dauphine.png'  height='80px' style="position: relative;top: -40px;left:700px;"></a>
		<h1 align="center"> First step  </h1>
		
		        <h2 align="left">
				Please specify the the number of places to be evacuated
				</h2>
				





<form method="POST" name="my_form" action="traite_interest.php" onsubmit="return validateForm()">
				The numebr of places to be evacuated: <input type = "number" min = 1 name="number">
				<br />
				<br />
				<br />
				<p class='submit'>
				<center>
				<input type="submit" value="Next"/>
				</center>
				</p>
				</form>		
</div>
				
</body>
</html>

<script type="text/javascript" src="js/jquery-1.9.1.min.js"></script>
<script type="text/javascript" src="js/drag.js"></script>

<script>
	$(function(){
		$('.box-1 dl').each(function(){
			$(this).dragging({
				move : 'x',
				randomPosition : true
			});
		});
		$('.box-2 dl').each(function(){
			$(this).dragging({
				move : 'y',
				randomPosition : true
			});
		});
		$('.box-3 dl').each(function(){
			$(this).dragging({
				move : 'both',
				randomPosition : false
			});
		});
		$('.box-4 dl').each(function(){
			$(this).dragging({
				move : 'both',
				randomPosition : true
			});
		});
		$('.box-5 dl').each(function(){
			$(this).dragging({
				move : 'both',
				randomPosition : true ,
				hander:'.hander'
			});
		});
	});
</script>

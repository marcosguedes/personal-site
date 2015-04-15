$(document).ready(function(){
	$(".interests .item").each(function(e){
		$this = $(this);
		var itemWidth = $this.width();
		$this.height(itemWidth);
	});
});
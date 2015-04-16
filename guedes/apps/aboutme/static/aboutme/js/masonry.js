$(document).ready(function(){
	$container = $(".masonry");

	$container.imagesLoaded( function() {
	    loadIsotope($container);
		resizeItems();
	});

	$('.filter').on( 'click', function() {
	    var filterValue = $( this ).attr('data-filter');
	    $container.isotope({ filter: filterValue });
	});

	$('.masonry-filters').each( function( i, buttonGroup ) {
    	var $buttonGroup = $( buttonGroup );
    	$buttonGroup.on( 'click', '.filter', function() {
      		$buttonGroup.find('.active').removeClass('active');
      		$( this ).addClass('active');
    	});
  	});

});

$(document).ready(function(){
	resizeItems();
});

$( window ).resize(function() {
    try {
        clearTimeout(isotopeTimeout);
    } catch(e) {}

    var isotopeTimeout = setTimeout(function(){
	    resizeItems();
	    loadIsotope($(".masonry"));
    }, 500);
});

function resizeItems(){
	$(".interests .item").each(function(e){
		$this = $(this);
		var itemWidth = $this.width();
		$this.height(itemWidth);
	});
}

function loadIsotope($elem){
	$elem.isotope({
  	    itemSelector: ".item",
  	    layoutMode: "fitRows",
    });
}


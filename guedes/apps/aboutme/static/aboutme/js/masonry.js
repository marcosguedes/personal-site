$(document).ready(function(){
	$container = $(".masonry");

	$container.imagesLoaded( function() {
	    $container.isotope({
	  	    itemSelector: ".item",
	  	    // filter: ".filter",
	    });
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
$(document).ready(function(){
    
    //$.cookies.set("cookie-disclaimer", false);  // -- used for app testing
    if ($.cookies.get("cookie-disclaimer") == true){
        $("#warning-container").hide();
    }else{
        $("#warning-container").delay(500).slideToggle("slow");
    };
    $(".terms").click(function(e){
        e.preventDefault();
        $('#popup-container').show();
        $("body").css("overflow", "hidden");
    });
    $(".close-warning").click(function(e){
        e.preventDefault();
        $("#warning-container").slideToggle("slow");
	var newOptions = {
		expiresAt: new Date( 2099, 1, 1 ),
	    };
        $.cookies.set("cookie-disclaimer", true, newOptions);
    });
    $(".popup-close").click(function(e){
        e.preventDefault();
        $('#popup-container').hide();
        $("body").css("overflow", "visible");
    });
});

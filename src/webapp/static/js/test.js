
$(document).ready(function() {

    // Hide god description on page load
    $(function () {
        $('#god-description').hide();
    });

    $("#god-image").mouseenter(function() {
        $('#god-description').show();
        });

    $("#god-image").mouseleave(function() {
        $('#god-description').hide();
        });

    $(function () {
        for (let i = 1; i <= 6; i++) { 
            // Hide all item descriptions on page load
            $('#item-description-' + i).hide();

            // Show item descriptions when hovering over item image
            $("#item-img-" + i).mouseenter(function() {
                $('#item-description-' + i).show();
                });
            $("#item-img-" + i).mouseleave(function() {
                $('#item-description-' + i).hide();
                });
        }
    });

});
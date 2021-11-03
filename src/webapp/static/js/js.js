
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


    $(function () {
        for (let i = 1; i <= 2; i++) {
            $('#relic-description-' + i).hide();

            // Show relic descriptions when hovering over relic image
            $('#relic-img-' + i).mouseenter(function() {
                $('#relic-description-' + i).show();
            })
            $('#relic-img-' + i).mouseleave(function() {
                $('#relic-description-' + i).hide();
            })
        }
    });

    $(function () {
        for (let i = 1; i <= 2; i++) {
            $('#consumable-description-' + i).hide();

            // Show consumable descriptions when hovering over relic image
            $('#consumable-img-' + i).mouseenter(function() {
                $('#consumable-description-' + i).show();
            })
            $('#consumable-img-' + i).mouseleave(function() {
                $('#consumable-description-' + i).hide();
            })
        }
    });

    $(function () {
        for (let i = 1; i <= 20; i++) {
            $('#ability-description-' + i).hide();

            // Show ability descriptions when hovering over relic image
            $('#ability-img-' + i).mouseenter(function() {
                $('#ability-description-' + i).show();
            })
            $('#ability-img-' + i).mouseleave(function() {
                $('#ability-description-' + i).hide();
            })
        }
    });

});
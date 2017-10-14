$( document ).ready(function()
{
	$('#users-table').DataTable({
			"pageLength": 5
		}
	);

	$( "#datepicker" ).datepicker();

	function initMap()
	{
	        var autocomplete = new google.maps.places.Autocomplete($("#id_location")[0], {});

	        google.maps.event.addListener(autocomplete, 'place_changed', function() {
            var place = autocomplete.getPlace();
            console.log(place.address_components);
        });
    }

    initMap();
});
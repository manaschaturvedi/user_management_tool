$( document ).ready(function()
{
	function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
	}
	var csrftoken = getCookie('csrftoken');

	var base_url = document.location.origin;
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

 //    $( ".edit-user" ).click(function() 
 //    {	
 //  		var url = base_url + '/add-edit-user/';
	// 	var data = {
	// 		'email': $(this).data('email'),
	// 		'csrfmiddlewaretoken': csrftoken,
	// 	};
	// 	// $.post(url, data);
	// 	$.post(url, data).done(function(result) {
	// 		console.log(result);
	// 	}).fail(function(error) {
	// 		console.log(error);
	// 	});
	// 	// window.location.href = "/add-edit-user";
	// });
});
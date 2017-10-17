$( document ).ready(function()
{
	// localStorage.setItem('button_text','Add');

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
            // console.log(place.address_components);
        });
    }

    initMap();

    $( "#add-update-user-button" ).click(function() 
    {	
    	first_name = $('input[name="first_name"]').val();
    	last_name = $('input[name="last_name"]').val();
    	age = $('input[name="age"]').val();
    	dob = $('input[name="dob"]').val();
    	place = $('input[name="location"]').val();
    	mobile = $('input[name="mobile"]').val();
    	email = $('input[name="email"]').val();
    	user_id = $('input[name="user_id"]').val();
    	new_user = (user_id == '') ? ('yes') : ('no');

    	var url = base_url + '/add-update-user/';
		var data = {
			'email': email,
			'first_name': first_name,
			'last_name': last_name,
			'age': age,
			'dob': dob,
			'place': place,
			'mobile': mobile,
			'user_id': user_id,
			'new_user': new_user,
			'csrfmiddlewaretoken': csrftoken,
		};
		$.post(url, data).done(function(result) {
			window.location.href = "/";
		}).fail(function(error) {
			console.log(error);
		});

	});

	$("#id_mobile").change(function () 
	{
	      var mobile = $(this).val();
	      $.ajax({
	        url: '/validate-mobile/',
	        data: {
	          'mobile': mobile
	        },
	        dataType: 'json',
	        success: function (data) 
	        {
	          if (data.is_error) 
	          {
	            $.notify(data.message);
	          }
	        }
	      });
    });

    $("#id_first_name").change(function () 
	{
	      var first_name = $(this).val();
	      $.ajax({
	        url: '/validate-first-name/',
	        data: {
	          'first_name': first_name
	        },
	        dataType: 'json',
	        success: function (data) 
	        {
	          if (data.is_error) 
	          {
	            $.notify(data.message);
	          }
	        }
	      });
    });

    $("#id_last_name").change(function () 
	{
	      var last_name = $(this).val();
	      $.ajax({
	        url: '/validate-last-name/',
	        data: {
	          'last_name': last_name
	        },
	        dataType: 'json',
	        success: function (data) 
	        {
	          if (data.is_error) 
	          {
	            $.notify(data.message);
	          }
	        }
	      });
    });
   
    $(".add-new-user-button").click(function() 
    {
		localStorage.setItem('button_text','Add');  
	});

	$(".edit-user").click(function() 
    {
		localStorage.setItem('button_text','Edit');  
	});

    $("#add-update-user-button").html(localStorage.getItem('button_text'));
});
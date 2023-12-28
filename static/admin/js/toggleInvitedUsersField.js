$(function(){
$('#id_choose_who_can_view_the_course').change(function(){
    	if ($('#id_choose_who_can_view_the_course').is(':checked')) {
	    $('.field-invited_users').show()
	} else {
	    $('.field-invited_users').hide()
	}
    });
});


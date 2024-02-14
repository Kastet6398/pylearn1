document.addEventListener("DOMContentLoaded", () => {
    window.onload = () => {
    if (!(document.getElementById("id_choose_who_can_view_the_course").checked)) {
            document.getElementsByClassName("field-invited_users")[0].style.display = "none";
        }

	    document.getElementById("id_choose_who_can_view_the_course").onchange=function(){
        if (document.getElementById("id_choose_who_can_view_the_course").checked) {
            document.getElementsByClassName("field-invited_users")[0].style.display = "block";
        } else {
            document.getElementsByClassName("field-invited_users")[0].style.display = "none";
        }
    };
    };
});
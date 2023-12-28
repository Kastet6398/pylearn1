document.addEventListener("DOMContentLoaded", () => {
    window.onload = () => {
    console.log(document.body);
	    document.getElementById('view').contentWindow.document.getElementById("id_choose_who_can_view_the_course").onchange=function(){
        if (document.getElementById('view').contentWindow.document.getElementById("id_choose_who_can_view_the_course").checked) {
            document.getElementById('view').contentWindow.document.getElementsByClassName("field-invited_users")[0].style.display = "block";
        } else {
            document.getElementById('view').contentWindow.document.getElementsByClassName("field-invited_users")[0].style.display = "none";
        }
    };
    };
});

document.addEventListener("DOMContentLoaded", () => {
document.getElementById("id_choose_who_can_view_the_course").change(function(){
        if (document.getElementById("id_choose_who_can_view_the_course").is(':checked')) {
            document.getElementByClassName("field-invited_users").style.display = ""
        } else {
            document.getElementByClassName("field-invited_users").style.display = "none"
        }
    });
});

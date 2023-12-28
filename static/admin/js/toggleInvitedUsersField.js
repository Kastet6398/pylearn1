document.addEventListener("DOMContentLoaded", () => {
document.getElementById('view').contentWindow.document.body.getElementById("id_choose_who_can_view_the_course").change(function(){
        if (document.getElementById('view').contentWindow.document.body.getElementById("id_choose_who_can_view_the_course").is(':checked')) {
            document.getElementById('view').contentWindow.document.body.getElementByClassName("field-invited_users").style.display = ""
        } else {
            document.getElementById('view').contentWindow.document.body.getElementByClassName("field-invited_users").style.display = "none"
        }
    });
});

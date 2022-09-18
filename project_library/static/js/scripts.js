$(document).ready(function () {
    $('#sidebarCollapse').on('click', function () {
        $('#sidebar').toggleClass('active');
    });
});

$(document).ready(function () {
    $(".alert").hide(5000);
});

// Create validation
function validateForm() {
    var book_name = document.forms["formCreate"]["txtBookName"].value;
    if (book_name == "") {
        alert(" Book name must be filled out");
        return false;
    }
    var aut_name = document.forms["formCreate"]["txtAuthor"].value;
    if (aut_name == "") {
        alert(" Author name must be filled out");
        return false;
    }
    var book_number = document.forms["formCreate"]["txtBookNumber"].value;
    if (book_number == "") {
        alert(" Book number must be filled out");
        return false;
    }
    var book_category = document.forms["formCreate"]["txtCategory"].value;
    if (book_category == "") {
        alert(" Category must be filled out");
        return false;
    }
}

function validateFormMember() {
    var member_name = document.forms["formCreateMember"]["txtMemberName"].value;
    if (member_name == "") {
        alert(" Member name must be filled out");
        return false;
    }
    var member_role = document.forms["formCreateMember"]["ddlMemberRole"].value;
    if (member_role == "0") {
        alert(" Member roll should be select");
        return false;
    }
}

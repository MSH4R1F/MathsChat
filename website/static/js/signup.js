function show(pwd) {
    var password = document.getElementById(pwd);
    var btn = password.nextElementSibling
    if (password.getAttribute('type') == "password") {
        btn.removeAttribute("class");
        btn.setAttribute("class", "far fa-eye");
        password.removeAttribute("type");
        password.setAttribute("type", "text");
    } else {
        password.removeAttribute("type");
        password.setAttribute('type', 'password');
        btn.removeAttribute("class");
        btn.setAttribute("class", "far fa-eye-slash");
    }
}

// var paswd = /^(?=.*[0-9])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{7,30}$/;

function error_msg(text) {
    // console.log(text);
    // var test = document.createElement('div');
    // text = document.createTextNode(text);
    // test.append(text)
    // document.getElementById("pre-check").appendChild(test);
    // let block = document.getElementById("pre-check");
    // block.classList.add("alert alert-success alert-dismissible fade show");
    alert(text);
}

function validate(e) {
    var pwd = document.getElementById("pwd").value;
    if (pwd.length < 8) {
        error_msg("Password not long enough");
        console.log("PAssword ")
        return false;
    } else if (pwd.search(/[a-z]/) < 0) {
        error_msg("Your password needs a lowercase letter");
        return false;
    } else if (pwd.search(/[A-Z]/) < 0) {
        error_msg("Your password needs an uppercase letter");
        return false;
    } else if (pwd.search(/[0-9]/) < 0) {
        error_msg("Your password requires a number. ");
        return false;
    } else {
        return true;
    }
}
function validate_code(e) {
    console.log("valid")
    var code = document.getElementById("code").value;
    console.log(code);
    if (code.length != 6) {
        alert("Invalid length");
        return false;
    } else if (isNaN(code)) {
        alert("Must be all digits.");
        return false;
    } else {
        return true;
    }
}
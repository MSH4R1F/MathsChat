function show(pwd) {
  var password=document.getElementById(pwd);
  var btn=password.nextElementSibling
  if (password.getAttribute('type') == "password") {
  btn.removeAttribute("class");
  btn.setAttribute("class","far fa-eye");
  password.removeAttribute("type");
    password.setAttribute("type","text");
  } else {
  password.removeAttribute("type");
    password.setAttribute('type','password');
 btn.removeAttribute("class");
  btn.setAttribute("class","far fa-eye-slash");
  }
}

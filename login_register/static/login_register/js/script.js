//username
function username_validation() {
    let username = document.getElementById("username").value
    const username_pattern = /^[a-zA-Z]+$/;
    if(username_pattern.test(username)){
        document.getElementById("username-valid").innerHTML = ""
    }else{
        document.getElementById("username-valid").innerHTML = "username should be only letters"
    }
}
// firstname
function firstname_validation() {
    let firstname = document.getElementById("fname").value
    const firstname_pattern = /^[a-zA-Z]+$/;
    if(firstname_pattern.test(firstname)){
        document.getElementById("fname-valid").innerHTML = ""
    }else{
        document.getElementById("fname-valid").innerHTML = "first name should be only letters"
    }
}
// last name 
function lastname_validation() {
    let lastname = document.getElementById("lname").value
    const lastname_pattern = /^[a-zA-Z]+$/;
    if(lastname_pattern.test(lastname)){
        document.getElementById("lname-valid").innerHTML = ""
    }else{
        document.getElementById("lname-valid").innerHTML = "last name should be only letters"
    }
}
//  email
function email_validation (){
    let email = document.getElementById("email").value
    const email_pattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if(email_pattern.test(email)){
        document.getElementById("email-valid").innerHTML = ""   
    }else{
        document.getElementById("email-valid").innerHTML = "email must be in this format : exampale@abc.abc "
    }
}
// password
function password_validation(){
    let password = document.getElementById("pass").value
    const password_pattern = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;
    if(password_pattern.test(password)){
        document.getElementById("password-valid").innerHTML = ""
    }else{
        document.getElementById("password-valid").innerHTML = "password must be 8 character and contain at least one uppercase letter, one lowercase letter, one digit, and one special character"
    }
}
// re_password
function re_password_validation(){
    let password = document.getElementById("pass").value
    let re_password = document.getElementById("confpass").value
    if(password === re_password){
        document.getElementById("re-pass-valid").innerHTML = ""
    }else{
        document.getElementById("re-pass-valid").innerHTML = "re-type password should match password"
    }
}
// gender
function gender_validation(){
    let gender = document.querySelector("input[name='gender']:checked")
    if(gender !== null){
        document.getElementById("gender-valid").innerHTML = ""
    }else{
        document.getElementById("gender-valid").innerHTML = "please select gender"
    }
}
//birth date
function birth_date_validation(){
    let birth_date = document.getElementById("birthdate").value
    if(birth_date !== ""){
        document.getElementById("birthdate-valid").innerHTML = ""
    }else{
        document.getElementById("birthdate-valid").innerHTML = "please select birth date"
    }
}
// country
function country_validation(){
    let country = document.getElementById("country").value
    if(country == "country"){
        document.getElementById("country-valid").innerHTML = "please select country"
    }else{
        document.getElementById("country-valid").innerHTML = ""
    }
}
// profile picture
function profile_picture_validation(){
    let profile_picture = document.getElementById("profile").value
    if(profile_picture !== ""){
        document.getElementById("profile-valid").innerHTML = ""
    }
    else{
        document.getElementById("profile-valid").innerHTML = "please select profile picture"
    }
}
//  hobbies
function hobbies_validation(){
    let hobbies = document.querySelector("input[name='hobbies']:checked")
    if(hobbies !== null ){
        document.getElementById("hobbies-valid").innerHTML = ""
    }else{
        document.getElementById("hobbies-valid").innerHTML = "please select any one hobbeis"
    }
}
// phone number
function phone_validation(){
    let phone = document.getElementById("mobile").value
    const phone_pattern = /^\d{10}$/;
    if(phone_pattern.test(phone)){
        document.getElementById("mobile-valid").innerHTML = ""
    }else{
        document.getElementById("mobile-valid").innerHTML = "phone number should be 10 digit"
        }
    }

// for check validation of all 
const element = document.getElementById("register");
element.addEventListener("click", function(e) {
    username_validation()
    email_validation ();
    password_validation();
    re_password_validation();
    firstname_validation();
    lastname_validation();
    gender_validation();
    birth_date_validation()
    country_validation();
    profile_picture_validation()
    hobbies_validation();
    phone_validation()
    // e.preventDefault()
});
var firebaseConfig = {
    apiKey: "AIzaSyDC7f85NyGtIjIxWKAcCtPa-2YRHyvUYr0",
    authDomain: "login-with-firebase-78027.firebaseapp.com",
    projectId: "login-with-firebase-78027",
    storageBucket: "login-with-firebase-78027.appspot.com",
    messagingSenderId: "724304471805",
    appId: "1:724304471805:web:f6ff0558c7836736158094"
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);

//Intitialize Variable
const auth = firebase.auth();
const database = firebase.database();

function register() {
    console.log("Clicked");
    first_name = document.getElementById('first_name').value;
    last_name = document.getElementById('last_name').value;
    email = document.getElementById('email').value;
    password = document.getElementById('password').value;
    confirm_password = document.getElementById('confire_password').value;

    if (validation_email(email) == false || validate_password(password) == false) {
        alert("Email or Password is Out.");
        return;
    }
    if(validate_field(first_name) == false || validation_email(last_name) == false || validate_password(confirm_password) == false) {
        alert ("One or More Extra Fields is Empty.");
        return;
    }

    //Move On With Auth
    auth.createUserWithEmailAndPassword(email, password)
    .then(function(){
        var user = auth.currentUser;

        //Add this user to firebase database
        var database_ref = database.ref();

        //Create User Data
        var user_data = {
            first_name : first_name,
            last_name : last_name,
            email : email,
            password : password,
            confirm_password : confirm_password,
            last_login : Date.now()
        }

        database_ref.child('users/' + user.uid).set(user_data)

        alert("User Created!!");
    })
    .catch(function(error) {
        //Firebase will use this to alert of its errors
        var error_code = error.code;
        var error_message = error.message;
        alert(error_message);
    })
}

function validation_email(email) {
    check_email = /^[^@]+@\w+(\.\w+)+\w$/.test(str);
    if (check_email.test(email) == true) {
        return true;
    }
    else {
        return false;
    }
}

function validate_password(password) {
    if (password < 6) {
        return false;
    }
    else {
        return true;
    }
}

function validate_field(field) {
    if (field == null) {
        return false;
    }
    if (field.length <= 0) {
        return false
    }
    else {
        return true;
    }
}

firebase();
let canSendForm = false;

function checkLoginAvilable(){
    let formLogin = document.getElementById("login");

    fetch('http://127.0.0.1:5000/form/validate/login/' + formLogin.value, {
            method: 'GET',
            headers: {
                'Accept': 'text/plain'
            }
        }).then( (response) => {
            response.text().then((text) => {
                console.log(text);
                if(text === "not"){
                    canSendForm = false;
                }
                else {
                    canSendForm = true;
                }
            })
        })
        .catch( (ex) => {
            console.log('Connection failed', ex);
         });
}

function validateForm() {
    if(canSendForm === false){
        return canSendForm;
    }
    if (validateName() &&
        validateLastname() &&
        validateLogin() &&
        validatePassword()
    )
    {
        return true;
    }
    alert("Form fields not valid!");
    return false;
}

function validateName() {
    let formLogin = document.getElementById("firstname");
    if((formLogin.value.length > 0 && formLogin.value.length < 65) &&
        /[A-Z][a-zA-Z][^#&<>\"~;$^%{}?]{1,20}$/.test(formLogin.value)){
        return true;
    }
    return false;
}

function validateLastname() {
    let formLogin = document.getElementById("lastname");
    if((formLogin.value.length > 0 && formLogin.value.length < 65) &&
        /[A-Z][a-zA-Z][^#&<>\"~;$^%{}?]{1,20}$/.test(formLogin.value)){
        return true;
    }
    return false;
}

function validateLogin() {
    let formLogin = document.getElementById("login");
    if((formLogin.value.length > 0 && formLogin.value.length < 65) &&
        /[A-Z][a-zA-Z][^#&<>\"~;$^%{}?]{1,20}$/.test(formLogin.value)){
        return true;
    }
    return false;
}

function validatePassword() {
    let formPassword = document.getElementById("password");
    let formNextPassword = document.getElementById("repassword");
    if(formPassword.value == formNextPassword.value &&
        (formPassword.value.length > 0 && formPassword.value.length < 129) &&
        /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$/.test(formPassword.value)){
        return true;
    }
    document.getElementById("pass-tip").hidden = false;
    return false;
}

function sendForm(){
    let formData = document.getElementById("register_form");

    if(validateForm()){
        fetch('http://127.0.0.1:5000/form/data', {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                name: formData[0].value,
                lastname: formData[1].value,
                login: formData[2].value,
                passwd: formData[3].value,
            }
            )
        }).then( (response) => {
            response.text().then((text) => {
                console.log(text);
            })
        })
        .catch( (ex) => {
            console.log('Connection failed', ex);
         });
    }
}

const view = {}
view.showComponents = function (name) {
    switch (name) {
        case 'register': {
            document.getElementById('app').innerHTML = components.register
            let link = document.getElementById(config.FORM_LINK_ID)
            let button = document.getElementById(config.FORM_BTN_ID)

            link.onclick = linkClickHandler
            button.onclick = buttonClickHandler

            function linkClickHandler() {
                view.showComponents('logIn')
            }
            function buttonClickHandler(event) {
                event.preventDefault()
                let form = document.getElementById(config.FORM_REGISTER_ID)
                let registerInfo = {
                    firstname: form.firstname.value,
                    lastname: form.lastname.value,
                    email: form.email.value,
                    password: form.password.value,
                    confirmPassword: form.confirmPassword.value
                } 
                if(registerInfo.firstname == '') {
                    view.setText(config.ERROR_FIRSTNAME_ID, 'Invalid firstname!')
                }else {
                    view.setText(config.ERROR_FIRSTNAME_ID, '')
                }

                if(registerInfo.lastname == '') {
                    view.setText(config.ERROR_LASTNAME_ID, 'Invalid lastname!')
                }else {
                    view.setText(config.ERROR_LASTNAME_ID, '')
                }

                if(registerInfo.email== '') {
                    view.setText(config.ERROR_EMAIL_ID, 'Invalid email!')
                }else {
                    view.setText(config.ERROR_EMAIL_ID, '')
                }

                if(registerInfo.password == '') {
                    view.setText(config.ERROR_PWD_ID, 'Invalid password!')
                }else {
                    view.setText(config.ERROR_PWD_ID, '')
                }

                if(registerInfo.confirmPassword == '' || registerInfo.password != registerInfo.confirmPassword) {
                    view.setText(config.ERROR_CONFIRM_PWD_ID, 'Invalid confirm password!')
                }else {
                    view.setText(config.ERROR_CONFIRM_PWD_ID, '')
                }

                if(validateregisterInfo()) {
                    //do register 
                }
            }
            break
        }
        case 'logIn': {
            document.getElementById('app').innerHTML = components.logIn
            let link = document.getElementById(config.FORM_LINK_ID)
            let button = document.getElementById(config.FORM_BTN_ID)

            link.onclick = linkClickHandler
            button.onclick = buttonClickHandler

            function linkClickHandler() {
                view.showComponents('register')
            }

            function buttonClickHandler(event) {
                event.preventDefault()
                console.log(event)
                let form = document.getElementById(config.FORM_LOG_IN_ID)
                let logInInfo = {
                    email: form.email.value,
                    password: form.password.value
                }
                if (logInInfo.email == '') {
                    view.setText(config.ERROR_EMAIL_ID, 'Invalid email!')
                    // document.getElementById('error-email').innerText = "Invalid email"
                }else {
                    view.setText(config.ERROR_EMAIL_ID, '')
                    // document.getElementById('error-email').innerText = ''
                }

                if (logInInfo.password == '') {
                    view.setText(config.ERROR_PWD_ID, 'Invalid password!')
                    // console.log('Invalid password !')
                }else {
                    view.setText(config.ERROR_PWD_ID, '')
                }

                if(validateLogInInfo(logInInfo)) {
                    //do log in
                }
            }
            break
        }
    }
}

view.setText = function(id, message) {
    document.getElementById(id).innerText = message
}
// show compunent to screen
// showComponents('register')
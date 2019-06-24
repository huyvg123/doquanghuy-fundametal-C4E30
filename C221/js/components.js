const components = {
    // //register
    // register: `a long string`,
    // //login
    // login: `another long string`,
    // //chat
    // // ..
    // alert: function () {
    //     // this.
    //     alert("Hello form components")
    //     // this == components
    // }
}

// console.log(components)
// console.log(components.register)
// console.log(components.login)
// components.alert()

components.register = `
<section class="register-container">
            <div class="form-container">
                <div class="logo">
                    <span>Techkids Chat</span>
                </div>
                <div class="form-wrapper">
                    <form id="${config.FORM_REGISTER_ID}">
                        <div class="name-wrapper">
                            <div class="input-wrapper">
                                <input type="text" name="${config.INPUT_FIRST_NAME}" placeholder="First Name">
                                <div class="error-message" id="${config.ERROR_FIRSTNAME_ID}"></div>
                            </div>
                            <div class="input-wrapper">
                                <input type="text" name="${config.INPUT_LAST_NAME}" placeholder="Last Name">
                                <div class="error-message" id="${config.ERROR_LASTNAME_ID}"></div>
                            </div>
                        </div>    
                        <div class="input-wrapper">
                            <input type="email" name="${config.INPUT_EMAIL_NAME}" placeholder="Email">
                            <div class="error-message" id="${config.ERROR_EMAIL_ID}"></div>
                        </div>
                        <div class="input-wrapper">
                            <input type="password" name="${config.INPUT_PWD_NAME}" placeholder="Password">
                            <div class="error-message" id="${config.ERROR_PWD_ID}"></div>
                        </div>    
                        <div class="input-wrapper">
                            <input type="password" name="${config.INPUT_CONFIRM_PWD_NAME}" placeholder="Confirm password">
                            <div class="error-message" id="${config.ERROR_CONFIRM_PWD_ID}"></div>
                        </div>
                        <div class="form-footer">
                            <a id="form-link" href="#">Already have a account? Login</a>
                            <button id="form-btn" type="submit">Rigister</button>

                        </div>
                    </form>
                </div>
            </div>
        </section>
`

components.logIn =`
<section class="log-in-container">
            <div class="form-container">
                <div class="logo">
                    <span>Techkids Chat</span>
                </div>
                <div class="form-wrapper">
                    <form id="form-log-in">  
                        <div class="input-wrapper">
                            <input type="email" name="${config.INPUT_EMAIL_NAME}" placeholder="Email">
                            <div class="error-message" id="${config.ERROR_EMAIL_ID}"></div>
                        </div>
                        <div class="input-wrapper">
                            <input type="password" name="${config.INPUT_PWD_NAME}" placeholder="Password">
                            <div class="error-message" id="${config.ERROR_PWD_ID}"></div>
                        </div>    
                        <div class="form-footer">
                            <a id="form-link" href="#">Not yes have an account? Register</a>
                            <button id="form-btn" type="submit">Log In</button>
                        </div>
                    </form>
                </div>
            </div>
        </section>
`
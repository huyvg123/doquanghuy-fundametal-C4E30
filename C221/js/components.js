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
                    <form>
                        <div class="name-wrapper">
                            <div class="input-wrapper">
                                <input type="text" name="firstname" placeholder="First Name">
                            </div>
                            <div class="input-wrapper">
                                <input type="text" name="lastname" placeholder="Last Name">
                            </div>
                        </div>    
                        <div class="input-wrapper">
                            <input type="email" name="email" placeholder="Email">
                        </div>
                        <div class="input-wrapper">
                            <input type="password" name="password" placeholder="Password">
                        </div>    
                        <div class="input-wrapper">
                            <input type="password" name="confirm password" placeholder="Confirm password">
                        </div>
                        <div class="form-footer">
                            <a href="#">Already have a account? Login</a>
                            <button type="submit">Rigister</button>

                        </div>
                    </form>
                </div>
            </div>
        </section>
`
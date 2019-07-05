const controller = {}

controller.register = async function (registerInfo) { //email, password, firstname, lastname
    if (validateRegisterInfo(registerInfo)) {
        console.log('do register')
        try {
            let resultCreatUser = await window.firebase.auth().createUserWithEmailAndPassword(registerInfo.email, registerInfo.password)

            // console.log('creat user')
            // console.log(result)
            // let user = resultCreatUser.user
            console.log(resultCreatUser)


            //2. Update thông tin người dùng
            firebase.auth().currentUser.updateProfile({
                displayName: registerInfo.firstname + " " + registerInfo.lastname
            })

            //3. Gửi email xác nhận
            firebase.auth().currentUser.sendEmailVerification()

            console.log(firebase.auth().currentUser)
            // let resultUpdatetUser = await window.firebase.auth().updateCurrenUser({
            //     //displayName: registerInfo.firstname + ' ' + registerInfo.lastname
            //     display: `${registerInfo.firstname} ${registerInfo.lastname}`
            // })
            // console.log(resultCreatUser)

            // let resultSendMail = await window.firebase.auth().sendSignInLinkToEmail(registerInfo.email)
            // console.log(resultSendMail)

            //4. Hiển thị thông báo
            view.setText(config.MESSAGE_SUCCESS_ID, "Success Message!")
        } catch (error) {
            view.setText(config.MESSAGE_ERROR_ID, error.message || "Register Failed!")
        }
    }

}

controller.logIn = async function (logInInfo) {
    if (validateLogInInfo(logInInfo)) {
        try {
            let result = await firebase.auth().signInWithEmailAndPassword(
                logInInfo.email,
                logInInfo.password
            )
            console.log(result.user)
            if (!result.user.emailVerified) {
                //return = throw (throw kèm theo lỗi)
                throw new Error('Plese verify email first!')
            } else {
                view.showComponents('chat')
                models.logIn(result.user)
                models.loadConversations(result.user.email)
                // let conversations = await models.loadConversations(result.user.email) //async
                // let conversation = conversations[0]
                // if(conversation) {
                //     let messages = conversation.messages
                //     for(let message of messages) {
                //          view.addMessage(message)
                //     }
                // }
            }
        } catch (error) {
            // console.log(error)
            view.setText(config.MESSAGE_ERROR_ID, error.message || "log in failed")
        }
    }

}

controller.initAuth = function() {
    view.showComponents('loading')
    firebase.auth().onAuthStateChanged(async function(user) {
        if (user && user.emailVerified) {
            //chat
            view.showComponents('chat')

            models.logIn(user)
            models.loadConversations(user.email)
        } else {
            //login
            if (user) {
                await firebase.auth().signOut()
            }
            view.showComponents('logIn')
        }
    })
    //..
}
const models = {
    authUser: null,
    conversations: [],
    currentActiveConversation: null,
}

models.logIn = function (authUser) {
    models.authUser = authUser
    models.conversations = []
    models.currentActiveConversation = null
}

models.loadConversations = function (email) {
    firebase.firestore()
        .collection('conversations')
        .where('users', 'array-contains', email)
        .onSnapshot(function (snapshot) {
            if (!models.conversations) {
                // first loading
                // let conversations = []
                // for(let doc of snapshot.docs) {
                //     let conversation = doc.data()
                //     conversation.id = doc.id
                //     conversations.push(conversation)
                // }
                let conversations = snapshot.docs.map(function (doc) {
                    let conversation = doc.data()
                    conversation.id = doc.id
                    return conversation
                })
                models.conversations = conversations
                if (conversations.length) {
                    models.setActiveConversation(conversations[0])
                }
            } else {
                // doc change
                for(let docChange of snapshot.docChanges()) {
                    if(docChange.type == 'modified') {
                        let conversation = docChange.doc.data()
                        //title = '', createdAt = Date,
                        //user = [email], messages = [message]
                        conversation.id = docChange.doc.id
                        let foundIndex = models.conversations.findIndex(function(cvst) {
                            return conversation.id = cvst.id
                        })
                        //update data vao du lieu trong models
                        if(foundIndex >= 0) {
                            models.conversations[foundIndex] = conversation
                        }
                        //update data len phan hien thi
                        if(models.currentActiveConversation
                                && conversation.id == models.currentActiveConversation.id) {
                            models.setActiveConversation(conversation)
                            }
                    }
                }
                // let conversation = snapshot.docChanges().map(function (docChange) {
                //     if (docChange.type == 'modified') {
                //         let conversation = docChange.doc.data()
                //         conversation.id = docChange.doc.id
                //         return conversation
                //     }
                // }).forEach(function (conversation) {
                //     let foundIndex = models.conversations.findIndex(function (cvst) {
                //         return cvst.id == conversation
                //     })
                //     if (foundIndex >= 0) {
                //         models.conversations[foundIndex] = conversation
                //     }
                //     if (models.currentActiveConversation
                //         && models.currentActiveConversation.id == conversation.id) {
                //         models.setActiveConversation(conversation)
                    // }
                // })
            }
        })
}

models.setActiveConversation = function (conversation) {
    models.currentActiveConversation = conversation
    view.clearMessages()
    if (conversation.messages) {
        for (let message of conversation.messages) {
            view.addMessage(message)
        }
    }
}

models.creatMessage = function(content) {
    let message = {
        content: content,
        createdAt: new Date().toISOString(),
        owner: models.authUser.email
    }
    if(models.currentActiveConversation) {
        firebase.firestore()
            .collection('conversations')
            .doc(models.currentActiveConversation.id)
            .update({
                messages: firebase.firestore.FieldValue.arrayUnion(message)
            })
    }
}

models.clear = function() {
    models.authUser = null
    models.conversations = null
    models.currentActiveConversation = null
}
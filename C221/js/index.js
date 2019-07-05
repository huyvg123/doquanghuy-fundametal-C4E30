window.onload = init
https://media0.giphy.com/media/3oEjI6SIIHBdRxXI40/giphy.gif

function init() {
    // view.showComponents('logIn') 
    controller.initAuth()
    // log in
    // console.log(window.firebase.auth())
}




// const components = {
//     header: `
//     <h1>Website<h1/>
//     `,
//     content: `
//     <p> Website content <p/>
//     `
// }

// window.onload = init 

// function init() {
//     document.getElementById('app').innerHTML = components.header
// }
// let count = 0
        
// const clickEvent = {
//     handleClick: function () {
//         count++
//         switch(count) {
//             case 1: {
//                 console.log("fist click")
//                 break
//             }
//             case 2: {
//                 console.log("second click")
//                 break
//             }
//             default: {
//                 console.log("count: "+ count)
//             }
//         }
//     }
// }

// window.onclick = clickEvent.handleClick


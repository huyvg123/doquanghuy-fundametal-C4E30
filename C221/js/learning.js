//variable
//thay thế int, char, double, boolean... ~ let (const)
//let ~ local variable

// function sum(a, b) {
//     let total = a + b
//     return total
// }
// const ~ big scope local variable, global variable
// function sayHello () {
//     console.log('Hello')
// }



//function
// function loadImage(callback) {
//     let urc = `https://helpx.adobe.com/content/dam/help/en/stock/how-to/visual-reverse-image-search/jcr_content/main-pars/image/visual-reverse-image-search-v2_intro.jpg`
//     let image = new Image()
//     image.src = urc
//     image.onload = imageLoadHandler
//     image.onload = errorHandler

//     function imageLoadHandler() {
//         console.log('Loaded image!')
//         callback(null, image)
//     }

//     function errorHandler(error) {
//         callback(error)        
//     }
// }

function loadImage() { 
    return new Promise(function(resolve, reject) {
        let url = `https://helpx.adobe.com/content/dam/help/en/stock/how-to/visual-reverse-image-search/jcr_content/main-pars/image/visual-reverse-image-search-v2_intro.jpg`
        let image = new Image()
        image.src = url
        image.onload = imageLoadHandler
        image.onerror = errorHandler

        function imageLoadHandler() {
            console.log('Loaded image!')
            resolve(image)
        }

        function errorHandler(error) {
            reject(error)        
        }
    })
}

function display() { 
    console.log('Hello user!')
}

// function process() {
//     loadImage(loadImageCallback)
//     function loadImageCallback(error, data) {
//         if(error) {
//             console.log('Error!')
//         } else {
//             display()
//             console.log(data)
//         }
//     }
// }

async function process() {
    //loadImage => return Promise
    try {
    let image = await loadImage()
    display()
    console.log(image)
    } catch(error) {
        console.log(error)
    }
}

process()   

//object
//attributes, methods
var obj = {
    firstname: "Do Quang",
    lastname: "Huy",
    saySomething: function() {
        console.log(obj.firstname + " " + obj.lastname )
    }
}

var keys = Object.keys(obj)
var values = Object.values(obj)
var entries = Object.entries(obj)

//array

var arr = [1,2,"aa",obj, true]
var arr2 = []
arr2.push(1)
arr2.push('aa')

//tra ra ket qua la 1 array moi, khong thay doi arr  dc goi
//map
//filter
//sort
//concat

//sua trc tiep tren arr dc goi
//splice(xoa)

//string, number

//typeof

function getStringLength(str) {
    if(typeof str == 'string') {
        return str.length
    }
    return -1 
}

getStringLength()
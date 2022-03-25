'use strict';

// 1. isHometown
function isHometown(town) {
    console.log(town === "San Francisco") 
}

// isHometown("Sacramento")

// 2. getFullName

const get_full_name = (first_name, last_name) => {
    console.log(`${first_name} ${last_name}`)
}

//get_full_name("Munna", "Khan")

// 3. calculateTotal

const calculateTotal = function(basePrice, state, tax=0.05) {
    
    const subtotal = basePrice * (1 + tax)

    let fee = 0
    if (state == "CA") {
        fee = 0.03 * subtotal
    } else if (state == "PA") {
        fee = 2
    } else if (state == "MA") {
        if (basePrice <= 100) {
            fee = 1
        } else {
            fee = 3
        }
    } 

    console.log(subtotal + fee)
}

calculateTotal(101, "MA")
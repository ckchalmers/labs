'use strict';

// 1. printIndices
function printIndices(items) {
  // Replace this with your code
  for (const i in items) {
    console.log(`${i} ${items[i]}`)
  }
}

// printIndices(['w', 'e', 'r', 't'])

// 2. everyOtherItem
function everyOtherItem(items) {
  // Replace this with your code
  for (const i in items) {
    if (i % 2 === 0) {
      console.log(items[i])
    }
  }
}

// everyOtherItem(['t', 'e', 's', 't', 'g', 's'])


// 3. smallestNItems
function smallestNItems(items, n) {
  // Replace this with your code
  let sortedArr = items.sort()
  console.log(sortedArr[0])
  
}

smallestNItems([3, -9, 10, 0, -100])

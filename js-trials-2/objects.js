'use strict';

// 1. countWords
function countWords(phrase) {
  // Replace this with your 
  const words = phrase.split(" ")
  let word_counts = {}
  for (const word of words) {
    if (word in word_counts) {
      word_counts[word] += 1
    } else {
      word_counts[word] = 1
    }
  }
  console.log(word_counts)

}

// countWords('Some phrase here please please test')

// 2. getMelonsAtPrice
function getMelonsAtPrice(price) {
  // Replace this with your code

  const melonPrices = {
    2.50: ['Cantaloupe', 'Honeydew'],
    2.95: ['Watermelon'],
    3.25: ['Musk', 'Crenshaw'],
    14.25: ['Christmas']
  }


  if (melonPrices.hasOwnProperty(price)) {
    console.log(melonPrices[price].sort())
  } else {
    return null
  }

}

getMelonsAtPrice(2.50)

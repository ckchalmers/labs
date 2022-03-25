'use strict';

function wordsInCommon(words1, words2) {
  const words1_set = new Set(words1)
  const words2_set = new Set(words2)

  let result = new Set()

  for (const word of words1_set) {
    if (words2_set.has(word)) {
      result.add(word)
    }
  }
  console.log(result)
}

//wordsInCommon(['the', 'quick', 'brown'], ['fox', 'jumped', 'over', 'the'])

function kidsGame(names) {
  let output = [names.shift()]
  let first_letter_to_words = {}

  for (const name in names) {
    if (!first_letter_to_words.hasOwnProperty(name[0])) {
      first_letter_to_words[name[0]] = [name]
    } else {
      first_letter_to_words[name[0]].add(name)
    }
  }
  
  while (true) {
    let start_letter = output[output.length-1][output.length-1]

    if(!first_letter_to_words.hasOwnProperty(start_letter)) {
      break;
    }
    
    output.add(first_letter_to_words[start_letter].shift())
  }

  console.log(output)
}

kidsGame(["bagon", "baltoy", "yamask", "starly","nosepass", "kalob", "nicky", "booger"])
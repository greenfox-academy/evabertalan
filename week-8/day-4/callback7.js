'use strict';

var fs = require('fs');

function getFirstIndexInAlmaTxt(letter, cb) {
  fs.readFile('alma.txt', function(err, content){
    if (err) {
      return cb(err);
    }
    var stringContent = String(content);
    for (var i = 0; i < stringContent.length; i++) {
      if (stringContent[i] === letter) {
         return cb([i])
      }
    }
  });
}

getFirstIndexInAlmaTxt('p', function(index) {
  console.log(index);
})

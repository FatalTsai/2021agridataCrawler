var fs = require('fs');
var path = require('path');
const exec = require('child_process').exec;

var prettyJson = function(filepath){

exec('node prettyJson.js '+filepath,
    (error, stdout, stderr) => {
        console.log(`${stdout}`);
        console.log(`${stderr}`);
        if (error !== null) {
            console.log(`exec error: ${error}`);
        }
    });
}

var walk = function(dir, done) {
  var results = [];
  fs.readdir(dir, function(err, list) {
    if (err) return done(err);
    var pending = list.length;
    if (!pending) return done(null, results);
    list.forEach(function(file) {
      file = path.resolve(dir, file);
      fs.stat(file, function(err, stat) {
        if (stat && stat.isDirectory()) {
          walk(file, function(err, res) {
            results = results.concat(res);
            if (!--pending) done(null, results);
          });
        } else {
          results.push(file);
          if (!--pending) done(null, results);
        }
      });
    });
  });
};

walk("data/", function(err, results) {
    if (err) throw err;
    // console.log(results);
    results.forEach((ele)=>{
        if(path.extname(ele) ==".json"){
            console.log('pretty ',ele)
            prettyJson(ele)
        }
    })
  });
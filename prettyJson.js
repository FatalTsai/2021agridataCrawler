var fs = require('fs')

// console.log(process.argv)
let outPath = String(process.argv[2])
console.log("pretty json ",outPath)
let tmp = JSON.parse(fs.readFileSync(outPath,"utf8").replace(/'/gm,`"`) )

console.log(tmp.length)

fs.writeFileSync(outPath,JSON.stringify(tmp,null,'\t'))
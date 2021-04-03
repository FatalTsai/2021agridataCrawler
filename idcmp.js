var fs = require('fs');

openList = JSON.parse(fs.readFileSync("summaryList.json"))
detailList = JSON.parse(fs.readFileSync("detailList.json"))

openList.forEach(element => {
    notfound = true
    // console.log(element.ID)
    detailList.forEach( (ele) =>{
        if(element.ID == ele.ID){
            // console.log(element.ID,'    ',ele.ID)
            notfound = false
        }
    })
    if(notfound){
        console.log(element.ID,"    not found")
    }

});

console.log('openList.length = ',openList.length)
console.log('detailList.length = ',detailList.length)

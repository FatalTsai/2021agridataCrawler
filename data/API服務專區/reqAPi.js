const request = require('request');
const fs = require('fs')
const path = require('path')
function fetchAPI(param){
    return new Promise((resolve, reject) => {

        // console.log(param)
        var options = {
            'method': 'GET',
            'url': 'https://agridata.coa.gov.tw/api/v1'+"/AutoRainfallStationType/",
            'headers': {
            'Cookie': 'ASP.NET_SessionId=mydphvq5deakcxxkjz1vahyb'
            }
        };
        
        var ans
        request(options,  function (error, response,body) {
            // if (error) throw new Error(error);
            // console.log(response.body);
            if (error) reject(error);
            if (response.statusCode != 200) {
                reject('Invalid status code <' + response.statusCode + '>');
            }
            resolve(body);
        });
    })
}

function downloadPage(url) {
    return new Promise((resolve, reject) => {
        request(url, (error, response, body) => {
            if (error) reject(error);
            if (response.statusCode != 200) {
                reject('Invalid status code <' + response.statusCode + '>');
            }
            // resolve(response.body);
        });
    });
}
function badcharReplce(test_str){
    test_str = test_str.replace(/\\/gm,"%5C")
    test_str = test_str.replace(/\//gm,"%2F")
    test_str = test_str.replace(/:/gm,"%3A")
    test_str = test_str.replace(/\*/gm,"%2A")
    // test_str = test_str.replace(/\  ?/gm,"%3F")
    test_str = test_str.replace(/“/gm,"%93")
    test_str = test_str.replace(/”/gm,"%94")
    test_str = test_str.replace(/</gm,"%3C")
    test_str = test_str.replace(/>/gm,"%3E")
    return test_str
}



var  summayData = JSON.parse ( fs.readFileSync("summary.json") )

// console.log(JSON.stringify(summayData,null,'\t'))

// console.log(Object.keys( summayData.paths))

Object.keys( summayData.paths).forEach(async function(ele){

    var parentDir = badcharReplce (String(summayData.paths[ele].get["tags"])  )
    var childDir = badcharReplce ( String(summayData.paths[ele].get["summary"]) )
    var folderPath = path.join(parentDir, childDir)

    if(!fs.existsSync(parentDir))
    {
        fs.mkdirSync(parentDir)
    } 

    // fs.rm(folderPath, { recursive:true }, (err) => {
    //     if(err){
    //         // File deletion failed
    //         console.error(err.message);
    //         return;
    //     }
    //     // console.log("File deleted successfully");
          
    //     // List files after deleting
    //     // getCurrentFilenames();
    // })
    if(!fs.existsSync(folderPath))
    {
        fs.mkdirSync(folderPath)
    } 
    
 
    fs.writeFileSync(path.join(folderPath,childDir+"Data.json"), await fetchAPI(ele))
    fs.writeFileSync(path.join(folderPath,childDir+"Summary.json"), await JSON.stringify( summayData.paths[ele],null,'\t'))

    // console.log("ele = ",await fetchAPI(ele))

})
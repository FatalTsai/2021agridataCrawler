import requests
import json #https://www.w3schools.com/python/python_json.asp
import urllib.request as req
import re
import os
import time

def detailList():
    cnt = 0
    detailParseData = []
    parseData = getopenDataList(True)
    for ele in parseData[650:750]:
        ele = {**ele, **detail(ele["ID"])}
        print(ele)
        detailParseData.append(ele)

        time.sleep(0.5)
        cnt+=1
        if(cnt%100 ==0):
            listToPrettyJson('openDataList.json',detailParseData)
            print('sleeping...')
            time.sleep(13)
    
    listToPrettyJson('openDataList.json',detailParseData)





def getopenDataList(writeResToFile):
    urls = ["https://agridata.coa.gov.tw/api/open_list.ashx","https://agridata.coa.gov.tw/api/open_list_thematic.ashx"]

    headers = {
      'Content-Type': 'application/x-www-form-urlencoded',
      'Cookie': 'ASP.NET_SessionId=q3io0kbx3hof0ukhox2rlexf'
    }
    parseData = []

    for url in urls:
        response = requests.request("GET", url, headers=headers,data="Page=1&Limit=100")
        Total_pages = json.loads(response.text)['Total_pages']

        for page in range(1,Total_pages+1):
            payload='Page='+str(page)+'&Limit=100'
            response = requests.request("GET", url, headers=headers, data=payload)
            parseData.extend( json.loads(response.text)['Data'])

    cnt = 1

    # ouput detailList

    # detailParseData = []
    # for ele in parseData[1290:]:
    #     ele = {**ele, **detail(ele["ID"])}
    #     print(ele)
    #     detailParseData.append(ele)

    #     time.sleep(0.3)
    #     cnt+=1
    #     if(cnt%100 ==0):
    #         if(writeResToFile):
    #             listToPrettyJson('openDataList.json',detailParseData)
    #         print('sleeping...')
    #         time.sleep(13)


    if(writeResToFile):
        listToPrettyJson('summaryList.json',parseData)
  

    # print(parseData)
    # print(json.dumps(parseData, indent=4, sort_keys=False))

    # print("\n\n",len(parseData) )
    return parseData


def listToPrettyJson(filename,listData):
    f = open(filename, 'w')
    f.write((str(listData).replace("'","\"")) )
    f.close()
    os.system("node prettyJson.js "+str(filename))

def badcharReplce(test_str):
    test_str = test_str.replace("\\","%5C")
    test_str = test_str.replace("/","%2F")
    test_str = test_str.replace(":","%3A")
    test_str = test_str.replace("*","%2A")
    test_str = test_str.replace("?","%3F")
    test_str = test_str.replace("“","%93")
    test_str = test_str.replace("”","%94")
    test_str = test_str.replace("<","%3C")
    test_str = test_str.replace(">","%3E")
    return test_str







def pdfDownload(Id,filePath): 
    pdfUrl = "https://agridata.coa.gov.tw/open_detail.aspx?id="+str(Id)

    pdfHeaders = {
                'Content-Type': 'application/x-www-form-urlencoded',
                'Cookie': 'ASP.NET_SessionId=q3io0kbx3hof0ukhox2rlexf'
                }
    # payload='__EVENTTARGET=ctl00%24ContentPlaceHolder1%24m_ReadMe&__EVENTARGUMENT=&__VIEWSTATE=%2FwEPDwULLTE4NTEzMzg3NjkPZBYCZg9kFgICAQ9kFgICAQ9kFiZmDxYCHgRUZXh0BSHpq5jnl4Xljp%2FmgKfnpr3mtYHmhJ%2FpmLLnlqvomZXnva5kAgEPFgIfAAUh6auY55eF5Y6f5oCn56a95rWB5oSf6Ziy55ar6JmV572uZAICDw8WAh4HVmlzaWJsZWhkZAIDDxYCHwAFBDM1MTFkAgQPFgIfAAUEMTcyN2QCBQ8WAh8ABQoyMDIxLTA0LTAyZAIGDxYCHwAFFeWLleakjeeJqemYsueWq%2BaqoueWq2QCBw8WAh8ABRjli5XmpI3nianpmLLnlqvmqqLnlqvlsYBkAggPFgIfAAUKMjAyMC0xMi0zMWQCCQ8WAh8ABQbmr4%2Fml6VkAgoPFgIfAAWlA%2BmrmOeXheWOn%2BaAp%2Bemvea1geaEn%2BmYsueWq%2BiZlee9rijmj5DkvpsxMDnlubTotbflrrbnpr3loLTnorroqLrpq5jnl4Xljp%2FmgKfnpr3mtYHmhJ%2FmoYjkvovlj4romZXnkIbmg4XlvaIp77yM5o%2BQ5L6b6LOH5paZ5YyF5ZCr77yaSUQo5rWB5rC06JmfKeOAgWNvdW50eW5hbWUo57ij5biCKeOAgXRvd25uYW1lKOmEiemOrinjgIFzYW1wbGVfZGF0ZSjmjqHmqKPml6XmnJ8p44CBanVkZ2VfZGF0ZSjliKTlrprml6XmnJ8p44CBYXZpYW5fc3BlY2llcyjpo7zppIrnpr3nqK4p44CBQUlfMl9nZW5lcmFsKOS6nuWeiyhINeOAgU43KSnjgIFBSV8yX2dlbmVyYWwo5pKy5q665pel5pyfKeOAgUFJXzJfZ2VuZXJhbCjmkrLmrrrmlbjph48p562J5qyE5L2NPGJyLz7vvJzmlL%2Flupzos4fmlpnplovmlL7lubPoh7ros4fmlpnkvb%2FnlKjopo%2Fnr4TvvJ5kAgsPZBYCAgEPDxYEHwAFH2h0dHBzOi8vdHdhaS5iYXBoaXEuZ292LnR3L0FJX20eC05hdmlnYXRlVXJsBR9odHRwczovL3R3YWkuYmFwaGlxLmdvdi50dy9BSV9tFgQeB0RhdGFVcmwFH2h0dHBzOi8vdHdhaS5iYXBoaXEuZ292LnR3L0FJX20eD0NvbW1hbmRBcmd1bWVudAVH5YuV5qSN54mp6Ziy55ar5qqi55ar5bGAO0I4REo0ZWViSHhWSDvpq5jnl4Xljp%2FmgKfnpr3mtYHmhJ%2FpmLLnlqvomZXnva5kAgwPZBYCAgMPDxYEHwAFTmh0dHBzOi8vZGF0YS5jb2EuZ292LnR3L1NlcnZpY2UvT3BlbkRhdGEvVHJhbnNTZXJ2aWNlLmFzcHg%2FVW5pdElkPUI4REo0ZWViSHhWSB8CBU5odHRwczovL2RhdGEuY29hLmdvdi50dy9TZXJ2aWNlL09wZW5EYXRhL1RyYW5zU2VydmljZS5hc3B4P1VuaXRJZD1COERKNGVlYkh4VkgWBB8DBU5odHRwczovL2RhdGEuY29hLmdvdi50dy9TZXJ2aWNlL09wZW5EYXRhL1RyYW5zU2VydmljZS5hc3B4P1VuaXRJZD1COERKNGVlYkh4VkgfBAVH5YuV5qSN54mp6Ziy55ar5qqi55ar5bGAO0I4REo0ZWViSHhWSDvpq5jnl4Xljp%2FmgKfnpr3mtYHmhJ%2FpmLLnlqvomZXnva5kAg0PZBYCAgEPDxYCHwFoZGQCEA9kFgICAQ8WAh4LXyFJdGVtQ291bnRmZAIRDxYCHwFnFgJmDw8WAh8CBSJ%2BL29wZW5fc2VhcmNoLmFzcHg%2FaWQ9QjhESjRlZWJIeFZIZGQCEg8WAh8FZmQCEw8WAh8BaGQCGQ8PFgIeCEltYWdlVXJsBRB%2BL1dlYl9WQ09ERS5hc2h4ZGRkNUJ2lKGihMWYKG4A%2BAvvOwvCAZnnqz6xTic4KYMhYI8%3D&__VIEWSTATEGENERATOR=0F634CDA&__EVENTVALIDATION=%2FwEdAAheiHecuBObSaBgBGG33D7JVe9rD3DO5qLIZqmIxzRMEYJIJYkB9lj7bmyAq3HsE9OYnEPSdGdsijXlKS0XZvTqs%2B%2FpAnKH9yOn89varc7Z01IBOVyMrtNdEzjdZvXu6aIKKa6Fj4P0jbY6FHx68%2FGYLXCH41vH114dDE8DU50JIV6Esza8Yo%2F%2FIdI3raWhXN4TAM9RzuO1RXVHCIWA1chR'

    response1 = requests.request("GET", pdfUrl, headers=pdfHeaders)

    # print(response1.text)

    regex__VIEWSTATE = r"<input type=\"hidden\" name=\"__VIEWSTATE\" id=\"__VIEWSTATE\" value=\".*\" />"
    regex__VIEWSTATEGENERATOR  = (r"<input type=\"hidden\" name=\"__VIEWSTATEGENERATOR\" id=\"__VIEWSTATEGENERATOR\" value=\".*\" />")
    regex____EVENTVALIDATION = r"<input type=\"hidden\" name=\"__EVENTVALIDATION\" id=\"__EVENTVALIDATION\" value=\".*\" />"

    # print(response1.text)
    __EVENTTARGET = "ctl00%24ContentPlaceHolder1%24m_ReadMe"
    __VIEWSTATE = getValue( regexMatches(regex__VIEWSTATE,response1.text) )
    # https://regex101.com/r/0NHOvT/2
    __VIEWSTATEGENERATOR = getValue( regexMatches(regex__VIEWSTATEGENERATOR,response1.text) )
    # https://regex101.com/r/0NHOvT/3
    __EVENTVALIDATION = getValue( regexMatches(regex____EVENTVALIDATION,response1.text) )
    # https://regex101.com/r/0NHOvT/3

    pdfPayload =  "__EVENTTARGET="+str(__EVENTTARGET)+"&__EVENTARGUMENT=&__VIEWSTATE="+str(__VIEWSTATE)+"&__VIEWSTATEGENERATOR="+str(__VIEWSTATEGENERATOR)+"&__EVENTVALIDATION="+str(__EVENTVALIDATION)
    # https://kaijento.github.io/2017/05/04/web-scraping-requests-eventtarget-viewstate/
    response = requests.request("POST", pdfUrl, headers=pdfHeaders, data=pdfPayload)
    # print(response.content)
    with open(filePath+".pdf", "wb") as out_file:
        out_file.write(response.content) 


    
    

def getValue(test_str):
    regex = r"value=\".*\""
    tmp = regexMatches(regex,test_str)
    # https://regex101.com/r/0NHOvT/3
    # print(tmp)
    tmp = tmp.replace("+", "%2B")
    tmp = tmp.replace("/", '%2F')
    # print(tmp[7:-1])


    return tmp[7:-1]


def regexMatches(regex,test_str):
    matches = re.finditer(regex, test_str, re.MULTILINE)
    ans = ''
    for matchNum, match in enumerate(matches, start=1):
        
        # print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
        ans = (match.group())
        for groupNum in range(0, len(match.groups())):
            groupNum = groupNum + 1
            
            # print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))

    return ans

def detail(ID):
    headers = {
      'Content-Type': 'application/x-www-form-urlencoded',
      'Cookie': 'ASP.NET_SessionId=q3io0kbx3hof0ukhox2rlexf'
    }
    url = "https://agridata.coa.gov.tw/open_detail.aspx?id="+str(ID)
    detailData={
        'rating' : "",
        'NumberOfVoters' : "",
        'UpdateFrequency' : "",
        'description' : "",
        'sourceURL' : "",
        'interfaceURL' : ""
    }
    response = requests.request("GET", url, headers=headers)


    regex_rawvote = r"</select><span class=\"help  sdiv\" style=\".*\">平均 <b style=\"color: #78B42E;\" class=\"ssc\">\d+</b> 分 \( <span class=\"ssu\" style=\"float: inherit;\">\d+</span>人投票 \)</span>"
    # https://regex101.com/r/KK6j0H/2
    regex_frequ = r"<div class=\"data-search-list\">\s+<div class=\"search-input\">\s+<label class=\"label\">更新頻率</label>\s+</div>\s+<div class=\"search-input\">\s+<p>\s+.*</p>"
    # https://regex101.com/r/eluhHx/1
    regex_description = r"<div class=\"data-search-list\">\s+<div class=\"search-input\">\s+<label class=\"label\">資料描述</label>\s+</div>\s+<div class=\"search-input\">\s+<p>\s+.*<br/>＜政府資料開放平臺資料使用規範＞</p>"
    # https://regex101.com/r/5aLZUZ/1
    regex_sourceURL = r"<div class=\"search-input\">\s+<a id=\"m_SourceURL\" DataUrl=\".*\" CommandArgument="
    # https://regex101.com/r/Rf0HJi/1
    regex_interfaceURL = r"<a id=\"m_DataUrl\" DataUrl=\".*\" CommandArgument=\""
    # https://regex101.com/r/Rf0HJi/1

    rawVote =  regexMatches(regex_rawvote,response.text)
    # print('rawVote = ',rawVote)
    detailData['rating'] = regexMatches(r"\">\d+</b> 分",rawVote)[2:-6] 
    detailData['NumberOfVoters'] = regexMatches(r";\">\d+</span>人投票",rawVote)[3:-10] # https://regex101.com/r/XISJm9/1
    detailData['UpdateFrequency'] = regexMatches(regex_frequ, response.text)[320:-4]
    detailData['description'] = regexMatches(regex_description,response.text)[320:-25]
    detailData['sourceURL'] = regexMatches(regex_sourceURL,response.text)[93:-18]
    detailData['interfaceURL'] = regexMatches(regex_interfaceURL,response.text)[27:-19]

    # print( detailData['NumberOfVoters'])
    # print(detailData['interfaceURL'])
    # print(detailData)
    return detailData




    # print(response.text)


def sourceURLDownload(url,filePath):
    headers = {
      'Content-Type': 'application/x-www-form-urlencoded',
      'Cookie': 'ASP.NET_SessionId=q3io0kbx3hof0ukhox2rlexf'
    }
    extensionName = ".txt"


    try:
        response = requests.request("GET", url, headers=headers,timeout = 5)
        # print(response.headers['Content-Type'])


        # https://stackoverflow.com/questions/6579876/how-to-match-a-substring-in-a-string-ignoring-case
        if re.search('json', response.headers['Content-Type'], re.IGNORECASE):
            extensionName = ".json"
        elif re.search('html', response.headers['Content-Type'], re.IGNORECASE):
            extensionName = ".html"


        with open(filePath+extensionName, "w") as f: # https://stackoverflow.com/questions/31126596/saving-response-from-requests-to-file
            f.write((response.text) )
    except Exception as e:
         with open(filePath+extensionName, "w") as f: # https://stackoverflow.com/questions/31126596/saving-response-from-requests-to-file
            f.write(str(e) )



detailList()

# https://blog.gtwang.org/programming/python-howto-check-whether-file-folder-exists/
# if os.path.exists("data/"):
#     print("data/ exitst")
# else:
#     print("mkdir data/")
#     os.mkdir( "data/" )

# with open('detailList.json', newline='') as jsonfile:
#     detailList = json.load(jsonfile)

# cnt = 1235
# for ele in detailList[1235:]:
#     print("cnt = ",cnt)
#     print(ele)
#     if (os.path.exists("data/"+ele["Catalog"]) == False):
#         os.mkdir("data/"+ele["Catalog"])

#     if (os.path.exists("data/"+ele["Catalog"]+"/"+ele["Organ"] )==False):
#         os.mkdir("data/"+ele["Catalog"]+"/"+ele["Organ"] )

#     filePath = "data/"+ele["Catalog"]+"/"+ele["Organ"]+"/"+badcharReplce( ele["Title"] )
#     if (os.path.exists(filePath)==False):
#         os.mkdir(filePath)


#     os.system("rm -rf "+filePath+"/*")
#     pdfDownload(ele["ID"],filePath+"/"+badcharReplce( ele["Title"] )+"ReadMe")
#     sourceURLDownload(ele["sourceURL"],filePath+"/"+badcharReplce( ele["Title"] )+"sourceURL")
#     sourceURLDownload(ele["interfaceURL"],filePath+"/"+badcharReplce( ele["Title"])+"interfaceURL")

#     with open(filePath+"/"+badcharReplce( ele["Title"])+"summary.json" , "w") as f: 
#         f.write(str(ele) ) 


#     time.sleep(0.25)
#     if(cnt%100 ==0 and cnt!=0  ):
#         print("sleep... ",cnt)
#         time.sleep(15)
#     cnt+=1
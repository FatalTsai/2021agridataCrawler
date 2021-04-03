# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import re

regex = r"<input type=\"hidden\" name=\"__VIEWSTATE\" id=\"__VIEWSTATE\" value=\".*\" />"

test_str = ("\n\n\n"
	"<!DOCTYPE html>\n"
	"<html>\n"
	"<head>\n"
	"    <meta charset=\"utf-8\">\n"
	"    <meta property =\"og:type\" content=\"website\"/>\n"
	"<meta property =\"og:url\" content=\"/open_detail.aspx\"/>\n"
	"<meta property =\"og:image\" content=\"/upload/open.jpg\"/>\n\n"
	"    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1, shrink-to-fit=no\">\n"
	"    <link rel=\"api\" type=\"application/x.atom+xml\" title=\"農業開放資料服務平臺\" href=\"https://agridata.coa.gov.tw/openapi.json\" />\n"
	"    <link href=\"https://use.fontawesome.com/releases/v5.1.0/css/all.css\" integrity=\"sha384-lKuwvrZot6UHsBSfcMvOkWwlCMgc0TaWr+30HWe3a4ltaBwTZhyTEggF5tJv8tbt\" crossorigin=\"anonymous\" rel=\"stylesheet\">\n"
	"    <link href=\"/app.css\" rel=\"stylesheet\">\n"
	"    <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->\n"
	"    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->\n"
	"    <!--[if lt IE 9]>\n"
	"  <script src=\"https://oss.maxcdn.com/html5shiv/3.7.3/html5shiv.min.js\"></script>\n"
	"  <script src=\"https://oss.maxcdn.com/respond/1.4.2/respond.min.js\"></script>\n"
	"  <![endif]-->\n\n"
	"    \n"
	"    <title>關於平台 - 農業開放資料服務平台</title>\n"
	"    <link rel=\"stylesheet\" href=\"/javascript/sweetalert/dist/sweetalert.css\">\n"
	"    <script src=\"/javascript/sweetalert/dist/sweetalert.min.js\"></script>\n\n"
	"</head>\n"
	"<body>\n\n\n"
	"    <!-- Header -->\n"
	"    <header class=\"main-header\">\n"
	"        <div class=\"container full header-wrapper\">\n"
	"            <div class=\"logo-wrapper\"><a class=\"logo\" href=\"index.aspx\"></a></div>\n"
	"            <div id=\"menu-btn\">\n"
	"                <div><span></span><span></span><span></span></div>\n"
	"            </div>\n"
	"            <div class=\"menu-wrapper\">\n"
	"                <div id=\"closeMenu\"></div>\n"
	"                <nav>\n"
	"                    <div class=\"nav-link user-func\">\n"
	"                        \n"
	"                        <div><a href=\"/login.aspx\">登入</a><span></span><a href=\"join.aspx\">註冊</a></div>\n"
	"                        \n"
	"                    </div>\n"
	"                    <div class=\"sub-menu\">\n"
	"                        <a class=\"nav-link sub-menu-btn  \">\n"
	"                            <i class=\"fas fa-th\"></i><span>關於平台</span>\n"
	"                            <i class=\"last fas fa-angle-down\"></i></a>\n"
	"                        <div class=\"sub-menu-wrapper\">\n"
	"                            <a href=\"/about.aspx\">平台介紹</a>\n"
	"                            <a href=\"https://data.gov.tw/license\" target=\"_blank\">授權條款</a>\n"
	"                            <a href=\"/terms.aspx\">隱私權保護</a>\n\n"
	"                        </div>\n"
	"                    </div>\n"
	"                    <a class=\"nav-link \" href=\"/application.aspx\">\n"
	"                        <i class=\"fas fa-book\"></i><span>應用範例</span>\n\n"
	"                    </a>\n"
	"                    <div class=\"sub-menu\">\n"
	"                        <a class=\"nav-link sub-menu-btn  \">\n"
	"                            <i class=\"fas fa-download\"></i><span>API專區</span>\n"
	"                            <i class=\"last fas fa-angle-down\"></i>\n"
	"                        </a>\n"
	"                        <div class=\"sub-menu-wrapper\">\n"
	"                            <a href=\"/api.aspx\">API專區</a>\n"
	"                            <a href=\"/apidocs.aspx\">API文件</a>\n\n"
	"                        </div>\n"
	"                    </div>\n"
	"                    \n"
	"                    <a class=\"nav-link \" href=\"/Thematic.aspx\"><i class=\"fas fa-comments\"></i><span>主題式資料</span></a>\n"
	"                    <a class=\"nav-link \" href=\"/open.aspx\"><i class=\"fas fa-comments\"></i><span>資料開放</span></a>\n"
	"                    <a class=\"nav-link \" href=\"/question.aspx\"><i class=\"fas fa-comments\"></i><span>常見問答</span></a>\n"
	"                    \n"
	"                </nav>\n"
	"            </div>\n"
	"        </div>\n"
	"    </header>\n"
	"    <!-- End Header -->\n"
	"    <div class=\"content-area\">\n"
	"        \n"
	"        <div class=\"page-banner-wrapper\" style=\"background: url('/upload/open.jpg') 50% 50% / cover;\"></div>\n"
	"        \n"
	"    <form method=\"post\" action=\"./open_detail.aspx?id=608\" id=\"form1\">\n"
	"<div class=\"aspNetHidden\">\n"
	"<input type=\"hidden\" name=\"__EVENTTARGET\" id=\"__EVENTTARGET\" value=\"\" />\n"
	"<input type=\"hidden\" name=\"__EVENTARGUMENT\" id=\"__EVENTARGUMENT\" value=\"\" />\n"
	"<input type=\"hidden\" name=\"__VIEWSTATE\" id=\"__VIEWSTATE\" value=\"/wEPDwULLTE4NTEzMzg3NjkPZBYCZg9kFgICAQ9kFgICAQ9kFiZmDxYCHgRUZXh0BRjmo67mnpfngb3lrrPooqvlrrPlg7nlgLxkAgEPFgIfAAUY5qOu5p6X54G95a6z6KKr5a6z5YO55YC8ZAICDw8WAh4HVmlzaWJsZWhkZAIDDxYCHwAFBDc3NjBkAgQPFgIfAAUCNzJkAgUPFgIfAAUKMjAyMS0wNC0wMWQCBg8WAh8ABQbkuLvoqIhkAgcPFgIfAAUJ57Wx6KiI5a6kZAIIDxYCHwAFCjIwMTYtMTAtMDFkAgkPFgIfAAUG5q+P5bm0ZAIKDxYCHwAFiQHmj5Dkvpvos4fmlpnljIXlkKvvvJrmo67mnpfngb3lrrPliKXjgIHlubTku73jgIHmlbjlgLzjgIHllq7kvY3jgIHnrYnmrITkvY3os4fmlpnjgII8YnIvPu+8nOaUv+W6nOizh+aWmemWi+aUvuW5s+iHuuizh+aWmeS9v+eUqOimj+evhO+8nmQCCw9kFgICAQ8PFgQfAAU/aHR0cHM6Ly9hZ3JzdGF0LmNvYS5nb3YudHcvc2R3ZWIvcHVibGljL2lucXVpcnkvSW5xdWlyZUFkdmFuLi4uHgtOYXZpZ2F0ZVVybAVDaHR0cHM6Ly9hZ3JzdGF0LmNvYS5nb3YudHcvc2R3ZWIvcHVibGljL2lucXVpcnkvSW5xdWlyZUFkdmFuY2UuYXNweBYEHgdEYXRhVXJsBUNodHRwczovL2FncnN0YXQuY29hLmdvdi50dy9zZHdlYi9wdWJsaWMvaW5xdWlyeS9JbnF1aXJlQWR2YW5jZS5hc3B4Hg9Db21tYW5kQXJndW1lbnQFJue1seioiOWupDs2MDg75qOu5p6X54G95a6z6KKr5a6z5YO55YC8ZAIMD2QWAgIDDw8WBB8ABVBodHRwczovL2RhdGEuY29hLmdvdi50dy9zZXJ2aWNlL29wZW5kYXRhL2FncnN0YXRVbml0LmFzcHg/aXRlbV9jb2RlPTIyMzQwMTAzMTE0MB8CBVBodHRwczovL2RhdGEuY29hLmdvdi50dy9zZXJ2aWNlL29wZW5kYXRhL2FncnN0YXRVbml0LmFzcHg/aXRlbV9jb2RlPTIyMzQwMTAzMTE0MBYEHwMFUGh0dHBzOi8vZGF0YS5jb2EuZ292LnR3L3NlcnZpY2Uvb3BlbmRhdGEvYWdyc3RhdFVuaXQuYXNweD9pdGVtX2NvZGU9MjIzNDAxMDMxMTQwHwQFJue1seioiOWupDs2MDg75qOu5p6X54G95a6z6KKr5a6z5YO55YC8ZAIND2QWAgIBDw8WAh8BaGRkAhAPZBYCAgEPFgIeC18hSXRlbUNvdW50ZmQCEQ8WAh8BZxYCZg8PFgIfAgUZfi9vcGVuX3NlYXJjaC5hc3B4P2lkPTYwOGRkAhIPFgIfBWZkAhMPFgIfAWhkAhkPDxYCHghJbWFnZVVybAUQfi9XZWJfVkNPREUuYXNoeGRkZHxtwl2Dy4MZfkmWCFRtLrycu8U3g894rdiGdkH0yypq\" />\n"
	"</div>\n\n"
	"<script type=\"text/javascript\">\n"
	"//<![CDATA[\n"
	"var theForm = document.forms['form1'];\n"
	"if (!theForm) {\n"
	"    theForm = document.form1;\n"
	"}\n"
	"function __doPostBack(eventTarget, eventArgument) {\n"
	"    if (!theForm.onsubmit || (theForm.onsubmit() != false)) {\n"
	"        theForm.__EVENTTARGET.value = eventTarget;\n"
	"        theForm.__EVENTARGUMENT.value = eventArgument;\n"
	"        theForm.submit();\n"
	"    }\n"
	"}\n"
	"//]]>\n"
	"</script>\n\n\n"
	"<div class=\"aspNetHidden\">\n\n"
	"	<input type=\"hidden\" name=\"__VIEWSTATEGENERATOR\" id=\"__VIEWSTATEGENERATOR\" value=\"0F634CDA\" />\n"
	"	<input type=\"hidden\" name=\"__EVENTVALIDATION\" id=\"__EVENTVALIDATION\" value=\"/wEdAAgphLzqptZwP1KPTkEC/Y1uVe9rD3DO5qLIZqmIxzRMEYJIJYkB9lj7bmyAq3HsE9OYnEPSdGdsijXlKS0XZvTqs+/pAnKH9yOn89varc7Z01IBOVyMrtNdEzjdZvXu6aIKKa6Fj4P0jbY6FHx68/GYLXCH41vH114dDE8DU50JISYrHTKTTzaj6mO9S9hZxEq9YSI59SN5QnKYJiWuKnBv\" />\n"
	"</div>\n"
	"        <article class=\"container\">\n"
	"            <div class=\"top-info\">\n"
	"                <h3 class=\"title-h3\">資料開放<span>OpenData</span></h3>\n"
	"                <div class=\"page-breadcrumb\">\n"
	"                    <a class=\"icon-logo\" href=\"index.aspx\"></a><i class=\"fas fa-angle-right\"></i><a href=\"open.aspx\">資料開放</a><i class=\"fas fa-angle-right\"></i><a href=\"#\">森林災害被害價值</a>\n"
	"                </div>\n"
	"            </div>\n"
	"            <hr>\n"
	"            <div class=\"category-container\">\n"
	"                <div class=\"data-wrapper open-detail\">\n\n"
	"                    <div class=\"data-title-wrapper\">\n"
	"                        <h4 class=\"title-h4\">\n"
	"                            森林災害被害價值</h4>\n"
	"                        \n"
	"                        <div class=\"help\"><span>瀏覽次數\n"
	"                            7760</span><span>介接次數\n"
	"                                72</span><span>資料更新日期\n"
	"                                    2021-04-01</span></div>\n"
	"                    </div>\n"
	"                    <div class=\"data-search data-content\">\n"
	"                        <div class=\"data-search-list\">\n"
	"                            <div class=\"search-input\">\n"
	"                                <label class=\"label\">資料評分</label>\n"
	"                            </div>\n"
	"                            <div class=\"search-input\">\n"
	"                                <select id=\"rating\">\n"
	"                                    <option value=\"1\"></option>\n"
	"                                    <option value=\"2\"></option>\n"
	"                                    <option value=\"3\"></option>\n"
	"                                    <option value=\"4\"></option>\n"
	"                                    <option value=\"5\"></option>\n"
	"                                </select><span class=\"help  sdiv\" style=\"display: none; \">平均 <b style=\"color: #78B42E;\" class=\"ssc\">3</b> 分 ( <span class=\"ssu\" style=\"float: inherit;\">0</span>人投票 )</span>\n"
	"                            </div>\n"
	"                        </div>\n"
	"                        <div class=\"data-search-list\">\n"
	"                            <div class=\"search-input\">\n"
	"                                <label class=\"label\">資料分類</label>\n"
	"                            </div>\n"
	"                            <div class=\"search-input\">\n"
	"                                <p>\n"
	"                                    主計</p>\n"
	"                            </div>\n"
	"                        </div>\n"
	"                        <div class=\"data-search-list\">\n"
	"                            <div class=\"search-input\">\n"
	"                                <label class=\"label\">提供單位</label>\n"
	"                            </div>\n"
	"                            <div class=\"search-input\">\n"
	"                                <p>\n"
	"                                    統計室</p>\n"
	"                            </div>\n"
	"                        </div>\n"
	"                        <div class=\"data-search-list\">\n"
	"                            <div class=\"search-input\">\n"
	"                                <label class=\"label\">上架日期</label>\n"
	"                            </div>\n"
	"                            <div class=\"search-input\">\n"
	"                                <p>\n"
	"                                    2016-10-01</p>\n"
	"                            </div>\n"
	"                        </div>\n"
	"                        <div class=\"data-search-list\">\n"
	"                            <div class=\"search-input\">\n"
	"                                <label class=\"label\">更新頻率</label>\n"
	"                            </div>\n"
	"                            <div class=\"search-input\">\n"
	"                                <p>\n"
	"                                    每年</p>\n"
	"                            </div>\n"
	"                        </div>\n"
	"                        <div class=\"data-search-list\">\n"
	"                            <div class=\"search-input\">\n"
	"                                <label class=\"label\">資料描述</label>\n"
	"                            </div>\n"
	"                            <div class=\"search-input\">\n"
	"                                <p>\n"
	"                                    提供資料包含：森林災害別、年份、數值、單位、等欄位資料。<br/>＜政府資料開放平臺資料使用規範＞</p>\n"
	"                            </div>\n"
	"                        </div>\n"
	"                        \n"
	"                            <div class=\"data-search-list\">\n"
	"                                <div class=\"search-input\">\n"
	"                                    <label class=\"label\">原始資料來源</label>\n"
	"                                </div>\n"
	"                                <div class=\"search-input\">\n"
	"                                    <a id=\"m_SourceURL\" DataUrl=\"https://agrstat.coa.gov.tw/sdweb/public/inquiry/InquireAdvance.aspx\" CommandArgument=\"統計室;608;森林災害被害價值\" href=\"https://agrstat.coa.gov.tw/sdweb/public/inquiry/InquireAdvance.aspx\" target=\"_blank\">https://agrstat.coa.gov.tw/sdweb/public/inquiry/InquireAdvan...</a>\n"
	"                                </div>\n"
	"                            </div>\n"
	"                        \n"
	"                        \n"
	"                            <div class=\"data-search-list\">\n"
	"                                <div class=\"search-input\">\n"
	"                                    <label id=\"ContentPlaceHolder1_m_DataLabel\" class=\"label\">資料介接</label>\n"
	"                                </div>\n"
	"                                <div class=\"search-input\">\n"
	"                                    <a id=\"m_DataUrl\" DataUrl=\"https://data.coa.gov.tw/service/opendata/agrstatUnit.aspx?item_code=223401031140\" CommandArgument=\"統計室;608;森林災害被害價值\" href=\"https://data.coa.gov.tw/service/opendata/agrstatUnit.aspx?item_code=223401031140\" target=\"_blank\">https://data.coa.gov.tw/service/opendata/agrstatUnit.aspx?item_code=223401031140</a></div>\n"
	"                            </div>\n"
	"                            <div class=\"data-search-list\">\n"
	"                                <div class=\"search-input\">\n"
	"                                    <label class=\"label\">介接說明文件</label>\n"
	"                                </div>\n"
	"                                <div class=\"search-input\">\n"
	"                                    <a id=\"ContentPlaceHolder1_m_ReadMe\" class=\"rm-link\" href=\"javascript:__doPostBack(&#39;ctl00$ContentPlaceHolder1$m_ReadMe&#39;,&#39;&#39;)\"></a></div>\n"
	"                            </div>\n\n"
	"                        \n"
	"                        \n"
	"                        \n"
	"                        \n"
	"                        \n"
	"                    </div>\n"
	"                    <a id=\"ContentPlaceHolder1_m_AdvSearchUrl\" class=\"button is-info data-search-btn\" title=\"提供該資料集之篩選條件及相關查詢。\" href=\"open_search.aspx?id=608\">進階資料</a>\n\n"
	"                    <!---------------------------->\n"
	"                    <div class=\"data-comments-wrapper\">\n\n"
	"                        \n"
	"                        <div class=\"data-more-comments\">\n"
	"                            \n"
	"                        </div>\n"
	"                        \n"
	"                    </div>\n"
	"                    <div class=\"data-comments data-post\">\n\n"
	"                        <div class=\"contact-reply-form\">\n"
	"                            <div class=\"input-group\">\n"
	"                                <div class=\"field\">\n"
	"                                    <label class=\"label\">姓名<span class=\"require\">*</span></label>\n"
	"                                    <div class=\"control\">\n"
	"                                        <input name=\"ctl00$ContentPlaceHolder1$m_Editor\" type=\"text\" id=\"ContentPlaceHolder1_m_Editor\" class=\"input feedbackform\" placeholder=\"您的大名\" required=\"\" />\n"
	"                                    </div>\n"
	"                                </div>\n"
	"                                <div class=\"field\">\n"
	"                                    <label class=\"label\">電子郵件<span class=\"require\">*</span></label>\n"
	"                                    <div class=\"control\">\n"
	"                                        <input name=\"ctl00$ContentPlaceHolder1$m_ReportMail\" id=\"ContentPlaceHolder1_m_ReportMail\" class=\"input feedbackform\" type=\"email\" placeholder=\"example@mail.com\" required=\"\" />\n"
	"                                    </div>\n"
	"                                </div>\n"
	"                            </div>\n"
	"                            <div class=\"field-group\">\n"
	"                                <div class=\"field\">\n"
	"                                    <label class=\"label\">標題</label>\n"
	"                                    <div class=\"control\">\n"
	"                                        <input name=\"ctl00$ContentPlaceHolder1$m_Title\" type=\"text\" id=\"ContentPlaceHolder1_m_Title\" class=\"input feedbackform\" placeholder=\"標題\" />\n"
	"                                    </div>\n"
	"                                </div>\n"
	"                                <div class=\"field\">\n"
	"                                    <label class=\"label\">留言內容<span class=\"require\">*</span></label>\n"
	"                                    <div class=\"control\">\n"
	"                                        <textarea name=\"ctl00$ContentPlaceHolder1$m_description\" rows=\"2\" cols=\"20\" id=\"ContentPlaceHolder1_m_description\" class=\"textarea\" placeholder=\"留言內容\">\n"
	"</textarea>\n"
	"                                    </div>\n"
	"                                </div>\n"
	"                            </div>\n"
	"                            <div class=\"input-group\">\n"
	"                                <div class=\"field\">\n"
	"                                    <label class=\"label\">請輸入驗證碼<span class=\"require\">*</span></label>\n"
	"                                    <div class=\"control\">\n"
	"                                        <input name=\"ctl00$ContentPlaceHolder1$m_CheckCode\" id=\"ContentPlaceHolder1_m_CheckCode\" class=\"input feedbackform\" type=\"text\" placeholder=\"驗證碼\" required=\"\" />\n"
	"                                    </div>\n"
	"                                </div>\n"
	"                                <div class=\"field\">\n"
	"                                    <div class=\"code\">\n"
	"                                        <div class=\"img\"><a href=\"javascript:refreshCc();\">\n"
	"                                            <img id=\"ContentPlaceHolder1_m_ccimg\" src=\"Web_VCODE.ashx\" /></a></div>\n"
	"                                        <a id=\"ContentPlaceHolder1_m_Send\" class=\"button is-link\" href=\"javascript:__doPostBack(&#39;ctl00$ContentPlaceHolder1$m_Send&#39;,&#39;&#39;)\">送   出</a>\n"
	"                                    </div>\n"
	"                                </div>\n"
	"                            </div>\n"
	"                        </div>\n"
	"                    </div>\n\n"
	"                </div>\n\n"
	"            </div>\n"
	"        </article>\n"
	"    </form>\n\n"
	"        <!-- Footer -->\n"
	"        <footer class=\"main-footer bg-dark-green \">\n"
	"            <div class=\"container full\">\n"
	"                <div class=\"footer-logo\">\n"
	"                    <img src=\"images/footer-logo.png\"></div>\n"
	"                <div class=\"footer-info\">\n"
	"                    <ul>\n"
	"                        <li>台北市中正區南海路37號</li>\n"
	"                        <li>服務時間：AM9:00~PM5:30</li>\n"
	"                        <li>服務電話：<a href=\"tel: 07-970-3898\">(07)970-3898</a></li>\n"
	"                        <li>服務信箱：<a href=\"mailto:opendata@mail.coa.gov.tw\">opendata@mail.coa.gov.tw</a></li>\n"
	"                    </ul>\n"
	"                    <p>※最佳瀏覽解析度為1024x768</p>\n"
	"                </div>\n"
	"                <div class=\"footer-declare\">\n"
	"                    <nav><a href=\"https://data.gov.tw/license\">授權條款</a><a href=\"terms.aspx\">隱私權保護宣告</a></nav>\n"
	"                    <p>除另有註明，網站之內容皆採用 政府資料開放平臺資料使用規範</p>\n"
	"                </div>\n"
	"            </div>\n"
	"        </footer>\n"
	"        <!-- End Footer -->\n"
	"    </div>\n"
	"    <script type=\"text/javascript\" src=\"/app.bundle.js\"></script>\n\n"
	"    \n"
	"    <script>\n"
	"        window.onload = function () {\n"
	"            $('#rating').barrating({\n"
	"                theme: 'fontawesome-stars',\n"
	"                initialRating: 3,\n"
	"              onSelect: function (value, text, event) {\n"
	"                  chg(value);\n"
	"              }\n"
	"          });\n"
	"            $('.data-more-btn').click(function () {\n"
	"                $('.data-more-comments').toggleClass('is-opened');\n"
	"            });\n"
	"        }\n\n"
	"    </script>\n"
	"    <script type=\"text/javascript\">\n"
	"        $(document).ready(function () {\n"
	"            refreshCc();\n"
	"            $(\".feedbackform\").keypress(function (e) {\n"
	"                code = (e.keyCode ? e.keyCode : e.which);\n"
	"                if (code == 13) {\n"
	"                    $(\"#ContentPlaceHolder1_m_Send\").click();\n"
	"                }\n"
	"            });\n\n"
	"            $('#m_SourceURL,#m_DataUrl').on(\"click\", function () {\n"
	"                var link = $(this).attr(\"DataUrl\");\n"
	"                var CommandArgument = $(this).attr(\"CommandArgument\");\n"
	"                var result;\n"
	"                $.ajax({\n"
	"                    url: '/open_detail.aspx/Record',\n"
	"                    data: JSON.stringify({\n"
	"                        \"DataUrl\": link,\n"
	"                        \"CommandArgument\": CommandArgument\n"
	"                    }),\n"
	"                    async: false,\n"
	"                    contentType: \"application/json; charset=utf-8\",\n"
	"                    dataType: \"json\",\n"
	"                    method: 'POST',\n"
	"                    success: function (response) {\n"
	"                        if (response != null && response.d != null) {\n"
	"                            var data = response.d;\n\n"
	"                            data = $.parseJSON(data);\n"
	"                            result = data;\n"
	"                        }\n"
	"                    }\n"
	"                });\n\n"
	"                return result;\n"
	"            });\n"
	"        });\n\n"
	"        function refreshCc() {\n"
	"            var ImgId = 'ContentPlaceHolder1_m_ccimg';\n"
	"             var ccImgSrc = \"\";\n"
	"             if ($(\"#\" + ImgId).lenght != 0) {\n"
	"                 ccImgSrc = '/Web_VCODE.ashx?r=' + Math.random();\n"
	"                $(\"#\" + ImgId).attr(\"src\", ccImgSrc);\n"
	"            }\n"
	"        }\n"
	"        function NewWindow() {\n"
	"            document.forms[0].target = \"_blank\";\n"
	"        }\n\n"
	"        function chg(score) {\n\n"
	"            $.ajax({\n"
	"                dataType: \"json\",\n"
	"                url: 'api/odscore.ashx',\n"
	"                data: {\n"
	"                    sc: score,\n"
	"                    id: '608'\n"
	"         },\n"
	"         type: 'post'\n"
	"     }).done(function (responseData) {\n\n"
	"         if (responseData.RS == 'OK') {\n"
	"             if (responseData.S.length > 0 && responseData.C.length > 0) {\n"
	"                 $('.sdiv').show();\n"
	"                 $('.ssc').text(responseData.S);\n"
	"                 $('.ssu').text(responseData.C);\n"
	"             }\n"
	"         }\n"
	"         //  console.log('Done: ', responseData);\n"
	"     }).fail(function () {\n"
	"         //  console.log('Failed');\n"
	"     });\n"
	"        }\n\n"
	"    </script>\n\n\n\n\n\n\n"
	"</body>\n"
	"</html>\n")

matches = re.finditer(regex, test_str, re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):
    
    print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        
        print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))

# Note: for Python 2.7 compatibility, use ur"" to prefix the regex and u"" to prefix the test string and substitution.
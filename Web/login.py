# parser.py
import requests

username = ""
userpasswd = ""

# 로그인할 유저정보를 넣어주자 (모두 문자열)
LOGIN_INFO = {
    'ctl00$ctl00$NICEMasterPageBodyContent$SiteContentPlaceholder$txtFormsLogin': username,
    'ctl00$ctl00$NICEMasterPageBodyContent$SiteContentPlaceholder$txtFormsPassword': userpasswd
}

# Session 생성, with 구문 안에서 유지
with requests.Session() as s:
    # HTTP POST request: 로그인을 위해 POST url와 함께 전송될 data를 넣어주자.
    login_req = s.post('https://login.cern.ch/adfs/ls/?wa=wsignin1.0&wreply=https%3A%2F%2Fcms.web.cern.ch%2FShibboleth.sso%2FADFS&wct=2019-11-21T15%3A38%3A09Z&wtrealm=https%3A%2F%2Fcms.web.cern.ch%2FShibboleth.sso%2FADFS&wctx=cookie%3A1574350689_37c1', data=LOGIN_INFO)
    # 어떤 결과가 나올까요?
    print(login_req.status_code)

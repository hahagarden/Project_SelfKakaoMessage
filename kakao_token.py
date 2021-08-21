import json
import requests
import datetime
import os

print("/////////////run//////////////")





#토큰 발급하기
url = "https://kauth.kakao.com/oauth/token"  # 사용자 토큰 발급용 url

data = {
    "grant_type": "authorization_code",
    "client_id": "cc335daa766cc74b3de1b1c372a6cce8",  # REST_API
    "redirect_uri": "https://localhost.com",
    "code": "Uqaqu3KvA7QxO72vqJcyLxLLpax2Gwqpihjm1gyba3m4ZrQUUTPA0mcF2VIQQ8runL_a3worDKgAAAF7Zs5TDw",  # 인증코드: run할때마다 새로 발급받아야함
}

response = requests.post(url, data=data)  # 검색(사용자 토큰 발급 요청)

# 요청에 실패했다면,
if response.status_code != 200:
    print("error! because ", response.json())
else:  # 성공했다면,
    tokens = response.json()  # tokens변수에 담기
    print(tokens)
# 토큰 발급에 성공했다면 다시 인증코드를 발급받을 필요가 없음. 이제부터 계속 token사용하면 됨. token 잘 관리하기.
print("//////////////token requested//////////////")







#토큰 관리하기
#카카오 토큰을 저장할 파일명
KAKAO_TOKEN_FILENAME="Project_SelfKakaoMessage/kakao_token.json"

#저장하는 함수
def save_tokens(filename, tokens):
    with open(filename, 'w') as f:
        json.dump(tokens,f)

#읽어오는 함수
def load_tokens(filename):
    with open(filename) as f:
        tokens=json.load(f)

    return tokens

#refresh_token으로 access_token 갱신하는 함수
def update_tokens(app_key, filename):
    tokens=load_tokens(filename)

    url= "https://kauth.kakao.com/oauth/token"
    data={
        "grant_type" : "refresh_token",
        "client_id" : app_key,
        "refresh_token" : tokens['refresh_token']
    }
    response=requests.post(url, data=data)

    #요청에 실패했다면,
    if response.status_code !=200:
        print("error! because ", response.json())
        tokens=None
    else: #성공했다면,
        print(response.json())
        #기존파일 백업
        now=datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_filename=filename+"."+now
        os.rename(filename, backup_filename)
        #갱신된 토큰 저장
        tokens['access_token']=response.json()['access_token']
        save_tokens(filename, tokens)

    return tokens

#토큰 저장
save_tokens(KAKAO_TOKEN_FILENAME,tokens)
print("///////////////token saved///////////////////")



#토큰 업데이트->토큰 저장 필수!
#KAKAO_APP_KEY="cc335daa766cc74b3de1b1c372a6cce8"
#tokens=update_tokens(KAKAO_APP_KEY, KAKAO_TOKEN_FILENAME)
#save_tokens(KAKAO_TOKEN_FILENAME, tokens)
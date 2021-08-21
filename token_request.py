import requests

url = "https://kauth.kakao.com/oauth/token"  # 사용자 토큰 발급용 url

data = {
    "grant_type": "authorization_code",
    "client_id": "cc335daa766cc74b3de1b1c372a6cce8",  # REST_API
    "redirect_uri": "https://localhost.com",
    "code": "AbHhMBpDVNt8Bmg6-AftzVbP4406eNXW0tncsmiab-yDnH3be4Votug0Qw10DododbzyTwo9dNkAAAF7ZoafNQ",  # 인증코드: run할때마다 새로 발급받아야함
}

response = requests.post(url, data=data)  # 검색(사용자 토큰 발급 요청)

# 요청에 실패했다면,
if response.status_code != 200:
    print("error! because ", response.json())
else:  # 성공했다면,
    tokens = response.json()  # tokens변수에 담기
    print(tokens)
# 토큰 발급에 성공했다면 다시 인증코드를 발급받을 필요가 없음. 이제부터 계속 token사용하면 됨. token 잘 관리하기.

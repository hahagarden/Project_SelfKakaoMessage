import json
import requests
import token_def

KAKAO_TOKEN_FILENAME = "kakao_token.json"  # Token in this file(.json)
# 저장된 토큰 정보를 읽어옴
tokens = token_def.load_tokens(KAKAO_TOKEN_FILENAME)

# list message url
url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"

# set request parameters
headers = {"Authorization": "Bearer " + tokens["access_token"]}

template = {
    "object_type": "list",
    "header_title": "초밥 사진",
    "header_link": {"web_url": "www.naver.com", "mobile_web_url": "www.naver.com"},
    "contents": [
        {
            "title": "1. 광어초밥",
            "description": "광어는 맛있다",
            "image_url": "https://search1.kakaocdn.net/argon/0x200_85_hr/8x5qcdbcQwi",
            "image_width": 50,
            "image_height": 50,
            "link": {"web_url": "www.naver.com", "mobile_web_url": "www.naver.com"},
        },
        {
            "title": "2. 참치초밥",
            "description": "참치는 맛있다",
            "image_url": "https://search2.kakaocdn.net/argon/0x200_85_hr/IjIToH1S7J1",
            "image_width": 50,
            "image_height": 50,
            "link": {"web_url": "www.naver.com", "mobile_web_url": "www.naver.com"},
        },
    ],
    "buttons": [
        {
            "title": "웹으로 이동",
            "link": {"web_url": "www.naver.com", "mobile_web_url": "www.naver.com"},
        }
    ],
}

data = {"template_object": json.dumps(template)}

# 나에게로 카카오톡 메세지 보내기 요청(list)
res = requests.post(url, data=data, headers=headers)
print(res.status_code)

if res.status_code != 200:
    print("error! because ", res.json())

else:
    print("메시지를 성공적으로 보냈습니다.")

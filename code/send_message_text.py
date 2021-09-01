# 텍스트 메시지 템플릿 구현
import json
import requests
import token_def


KAKAO_TOKEN_FILENAME = "/git/project_kakao_message/json/kakao_token.json"  # Token in this file(.json)

# To load the saved Token
tokens = token_def.load_tokens(KAKAO_TOKEN_FILENAME)

# Text message url
url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"

# Set request parameters
headers = {"Authorization": "Bearer " + tokens["access_token"]}

print(tokens["access_token"])

data = {
    "template_object": json.dumps(
        {
            "object_type": "text",
            "text": "You did a good job",
            "link": {"web_url": "www.naver.com"},
        }
    )
}


# Request Send message to me(text)
response = requests.post(url, headers=headers, data=data)
print(response.status_code)

# if failed to request,
if response.status_code != 200:
    print("error! because= ", response.json())
else:  # if succeed,
    print("메시지를 성공적으로 보냈습니다.")

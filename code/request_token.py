import token_def

# To get Authorization Code
# https://kauth.kakao.com/oauth/authorize?client_id=(REST_API app key)&response_type=code&redirect_uri=https://localhost.com

KAKAO_APP_KEY = "cc335daa766cc74b3de1b1c372a6cce8"  # REST_API app key
AUTHORIZATION_CODE = "KG4EbiURUdVXYMa9pYmYrKIW_BZkp7NYPs9oKj-ogtAalTUxcOSWO5BZ_xCjmZSSOUXqhwo9c-wAAAF7oZHGXw"  # once in a run
KAKAO_TOKEN_FILENAME = "/git/Project_KakaoMessage/json/kakao_token.json"  # Token in this file(.json)

# To get Access Token
tokens = token_def.request_tokens(KAKAO_APP_KEY, AUTHORIZATION_CODE)

# To save Access Token in the file(.json)
token_def.save_tokens(KAKAO_TOKEN_FILENAME, tokens)

# # To update Refresh Token after the Access Token is expired
# tokens=token_def.update_tokens(KAKAO_APP_KEY, KAKAO_TOKEN_FILENAME)
# token_def.save_tokens(KAKAO_TOKEN_FILENAME, tokens)

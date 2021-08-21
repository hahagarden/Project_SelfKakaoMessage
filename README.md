# Project_SelfKakaoMessage
 파이썬 생활밀착형 프로젝트2

## 21.08.21.
* request_token 실행 후 save_update_token 실행(save)
* send_message_text 실행 후 카카오톡 내 메세지에서 확인
* send_messgae_text 실행이 안되는건 access token이 expired된 것 때문일 수 있으므로 save_update_token 실행(update)하여 refresh token 발급
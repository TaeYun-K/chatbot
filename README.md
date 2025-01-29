# 자동 답장 챗봇

이 프로젝트는 **FastAPI**, **Gemini API**, **메신저봇R**을 활용하여 사용자가 보낸 **카카오톡 문자**의  답장을 해주는 챗봇입니다.

## 🛠 주요 기능
1. 사용자가 **메신저봇R**에서 카카오톡 알림을 받으면 이를 FastAPI 서버로 전달합니다.
2. **FastAPI** 서버가 카카오톡 내용을 **Gemini API**에 보내 답장을 생성합니다.
3. 생성된 답장을 **메신저봇R**을 통해 사용자에게 다시 전송합니다.

## 🚀 사용법

1. 메신저봇R 다운로드 (안드로이드만 지원)
2. 자바 스크립트 코드를 메신저봇R에 복사, fastapi의 ip주소는 pc 의 ip 주소로 지정
3. pc에서 파이썬 코드와 제미나이 api 수정
4. uvicorn 명령어로 fastapi 서버 오픈



## 🚀 자세한 정보
[자세한 정보 블로그 참조](https://velog.io/@kty8600/%EB%A9%94%EC%8B%A0%EC%A0%80%EB%B4%87R%EA%B3%BC-gemini-api%EB%A5%BC-%ED%99%9C%EC%9A%A9%ED%95%9C-%EC%B9%B4%EC%B9%B4%EC%98%A4%ED%86%A1-chatbot-%EB%A7%8C%EB%93%A4%EA%B8%B0)

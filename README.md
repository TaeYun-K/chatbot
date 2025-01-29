# URL 요약 챗봇

이 프로젝트는 **FastAPI**, **Gemini API**, **메신저봇R**을 활용하여 사용자가 보낸 **유튜브 링크**를 요약해주는 챗봇입니다.

## 🛠 주요 기능
1. 사용자가 **메신저봇R**에서 URL을 전송하면 이를 FastAPI 서버로 전달합니다.
2. **FastAPI** 서버가 URL을 **Gemini API**에 보내 요약을 생성합니다.
3. 생성된 요약을 **메신저봇R**을 통해 사용자에게 다시 전송합니다.

## 🚀 사용법
### 1. 환경 설정
```bash
git clone https://github.com/your-repo/url-summary-chatbot.git
cd url-summary-chatbot
pip install -r requirements.txt

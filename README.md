<!DOCTYPE html>
<html lang="ko">
<head>
</head>
<body>
    <h1>📌 챗봇 사용 안내</h1>
    <p>이 챗봇은 <strong>메신저봇R</strong>, <strong>FastAPI</strong>, <strong>Gemini API</strong>를 활용하여 사용자가 보낸 URL을 요약하여 제공하는 서비스입니다.</p>
    
    <h2>🚀 사용 방법</h2>
    <ol>
        <li>메신저봇R에서 챗봇과 대화를 시작합니다.</li>
        <li>URL을 포함하여 <code>/요약 [URL]</code> 형식으로 메시지를 보냅니다.</li>
        <li>챗봇이 URL을 분석하여 요약된 내용을 응답합니다.</li>
    </ol>
    
    <h2>🛠️ 설치 방법</h2>
    <p>이 프로젝트를 로컬에서 실행하려면 아래 단계를 따르세요:</p>
    <pre>
1. Python 3 설치 확인
2. 필요한 라이브러리 설치:
   <code>pip install fastapi uvicorn requests</code>
3. FastAPI 서버 실행:
   <code>uvicorn main:app --reload --host 0.0.0.0 --port 8000 </code>
   
4. 메신저봇R에서 FastAPI 엔드포인트를 설정하여 연동</pre>
    
    <h2>📞 문의</h2>
    <p>문제가 발생하거나 개선 사항이 있다면 문의해 주세요!</p>
</body>
</html>

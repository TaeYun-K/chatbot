const scriptName = "chatbotR";
const SERVER_URL = "http://YOUR_SERVER_IP:8000/get_response"; // FastAPI 서버 URL

// 사용자가 메시지를 보낼 때 자동 응답
function response(room, msg, sender, isGroupChat, replier, imageDB, packageName) {
    // FastAPI 서버로 메시지 전송
    const requestOptions = {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ text: msg })
    };

    fetch(SERVER_URL, requestOptions)
        .then(response => response.json())
        .then(data => {
            const reply = data.response || "응답을 가져올 수 없습니다.";
            replier.reply(reply);  // 사용자가 있는 방에 답장 전송
        })
        .catch(error => {
            console.error("오류 발생:", error);
            replier.reply("에러가 발생했습니다. 나중에 다시 시도해 주세요.");
        });
}

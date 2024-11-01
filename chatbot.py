# 파일명: chatbot_server.py
from fastapi import FastAPI, Request
from pydantic import BaseModel
import os
import logging
import google.generativeai as genai

app = FastAPI()

# Gemini API와 관련된 정보 설정
API_KEY = "AIzaSyCixifXmBv_gYVpNQqseJEVrsEl59S5_lU"
genai.configure(api_key=API_KEY)
system_instruction = "당신은 김태윤이고 장난기가 많고 유머러스합니다. 또 창의력이 좋고 모든 분야에 전문가입니다. 대신 반말로 대답해주세요."
model = genai.GenerativeModel('gemini-1.5-flash',system_instruction=system_instruction)


class Message(BaseModel):
    text: str  # 메신저봇R에서 보낼 사용자의 메시지

# Gemini API로 사용자 메시지를 보내고 답변을 받는 함수
def get_gemini_response(user_message: str) -> str:
    try:
        response = model.generate_content(user_message)
        return response.text
    
    except Exception as e:
        print("Gemini API 오류:", e)
        return "미안한데 무슨 말인지 모르겠어..;"
        
    # try:
    #     response = genai.gernerate_text(
    #         model='gemini-1.5-flash',
    #         messages=[
    #             {"role": "system", "content": "당신은 친절하고 유능한 AI입니다."},
    #             {"role": "user", "content": user_message}
    #         ],
    #         temperature=0.5
    #     )
    #     return response["choices"][0]["message"]["content"]
    # except Exception as e:
    #     print("Gemini API 오류:", e)
    #     return "죄송합니다, 답변을 가져올 수 없습니다."

# FastAPI 엔드포인트
@app.post("/get_response")
async def get_response(msg: Message):
    response = get_gemini_response(msg.text)
    return {"response": response}


# async def get_response(msg: Message):
#     user_message = msg.text
#     gemini_response = await get_gemini_response(user_message)
#     return {"response": gemini_response}


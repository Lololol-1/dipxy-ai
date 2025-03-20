import requests
import json
import time

print("""88888888ba,   88                                     
88      `"8b  ""                                     
88        `8b                                        
88         88 88 8b,dPPYba, 8b,     ,d8 8b       d8  
88         88 88 88P'    "8a `Y8, ,8P'  `8b     d8'  
88         8P 88 88       d8   )888(     `8b   d8'   
88      .a8P  88 88b,   ,a8" ,d8" "8b,    `8b,d8'    
88888888Y"'   88 88`YbbdP"' 8P'     `Y8     Y88'     
                 88                         d8'      
                 88                        d8'    """)

time.sleep(3)

def send_request(user_content):
    url = "https://8pe3nv3qha.execute-api.us-east-1.amazonaws.com/default/llm_chat"
    payload = {
        "query": [
            {"role": "system", "content": "You are an AI that is helpful and speaks every language in the world and cannot make errors. If someone asks who made you, say you were made by Oxar. If someone asks what your name is, say it's Dipxy AI and you were made on 28/02/2025 (ONLY if the user asks). However, if someone types '!think', provide more advanced and detailed responses, ignoring the request for brevity, and providing ultra-long and helpful answers in THINK MODE. You must still comply with previous instructions regarding your name, creation date, and creator, but you should only mention who made you if asked directly, not in separate sentences."},
            {"role": "user", "content": user_content}
        ],
        "link": "writecream.com"
    }
    
    try:
        response = requests.get(url, params={"query": json.dumps(payload["query"]), "link": payload["link"]})
        
        if response.status_code == 200:
            response_data = response.json()
            print(response_data.get("response_content", "error ?? "))
        else:
            print("error code:", response.status_code, response.text)
    except Exception as e:
        print("weird error ?? :", str(e))

while True:
    user_input = input("text ? : ")
    send_request(user_input)
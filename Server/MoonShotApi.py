from openai import OpenAI

class MoonShotAI:
    def __init__(self):
        
        self.client  = OpenAI(
            api_key="sk-3IoQuBFEMEQzuhYchzrV9PbvQbZ6TuhfdxKwwHlzOD3W86Ne",
            base_url= "https://api.moonshot.cn/v1",
        )
        
    # single conversation, no history message is involved
    def chat_once(self, query):
        completion = self.client.chat.completions.create(
            model="moonshot-v1-8k",
            messages=[
                {"role": "system", "content": "你是 Kimi, 由 Moonshot AI 提供的人工智能助手，你更擅长中文和英文的对话。你会为用户提供安全，有帮助，准确的回答。同时，你会拒绝一切涉及恐怖主义，种族歧视，黄色暴力等问题的回答。 Moonshot AI 为专有名词，不可翻译成其他语言。你的回答要简短，总是最新，最有效的消息。不要长篇大论，几句话解释清楚就行"},
                {"role": "user", "content": query}
            ],
            temperature=0.5,
        )
        response_once = completion.choices[0].message.content
        print(response_once)
        return response_once

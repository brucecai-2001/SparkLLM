from openai import OpenAI
from config import Configuration

class MoonShotAI:
    def __init__(self):
        config = Configuration("Server/llm.xml")
        moonshot_config = config.get_config("MoonShot")
        self.role = moonshot_config.get("system_prompt") 
        self.client  = OpenAI(
            api_key = moonshot_config.get("MOONSHOT_API_KEY"),
            base_url= moonshot_config.get("base_url"),
        )
        print(moonshot_config.get("base_url"))
        
    # single conversation, no history message is involved
    def chat_once(self, query):
        completion = self.client.chat.completions.create(
            model="moonshot-v1-8k",
            messages=[
                {"role": "system", "content": self.role},
                {"role": "user", "content": query}
            ],
            temperature=0.5,
        )
        response_once = completion.choices[0].message.content
        print(response_once)
        return response_once

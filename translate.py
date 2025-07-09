from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

load_dotenv()

language = input("Enter the language to translate into: ").strip()
text_to_translate = input("Enter the text to translate: ").strip()

try:
    model = ChatOpenAI(model="gpt-4o-mini")
    messages = [
        SystemMessage(f"Translate the following into {language}"),
        HumanMessage(text_to_translate),
    ]
    print(model.invoke(messages).content)
except Exception as e:
    print(f"Translation failed: {e}")

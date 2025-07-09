from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

load_dotenv()

language = input("Enter the language to translate into: ").strip()
text_to_translate = input("Enter the text to translate: ").strip()

try:
    model = ChatOpenAI(model="gpt-4o-mini")
    messages = [
        SystemMessage("You are a translator. Translate the given text into the specified language. Respond with the translation and no other text."),
        HumanMessage(f"Translate '{text_to_translate}' into {language}"),
    ]

    print(model.invoke(messages).content)
except Exception as e:
    print(f"Translation failed: {e}")
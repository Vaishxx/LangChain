from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model=ChatOpenAI()

msg=[
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="Tell me a joke.")
]

result=model.invoke(msg)

msg.append(AIMessage(content=result.content))
print(msg)
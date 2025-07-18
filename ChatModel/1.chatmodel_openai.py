from langchain_openai import ChatOpenAI
from dotenv import load_dotenv 

load_dotenv()

model=ChatOpenAI(model='gpt-4',temperature=1,max_completion_tokens=100) #temperature is the para that controls the reandomnes of a language model's output.It affects how creative or dterministic  the response are.
# lower val- 0.0-0.3 ->more deterministic and predictible
# higher val- 0.7-1.5 -> more random creative and diverse

result=model.invoke("what is the capital of India")
# print(result) 
print(result.content)
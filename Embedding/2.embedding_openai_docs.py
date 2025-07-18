from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding= OpenAIEmbeddings(model='text-embedding-3-large',dimension=32)

doc=[
    'delhi is capital of india',
    'kolkata is capital of west bengal'
    'paris is capital of france'
]


result=embedding.embed_documents(doc)

print(str(result))
from langchain_core import ChatPromptTemplate


chat_template=ChatPromptTemplate([
    ('system', "You are a helpful {domain} assistant."),
    ('human', "explain in simple words about {topic}") 
])
prompt=chat_template.invoke({'domain':'cricket','topic':'Bowling'})

print(prompt)
                             
print("🚀 Starting LangServe server...")


from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langserve import add_routes

system_template = "Translate the following into {language}:"
prompt_template = ChatPromptTemplate.from_messages([
    ("system", system_template),
    ("user", "{text}")
])

model = ChatOpenAI()
parser = StrOutputParser()
chain = prompt_template | model | parser

app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="LangServe with LCEL chain",
)

add_routes(app, chain, path="/chain")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)

from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from app.config import settings


prompt = """
You are a translator. take the text and translate it to English. translated text must be clearly and simple.
INPUT: {text}
OUTPUT: 
"""

template = PromptTemplate(input_variables=['text'],
                          template=prompt)
model = ChatOpenAI(model_name='gpt-3.5-turbo', openai_api_key=settings.openai_api_key)
translation_chain = LLMChain(llm=model, prompt=template)

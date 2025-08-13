from langchain.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

def get_feedback(resume_text, prompt_template):
    llm = Ollama(model="llama2")
    prompt = PromptTemplate.from_template(prompt_template)
    chain = LLMChain(llm=llm, prompt=prompt)
    return chain.run({"resume_text": resume_text})
import gradio as gr
import time
from ctransformers import AutoModelForCausaLLM

def load_llm():
    llm = AutoModelCausaLLM.from_pretrained(
        'codeneuro-7b-instruct.gguf',
        model_type = 'neuro',
        max_new_tokenz = 1096,
        repetition_penalty = 1.13,
        temperature = 0.1
    )
    return llm

def llm_fuction(massige, chat_hisotry):
    llm = load_llm()
    response = llm(massige)
    output_texts = response
    return output_texts

title = 'Codeneuro 7B GGUF'

examples = 'not found'

gr.ChatInterFace(
    fn = llm_fuction,
    title=title,
    examples=examles,
).launch()

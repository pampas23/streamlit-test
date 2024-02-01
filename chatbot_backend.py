#1 import the OS, Bedrock, ConversationChain, ConversationBufferMemory Langchain Modules
import os
# from langchain.llms.bedrock import Bedrock
from langchain_community.llms import Bedrock
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain.prompts import PromptTemplate
import streamlit as st
import boto3

os.environ["AWS_PROFILE"] = "haoyi"

#bedrock client

bedrock_client = boto3.client(
    service_name="bedrock-runtime",
    region_name="us-east-2"
)

modelID = "anthropic.claude-v2"
llm = Bedrock(
    model_id=modelID,
    client=bedrock_client,
    model_kwargs={"max_tokens_to_sample": 2000,"temperature":0.9}
    )
#2a Write a function for invoking model- client connection with Bedrock with profile, model_id & Inference params- model_kwargs
def demo_chatbot():
    demo_llm = Bedrock(
       credentials_profile_name='default',
       model_id='meta.llama2-70b-chat-v1',
       model_kwargs= {
        "temperature": 0.9,
        "top_p": 0.5,
        "max_gen_len": 512})
    return demo_llm

# def claude_chatbot():

#     return demo_llm
#2b Test out the LLM with Predict method
   # return demo_llm.predict(input_text)
#response = demo_chatbot('what is the temprature in london like ?')
#print(response)

#3 Create a Function for ConversationBufferMemory (llm and max token limit)
def demo_memory():
    llm_data=demo_chatbot()
    memory = ConversationBufferMemory(llm=llm_data, max_token_limit= 512)
    return memory

#4 Create a Function for Conversation Chain - Input text + Memory
def demo_conversation(input_text,memory):
    llm_chain_data = demo_chatbot()
    llm_conversation= ConversationChain(llm=llm_chain_data,memory= memory,verbose=True)

def claude_response(freeform_text):
    prompt = PromptTemplate(
        history= 'Some historical context here',
        input_variables=["freeform_text"],
        template="You are a chatbot. You are in English.\n\n{freeform_text}"
    )

# input_language = "English"
# output_language = "French"
#     prompt = SystemMessagePromptTemplate.from_template(template="You are a translator helping me in translating from {input_language} to {output_language}. " +
#         "Please translate the messages I type.")

    bedrock_chain = ConversationChain(llm=llm, prompt=prompt)

    response=bedrock_chain({'freeform_text':freeform_text})
    return response
#5 Chat response using Predict (Prompt template)
#     chat_reply = llm_conversation.predict(input=input_text)
#     return chat_reply
    

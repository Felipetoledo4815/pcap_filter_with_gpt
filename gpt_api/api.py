import os
import openai

CONTEXT_CHAT_COMPLETION_0 = "We have a mysql table called 'packets', created from a pcap file, that contains the following fields: [src_ip VARCHAR,dst_ip VARCHAR,src_port INT,dst_port INT,protocol VARCHAR,length INT,timestamp DOUBLE,syn_flag INT,ack_flag INT,fin_flag INT,handshake VARCHAR,record VARCHAR] where all VARCHAR columns if empty, are initialized with ''."
PRE_QUESTION_CHAT_COMPLETION = "Output mysql code to answer the following question with no explanation: "

# CONTEXT_START_COMPLETION = """
# context: "We have a mysql table called 'packets', created from a pcap file, that contains the following fields: [src_ip VARCHAR,dst_ip VARCHAR,src_port INT,dst_port INT,protocol VARCHAR,length INT,timestamp DOUBLE,syn_flag INT,ack_flag INT fin_flag INT,handshake VARCHAR,record VARCHAR] where all VARCHAR columns if empty, are initialized with ''.
# task: Only return a mysql query to answer the following question: What is the IP address that has sent the most number of TCP packages?
# answer: SELECT src_ip \nFROM packets \nWHERE protocol='TCP' \nGROUP BY src_ip \nORDER BY COUNT(*) DESC \nLIMIT 1;
# """


def get_mysql_query(text):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    # ChatCompletion
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "assistant", "content": CONTEXT_CHAT_COMPLETION_0},
            {"role": "user", "content": PRE_QUESTION_CHAT_COMPLETION + text}
        ],
        temperature=0,
        max_tokens=100
    )
    # print(response['choices'][0]['message']['content'])
    return response['choices'][0]['message']['content']

    # ### Completion
    # prompt = CONTEXT_START_COMPLETION + f"task: Only return a mysql query to answer the following question: {text}\nanswer:"
    # response = openai.Completion.create(
    #     model="text-ada:001", prompt=prompt, temperature=0, max_tokens=50)
    # print(response['choices'][0]['text'])
    # return response['choices'][0]['text']

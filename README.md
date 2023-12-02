# local-models-project
Local LLMs final project for scientific computing class

Slides:
https://docs.google.com/presentation/d/19HmfS6m8bhqrGgwMPeb3PVf2PotyzEtcP94AUh6kER4/edit?usp=sharing

Instructions to run locally:


Before running anything:
pip install zmq
pip install llama_cpp

Also, download one or all of the models described at end of README and put in models folder. Smallest model should require 5.33GB of ram, largest model should require 7.28GB of ram.

To run server: 
python3 server.py <ip> <port> <model number>

such as
python3 server.py 127.0.0.1 7777 2

Where:
- 127.0.0.1 is localhost
- 7777 is a port
- 2 represents "models/llama-2-7b-chat.Q2_K.gguf", further defined in model mapping in server.py:
model_mapping = {
        "2": "models/llama-2-7b-chat.Q2_K.gguf",
        "3": "models/llama-2-7b-chat.Q3_K_M.gguf",
        "4": "models/llama-2-7b-chat.Q4_K_M.gguf",
        "5": "models/llama-2-7b-chat.Q5_K_M.gguf",
    }

To run the client:

python3 client.py <ip> <port>
such as
python3 client.py 127.0.0.1 7777
where ip and port should match server

Client is simple text UI to talk to server through input.

generate_figures.ipynb contains code to generate figures. Values in it are from averaging values across runs, included in logs.txt. Time to first token is calculated from averaging load time from server logs, tokens per second given by completion tokens / (load + eval time). Server logs provided in a big file as well.

I used these in the models folder:

llama-2-7b-chat.Q2_K.gguf
llama-2-7b-chat.Q3_K_M.gguf
llama-2-7b-chat.Q4_K_M.gguf
llama-2-7b-chat.Q5_K_M.gguf

Links:

https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF

https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF/blob/main/llama-2-7b-chat.Q2_K.gguf
https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF/blob/main/llama-2-7b-chat.Q3_K_M.gguf
https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF/blob/main/llama-2-7b-chat.Q4_K_M.gguf
https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF/blob/main/llama-2-7b-chat.Q5_K_M.gguf


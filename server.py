from llama_cpp import Llama
import sys
import zmq

if __name__ == "__main__":
    context = zmq.Context()
    post_socket = context.socket(zmq.REP)
    post_socket.bind(f"tcp://{sys.argv[1]}:{sys.argv[2]}")

    model_mapping = {
        "2": "models/llama-2-7b-chat.Q2_K.gguf",
        "3": "models/llama-2-7b-chat.Q3_K_M.gguf",
        "4": "models/llama-2-7b-chat.Q4_K_M.gguf",
        "5": "models/llama-2-7b-chat.Q5_K_M.gguf",
    }

    # defaults to Q5 if no model is specified
    model_path = model_mapping.get(sys.argv[3], "models/llama-2-7b-chat.Q5_K_M.gguf")

    llm = Llama(model_path=model_path, chat_format="llama-2")

    messages = []

    while True:
        message = post_socket.recv_json()
        messages.append({"role": "user", "content": message['message']})
        response = llm.create_chat_completion(messages=messages, max_tokens=32)
        print(f"Received message: {message}, Response: {response}")
        post_socket.send_json({"status": "Message received", "response": response['choices'][0]['message']['content']})
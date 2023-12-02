import datetime
import sys 
import zmq 

def sender(post_socket):
    while True:
        message = input('User: ')
        post_socket.send_json({"message": message})
        reply = post_socket.recv_json()
        print(f"Llama response: {reply['response']}")

if __name__ == "__main__":
    context = zmq.Context()

    post_socket = context.socket(zmq.REQ)
    post_socket.connect(f"tcp://{sys.argv[1]}:{sys.argv[2]}")

    sender(post_socket)
import os
import socket
import threading

from streamcipher import StreamCipher

def handle(c):

    flag = os.getenv("flag", "Q0M1MzJYLXRyeSBoYXJkZXItCg==")
    cipher = StreamCipher()
    encrypted_flag = cipher.encrypt(flag)
    flag = ''.join('{:02x}'.format(x) for x in encrypted_flag).encode()

    c.sendall(b"Flag is "  + flag + b"\n")

    while True:
        c.sendall(b"Send Text (max 1024 bytes):\n")
        received = c.recv(1024).strip().decode()
        encrypted_text = cipher.encrypt(received)
        text = ''.join('{:02x}'.format(x) for x in encrypted_text).encode()
        c.sendall(b"Encrypted version is "+text+b"\n")
        if not received:
            c.sendall(b"Bye!\n")
            break
    c.close()

if __name__ == "__main__":
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(("0.0.0.0", 15325))
        s.listen()

        while True:
            c, _ = s.accept()
            # Send each "client_soc" connection as a parameter to a thread.
            threading.Thread(target=handle,args=(c,), daemon=True).start()
    except KeyboardInterrupt:
        print("Closing socket...")
        s.close()
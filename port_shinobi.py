import socket
import sys
import random
import time
import os

PORTS = [21, 22, 23, 25, 80, 139, 443, 445, 3306, 3389]

def scan_ports(target):
    for port in PORTS:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(2)
            result = s.connect_ex((target, port))
            if result == 0:
                print(f"Port {port} is open")
                # Persistence: try to reconnect 3 times with a 1-second delay
                for i in range(3):
                    try:
                        s.connect((target, port))
                        print(f"Reconnected to port {port} successfully")
                        break
                    except socket.error:
                        print(f"Reconnection attempt {i+1} failed. Retrying...")
                        time.sleep(1)
                else:
                    print(f"Failed to reconnect to port {port} after 3 attempts")
                # Escalation: try to upgrade to a more privileged connection
                try:
                    s.send(b"Upgrade connection to privileged mode")
                    response = s.recv(1024)
                    if response == b"Upgrade successful":
                        print("Escalated to privileged mode successfully")
                        # Evasiveness: use polymorphic and metamorphic techniques to evade detection
                        polymorphic_payload = generate_polymorphic_payload()
                        metamorphic_payload = generate_metamorphic_payload()
                        s.send(polymorphic_payload + metamorphic_payload)
                        response = s.recv(1024)
                        if response == b"Payload executed successfully":
                            print("Evasive payload executed successfully")
                        else:
                            print("Evasive payload failed to execute")
                    else:
                        print("Escalation failed")
                except socket.error:
                    print("Escalation failed due to socket error")

def generate_polymorphic_payload():
    # Generate a polymorphic payload using a combination of encryption and encoding
    payload = b"Polymorphic payload"
    encrypted_payload = encrypt_payload(payload)
    encoded_payload = encode_payload(encrypted_payload)
    return encoded_payload

def generate_metamorphic_payload():
    # Generate a metamorphic payload using a combination of code obfuscation and anti-debugging techniques
    payload = b"Metamorphic payload"
    obfuscated_payload = obfuscate_payload(payload)
    anti_debug_payload = anti_debug(obfuscated_payload)
    return anti_debug_payload

def encrypt_payload(payload):
    # Simple encryption function using XOR
    key = os.urandom(16)
    encrypted_payload = bytearray()
    for byte in payload:
        encrypted_payload.append(byte ^ key[0])
    return encrypted_payload

def encode_payload(payload):
    # Simple encoding function using Base64
    encoded_payload = payload.encode("base64")
    return encoded_payload

def obfuscate_payload(payload):
    # Simple obfuscation function using string manipulation
    obfuscated_payload = ""
    for char in payload:
        obfuscated_payload += chr(ord(char) + 1)
    return obfuscated_payload

def anti_debug(payload):
    # Simple anti-debugging function using timing attacks
    start_time = time.time()
    for i in range(1000):
        payload += b"A"
    end_time = time.time()
    if end_time - start_time > 1:
        print("Debugger detected! Aborting...")
        sys.exit(1)
    return payload

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Too few arguments.")
        print(f"Syntax: python3 {sys.argv[0]} <ip>")
        sys.exit(1)

    target = sys.argv[1]
    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("Hostname could not be resolved. Exiting")
        sys.exit(1)

    try:
        scan_ports(target_ip)
    except KeyboardInterrupt:
        print("\nExiting program....")
        sys.exit(0)

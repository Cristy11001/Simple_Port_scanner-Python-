import socket
import sys

def scan_port(target, port):
    """Scan a single port"""
    try:
        print(f"Testing {target}:{port}")
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        sock.close()
        print(f"Result for port {port}: {result}")
        return result == 0
    except Exception as e:
        print(f"Error on port {port}: {e}")
        return False

def main():
    target = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
    
    print(f"Testing basic socket connection to {target}")
    
    # Test one port
    if scan_port(target, 80):
        print("Port 80 is OPEN")
    else:
        print("Port 80 is CLOSED")

if __name__ == "__main__":
    main()

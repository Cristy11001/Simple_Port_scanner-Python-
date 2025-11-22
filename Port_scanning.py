import socket
import sys

def scan_port(target, port):
    """Scan a single port"""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        sock.close()
        
        if result == 0:
            return True
    except:
        pass
    return False

def get_service_name(port):
    """Get common service name for port"""
    services = {
        21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP",
        53: "DNS", 80: "HTTP", 110: "POP3", 143: "IMAP",
        443: "HTTPS", 3389: "RDP"
    }
    return services.get(port, "Unknown")

def main():
    if len(sys.argv) != 2:
        print("Usage: python port_scanner.py <IP_ADDRESS>")
        print("Example: python port_scanner.py 192.168.1.1")
        return
    
    target = sys.argv[1]
    
    print(f"Scanning {target} for open ports...")
    print("-" * 40)
    
    # Common ports to scan
    common_ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 3389]
    open_ports = []
    
    for port in common_ports:
        if scan_port(target, port):
            service = get_service_name(port)
            print(f"Port {port} open - {service}")
            open_ports.append(port)
    
    print("-" * 40)
    print(f"Found {len(open_ports)} open ports")

if __name__ == "__main__":
    main()
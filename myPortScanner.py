import socket

def scan_ports(ip, start_port, end_port):
    open_ports = []

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Set a timeout for the connection attempt
        result = sock.connect_ex((ip, port))

        if result == 0:
            open_ports.append(port)

        sock.close()

    return open_ports

if __name__ == "__main__":
    target_ip = "192.168.56.1"  # Replace with your laptop's IP address or "localhost"
    start_port = 1
    end_port = 1024  # You can adjust this range based on your needs

    open_ports = scan_ports(target_ip, start_port, end_port)

    if open_ports:
        print(f"Open ports on {target_ip}: {open_ports}")
    else:
        print(f"No open ports found on {target_ip}")

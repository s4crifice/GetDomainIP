import socket
import sys

def get_ip_address(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.error as e:
        print(f"Error occurred while resolving {domain}: {e}")
        return None

def main(input_file, output_file):
    ips = []
    try:
        with open(input_file, "r") as file:
            domains = file.readlines()
            for domain in domains:
                domain = domain.strip()
                ip_address = get_ip_address(domain)
                if ip_address:
                    print(f"Domain: {domain} -> IP Address: {ip_address}")
                    if ip_address not in ips:
                        ips.append(ip_address)

        with open(output_file, 'w') as f:
            for j in ips:
                full = str(j) + '\n'
                f.write(full)

        print(f'\nIP\'s saved to {output_file}')

    except FileNotFoundError:
        print(f"File '{input_file}' not found.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py input_file output_file")
        sys.exit(1)
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    main(input_file, output_file)

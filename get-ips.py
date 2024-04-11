import socket

def get_ip_address(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.error as e:
        print(f"Error occurred while resolving {domain}: {e}")
        return None

def main():
    ips = []
    file_path = "scope.txt"
    try:
        with open(file_path, "r") as file:
            domains = file.readlines()
            for domain in domains:
                domain = domain.strip()
                ip_address = get_ip_address(domain)
                if ip_address:
                    print(f"Domain: {domain} -> IP Address: {ip_address}")
                    if ip_address not in ips:
                        ips.append(ip_address)


        with open('ips.txt', 'w') as f:
            for j in ips:
                full = str(j) + '\n'
                f.write(full)

        print('\nIP\'s save to ips.txt')

    except FileNotFoundError:
        print(f"File '{file_path}' not found.")

if __name__ == "__main__":
    main()

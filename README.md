# GetDomainIP

Simple Python script to enumerate multiple domains and subdomains IPs using the socket module and save them to the ips.txt file.

## Usage

1. Clone the repository
    ```
    git clone https://github.com/s4crifice/GetDomainIP.git
    ```

2. Create a file containing all desired domains and subdomains.
    ``` 
    EXAMPLE scope.txt
    example.com
    www.example.com
    subdomain.example.com
    ```

3. Make sure there isn't an ips.txt file in the current directory!
   
4. Run the script
    ```
    python3 get-ips.py <input file> <output file>
    ```
    ```
    python3 get-ips.py scope.txt output.txt
    ```

## License

**This script is under MIT License, feel free to use!**

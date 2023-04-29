import nmap


def ip_scanner():
    nmap_path = "/usr/local/bin/nmap"
    nmap.PortScanner().nmap_search_path = nmap_path
    nm = nmap.PortScanner()

    nm.scan('147.235.180.0-255')

    print(nm.all_hosts())
    print(nm['147.235.180.154'].all_tcp())


if __name__ == '__main__':
    ip_scanner()

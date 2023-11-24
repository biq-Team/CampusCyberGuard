import wmi
import socket

def get_ip_address(domain_name):
    try:
        return socket.gethostbyname(domain_name)
    except socket.gaierror:
        return None

def set_dns_manually(dns_addresses):
    c = wmi.WMI()
    network_adapters = c.Win32_NetworkAdapterConfiguration()
    
    for adapter in network_adapters:
        try:
            if adapter.IPEnabled and adapter.IPConnectionMetric != None:
                adapter.SetDNSServerSearchOrder(dns_addresses)
                print(f"DNS address changed to {dns_addresses}. (Interface: {adapter.Description})")
            else:
                print(f"Cannot change DNS address because the connection status is disabled (Interface: {adapter.Description})")
        except Exception as e:
            print(f"DNS Error changing address: {e} (Interface: {adapter.Description})")

import time

while True:
    biq = "biqapp.com"
    jongno = "jongno.biq.kr"
    biq_ip = get_ip_address(biq)
    jongno_ip = get_ip_address(jongno)
    if biq_ip or jongno_ip:
        new_dns_addresses = [biq_ip, jongno_ip] #164.124.101.2
    else:
        new_dns_addresses = ["164.124.101.2"]
        print(f"{biq} or {jongno}The IP address of could not be found.")

    set_dns_manually(new_dns_addresses)
    time.sleep(300)



from scrapli.driver.core import IOSXEDriver

Cor = {
    "host": "10.10.10.9",
    "auth_username": "user",
    "auth_password": "cisco",
    "auth_secondary": "cisco",
    "auth_strict_key": False,
    "transport": "ssh2",
    # "driver": IOSXEDriver, 
    "ssh_config_file": True,   
}


stop = False
with IOSXEDriver(**Cor) as conn:
    while not stop:
        check_me = input("Please enter mac or IP you want to check \nFormat ex: aaaa.bbbb.cccc or 0.0.0.0\n> ")
        # Platform drivers will auto-magically handle disabling paging for you
        result = conn.send_command(f"show ip arp {check_me}")
        formatted_result = result.textfsm_parse_output()
        mac_addr = formatted_result[0]["mac"]
        ip_addr = formatted_result[0]["address"]
        print(f"IP Address: {ip_addr}\nMAC Address: {mac_addr}")
        restart = input("Lookup another Device? y or n ")
        if restart == 'n':
            stop = True
            print("Goodbye")

 


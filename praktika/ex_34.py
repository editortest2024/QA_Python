logs = [
    '192.168.0.1 /home',
    '192.168.0.1 /about',
    '192.168.0.2 /home',
    '192.168.0.1 /home',
    '192.168.0.2 /contact',
    '192.168.0.1 /about',
]


def analyze_logs(logs):


    ip_dict = {}


    for log in logs:
        ip,url = log.split()
        print(ip,url)
        if ip not in ip_dict:
            ip_dict[ip] = set()
            print(ip_dict)


        ip_dict[ip].add(url)


    uniq = {ip:len(url) for ip, url in ip_dict.items()}
    return uniq


print(analyze_logs(logs))

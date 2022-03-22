import netlas
import re
from sys import argv

def parse_args(argv):
    if argv[1][0] != '-':
        args = [argv[1]]
        print("arg = ",args[0])                
    elif len(argv) == 2:
        args = [argv[1]]
        print("flags = ",args[0])  
    else:
        args = [argv[1], argv[2]]
        print("flags = ",args[0])
        print("arg = ",args[1])
    return args

def print_help():
    print("Usage: python3 main.py [flags] [target] \n")
    print("Target specification: Domain names or IP-adresses\n")
    print("Flags:")
    print("    -h: Print this page")
    print("    -c: Enter Netlas API key: main.py -c \'API key\'")

def is_ip(s):
    match = re.fullmatch(r'((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)', s)
    if match:
        return 1
    else:
        return 0

def is_domain(s):
    match = re.fullmatch(r'\b[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*', s)
    if match:
        return 1
    else:
        return 0

def is_uri(s):
    match = re.fullmatch(r'((http|https)\:\/\/){1}[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*', s)
    if match:
        return 1
    else:
        return 0    

def is_subnet(s):
    match = re.fullmatch(r'((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)/([1-3]?\d)', s)
    if match:
        return 1
    else:
        match = re.fullmatch(r'((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)-((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)', s)
        if match:
            return 1  
        return 0

def is_as(s):
    match = re.fullmatch(r'AS\d{1,5}', s)
    if match:
        return 1
    else:
        return 0

def is_flags(s):
    if (s[0] == '-'):
        return 1
    else:
        return 0

def domain_research():
    print("tbd")

def IP_research():
    print("tbd")

def enter_api_key(args):
    for i in args:
        if (is_flags(i) == 0):
            api_key = i
            f = open('config', 'w')
            f.write(i)
            f.close()
            break

def parse_flags(flags, args):
    for i in flags:
        if i == 'h':
            print_help()
        elif i == 'c':
            enter_api_key(args)

args = parse_args(argv)
for i in args:
    if is_uri(i):
        print("URI\n")
    elif is_domain(i):
        print("domain\n")
    elif is_ip(i):
        print("IP\n")
    elif is_subnet(i):
        print("subnet\n")
    elif is_as(i):
        print("AS\n")
    elif is_flags(i):
        parse_flags(i, args)
    else:
        print(i, "is not a valid target")
f = open('config')
apikey = f.read()
print(apikey)
if (apikey == ''):
    print('Enter your Netlas API key')
else:    
    netlas_connection = netlas.Netlas(api_key=apikey)
    
    
    



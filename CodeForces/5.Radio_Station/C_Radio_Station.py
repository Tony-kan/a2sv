# #get servers and commands # as n,m respectively
# #get all servers and commands names & assign them in lists:servers and commands respectively

#function to map names and ip 
#removing trailing semi colon
#add names to commands
def server_names_ip(servers, commands):
    ip_to_server = {}
    for name, ip in servers:
        ip_to_server[ip] = name

    for command in commands:
        parts = command.split()
        ip = parts[1][:-1]
        server_name = ip_to_server[ip]
        print(command.strip() + " #" + server_name)

n, m = map(int, input().split())

servers = []
commands = []

# get all server names
#split the input to get server name and ip
for _ in range(n):
    svs = input().split()
    servers.append((svs[0], svs[1]))

# get all commands
for _ in range(m):
    cmds = input()
    commands.append(cmds)

server_names_ip(servers, commands)

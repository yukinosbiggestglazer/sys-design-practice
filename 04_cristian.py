import random

server_time = 1000   # server's clock (in seconds)
client_time = 950    # client's clock


delay_to_server = random.randint(1, 5)
delay_from_server = random.randint(1, 5)
rtt = delay_to_server + delay_from_server

server_time_at_reply = server_time + delay_from_server

new_client_time = server_time_at_reply + rtt / 2

print("Client time before:", client_time)
print("Round trip time (RTT):", rtt)
print("Synchronized client time:", new_client_time)

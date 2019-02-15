# import the libraries
import speedtest
import socket

# Find IP Address
# s = speedtest.Speedtest()
# hostname = socket.gethostname()
# IpAddr = socket.gethostbyname(hostname)

source = str(IpAddr)
s = speedtest.Speedtest(source_address=source)
s.get_best_server()
s.download()
s.upload()

print (source)
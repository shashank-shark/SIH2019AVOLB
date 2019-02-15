import wmi
import speedtest

c = wmi.WMI ()

source = ""
 
for interface in c.Win32_NetworkAdapterConfiguration (IPEnabled=1):
  if "ireless" in interface.Description:
  	source = str(interface.IPAddress[0])


s = speedtest.Speedtest(source_address=source)
s.get_best_server()
print(s.download())
print(s.upload())


# for interface in c.Win32_NetworkAdapterConfiguration (IPEnabled=1):
#   print (interface.Description)
#   print (type(interface.Description))
#   for ip_address in interface.IPAddress:
#     print (ip_address)
#     source = str(ip_address)
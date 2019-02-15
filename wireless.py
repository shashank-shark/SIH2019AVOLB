import wmi
c = wmi.WMI ()
 
for interface in c.Win32_NetworkAdapterConfiguration (IPEnabled=1):
  print (interface.Description)
  for ip_address in interface.IPAddress:
    print (ip_address)
  print("\n")
# get the bandwidth and speed test info here
import speedtest

# creating object of speedtest
s = speedtest.Speedtest()
# s.get_best_server()

# results_dict = s.results.dict()

# # Now print it line by line
# print (results_dict)
print(s.upload(pre_allocate=False))
print (s.download(pre_allocate=False))
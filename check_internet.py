import os, sys
import datetime
import time

def init_log_file(file_path):
    if not os.path.isfile(file_path):
        with open(file_path,'w') as f:
            f.write('DateTime,Host,Status\n')

def host_test(host):
    if os.system("ping -c 1 " + host) == 0: #Pass
        return 'Pass'
    else: #Fail
        return 'Fail'

def log_result(dt, host, status, file_path):
    with open(file_path, 'a') as f:
        f.write('{},{},{}\n'.format(dt,host,status))

def test_hosts(hosts, file_path):
    for host in hosts:
        dt = datetime.datetime.now()
        status = host_test(host)
        if status != 'Pass':
            log_result(dt, host, status, file_path)

def main():
    hosts = ['192.168.1.1', '192.168.100.1', 'google.com']
    pause_time = 60*2 # time in seconds to pause
    log_file = 'test_log_file.csv'
    file_path = os.path.join(sys.path[0], log_file)
    
    #1: Initialize/Empty the Log File
    init_log_file(file_path)

    #2: Loop every *pause_time* seconds and test hosts
    while True:
        test_hosts(hosts, file_path)
        time.sleep(pause_time)

if __name__ == '__main__':
    main()


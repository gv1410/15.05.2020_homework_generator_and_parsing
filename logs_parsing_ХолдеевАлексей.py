
import re

    
def reader(filename_logs, pattern_data):

    with open(filename_logs) as fp:
        
        log = fp.read()

        ip_list = re.findall(pattern_data, log)

        return ip_list

def main():

    reg_ip_pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s\-\s\-'

    browsers = ('Opera', 'Firefox', 'Safari', 'Chrome')

    number_of_request_ip = reader('apache_logs.txt', reg_ip_pattern)

    print('Число уникальных запросов к серверу равно: ' + str(len(set(number_of_request_ip))))    
    print('Число запросов к серверу равно: ' + str(len(number_of_request_ip)))

    
    for i in browsers:
        number_of_request_browser = reader('apache_logs.txt', i)
        print('Число обращений от браузера ' + i + ': ' + str(len(number_of_request_browser)))
    

if __name__ == "__main__":
    main()
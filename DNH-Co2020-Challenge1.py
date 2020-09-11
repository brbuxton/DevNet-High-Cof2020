"""DevNet High - Class of 2020 - Challenge 1"""

import random
import ipaddress

# TODO: Write a print statement that displays both the type and value of 'ip'
ip = "10.1.1.200"

# TODO: Write a conditional to print out if `iosversion` is less than or greater than 14
i = random.randint(12, 17)
print('i is {}'.format(i))
if i >= 14:
    print(f'{i} is greater or equal to 14')
else:
    print(f'{i} is less than 14')

# TODO: Write a conditional that prints the serial number of the device
devices = ({'CAT9300':'XVNM1245ERGC'}, {'ISR4331':'VNMM8742THBX'}, {'NGFW2120':'EAQP4900RTJO'})
device = random.sample(devices, 1)[0]
device = list(device.values())[0]
for dictionary in devices:
    for key, value in dictionary.items():
        if value in device:
            print(f'The randomly selected device for serial number {value} is {key}')


# Function for converting CIDR notation into 32-bit netmask (nothing to do here)
def cidr_to_netmask(ip_str):
    ip = ipaddress.IPv4Network(ip_str)
    return ip.with_netmask


'''
TODO: Call the function above few times to so that the input of IP network with CIDR displays the IP network with 32-bit netmask
Example:
Input would be '10.1.1.0/24' and when printed out the output would be '10.1.1.0/255.255.255.0'
'''
cidr = cidr_to_netmask(ip)
print(f'input was {ip} and conversion is {cidr}')

cidr = cidr_to_netmask('10.0.0.0/8')
print(f'input was {ip} and conversion is {cidr}')

cidr = cidr_to_netmask('172.16.0.0/12')
print(f'input was {ip} and conversion is {cidr}')

while True:
    try:
        address_input = input("Enter the IP network and mask in CIDR format: ")
        if ipaddress.IPv4Network(address_input):
            print(cidr_to_netmask(address_input))
            break
    except Exception as e:
        print(e)

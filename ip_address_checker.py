from bs4 import BeautifulSoup 
import ipaddress 

# Check if the IP address is valid
def is_valid_ip(ip):
  try:
    ipaddress.ip_address(ip)
    return True
  except ValueError:
    return False


# Delete IP address
def delete_ip_addresses(import_file, remove_list):
  with open(import_file, "r") as file:
    ip_addresses = file.read().split()

  for element in remove_list:
    if element in ip_addresses:
      ip_addresses.remove(element)
      print(f"Your IP address {element} has been removed.")
    else:
      print(f"You are trying to remove an IP address which is not in the list: {element}. Please check your IP address and try again.")

  ip_addresses = " ".join(ip_addresses)

  with open(import_file, "w") as file:
    file.write(ip_addresses)

# Insert IP address
def insert_ip_addresses(import_file, insert_list):
  with open(import_file, "r") as file:
    ip_addresses = file.read().split()

  ip_addresses_set = set(ip_addresses)

  for element in insert_list:
      if is_valid_ip(element):
        if element not in ip_addresses_set:
          ip_addresses_set.add(element)
          print(f"Your IP address {element} has been added.")
        else:
          print(f"The IP address {element} is already in the list.")
      else:
        print(f"You are trying to add an invalid IP address: {element}. Please check your IP address and try again.")

  with open(import_file, "w") as file:
    file.write(" ".join(ip_addresses_set))

# Example usage: 
remove_list = ["192.168.0.1"]
insert_list = ["192.168.0.4"]

# Call the functions
delete_ip_addresses("ip_addresses.txt", remove_list)
insert_ip_addresses("ip_addresses.txt", insert_list)

with open("ip_addresses.txt", "r") as file:
  text = file.read()

print(f"Actual list of IP addresses is: {text}")

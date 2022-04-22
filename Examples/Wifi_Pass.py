import subprocess
# get wifi details
data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'])
data = data.decode('utf-8').split('\n')
# list of wifi names
wifi_names = []
# iterate through data
for profile in data:
     
    # find "All User Profile" in each item
    if "All User Profile" in profile:
        # split profile items
        profile = profile.split(":")
         
        # get wifi name 
        profile = profile[1]
        profile = profile[1:-1]
         
        # append wifi name in wifi_names list
        wifi_names.append(profile)
print("{:<20}|  {:}\n".format('Wi-Fi Names', 'Passwords'))
# iterate through wifi_names 
for name in wifi_names:
    # get password details
    data = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', name, 'key=clear'])
    data = data.decode('utf-8').split('\n')
    # list of passwords
    passwords = []
    # iterate through data
    for passw in data:
        if "Key Content" in passw:
            # split passw items
            password = passw.split(":")
            
            # get password
            password = password[1]
            password = password[1:-1]
            
            # append paswords in passwords list
            passwords.append(password)
            
    try:
        # return Wi-Fi name and password
        print("{:<20}|  {:}".format(name, passwords[0]))
    except IndexError:
        print("{:<20}|  {:}".format(name, ""))

input()
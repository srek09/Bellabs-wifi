import subprocess
 
import time
 
#import notify2
 
 
 
# Function to scan for Wi-Fi networks
 
def scan_wifi():
 
    try:
 
        # Run the iwlist command to scan for Wi-Fi networks
 
        result = subprocess.run(['sudo', 'iwlist', 'wlan0', 'scan'], capture_output=True, text=True)
 
        networks = result.stdout
 
 
 
        # Parse the output to extract information
 
        cells = networks.split('Cell')
 
        wifi_list = []
 
        for cell in cells[1:]:
 
            ssid = ''
 
            signal = ''
 
            lines = cell.split('\n')
 
            for line in lines:
 
                if 'ESSID' in line:
 
                    ssid = line.split(':')[1].strip().strip('"')
 
                if 'Signal level' in line:
 
                    signal = line.split('=')[2].split(' ')[0].strip()
 
            if ssid:
 
                wifi_list.append(f'SSID: {ssid}, Signal: {signal} dBm')
 
        return wifi_list
 
    except Exception as e:
 
        return [f'Error: {e}']
 
 
 
# Initialize the notification system
 
#notify2.init('Wi-Fi Monitor')
 
 
 
while True:
 
    # Get Wi-Fi information
 
    wifi_info = scan_wifi()
 
    wifi_message = '\n'.join(wifi_info)
 
    print(wifi_message)
 
    # Create a notification
 
    #notification = notify2.Notification('Available Wi-Fi Networks', wifi_message)
 
    #notification.set_urgency(notify2.URGENCY_NORMAL)
 
    #notification.show()
 
     
 
    # Wait for 1 minute before updating the Wi-Fi info
 
    time.sleep(60)

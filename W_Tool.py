'''

Author: @cxrloskenobi / CvrlosKenobi
Updated beta version to October, 2020

'''

from speedtest import Speedtest
from colorama import init
from colorama import Fore
import socket
import subprocess
import os
init(autoreset=True)

def failsafe():
  secure = True # Safe mode is ON
  if secure == False:
    ping = ping('8.8.8.8', size=40, count=10).rtt_avg_ms
    return ping
  return secure

# Getting the IP address
secure = failsafe()
if secure == False:
    hostname = socket.gethostname()
    IPAddress = socket.gethostbyname(hostname) 
else:
    IPAddress = 'NULL'

def driving_variables():  # Basically the master variables
    st = Speedtest()
    mbs = 10**6
    down = (st.download()) / mbs
    up = st.upload() / mbs
    round_down = round(down, 2)
    round_up = round(up, 2)
    return round_down, round_up

def test_connection():  # Testing if internet's connection is on
    try:
        socket.create_connection(('Google.com', 80))
        return True
    except OSError:
        return False

def print_connection(secure, round_down, round_up, ping):  
  # Print the download and upload velocity
    # IP Address
    print(Fore.MAGENTA + "IP Adress: " + Fore.YELLOW +
             f'\t\t\t         {IPAddress}')

    # Internet Connection
    if test_connection() == True:
        print(Fore.MAGENTA + 'Internet connection: ' + Fore.GREEN +
              '\t                 Connected')
    else:
        print(Fore.MAGENTA + 'Internet connection: ' + Fore.RED +
              '\t         Disconnected')
        return 1
    
    if secure == False:
      # Ping
      #if ping > 110:
      print(Fore.MAGENTA + "Your Ping is: " + Fore.YELLOW + f'{ping} ms')
      #elif ping < 109:
      #  print(Fore.MAGENTA + "Your Ping is: " + Fore.GREEN + ping + 'ms')

    # Download's Speed
    if (round_down < 4):
        print(Fore.MAGENTA + f"Your Connection's Download speed is:" +
              Fore.RED + f"\t {round_down} Mb/s")
    else:
        print(Fore.MAGENTA + f"Your Connection's Download speed is:" +
              Fore.GREEN + f"\t {round_down} Mb/s")

    # Upload's Speed
    if (round_up < 1):
        print(Fore.MAGENTA + f"Your Connection's Upload speed is:" + Fore.RED +
              f"\t {round_up} Mb/s")
    else:
        print(Fore.MAGENTA + f"Your Connection's Upload speed is:" +
              Fore.GREEN + f"\t {round_up} Mb/s")

    return print('\n')


def main():  # Main ASCII Art
    return print(Fore.MAGENTA + '''\
    \t _    _ _______ _   _____           _ 
    \t| |  | (_)  ___(_) |_   _|         | |
    \t| |  | |_| |_   _    | | ___   ___ | |
    \t| |/\| | |  _| | |   | |/ _ \ / _ \| |
    \t\  /\  / | |   | |   | | (_) | (_) | |
    \t \/  \/|_\_|   |_|   \_/\___/ \___/|_|
                                                                           
        \tby @cvrloskenobi                                      
                                         
     ''')


if __name__ == '__main__':
    main()

# Yes/No loop
play = True
while (play == True):
    secure = failsafe()
    round_down, round_up = driving_variables()
    print_connection(secure, round_down, round_up, ping)
    again = str(input("Do you wanna start again? y/n \n> "))
    if (again == "n"):
        play = False

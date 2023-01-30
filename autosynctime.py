import os
import time
from rich.console import Console
import colorama
from colorama import Fore, Back, Style, init
init()

console = Console()
sleep = console.input("\n[bold white3]>>> Enter Times Second To Sleep : \n60 = 1 minute\n900 = 15 minute\n1800 = 30 minute\n3600 = 1 hour\n14400 = 4 hour\n21600 = 6 hour\n43200 = 12 hour\n\n Sleep zZZZzz >> : \n")
sleep = int(sleep)

def text_logo():
    print("")
    print(Fore.LIGHTGREEN_EX, Style.BRIGHT + "Welcome To Auto Windows Times Resync\n" + Style.RESET_ALL)
    promptpay_donate = 'Buy Me a Coffee : PromptPay : 095-518-8528'
    print(Fore.LIGHTYELLOW_EX, Style.BRIGHT + promptpay_donate + Style.RESET_ALL)
    print(Fore.LIGHTGREEN_EX, Style.BRIGHT + 'Thanks For Support' + Style.RESET_ALL)
    print('---------------------------------------------------------------------------------')
    print('██   ██ ██   ██  █████   ██ ███████  ██  ██████  ██████  ██████  ██   ██ ██████ ')
    print(' ██ ██  ██   ██ ██   ██ ███ ██      ███ ██            ██      ██ ██   ██      ██')
    print('  ███   ███████  █████   ██ ███████  ██ ███████   █████   █████  ███████  █████ ')
    print(' ██ ██       ██ ██   ██  ██      ██  ██ ██    ██ ██           ██      ██ ██     ')
    print('██   ██      ██  █████   ██ ███████  ██  ██████  ███████ ██████       ██ ███████')
    print('---------------------------------------------------------------------------------')
    print(Fore.CYAN + '')
    print('████████╗██╗███╗   ███╗███████╗    ██████╗ ███████╗███████╗██╗   ██╗███╗   ██╗ ██████╗')
    print('╚══██╔══╝██║████╗ ████║██╔════╝    ██╔══██╗██╔════╝██╔════╝╚██╗ ██╔╝████╗  ██║██╔════╝')
    print('   ██║   ██║██╔████╔██║█████╗      ██████╔╝█████╗  ███████╗ ╚████╔╝ ██╔██╗ ██║██║     ')
    print('   ██║   ██║██║╚██╔╝██║██╔══╝      ██╔══██╗██╔══╝  ╚════██║  ╚██╔╝  ██║╚██╗██║██║     ')
    print('   ██║   ██║██║ ╚═╝ ██║███████╗    ██║  ██║███████╗███████║   ██║   ██║ ╚████║╚██████╗')
    print('   ╚═╝   ╚═╝╚═╝     ╚═╝╚══════╝    ╚═╝  ╚═╝╚══════╝╚══════╝   ╚═╝   ╚═╝  ╚═══╝ ╚═════╝')
    print(Style.RESET_ALL + '')
    print('---------------------------------------------------------------------------------')
    print(Fore.BLUE, Style.BRIGHT + 'If You Found Some Bug Please Contact My Developer Master >> Here Line ID : x4815x')
    print(Style.RESET_ALL)
    return

def main():
    try:
        os.system("w32tm /resync") # resync the time with the time server
        print(Fore.YELLOW, Back.GREEN, Style.BRIGHT + f'Resync Windows Time ^^ Done' + Style.RESET_ALL)
    except Exception as Error:
        print(f'Error Resync Time : {Error}')
    return

service_name = "w32time"

def start_service(service_name):
    start_command = f"net start {service_name}"
    start_result = os.system(start_command)
    query_command = f"sc query {service_name}"
    query_result = os.system(query_command)
    if start_result == 0 or start_result == 4:
        if query_result == 0 or query_result == 4:
            print(f"Service Already Start | Service Name : {service_name} service.\nPass To Next Step\nWait For Update Windows Times")
        else:
            print(f"Could not start {service_name} service.")
    else:
        query_result = 0
        query_result = os.system(query_command)
        print(f"\nNow Set >>result<< = 0 For Start Service ^^\n\nService Already Start | Name : {service_name} service.\nPass To Next Step\nWait For Update Windows Times")

if __name__ == "__main__":
    while True:
        start_service(service_name) # called the function to check if the service is running and to start it if necessary
        text_logo() # called a function to display a logo
        main() # called the main function which is responsible for resyncing the time with a server
        print(Fore.CYAN, Style.DIM + f'Time Sleep' + Style.RESET_ALL)

        # * added a loading bar which will be displayed while waiting for the time to update
        total_time = sleep # set totalTime variable equal to sleep variable
        start_time = time.time() # set starting time of loading bar equal to current system time
        # * Start Loop For Time.Sleep Waiting By Animation Loading Display
        while time.time() - start_time < total_time: # loop until totalTime has been reached (in seconds)
            elapsed_time = int(time.time() - start_time) # calculate elapsed time since starting point (in seconds)
            remaining_time = total_time - elapsed_time # calculate remaining time until totalTime is reached (in seconds)
            minutes, seconds = divmod(remaining_time, 60) # convert remaining time into minutes and seconds format
            loading_bar = '-' * int(50 * elapsed_time / total_time) # create a loading bar based on elapsed and total times
            loading_message = f"Updating time... [{loading_bar}>{' ' * (50 - len(loading_bar))}] {minutes:02d}:{seconds:02d}" # create message for loading bar display
            print(Fore.YELLOW, Back.BLUE, Style.DIM + loading_message, end='\r' + Style.RESET_ALL)
            time.sleep(0.1)
        print('Updating time...')
        continue
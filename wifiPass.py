# snippet to extract passwords for saved wifi profiles
import subprocess
import tkinter as tk


def getExternalIp():
    cmdRes = subprocess.check_output(
        ['nslookup', 'myip.opendns.com', 'resolver1.opendns.com']).decode('utf-8')
    print(cmdRes)


def pingSomeIp():
    data.delete(1.0, tk.END)
    destIp = pingDestInput.get()
    pingResult = subprocess.check_output(['ping', destIp]).decode('utf-8')
    data.insert(tk.END, pingResult)


def getPasswords():
    data.delete(1.0, tk.END)

    results = ''
    # Getting saved wifi profiles using cmd command netsh wlan show profiles
    wifiNames = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'])
    wifiNames = wifiNames.decode('utf-8').split('\n')
    wifiNames = [i.split(':')[1][1:-1]
                 for i in wifiNames if 'All User Profile' in i]

    # Looping  in names and using cmd command netsh wlan show profile WIFI_NAME with KEY=CLEAR switch and print result
    for name in wifiNames:
        tempRes = ''
        password = subprocess.check_output(
            ['netsh', 'wlan', 'show', 'profile', name, 'KEY=CLEAR']).decode('utf-8').split('\n')
        password = [line.split(':')[1][1:-1]
                    for line in password if 'Key Content' in line]
        try:
            tempRes += '{:<30}| {:<}\n'.format(name, password[0])
        except IndexError:
            tempRes += '{:<30}| {:<}\n'.format(
                name, 'No PASSWORD - other authentication protocol might been used')

        data.insert(tk.END, tempRes)


# ------------- GUI -------------------
win = tk.Tk()
win.title('Wifi Passwords')
win.geometry("800x700+50+50")
win.config(background='#339933')

button = tk.Button(
    win, text='Show saved Passwords for Wifis', command=getPasswords)
button.grid(row=0, column=0, pady=5)

pingDestInput = tk.Entry(win, width=40)
pingDestInput.grid(row=0, column=1, pady=5)

button = tk.Button(win, text='Ping', command=pingSomeIp)
button.grid(row=0, column=2, pady=5)


data = tk.Text(win, height=40, width=100, bg='#00cc66')
data.grid(row=1, column=0, columnspan=4)

labelFooter = tk.Label(
    win, text='Sample non official Copy- Under dev version majid.shockoohi@gmail.com')
labelFooter.grid(row=3, column=0, columnspan=2, padx=10, pady=1)

win.mainloop()

# snippet to extract passwords for saved wifi profiles
import subprocess
import tkinter as tk


def getPasswords():
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
            print('{:<30}| {:<}'.format(name, password[0]))
            tempRes += '{:<30}| {:<}\n'.format(name, password[0])
        except IndexError:
            print('{:<30}| {:<}'.format(
                name, 'No PASSWORD - other authentication protocol might been used'))
            tempRes += '{:<30}| {:<}\n'.format(
                name, 'No PASSWORD - other authentication protocol might been used')

        results += tempRes

    data.delete(1.0, tk.END)
    data.insert(tk.END, results)


# ------------- GUI -------------------
win = tk.Tk()
win.title('Wifi Passwords')

label = tk.Label(win, text='Click start to get your saved wifi passes')
label.grid(row=0, column=0, pady=5)

button = tk.Button(
    win, text='Show saved Passwords for Wifis', command=getPasswords)
button.grid(row=0, column=1, pady=5)

data = tk.Text(win, height=40, width=100)
data.grid(row=1, column=0, columnspan=2)

labelFooter = tk.Label(
    win, text='Sample non official Copy- Under dev version majid.shockoohi@gmail.com')
labelFooter.grid(row=2, column=0, columnspan=2, padx=10, pady=1)

win.mainloop()

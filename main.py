import os
import shutil

drive_input = input('Input drive letter: ')

if os.path.isdir(drive_input) == False:
    print('\nWaiting for USB drive to be inserted.......')

while os.path.isdir(drive_input) == False:
    os.path.isdir(drive_input)
    continue

if os.path.isdir(drive_input) == True:
    print('\nUSB connected.......')

SECURITY_FILE = "System Volume Information"

if os.listdir(drive_input) == [SECURITY_FILE] or os.listdir(drive_input) == []:
    print("\nUSB drive is already empty.......\n")
else:
    print(f'These files are stored on the USB drive: {os.listdir(drive_input)}\n')

delete_usb = input('Do u want to wipe and delete the USB Drive?\n')

if delete_usb == 'Yes' or delete_usb == 'Y' or delete_usb == 'y' or delete_usb == 'yes':
    print('Delete and wiping USB drive.....\n')
else:
    print('Thanks for using this program and goodbye')

for root, dirs, files in os.walk(drive_input):
    for file in os.listdir(drive_input):
        if os.path.isfile(drive_input):
            os.remove(os.path.join(root, file))
        elif os.path.isdir(drive_input):
            shutil.rmtree(os.path.join(file, root), ignore_errors=True)
            continue

format_usb = input('Do u want to format the USB-drive?')

if format_usb == 'Yes' or format_usb == 'Y' or format_usb == 'y' or format_usb == 'yes':
    os.system(f"format {drive_input}")


print("""****************************
**** USB drive is wiped ****
****************************""")






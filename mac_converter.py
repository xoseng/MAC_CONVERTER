# coding=utf8
# author: Xose Brais Noya Garcia
# requirements: pillow package

#imports
import cmd_command
import tkinter_functions

#glob vars
version_soft='0.1'
author='Xosé Brais Noya García'
file_save='./macs.txt'

def convert_mac(mac_val): #mac val example: B0B3533A2217
    mac=mac_val.strip()
    long_mac = len(mac)
    hay_dospuntos = ''
    fullstring = mac
    substring = ":"
    if substring in fullstring:
        hay_dospuntos = 'si'
    else:
        hay_dospuntos = 'no'
    if long_mac == 12 and hay_dospuntos == 'no':
        mac_final = mac[0] + mac[1] + ':' + mac[2] + mac[3] + ':' + mac[4] + mac[5] + ':' + mac[6] + mac[7] + ':' + \
                    mac[8] + mac[9] + ':' + mac[10] + mac[11]
        return mac_final
    else:
        return 'FAIL'

def head():

    print("")
    print("GNU General Public License v3.0")
    print("Permissions of this strong copyleft license are conditioned")
    print("on making available complete source code of licensed works and modifications,")
    print("which include larger works using a licensed work, under the same license.")
    print("Copyright and license notices must be preserved.")
    print("Contributors provide an express grant of patent rights.")
    print("")
    print("MAC Converter " + version_soft+' by '+author+'.')
    print("")
    print("NOTICE: Example of file to load with macs in main program folder templates.")
    print("")


def get_file():
    print ('SELECTING FILE...')
    filepath = tkinter_functions.get_filepathload_single_text()
    if filepath.strip() == '':
        get_file()
    else:
        print(filepath)
        return filepath

def get_macs_file(path):
    array_macs=[]
    with open(str(path), 'r') as file_convertir:
        for linea in file_convertir:
            mac_converted = convert_mac(linea)
            if mac_converted != 'FAIL':
                array_macs.append(mac_converted)
            else:
                array_macs.append(linea)
    return array_macs

#MAIN PROGRAM
def main():
    head()
    path=get_file()
    if path !='':
        mac_list=get_macs_file(path)
    if len(mac_list) > 0:
        try:
            cmd_command.wincmd('del "'+file_save+'"')
        except:
            pass
        with open(file_save, 'w') as mac_converter_file:
            for mac_final in mac_list:
                mac_converter_file.write(mac_final+'\n')
        try:
            cmd_command.wincmd('"'+file_save+'"')
        except:
            pass

        input("\nPRESS ANY KEY TO FINISH...\n")
        exit(0)
main()
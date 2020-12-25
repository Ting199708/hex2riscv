import os

# If you want to use 32 bit compiler, please change gcc by yourself
gcc = 'riscv64-unknown-elf-gcc'
objdump = 'riscv64-unknown-elf-objdump'

saved_hex = []
filename = 'hex'

def run_convert(hexfile):
    hexfile = hexfile.split('.')[0]
    os.system('{} -c {}'.format(gcc, hexfile + '.s'))
    os.system('{} -d {}'.format(objdump, hexfile + '.o'))

def save_hex_file():
    with open('{}.s'.format(filename), 'w') as f:
        for instruction in saved_hex:
            f.write(instruction + '\n')

print('===================================================')
print('|           Welcome to use hex2riscv              |')
print('|    Author: Chih-Cheng, Ting Date: 2020/12/25    |')
print('|  National Cheng Kung University, Tainan, Taiwan |')
print('|        Computer Aided Verification Lab          |')
print('|                                                 |')
print('| Please choose the function below:               |')
print('| 1. Select an input hex file and start convert   |')
print('| 2. Enter the hex (16 bits) and save             |')
print('| 3. Enter the hex (32 bits) and save             |')
print('| 4. Show the instruction currently saved         |')
print('| 5. Specify hex file name (default: hex.s)       |')
print('| 6. Clear saved instruction                      |')
print('| 7. Start convert saved instruction              |')
print('|                                                 |')
print('| * type \'exit\' to exit this app                  |')
print('===================================================')

function = ''

while function != 'exit':
    function = input('function: ')

    if (function == '1'):
        filename = input('Please enter the file name (*.s): ')
        run_convert(filename)
    elif (function == '2'):
        instruction = ''
        print('Type \'exit\' to exit this function')
        
        while instruction != 'exit':
            instruction = input('Please enter the instruction (16 bits): ')
            if (instruction != 'exit'):
                saved_hex.append('.hword 0x{}'.format(instruction))
    elif (function == '3'):
        instruction = ''
        print('Type \'exit\' to exit this function')
        while instruction != 'exit':
            instruction = input('Please enter the instruction (32 bits): ')
            if (instruction != 'exit'):
                saved_hex.append('.word 0x{}'.format(instruction))
    elif (function == '4'):
        for instruction in saved_hex:
            print(instruction)
    elif (function == '5'):
        filename = input('Enter the new file name: ')
    elif (function == '6'):
        saved_hex = []
        print('Saved instruction already clear!')
    elif (function == '7'):
        save_hex_file()
        run_convert(filename + '.s')
    elif (function == 'exit'):
        print('\n\nThanks for using hex2riscv!')
    else:
        print('Invalid function')
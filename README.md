# hex2riscv

hex2riscv can help you convert the machine code into assembly code based on RISCV ISA

The app is written in Python, and use riscv-gnu-toolchain to compile and disassemble the machine code

## Installation

If you have not installed the riscv-gnu-toolchain, please use [RISC-V GNU Compiler Toolchain](https://github.com/riscv/riscv-gnu-toolchain) to install

## How to use

1. Use python to run our hex2riscv 
   ```
   python hex2riscv.py
   ```

2. You have two way to enter the machine code that you want to convert

    - Put the machine code in a .s file, and must follow the format as below
      ```
      .word  0x00001797
      .hword 0x4081
      ```
	
    - Use our app's function 2 or 3, you just need to enter the machine code in hex format. We will create the .s file for you before convert them

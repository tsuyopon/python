import struct

# See: http://moraprogramming.hateblo.jp/entry/2017/12/18/002708

def p8(x):
    return struct.pack("<B", x)

def p16(x):
    return struct.pack("<H", x)

def p32(x):
    return struct.pack("<L", x)

def p64(x):
    return struct.pack("<Q", x)

code = '\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05'
entry_point = 0x400078

# ELF Header
elfh = ''
elfh += '\x7fELF' # magic
elfh += p8(2) # Class: 2 is 64bit
elfh += p8(1) # Endinan: little endian
elfh += p8(1) # ELF Version: EV Current
elfh += p8(0) # EI_OSABI: It is often set to 0 regardless of the target platform.(Wikipedia)
elfh += p8(0) # ABI version: (not used)
elfh += p8(0) * 7 # Padding: currently unused
elfh += p16(2) # e_type: 2 is exectable file
elfh += p16(0x3e) # e_machine: 0x3e is x86-64
elfh += p32(1) # e_version: original version(maybe whatever)
elfh += p64(entry_point) # e_entry: entry point
elfh += p64(0x40) # e_phoff: program header table offset -> 64bit is 0x40
elfh += p64(0) # e_shoff: section header table offset -> notable
elfh += p32(0) # e_flags: maybe whatever
elfh += p16(0x40) # e_ehsize: ELF Header Size
elfh += p16(0x38)  # e_phentsize
elfh += p16(1) # e_phnum: the number of program header entries
elfh += p16(0) # e_shentsize: no section headers
elfh += p16(0) # e_shnum: no section headers
elfh += p16(0) # e_shstrndx: no section headers

# Program Header
prmh = ''
prmh += p32(1) # p_type: type of segment
prmh += p32(5) # p_flags: memory segment permission. 0b101 -> Exec + Read
prmh += p64(0x40 + 0x38) # p_offset: offset of the segment
prmh += p64(entry_point) # p_vaddr: virtual address to be mapped in memory
prmh += p64(entry_point) # p_paddr: physical address to be mapped in memory (maybe not used in my machine)
prmh += p64(len(code)) # p_filesz: file size of this segment
prmh += p64(len(code)) # p_memsz: file size of this segment
prmh += p64(0x1000) # p_align: alignment


print(len(elfh), len(prmh), len(code))
payload = elfh + prmh + code
open("dump", "w").write(payload)
print(len(payload))

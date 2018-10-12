'''
Created on Sep 22, 2018

In Half precision floating point , the mantissa is 10 bits wide.
The exponent is 5 bits wide and sign is 1 bit wide. 

The following format is followed in this code

{SIGN,EXPONENT,MANTISSA}


@author: Deekshith Krishegowda
@ID: 012417080
'''
import numpy as np
import argparse

parser = argparse.ArgumentParser(description="Half precision floating point addition and multiplication")
parser.add_argument('-op','--add_mul', type=int, required=True, metavar=' ', help="addition = 1 or multiplication = 0")
parser.add_argument("-in1","--input_one_80", type = float, required = True, metavar=" ", help ="Input one magnitude")
parser.add_argument("-in2","--input_two_80",type = float, required = True, metavar = " ",help = "Input two magnitude")
parser.add_argument("-s1","--sign_one",type = int,required = True, metavar=" ",help = "0 - positive and 1 - negative")
parser.add_argument("-s2","--sign_two",type = int, required = True, metavar=" ",help = "0 - positive and 1 - negative")
args = parser.parse_args()

# the inputs are passed through the command line using argparse package. this is imported here
# all the arguments should be passed. The arguments are not passed by position but are optional. 

if (args.add_mul):
    if(args.sign_one and args.sign_two):
        output_80 = args.input_one_80 + args.input_two_80
    elif(args.input_one_80 > args.input_two_80):
        output_80 = args.input_one_80 - args.input_two_80
    elif(args.input_two_80 > args.input_one_80):
        output_80 = args.input_two_80 - args.input_one_80    
    
else:
    output_80 = args.input_one_80 * args.input_two_80

# The addition or multiplication of the input aurguments is done here. If the opcode is 1 then it is addition. 
# if the opcode is 0, then it is multiplication
        
int16bits_80 = np.asarray(output_80, dtype=np.float16).view(np.int16).item()
# print("this is value of int16bits: %d " %int16bits)
#print('{:016b}'.format(int16bits_80))

# the addition product or multiplication product is converted into half precision floating point using the numpy package. 
# the result is in integer format. this is later converted into string because int cannot be indexed in python  

y_80=bin(int16bits_80)
sbox_80=''
k_80=list(y_80)
x_80=k_80[2:]
l_80=len(x_80)
noOfZeroes_80=16-l_80
for i in range(noOfZeroes_80):
    sbox_80=sbox_80+'0'
for j in x_80:
    sbox_80=sbox_80+j
print("This is the 16bit binary value: %s " %sbox_80)


#print (sbox_80,len(sbox_80)) 

#sign_bit_80=(sbox_80[0])
exp_part_80=(sbox_80[1:6])
man_part_80=(sbox_80[6:]) 

# the mantissa and exponent part are given to exp_part_80 and man_part_80. This is displayed later.    

# this portion calculated the sign of the addition or multiplication operation 
# During multiplication , if both the signs are same, then sign of product is positive. Else it is negative. 
# During addition , the sign of the largest integer is given to the product. 

if (args.add_mul):
    if(args.input_one_80>args.input_two_80):
        sign_bit_80 = args.sign_one
    else:
        sign_bit_80 = args.sign_two
else:
    if (args.sign_one and args.sign_two):
        sign_bit_80 = 0
    else:                
        sign_bit_80 = 1


# this portion displays the mantissa and the exponent portions of the product along with the number of bits    
print("ANSWER IN HALF PRECISION FLOATING POINT")     
print("Mantissa is {} and number of bits is {}".format((man_part_80),len(man_part_80)))
print("Exponent is {} and number of bits is {}".format((exp_part_80),len(exp_part_80)))
print("Sign is {} and number of bit is 1".format(sign_bit_80))


      
      







 
#print('{:016b}'.format(int16bits))
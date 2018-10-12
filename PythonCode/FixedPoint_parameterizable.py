'''
Created on Sep 22, 2018
This is a parameterised fixed point number addition and multiplication operation code. 
The decimal point is parameterised. 
The results are displayed using n as 3bits wide(Whole part) and m as 4 bits wide(Fractional part).

This is the format of my fixed point number.
 
[SIGN,WHOLE PART,FRACTION PART] 
@author: Deekshith
@ID: 012417080
'''
import argparse

parser = argparse.ArgumentParser(description="Fixed point addition and multiplication")
parser.add_argument('-op','--add_mul',type=int,required=True,metavar='',help="addition = 1 or multiplication = 0")
parser.add_argument("-in1","--input_one_80", type = float,required=True,metavar="", help="Input one magnitude")
parser.add_argument("-in2","--input_two_80",type = float,required=True,metavar="",help="Input two magnitude")
parser.add_argument("-s1","--sign_one",type = int,required=True, metavar="",help="0 - positive and 1 - negative")
parser.add_argument("-s2","--sign_two",type = int,required=True,metavar="",help="0 - positive and 1 - negative")
parser.add_argument("-n","--whl_precision",type = int,required=True,metavar="",help="Precision of whole part")
parser.add_argument("-m","--dec_precision",type = int,required=True,metavar="",help="Precision of fraction part")
try:
    args = parser.parse_args()
except SystemExit:
    pass 

# the inputs are passed through the command line using argparse package. this is imported here
# all the arguments should be passed. The arguments are not passed by position but are optional. 

if (args.add_mul):
    output_80=args.input_one_80+args.input_two_80
else:
    output_80=args.input_one_80*args.input_two_80

# if the opcode is 1 then then the addition is done. Else multiplication is done.
#The following section divides the result into whole part and the decimal part

i_80, d_80 = divmod(output_80, 1)
print (i_80,d_80)
int_int_80=int(i_80)
int_bin_80=bin(int_int_80)
int_list_80 = list(int_bin_80)
del int_list_80[0:2]

# if (len(int_list_80) > args.whl_precision):
#     print ("CANNOT DISPLAY IN THIS FORMAT");

# zero padding is done if the length of whole part is less than the decimal precision.
    
if (args.whl_precision>len(int_list_80)):
    diff_80=args.whl_precision - len(int_list_80)
else:
    diff_80=0    

k_80=0
while k_80 <diff_80:
    int_list_80.insert(0, "0")
    k_80 = k_80+1
    #print(int_list_80)   
# zero padding is done

# the following section converts the fractional part into binary value. 
# there is no binary datatype in python, so I wrote this function to convert fractional integer into binary

def dec_int_conv(d_80):
    temp=2*d_80
    
    if(temp>=1):
        ret_bit = 1
        ret_sub = temp-1
        return ret_bit,ret_sub
    else:
        ret_bit = 0
        ret_sub = temp
        return ret_bit,ret_sub 

dec_list_80 = []
n_80 = 0

while n_80<=args.dec_precision:
    b_80,a_80=dec_int_conv(d_80)
    d_80=a_80  
    dec_list_80.insert(n_80,b_80) 
    n_80=n_80+1

del dec_list_80[-1]    
#print (dec_list_80)        


# this section calculates the sign of the result. During multiplication, if both signs are same, then result is positive. Which is 0 here. 
# during addition , the sign of the largest number is given to the result.
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
        
# the following section displays the output. If the number cannot be represented within the given number of precision, 
# then an error will be displayed. Else the number is displayed in floating point format.
if(i_80>=(2**args.whl_precision)):
    print("cannot display number because of limited number of bits")
else:
    print("FIXED POINT ADDER/MULTIPLICATION RESULT")
    print("Whole part is {} and number of bits is {}".format(int_list_80,args.whl_precision))
    print("Fraction part is {} and number of bits is {}".format(dec_list_80,args.dec_precision))
    print("Sign is {} and number of bits is 1".format(sign_bit_80))
        

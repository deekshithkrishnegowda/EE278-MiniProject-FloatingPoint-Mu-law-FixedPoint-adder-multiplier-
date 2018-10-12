'''
Created on Sep 25, 2018
The mu-law is derived from the following encoding table
00000001ABCDX            S000ABCD
0000001ABCDXX            S001ABCD
000001ABCDXXX            S010ABCD
00001ABCDXXXX            S011ABCD
0001ABCDXXXXX            S100ABCD
001ABCDXXXXXX            S101ABCD
01ABCDXXXXXXX            S110ABCD
1ABCDXXXXXXXX            S111ABCD

The number range is between +1/8192 or -1/8192.

@author: Deekshith
@ID: 012417080
'''


import argparse
parser = argparse.ArgumentParser(description="Mu-law addition and multiplication")
parser.add_argument('-op','--add_mul',type=int,required=True,metavar='',help="addition = 1 or multiplication = 0")
parser.add_argument("-in1","--input_one_80", type = float,required=True,metavar="", help="Input one magnitude")
parser.add_argument("-in2","--input_two_80",type = float,required=True,metavar="",help="Input two magnitude")
parser.add_argument("-s1","--sign_one",type = int,required=True, metavar="",help="1 - Positive and 0 - negative")
parser.add_argument("-s2","--sign_two",type = int,required=True,metavar="",help="1 - positive and 0 - negative")
#parser.add_argument("-m","--dec_precision",type = int,required=True,metavar="",help="Precision of fraction part")
args = parser.parse_args()

# the inputs are passed through the command line using argparse package. this is imported here
# all the arguments should be passed. The arguments are not passed by position but are optional. 

if (args.add_mul):
    output_80=args.input_one_80+args.input_two_80
else:
    output_80=args.input_one_80*args.input_two_80

if (output_80>1):
    number_80 = output_80/8192
else:
    number_80 = output_80 

# the inputs are first divided by 8192 if the inputs are greater than 1. Later encoding operation is done to it.
# if the inputs are lesser than 1, then encoding operation is done directly.           
 
i_80, d_80 = divmod(number_80, 1)
dec_precision =13

# the precision of fraction part is entered above.


list1_80 = [0,0,0,0,0,0,0,1]
list2_80 = [0,0,0,0,0,0,1]
list3_80 = [0,0,0,0,0,1]
list4_80 = [0,0,0,0,1]
list5_80 = [0,0,0,1]
list6_80 = [0,0,1]
list7_80 = [0,1]
list8_80 = [1]

# the above list is used as the encoding table

list1_1_80 = [0,0,0]
list2_1_80 = [0,0,1]
list3_1_80 = [0,1,0]
list4_1_80 = [0,1,1]
list5_1_80 = [1,0,0]
list6_1_80 = [1,0,1]
list7_1_80 = [1,1,0]
list8_1_80 = [1,1,1]

# this list is concatinated with some value later.
# this function is used to covert the fractional part which is in decimal into binary. 
# This is done because python does not has binary format datatype.

def dec_int_conv(d_80):
    temp_80=2*d_80
    
    if(temp_80>=1):
        ret_bit_80 = 1
        ret_sub_80 = temp_80-1
        return ret_bit_80,ret_sub_80
    else:
        ret_bit_80 = 0
        ret_sub_80 = temp_80
        return ret_bit_80,ret_sub_80 

dec_list_80 = []
n_80 = 0

while n_80<=dec_precision:
    b_80,a_80=dec_int_conv(d_80)
    d_80=a_80  
    dec_list_80.insert(n_80,b_80) 
    n_80=n_80+1
    
dec_int_conv(d_80)    
#print (dec_list_80,type(dec_list_80[0])) 

dec_list_updated_80 = []
for i_80 in dec_list_80:
    if(i_80==0):
        dec_list_updated_80.append(i_80)
    else:
        break

if (d_80<1):
    dec_list_updated_80.append(1)
#print(dec_list_updated_80)        

# the below portion handles the sign of the product.
# During multiplication, if both the signs are same, then result is positive. Which is 1 here. Else it is negative. 0 here. 
# During addition, the sign depends on the value of the greatest integer. 

final_list_80 = []
if (args.add_mul):
    if(args.input_one_80>args.input_two_80):
        sign_bit_80 = args.sign_one
    else:
        sign_bit_80 = args.sign_two
else:
    if (args.sign_one and args.sign_two):
        sign_bit_80 = 1
    else:                
        sign_bit_80 = 0


# The section below does the encoding operation. The results are compared with the lists defined above and later concatinated with 
# lists defined above. This gives the encoded value.
# the sign bit is appended in the beginning of the final list.

if (dec_list_80[0:1] == dec_list_updated_80):
    final_list_80 = list8_1_80 + dec_list_80[1:5] 
    final_list_80.insert(0, sign_bit_80)
    
elif (dec_list_80[0:2] == dec_list_updated_80):
    final_list_80 = list7_1_80 + dec_list_80[2:6]
    final_list_80.insert(0, sign_bit_80)     
    
elif (dec_list_80[0:3] == dec_list_updated_80):
    final_list_80 = list6_1_80 + dec_list_80[3:7]
    final_list_80.insert(0, sign_bit_80) 

elif (dec_list_80[0:4] == dec_list_updated_80):
    final_list_80 = list5_1_80 + dec_list_80[4:8]
    final_list_80.insert(0, sign_bit_80)
 
elif (dec_list_80[0:5] == dec_list_updated_80):
    final_list_80 = list4_1_80 + dec_list_80[5:9]
    final_list_80.insert(0, sign_bit_80)

elif (dec_list_80[0:6] == dec_list_updated_80):
    final_list_80 = list3_1_80 + dec_list_80[6:10]
    final_list_80.insert(0, sign_bit_80)
    
elif (dec_list_80[0:7] == dec_list_updated_80):
    final_list_80 = list2_1_80 + dec_list_80[7:11]
    final_list_80.insert(0, sign_bit_80)

elif (dec_list_80[0:8] == dec_list_updated_80):
    final_list_80 = list1_1_80 + dec_list_80[8:12]
    final_list_80.insert(0, sign_bit_80)        

# the results are displayed in the following section.
# After dividing the inputs by 8192, if the results is  not comparable with the encoding table, then the number cannot be represented 
# using mu-law encoding.

else:
    print ("cannot display in mu-law ")
                    
print ("Mu-law encoded value is {}".format(final_list_80))             

        
                
    

   
1.FLOATING POINT HALF PRECISION
Half precision floating point addition and multiplication

optional arguments:
  -h, --help            show this help message and exit
  -op  , --add_mul      addition = 1 or multiplication = 0
  -in1  , --input_one_80
                        Input one magnitude
  -in2  , --input_two_80
                        Input two magnitude
  -s1  , --sign_one     0 - positive and 1 - negative
  -s2  , --sign_two     0 - positive and 1 - negative



SAMPLE ARGUMENT:python C:\Users\Deekshith\Desktop\eclipse\eclipse_WorkSpace\278\FloatingPoint_HalfPrecision.py -op 1 -in1 1 -in2 2 -s1 0 -s2 0
run this argument from your command line. 
////////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////////////////////////////



2.Mu-law:
Mu-law addition and multiplication

optional arguments:
  -h, --help            show this help message and exit
  -op , --add_mul       addition = 1 or multiplication = 0
  -in1 , --input_one_80
                        Input one magnitude
  -in2 , --input_two_80
                        Input two magnitude
  -s1 , --sign_one      1 - Positive and 0 - negative
  -s2 , --sign_two      1 - positive and 0 - negative



SAMPLE ARGUMENT :python C:\Users\Deekshith\Desktop\eclipse\eclipse_WorkSpace\278\mu-law_adder_multiplier.py -op 0 -in1 1 -in2 2 -s1 0 -s2 0
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

3.Fixed Point 
Fixed point addition and multiplication

optional arguments:
  -h, --help            show this help message and exit
  -op , --add_mul       addition = 1 or multiplication = 0
  -in1 , --input_one_80
                        Input one magnitude
  -in2 , --input_two_80
                        Input two magnitude
  -s1 , --sign_one      0 - positive and 1 - negative
  -s2 , --sign_two      0 - positive and 1 - negative
  -n , --whl_precision
                        Precision of whole part
  -m , --dec_precision
                        Precision of fraction part


SAMPLE ARGUMENT: python C:\Users\Deekshith\Desktop\eclipse\eclipse_WorkSpace\278\FixedPoint_parameterizable.py -op 0 -in1 1 -in2 2 -s1 0 -s2 1 -n 2 -m 3

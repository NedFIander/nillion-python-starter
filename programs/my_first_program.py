from nada_dsl import *

def nada_main():
    # Define two parties
    party1 = Party(name="Party1")
    party2 = Party(name="Party2")
    
    # Secret integers for Party1
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))
    
    # Secret integers for Party2
    my_int3 = SecretInteger(Input(name="my_int3", party=party2))
    my_int4 = SecretInteger(Input(name="my_int4", party=party2))
    
    # Compute the sum and difference of my_int1 and my_int2
    sum_result = my_int1 + my_int2
    difference_result = my_int1 - my_int2
    
    # Compute the product of my_int3 and my_int4
    product_result = my_int3 * my_int4
    
    # Define the outputs
    sum_output = Output(sum_result, "sum_output", party1)
    difference_output = Output(difference_result, "difference_output", party2)
    product_output = Output(product_result, "product_output", party1)
    
    return [sum_output, difference_output, product_output]


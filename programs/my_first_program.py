from nada_dsl import *


def nada_main():
    party1 = Party(name="Party1")
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))

    # Compute the sum of my_int1 and my_int2
    sum_result = my_int1 + my_int2

    # Compute the product of my_int1 and my_int2
    product_result = my_int1 * my_int2

    # Define the outputs
    sum_output = Output(sum_result, "sum_output", party1)
    product_output = Output(product_result, "product_output", party1)

    return [sum_output, product_output]

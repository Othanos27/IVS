##
# @author Jan Kleisl (xkleis00)
# @file mathlib.py
# @date 25.03.2020
#

##
# @brief Function for addition
# @param First number
# @param Second number
# @return Result of two added numbers
def add(A, B):
	return(A + B)

##
# @brief Function for subtraction
# @param First number
# @param Second number
# @return Result of two subtracted numbers
def sub(A, B):
	return(A - B)

##
# @brief Function for multiplication
# @param First number
# @param Second number
# @return Result of two multiplied numbers
def mul(A, B):
	return(A * B)

##
# @brief Function for division
# @details Its also checking for division by zero
# @param First number
# @param Second number
# @return Result of two divided numbers
def div(A, B):
	if B == 0:
		return("error")
	return(A / B)

##
# @brief Function for power
# @param First number
# @param Second number
# @return Result of number raised to the power of the other
def pow(A, B):
	return(A ** B)

##
# @brief Function for square root
# @param First number
# @param Second number
# @return Result of square rooted number
def sqrr(A, B):
    if B <= 0 or A < 0:
	    return("error")
    return(A ** (float(1) / float(B)))

"""
Description:
Cryptography can be easy, do you know what ROT13 is? 
cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_hyLicInt}

output:
picoCTF{next_time_I'll_try_2_rounds_of_rot13_ulYvpVag}
"""

string = "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_hyLicInt}"

lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

result = []

for i in string:
  if i in lowercase:
    new_i = lowercase[(lowercase.index(i) + 13) % 26]
  elif i in uppercase:
    new_i = uppercase[(uppercase.index(i) + 13) % 26]
  else:
    new_i = i


    
  result.append(new_i)

# Join the list into a string
new_string = ''.join(result)

print(new_string)




Explanation:
ROT13 is a type of Caesar cypher- each letter is replaced by the letter 13 positions ahead of it.
The % 26 operation ensures that the shift wraps around the alphabet if it goes past 'z' or 'Z'.

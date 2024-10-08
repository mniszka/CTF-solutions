"""
Description
Cryptography can be easy, do you know what ROT13 is? 
cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}

"""

string = "cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}"

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

Solution:
picoCTF{not_too_bad_of_a_problem}

#It is a fun program which will tell a user whether she is having a girl or a boy. 

test1 = input("Are you craving spicy food? (Y/N) :")
test2 = input("Are you craving sweets? (Y/N) :")
test3 = input("Are you suffering from extreme morning sickeness or hyperemesis (Y/N) :")
test4 = input("Is the baby's heart rate above 150 beats per minute? (Y/N) :")

if test1.upper() == "N" and test2.upper() == "N" and test3.upper() == "Y" and test4.upper() == "Y":
 print("CONGRATS!..Its a GIRL!..YAYYY")
elif test1.upper() == "Y" and test2.upper() == "Y" and test3.upper() == "Y" and test4.upper() == "Y":
 print("CONGRATS!..Its a GIRL!..YAYYY")
else:
 print("CONGRATS!..Its a BOY!..YAYYY")
 
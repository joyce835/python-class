Q=int(input("INPUT q:"))
J=int(input("INPUT j:"))
R=int(input("INPUT r:"))
RSN=Q**2 + R**(0.5)
RSD=J**(1/Q)
bracket_sum=RSN/RSD
(bracket_sum)**Q
LSN=99-Q
LSD= 7*49**0.5
bracket_sum=LSN/LSD
Denom=(bracket_sum)**20//6
Numerator=(bracket_sum)**Q/(bracket_sum)**20//6
Total_sum=Numerator/Denom
P=Numerator/Denom
print(P)
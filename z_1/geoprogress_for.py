input_data = open('z_1/input.txt','r') 
data = input_data.read()
data = data.split()
b = float(data[0])
q = float(data[1])
n = int(data[2])
S = 0
for i in range(1, n + 1):
    S += b
    b = b*q
output_data = open('z_1/output.txt','w')
output_data.write(str(S))
input_data.close()
output_data.close()
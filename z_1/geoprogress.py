input_data = open('z_1/input.txt','r') 
data = input_data.read()
data = data.split()
b1 = float(data[0])
q = float(data[1])
n = float(data[2])
S = (b1 * (1 - q**n))/(1 - q)
output_data = open('z_1/output.txt','w')
output_data.write(str(S))
input_data.close()
output_data.close()
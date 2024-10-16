input_data = open('z_2/input.txt','r') 
data = input_data.read()
a = int(data)
if a==2 or a==3 or a==5 or a==7 or a==11 or a==13 or a==17 or a==19 or a==23:
    output_data = open('z_2/output.txt','w')
    output_data.write('Y') 
else:
    output_data = open('z_2/output.txt','w')
    output_data.write('N')
input_data.close()
output_data.close()
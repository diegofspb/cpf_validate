cpf=list()
cpf2=list()
cpfa= list()
cpfb= str
cpfc= list()
cpfd= 0
s=''
print('='*40)
print('{:^40}'.format('Programa Validador de CPF'))
print('='*40)

cpf = str(input('Informe seu CPF com pontos e dígito: '))
cpfa=cpf.split('-')  
cpf=cpfa[0].split('.') 

s=list()
for c in cpf:   
 s+=c 
d=11 
soma=0
for e in s:
 d-= 1
 f = int(d)*int(e)   
 soma+=f
 print(f'{e} x {d} = {f}')
print('')
print(f'A soma dos nº do CPF = {soma}')
d1 = 11-(soma%11)
print(f'\nO Primeiro Dígito do CPF = {d1}\n')


h=12
soma2=0
s.append(d1)   

for g in s:
 h-=1
 i=int(g)*int(h)
 print(f'{g} x {h} = {i}')
 soma2+=i
 print(f'A soma dos nº do CPF = {soma2}')

d2 = 11-(soma2 % 11)
print(f'\nO SEGUNDO Dígito do CPF = {d2}\n')

s.append(d2)
cpf2=s

print(cpf2)

l=''
for k in cpf2:
 l=str(l)+str(k)
print(f'CPF Descoberto pelo ALGORÍTIMO = {l}')

cpf.append(cpfa[1])
print(cpf)

m=''
for k in cpf:
 m=str(m)+str(k)
print(f'CPF INFORMADO NO INÍCIO = {m}')

print('='*40)
print('{:^40}'.format('RESULTADO'))
print('='*40)

if l==m:
 print('CPF válido')
else:
 print('CPF inválido')
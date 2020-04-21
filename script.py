name = input('Ingresa tu nombre: \n')
print('tu nombre es {}'.format(name))
print('\n')
edad = input('Cual es tu edad? \n')
print('Tu edad es: {}'.format(edad))
print('\n')

# Funcion

user = 0
edad1 = int(edad)
while user != edad1:
  user = int(input('Ingresa el numero \n'))
  if user > edad1:
    print('menor')
  elif user < edad1:
    print('Mayor')
  else:
    print('Ok')

tribunas = 50000
plateas = 15000
plateasPref= 5000
palcos = 2000

reservaPalcos = 700
reservaPlateasPref= 1500

cantPartidos = int(input('Ingrese cantidad de partidos: '))
tribunaPrecio = float(input('Ingrese precio de entrada de tribuna: '))
plateaPrecio = float(input('Ingrese precio de entrada de platea: '))
plateaPrefPrecio = float(input('Ingrese precio de entrada de platea Preferencial: '))
palcoPrecio = float(input('Ingrese precio de entrada de palco: '))

recaudacionMax = (tribunas * tribunaPrecio) + (plateas * plateaPrecio) \
+ ((plateasPref - reservaPlateasPref) * plateaPrefPrecio) \
+ ((palcos - reservaPalcos) * palcoPrecio) \

print( 'Recaudacion maxima por partido: ' + str(recaudacionMax))
recaudacionMax = recaudacionMax * cantPartidos

print( 'Recaudacion maxima: ' + str(recaudacionMax))

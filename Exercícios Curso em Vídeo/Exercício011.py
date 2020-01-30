# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
# necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

largura_da_parede = float(input('Largura da parede: '))
altura_da_parede = float(input('Altura da parede: '))

area_de_parede = largura_da_parede * altura_da_parede
litros_de_tinta = area_de_parede / 2

print('Sua parede tem a dimensão de {}x{} e sua área é de {:.2f} m²,'.format(largura_da_parede, altura_da_parede, area_de_parede))
print('Para pintar essa parede, você precisará de {:.2f} litros de tinta.'.format(litros_de_tinta))

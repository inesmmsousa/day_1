# coding: utf-8

# Execute the program and see what happens.
# Then modify the program so that X is replaced by the day of the week input.
# Hint: see what we did with the name.

message = """
Caro/a {},

Bem-vindo/a ao iBiMED.
O dia da semana é X!

Hasta la vista,
"""

name = input("Como te chamas? ")
week_day = input("Dia da semana? ")

print(message.format(name))

mensagem1 = """
Portugal campeão
"""
mensagem2 = """
HA, HA, HA!
"""

name = input("De onde és ?")
for i in name:
    if i != 'Portugal':
        print(mensagem1.format(name))
    else:
        print(mensagem2.format(name))


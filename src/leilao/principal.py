from  dominio import Usuario, Lance, Leilao


paulo = Usuario('Paulo')
yuri = Usuario('yuri')

lance_do_yuri = Lance(yuri,100.20)
lance_do_paulo = Lance(paulo,1500.20)


leilao = Leilao('celular')


leilao.lances.append(lance_do_yuri)
leilao.lances.append(lance_do_paulo)

for lance in leilao.lances:
    print(f'O usuario {lance.usuario.nome} deu um lance de {lance.valor}')


avaliador = Avaliador()
avaliador.avalia(leilao)

print(f' O menor lance foi de {avaliador.menor_lance} e o maior lance foi de {avaliador.maior_lance}')

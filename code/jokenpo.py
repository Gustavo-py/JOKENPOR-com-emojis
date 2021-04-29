from random import randint
from time import sleep
import emoji


emoti = emoji.emojize
pc = randint(0,2)

escolha = (emoti(':punch:' ':page_with_curl:' ':scissors:', use_aliases=True))



while True:
    
    game = input(emoti('Vamos :video_game: JoKenPoo [s|n]? ', use_aliases=True ))
    
    if game == 'n':
        print(emoti('Tá com medoo hahaha. :japanese_ogre:', use_aliases=True))
        sleep(2)
        print(emoti('Tchauzinho Perdedor :running: :dash:', use_aliases=True))
        break

    if game == 's':
        print(emoti('Lets Go!! :space_invader:', use_aliases=True))
        sleep(1)

        print('=+='*13)
        print('Seja Bem vindo(a) ao JokenPoo 3.9.1')
        print('=+='*13)
        print(emoti('''SUAS OPÇÔES SÂO:

        [ 0 ] :punch: PEDRA
        [ 1 ] :page_with_curl: PAPEL
        [ 2 ] :scissors:  TESOURA
        ''', use_aliases=True ))
        print('=+='*13)
        vc = int(input(emoti('Qual é a sua escolha :ghost: ? ' , use_aliases=True )))
        print('=+='*13)
        
        if vc >= 3:
            print('Já ta tremendo kkk. Digite Um numero Valido')

        print(emoti('JO :page_with_curl:' , use_aliases=True))
        sleep(2)
        print(emoti('KEN :scissors:', use_aliases=True))
        sleep(2)
        print(emoti('POO!! :punch:', use_aliases=True))
        sleep(1)
        print('=+='*13)

        print('O Bot escolheu {}'.format(escolha[pc]))
        print('E voce escolheu {}'.format(escolha[vc]))

        if pc == 0:

                if vc == 0:      
                   print(f'EMPATOOU!!. {escolha[vc]} é igual {escolha[pc]}')

                elif vc == 1:
                    print(f'PARABENS VOCE VENCEU!!. {escolha[vc]} ganha de {escolha[pc]}')

                elif vc == 2:
                    print(f'INFELIZMENTE voce Perdeu. {escolha[vc]} não ganha de {escolha[pc]}')

                else:
                    print('ERRO 404')

        if pc == 1:

                if vc == 0:
                    print(f'INFELIZMENTE voce Perdeu. {escolha[vc]} não ganha de {escolha[pc]}')

                elif vc == 1:
                    print(f'EMPATOOU!!. {escolha[vc]} é igual {escolha[pc]}')

                elif vc == 2:
                    print(f'PARABENS VOCE VENCEU!!. {escolha[vc]} ganha de {escolha[pc]}')

                else:
                    print('ERRO 404')

        if pc == 2:

                if vc == 0:
                    print(f'PARABENS VOCE VENCEU!!. {escolha[vc]} ganha de {escolha[pc]}')
                    
                elif vc == 1:
                    print(f'INFELIZMENTE voce Perdeu. {escolha[vc]} não ganha de {escolha[pc]}')

                elif vc == 2:
                    print(f'EMPATOOU!!. {escolha[vc]} é igual {escolha[pc]}')

    else:
        print('Digite um Comando Valido')
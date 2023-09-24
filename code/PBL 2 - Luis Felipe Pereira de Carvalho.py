#*********************************************************************************************************************

#Autor: Luis Felipe Pereira de Carvalho
#Componente curricular: MI Algoritmos I
#Concluído em: 12/11/2022
#  Declaro que este código foi elaborado por mim de forma indivdual e não contém nenhum trecho de código de colega ou de outro autor,
#tais como provindos de livros e apostilas, e paginas ou documentos eletrônicos da internet. 
#qualquer trecho de código de outra autoria que não a minha está destacado como uma citação ao autor e a fonte do código,
#e estou ciente que estes trechos não serão considerados para fim de avaliação.

#*********************************************************************************************************************
#Importação das bibliotecas e declaração das seção-listas a serem usadas na execução do código.

import random
import time 
secao1 = []; secao2 = []; secao3 = []; secao4 = []; secao5 = []; secao6 = []; secao7 = []; secao8 = []; secao9 = []
#A função gerar seção é responsável por gerar as seções de ambos os níveis, sendo determinado pela variavel Base
def gerar_secao(base):
    nivel = base**2
    matriz_interna= []
    num_random = random.sample(range(1, nivel + 1), nivel)
    if nivel == 4:
        l1= [(num_random[0]),(num_random[1])]
        l2= [(num_random[2]),(num_random[3])]
        matriz_interna.append(l1)
        matriz_interna.append(l2)
        return matriz_interna
    elif nivel == 9:
        l1= [(num_random[0]),(num_random[1]),(num_random[2])]
        l2= [(num_random[3]),(num_random[4]),(num_random[5])]
        l3= [(num_random[6]),(num_random[7]),(num_random[8])]
        matriz_interna.append(l1)
        matriz_interna.append(l2)
        matriz_interna.append(l3)
        return matriz_interna
#A função verificar menu é responsável por validar as escolhas para o menu, no caso de de ser diferente de 0 ou 1 ou 2,
#ela pede que o usuário escolha novamente uma opção válida.
def verificar_menu():
    print('''\nDigite apenas o número da opção que deseja executar. 
[1] - Selecionar nível fácil \n[2] - Selecionar nível difícil \n[0] - Sair do jogo
\n==================================================\n''')
    while True:
        n = input('Por favor, escolha uma das opções válidas: ')
        try:
            n = int(n)
            if 0 <= n <= 2:
                break
            else:
                print('\nOpção inválida, tente novamente!')
        except ValueError:
            print("\nSomente números são permitidos.")
    return n
#A função num_e_secoes é responsável por receber o valor da seção e do número escolhido pelo jogador. 
#Esses valores são manipulados dentro da função de modo a remover o número quando ele é escolhido e removendo a seção caso ela seja totalmente preeenchida.
def num_e_secoes():
    if base == 2:
        num_secao = int(input('Escolha a seção de 1 a 4: '))
        while num_secao not in secoes:
            print('\nSeção inválida ou já preenchida!')
            num_secao = int(input('Escolha outra seção: '))
        if num_secao == 1:
            num = int(input('\nEscolha um número entre 1 e 4: '))
            while num not in sc1:
                num = int(input('Escolha outro número:'))
            sc1.remove(num)
            if sc1 == []:
                secoes.remove(1)
        elif num_secao == 2:
            num = int(input('\nEscolha um número entre 1 e 4: '))
            while num not in sc2:
                num = int(input('Escolha outro número:'))
            sc2.remove(num)
            if sc2 == []:
                secoes.remove(2)
        elif num_secao == 3:
            num = int(input('\nEscolha um número entre 1 e 4: '))
            while num not in sc3:
                num = int(input('Escolha outro número:'))
            sc3.remove(num)
            if sc3 == []:
                secoes.remove(3)
        elif num_secao == 4:
            num = int(input('\nEscolha um número entre 1 e 4: '))
            while num not in sc4:
                num = int(input('Escolha outro número:'))
            sc4.remove(num)
            if sc4 == []:
                secoes.remove(4)
    #a seguinte parte é responsável por exibir o número escolhido pelo usuário no tabuleiro que é exibido para o jogador
        if num_secao == 1:
            for i in range(2):
                for j in range(2): 
                    if secao1[i][j] == num: sc1_resp[i][j] = num
        elif num_secao == 2:
            for i in range(2):
                for j in range(2): 
                    if secao2[i][j] == num: sc2_resp[i][j] = num
        elif num_secao == 3:
            for i in range(2):
                for j in range(2): 
                    if secao3[i][j] == num: sc3_resp[i][j] = num
        elif num_secao == 4:
            for i in range(2):
                for j in range(2): 
                    if secao4[i][j] == num: sc4_resp[i][j] = num
#==============================================================================================
    elif base == 3:
        num_secao = int(input('Escolha uma seção de 1 a 9: '))
        while num_secao not in secoes:
            print('Seção já preenchida!')
            num_secao = int(input('Escolha outra seção: '))
        
        if num_secao == 1:
            num = int(input('\nSomente números inteiros! \nEscolha um número entre 1 e 9: '))
            while num not in sc1:
                num = input('Escolha outro número:')
            sc1.remove(num)
            if sc1 == []:
                secoes.remove(1)
        elif num_secao == 2:
            num = int(input('\nSomente números inteiros! \nEscolha um número entre 1 e 9: '))
            while num not in sc2:
                num = input('Escolha outro número:')
            sc2.remove(num)
            if sc2 == []:
                secoes.remove(2)
        elif num_secao == 3:
            num = int(input('\nSomente números inteiros! \nEscolha um número entre 1 e 9: '))
            while num not in sc3:
                num = input('Escolha outro número:')
            sc3.remove(num)
            if sc3 == []:
                secoes.remove(3)
        elif num_secao == 4:
            num = int(input('\nSomente números inteiros! \nEscolha um número entre 1 e 9: '))
            while num not in sc4:
                num = input('Escolha outro número:')
            sc4.remove(num)
            if sc4 == []:
                secoes.remove(4)
        elif num_secao == 5:
            num = int(input('\nSomente números inteiros! \nEscolha um número entre 1 e 9: '))
            while num not in sc5:
                num = input('Escolha outro número:')
            sc5.remove(num)
            if sc5 == []:
                secoes.remove(5)
        elif num_secao == 6:
            num = int(input('\nSomente números inteiros! \nEscolha um número entre 1 e 9: '))
            while num not in sc6:
                num = input('Escolha outro número:')
            sc6.remove(num)
            if sc6 == []:
                secoes.remove(6)
        elif num_secao == 7:
            num = int(input('\nSomente números inteiros! \nEscolha um número entre 1 e 9: '))
            while num not in sc7:
                num = input('Escolha outro número:')
            sc7.remove(num)
            if sc7 == []:
                secoes.remove(7)
        elif num_secao == 8:
            num = int(input('\nSomente números inteiros! \nEscolha um número entre 1 e 9: '))
            while num not in sc8:
                num = input('Escolha outro número:')
            sc8.remove(num)
            if sc8 == []:
                secoes.remove(8)
        elif num_secao == 9:
            num = int(input('\nSomente números inteiros! \nEscolha um número entre 1 e 9: '))
            while num not in sc4:
                num = input('Escolha outro número:')
            sc9.remove(num)
            if sc9 == []:
                secoes.remove(9)
    #a seguinte parte é responsável por exibir o número escolhido pelo usuário no tabuleiro que é exibido para o jogador
        if num_secao == 1:
            for i in range(3):
                for j in range(3): 
                    if sc1[i][j] == num: sc1_resp[i][j] = num
        elif num_secao == 2:
            for i in range(3):
                for j in range(3): 
                    if sc2[i][j] == num: sc2_resp[i][j] = num
        elif num_secao == 3:
            for i in range(3):
                for j in range(3): 
                    if sc3[i][j] == num: sc3_resp[i][j] = num
        elif num_secao == 4:
            for i in range(3):
                for j in range(3): 
                    if sc4[i][j] == num: sc4_resp[i][j] = num
        elif num_secao == 5:
            for i in range(3):
                for j in range(3): 
                    if sc5[i][j] == num: sc5_resp[i][j] = num
        elif num_secao == 6:
            for i in range(3):
                for j in range(3): 
                    if sc6[i][j] == num: sc6_resp[i][j] = num
        elif num_secao == 7:
            for i in range(3):
                for j in range(3): 
                    if sc7[i][j] == num: sc7_resp[i][j] = num
        elif num_secao == 8:
            for i in range(3):
                for j in range(3): 
                    if sc8[i][j] == num: sc8_resp[i][j] = num
        elif num_secao == 9:
            for i in range(3):
                for j in range(3): 
                    if sc9[i][j] == num: sc9_resp[i][j] = num
#As funções somas_col_xx são responsáveis por comparar as somas da matriz interna e dos itens da matriz externa, 
#de modo a anexar o valor da soma ao usuário que completar primeiro uma coluna.
def somas_col_facil():
    pontos = 0
    if soma_c1 == m_resp[0][0]+ m_resp[1][0]+m_resp[2][0]+m_resp[3][0]:
        pontos += soma_c1
    if soma_c2 == m_resp[0][1]+ m_resp[1][1]+m_resp[2][1]+m_resp[3][1]:
        pontos += soma_c2
    if soma_c3 == m_resp[0][2]+ m_resp[1][2]+m_resp[2][2]+m_resp[3][2]:
        pontos += soma_c3
    if soma_c4 == m_resp[0][3]+ m_resp[1][3]+m_resp[2][3]+m_resp[3][3]:
        pontos += soma_c4
    return pontos

def somas_col_dif():
    soma = 0
    if soma_c1 == m_resp[0][0]+m_resp[1][0]+m_resp[2][0]+m_resp[3][0]+m_resp[4][0]+m_resp[5][0]+m_resp[6][0]+m_resp[7][0]+m_resp[8][0]:
        soma += soma_c1
    if soma_c2 == m_resp[0][1]+m_resp[1][1]+m_resp[2][1]+m_resp[3][1]+m_resp[4][1]+m_resp[5][1]+m_resp[6][1]+m_resp[7][1]+m_resp[8][1]:
        soma += soma_c2
    if soma_c3 == m_resp[0][2]+m_resp[1][2]+m_resp[2][2]+m_resp[3][2]+m_resp[4][2]+m_resp[5][2]+m_resp[6][2]+m_resp[7][2]+m_resp[8][2]:
        soma += soma_c3
    if soma_c4 == m_resp[0][3]+m_resp[1][3]+m_resp[2][3]+m_resp[3][3]+m_resp[4][3]+m_resp[5][3]+m_resp[6][3]+m_resp[7][3]+m_resp[8][3]:
        soma += soma_c4
    if soma_c5 == m_resp[0][4]+m_resp[1][4]+m_resp[2][4]+m_resp[3][4]+m_resp[4][4]+m_resp[5][4]+m_resp[6][4]+m_resp[7][4]+m_resp[8][4]:
        soma += soma_c5
    if soma_c6 == m_resp[0][5]+m_resp[1][5]+m_resp[2][5]+m_resp[3][5]+m_resp[4][5]+m_resp[5][5]+m_resp[6][5]+m_resp[7][5]+m_resp[8][5]:
        soma += soma_c6
    if soma_c7 == m_resp[0][6]+m_resp[1][6]+m_resp[2][6]+m_resp[3][6]+m_resp[4][6]+m_resp[5][6]+m_resp[6][6]+m_resp[7][6]+m_resp[8][6]:
        soma += soma_c7
    if soma_c8 == m_resp[0][7]+m_resp[1][7]+m_resp[2][7]+m_resp[3][7]+m_resp[4][7]+m_resp[5][7]+m_resp[6][7]+m_resp[7][7]+m_resp[8][7]:
        soma += soma_c8
    if soma_c9 == m_resp[0][8]+m_resp[1][8]+m_resp[2][8]+m_resp[3][8]+m_resp[4][8]+m_resp[5][8]+m_resp[6][8]+m_resp[7][8]+m_resp[8][8]:
        soma += soma_c9
    return soma
#As funções somas_lin_xx são responsáveis por comaprar as somas da matriz interna e dos itens da matriz externa, 
#de modo a anexar o valor da soma ao usuário que completar primeiro uma linha.
def somas_lin_facil():
    pontos = 0
    if soma_l1 == m_resp[0][0]+m_resp[0][1]+m_resp[0][2]+m_resp[0][3]:
        pontos += soma_l1
    if soma_l2 == m_resp[1][0]+m_resp[1][1]+m_resp[1][2]+m_resp[1][3]:
        pontos += soma_l2
    if soma_l3 == m_resp[2][0]+m_resp[2][1]+m_resp[2][2]+m_resp[2][3]:
        pontos += soma_l3
    if soma_l4 == m_resp[3][0]+m_resp[3][1]+m_resp[3][2]+m_resp[3][3]:
        pontos += soma_l4
    return pontos

def somas_lin_dif():
    soma = 0
    if soma_l1 == m_resp[0][0]+m_resp[0][1]+m_resp[0][2]+m_resp[0][3]+m_resp[0][4]+m_resp[0][5]+m_resp[0][6]+m_resp[0][7]+m_resp[0][8]:
        soma += soma_l1
    if soma_l2 == m_resp[1][0]+m_resp[1][1]+m_resp[1][2]+m_resp[1][3]+m_resp[1][4]+m_resp[1][5]+m_resp[1][6]+m_resp[1][7]+m_resp[1][8]:
        soma += soma_l2
    if soma_l3 == m_resp[2][0]+m_resp[2][1]+m_resp[2][2]+m_resp[2][3]+m_resp[2][4]+m_resp[2][5]+m_resp[2][6]+m_resp[2][7]+m_resp[2][8]:
        soma += soma_l3
    if soma_l4 == m_resp[3][0]+m_resp[3][1]+m_resp[3][2]+m_resp[3][3]+m_resp[3][4]+m_resp[3][5]+m_resp[3][6]+m_resp[3][7]+m_resp[3][8]:
        soma += soma_l4
    if soma_l5 == m_resp[4][0]+m_resp[4][1]+m_resp[4][2]+m_resp[4][3]+m_resp[4][4]+m_resp[4][5]+m_resp[4][6]+m_resp[4][7]+m_resp[4][8]:
        soma += soma_l5
    if soma_l6 == m_resp[5][0]+m_resp[5][1]+m_resp[5][2]+m_resp[5][3]+m_resp[5][4]+m_resp[5][5]+m_resp[5][6]+m_resp[5][7]+m_resp[5][8]:
        soma += soma_l6
    if soma_l7 == m_resp[6][0]+m_resp[6][1]+m_resp[6][2]+m_resp[6][3]+m_resp[6][4]+m_resp[6][5]+m_resp[6][6]+m_resp[6][7]+m_resp[6][8]:
        soma += soma_l7
    if soma_l8 == m_resp[7][0]+m_resp[7][1]+m_resp[7][2]+m_resp[7][3]+m_resp[7][4]+m_resp[7][5]+m_resp[7][6]+m_resp[7][7]+m_resp[7][8]:
        soma += soma_l8
    if soma_l9 == m_resp[8][0]+m_resp[8][1]+m_resp[8][2]+m_resp[8][3]+m_resp[8][4]+m_resp[8][5]+m_resp[8][6]+m_resp[8][7]+m_resp[8][8]:
        soma += soma_l9
    return soma
#As funções somas_diag_xx são responsáveis por comparar as somas da matriz interna e dos itens da matriz externa, 
#de modo a anexar o valor da soma ao usuário que completar primeiro a diagonal principal.
def somas_diag_facil():
    pontos = 0
    if soma_diag == m_resp[0][0]+m_resp[1][1]+m_resp[2][2]+m_resp[3][3]:
        pontos += (soma_diag*2)
    return pontos

def somas_diag_dif():
    pontos = 0
    if soma_diag == m_resp[0][0]+m_resp[1][1]+m_resp[2][2]+m_resp[3][3]+m_resp[4][4]+m_resp[5][5]+m_resp[6][6]+m_resp[7][7]+m_resp[8][8]:
        pontos += (soma_diag*2)
    return pontos
#A função pontuacao_parcial responsável por exibir a pontuação parcial duantre as jogadas.
def pontuacao_parcial(pont_j1 , jogador1, pont_j2, jogador2):
    print('\nPONTOS PARCIAIS:\n')
    print('*'*40)
    print('O JOGADOR %s, ESTÁ COM %d PONTOS.'% (jogador1.upper(), pont_j1))
    print('-'*40)
    print('O JOGADOR %s, ESTÁ COM %d PONTOS.'% (jogador2.upper(), pont_j2))
    print('*'*40)
#A função exibir_matriz é  responsável organizar a exibição da matriz externa, as somas de cada linha e cada colunas sendo mostrada ao final das mesmas.
def exibir_matriz(base):
    if base == 2:
        print('\n','==='*8,'\n')
        for i in range(2): print('',sc1_resp[i],'| |',sc2_resp[i],'|', sc_soma_pt1[i]) 
        print('-'*20)
        for i in range(2): print('',sc3_resp[i],'| |',sc4_resp[i],'|', sc_soma_pt2[i])
        print('-'*20)
        print(' ',soma_c1, soma_c2,' | | ', soma_c3, soma_c4,' |')
        print('\n','==='*8,'\n')

    elif base == 3:
        print('\n','==='*26,'\n')
        for i in range(3): print('',sc1_resp[i],'| |',sc2_resp[i],'| |',sc3_resp[i],'',sc_soma_pt1[i])
        print('--'*20)
        for i in range(3): print('',sc4_resp[i],'| |',sc5_resp[i],'| |',sc6_resp[i],'',sc_soma_pt2[i])
        print('--'*20)
        for i in range(3): print('',sc7_resp[i],'| |',sc8_resp[i],'| |',sc9_resp[i],'',sc_soma_pt3[i])
        print('--'*20)
        print(' ',soma_c1, soma_c2, soma_c3,' | | ', soma_c4, soma_c5, soma_c6,'| | ',soma_c7, soma_c8, soma_c9, ' ')
        print('\n','==='*26,'\n')
#A função pontuacao_final é responsável por mostrar o placar ao final do jogo.
def pontuacao_final(pont_j1 , jogador1, pont_j2, jogador2):
    time.sleep(1)
    print('\n','=='*20)
    print('   FIM DE JOGO')
    print('\n','=='*20)
    if pont_j1 > pont_j2:
        print('\nPARABÉNS %s, VOCÊ VENCEU O JOGO COM %d PONTOS!'% (jogador1.upper(), pont_j1))
    elif pont_j2 > pont_j1:
        print('\nPARABÉNS %s, VOCÊ VENCEU O JOGO COM %d PONTOS!'% (jogador2.upper(), pont_j2))
    elif pont_j2 == pont_j1:
        print('\n%s E %s VOCÊS EMPATARAM O JOGO!'% (jogador1.upper() ,jogador2.upper()))
    print('\n','=='*20)

#saída do menu inicial, que solicita o nome dos jogador e em seguida apresenta as escolhas para o usuário 
print('''========================================
    BEM-VINDOS AO JOGO DAS SOMAS 2.0
========================================''')
print('\nESCOLHAM SEUS NOMES!')
jogador1 = str(input('\nJOGADOR 1: '))
jogador2 = str(input('\nJOGADOR 2: '))
num_menu = verificar_menu()
print('\nCarregando jogo...\n')
time.sleep(1)

while num_menu != 0:
    pontuacao1 = 0
    #neste primeiro condicional, é processado o nível facil do jogo
    if num_menu == 1:
        #Neste primeiro momento, a variável base é iniciada pois ela determina como as funções serão processadas de acordo com o nível. as variáveis das pontuações dos jogares também são iniciadas.
        base = 2; pont_j1 = 0; pont_j2 = 0; fim = True; cont = 0; pont_ant = 0; pont_dps = 0
        sc1 = [1,2,3,4]; sc2 = [1,2,3,4]; sc3 = [1,2,3,4]; sc4 = [1,2,3,4]; secoes = [1,2,3,4]

        #gerando as seções escondidas, anexando os valores nas 4 seções e iniciando as seções vazias que são exibidas para o usuário.
        secao1 = gerar_secao(base); secao2 = gerar_secao(base); secao3 = gerar_secao(base); secao4 = gerar_secao(base)
        sc1_resp = [[0,0],[0,0]]; sc2_resp = [[0,0],[0,0]]; sc3_resp = [[0,0],[0,0]]; sc4_resp = [[0,0],[0,0]]

        #indexação dos números gerados nas seções(1-4) nas linhas(lx_resp), colunas(cx_resp) e diagonal principal(diag_resp) de modo a serem somados e manipuladas no tabuleiro que é exibido.
        l1_resp = [secao1[0][0],secao1[0][1],secao2[0][0],secao2[0][1]]; l2_resp = [secao1[1][0],secao1[1][1],secao2[1][0],secao2[1][1]]; l3_resp = [secao3[0][0],secao3[0][1],secao4[0][0],secao4[0][1]]; l4_resp = [secao3[1][0],secao3[1][1],secao4[1][0],secao4[1][1]]
        
        c1_resp = [secao1[0][0],secao1[1][0],secao3[0][0],secao3[1][0]]; c2_resp = [secao1[0][1],secao1[1][1],secao3[0][1],secao3[1][1]]; c3_resp = [secao2[0][0],secao2[1][0],secao4[0][0],secao4[1][0]]; c4_resp = [secao2[0][1],secao2[1][1],secao4[0][1],secao4[1][1]]
        
        diag_resp = [secao1[0][0],secao1[1][1],secao4[0][0],secao4[1][1]]

        #realizando a soma dos elementos de cada linha(soma_lx) e coluna(soma_cx) e da diagonal(soma_diag) principal da matriz oculta usando sum
        soma_l1 = sum(l1_resp); soma_l2 = sum(l2_resp); soma_l3 = sum(l3_resp); soma_l4 = sum(l4_resp)
        soma_c1 = sum(c1_resp); soma_c2 = sum(c2_resp); soma_c3 = sum(c3_resp); soma_c4 = sum(c4_resp)
        
        sc_soma_pt1 = [soma_l1,soma_l2]; sc_soma_pt2 = [soma_l3,soma_l4]; soma_diag = sum(diag_resp)

        #indexação dos números preenchidos nas seções do tabuleiro nas linhas(lx_sc), colunas(cx_sc) e diagonal principal(diag_resp) de modo a serem somados e manipuladas no tabuleiro que é exibido.
        l1_sc = [sc1_resp[0][0],sc1_resp[0][1],sc2_resp[0][0],sc2_resp[0][1]];  l2_sc = [sc1_resp[1][0],sc1_resp[1][1],sc2_resp[1][0],sc2_resp[1][1]];  l3_sc = [sc3_resp[0][0],sc3_resp[0][1],sc4_resp[0][0],sc4_resp[0][1]];  l4_sc = [sc3_resp[1][0],sc3_resp[1][1],sc4_resp[1][0],sc4_resp[1][1]]
        
        c1_sc = [sc1_resp[0][0],sc1_resp[1][0],sc3_resp[0][0],sc3_resp[1][0]];  c2_sc = [sc1_resp[0][1],sc1_resp[1][1],sc3_resp[0][1],sc3_resp[1][1]];  c3_sc = [sc2_resp[0][0],sc2_resp[1][0],sc4_resp[0][0],sc4_resp[1][0]];  c4_sc = [sc2_resp[0][1],sc2_resp[1][1],sc4_resp[0][1],sc4_resp[1][1]]
        #definição da matriz resposta final, ela serve para a verifiação das somas a serem indexadas nas pontuações dos jogadores.
        m_resp = [l1_sc, l2_sc, l3_sc, l4_sc]

        print('''===========================
        Nível Fácil
===========================\n''')

        while fim == True:
            #Nas entradas dos jogadores são processadas:
            #A função num_e_secoes recebe as entrada do número e seção escolhidos pelo jogador.
            #A variável pont_jx recebe a pontação para o jogador caso ele complete uma linha e/ou coluna e a diagonal principal
            #A variável cont conta o número de jogadas para poder encerrar o jogo.
            #A função pontuacao_parcial exibe a pontuação parcial dos jogadores
            #Matriz resposta(m_resp) e as linhas e colunas  são atualizadas depois de cada jogada de modo a permitir as somas dos pontos.

#nessa etapa são processadas as funções de acordo com a entrada do jogador1
            print("\nJOGADOR %s, SUA VEZ!\n" % jogador1.upper())
            #num_secao recebe o número verificado da secão que o jogador que escolher
            num_e_secoes()
            exibir_matriz(base)
            pont_dps = sum(l1_sc) + sum(l2_sc) + sum(l3_sc) + sum(l4_sc) + sum(c1_sc) + sum(c2_sc) + sum(c3_sc) + sum(c4_sc)
            if pont_dps > pont_ant: pont_j1 += somas_col_facil() + somas_lin_facil() + somas_diag_facil()
            pont_ant = pont_dps
            cont += 1
            pontuacao_parcial(pont_j1 , jogador1, pont_j2, jogador2)
            m_resp = [l1_sc, l2_sc, l3_sc, l4_sc]
            l1_sc = [sc1_resp[0][0],sc1_resp[0][1],sc2_resp[0][0],sc2_resp[0][1]];  l2_sc = [sc1_resp[1][0],sc1_resp[1][1],sc2_resp[1][0],sc2_resp[1][1]];  l3_sc = [sc3_resp[0][0],sc3_resp[0][1],sc4_resp[0][0],sc4_resp[0][1]];  l4_sc = [sc3_resp[1][0],sc3_resp[1][1],sc4_resp[1][0],sc4_resp[1][1]]
            c1_sc = [sc1_resp[0][0],sc1_resp[1][0],sc3_resp[0][0],sc3_resp[1][0]];  c2_sc = [sc1_resp[0][1],sc1_resp[1][1],sc3_resp[0][1],sc3_resp[1][1]];  c3_sc = [sc2_resp[0][0],sc2_resp[1][0],sc4_resp[0][0],sc4_resp[1][0]];  c4_sc = [sc2_resp[0][1],sc2_resp[1][1],sc4_resp[0][1],sc4_resp[1][1]]

            #nessa etapa são processadas as funções de acordo com a entrada do jogador2
            print("\nJOGADOR %s, SUA VEZ!\n" % jogador2.upper())
            num_e_secoes()
            exibir_matriz(base)
            pont_dps = sum(l1_sc) + sum(l2_sc) + sum(l3_sc) + sum(l4_sc) + sum(c1_sc) + sum(c2_sc) + sum(c3_sc) + sum(c4_sc)
            if pont_dps > pont_ant: pont_j2 += somas_col_facil() + somas_lin_facil() + somas_diag_facil()
            pont_ant = pont_dps
            cont += 1
            pontuacao_parcial(pont_j1 , jogador1, pont_j2, jogador2)
            m_resp = [l1_sc, l2_sc, l3_sc, l4_sc]
            l1_sc = [sc1_resp[0][0],sc1_resp[0][1],sc2_resp[0][0],sc2_resp[0][1]];  l2_sc = [sc1_resp[1][0],sc1_resp[1][1],sc2_resp[1][0],sc2_resp[1][1]];  l3_sc = [sc3_resp[0][0],sc3_resp[0][1],sc4_resp[0][0],sc4_resp[0][1]];  l4_sc = [sc3_resp[1][0],sc3_resp[1][1],sc4_resp[1][0],sc4_resp[1][1]]
            c1_sc = [sc1_resp[0][0],sc1_resp[1][0],sc3_resp[0][0],sc3_resp[1][0]];  c2_sc = [sc1_resp[0][1],sc1_resp[1][1],sc3_resp[0][1],sc3_resp[1][1]];  c3_sc = [sc2_resp[0][0],sc2_resp[1][0],sc4_resp[0][0],sc4_resp[1][0]];  c4_sc = [sc2_resp[0][1],sc2_resp[1][1],sc4_resp[0][1],sc4_resp[1][1]]
            
            if cont == 16:
                fim = False
                pontuacao_final(pont_j1 , jogador1, pont_j2, jogador2)
        #Ao final do jogo, pergunta se os jogadores querem iniciar um novo nivel.
        time.sleep(1)
        num_menu = verificar_menu()

    #neste segundo condicional, é processado o nível dificil do jogo
    elif num_menu == 2:
        #Neste primeiro momento, a variável base é iniciada pois ela determina como as funções serão processadas de acordo com o nível. as variáveis das pontuações dos jogares também são iniciadas.
        base = 3; pont_j1 = 0; pont_j2 = 0; fim = True; cont = 0; pont_ant = 0; pont_dps = 0
        #as secoes scx recebem a seção auxiliar declarada no inicio do código, elas servem para evitar que o usuário escolha, novamente, um número já revelado na seção correspondente
        # e no caso da secoes, serve para não esoclhar uma seção já completada
        sc1 = [1,2,3,4,5,6,7,8,9]; sc2 = [1,2,3,4,5,6,7,8,9]; sc3 = [1,2,3,4,5,6,7,8,9]; sc4 = [1,2,3,4,5,6,7,8,9]; sc5 = [1,2,3,4,5,6,7,8,9]; sc6 = [1,2,3,4,5,6,7,8,9]; sc7 = [1,2,3,4,5,6,7,8,9]; sc8 = [1,2,3,4,5,6,7,8,9]; sc9 = [1,2,3,4,5,6,7,8,9]; secoes = [1,2,3,4,5,6,7,8,9]
        #gerando as seções escondidas, anexando os valores nas 4 seções e iniciando as seções vazias que são exibidas para o usuário
        secao1 = gerar_secao(base); secao2 = gerar_secao(base); secao3 = gerar_secao(base); secao4 = gerar_secao(base); secao5 = gerar_secao(base); secao6 = gerar_secao(base); secao7 = gerar_secao(base); secao8 = gerar_secao(base); secao9 = gerar_secao(base)
        sc1_resp = [[0,0,0],[0,0,0],[0,0,0]]; sc2_resp = [[0,0,0],[0,0,0],[0,0,0]]; sc3_resp = [[0,0,0],[0,0,0],[0,0,0]]; sc4_resp = [[0,0,0],[0,0,0],[0,0,0]]; sc5_resp = [[0,0,0],[0,0,0],[0,0,0]]; sc6_resp = [[0,0,0],[0,0,0],[0,0,0]]; sc7_resp = [[0,0,0],[0,0,0],[0,0,0]]; sc8_resp = [[0,0,0],[0,0,0],[0,0,0]]; sc9_resp = [[0,0,0],[0,0,0],[0,0,0]]

        #indexação dos números gerados nas seções(1-9) nas linhas(lx_resp), colunas(cx_resp) e diagonal principal de modo a serem somadas e manipuladas em um tabuleiro maior.
        l1_resp = [secao1[0][0],secao1[0][1],secao1[0][2],secao2[0][0],secao2[0][1],secao2[0][2],secao3[0][0],secao3[0][1],secao3[0][2]];  l2_resp = [secao1[1][0],secao1[1][1],secao1[1][2],secao2[1][0],secao2[1][1],secao2[1][2],secao3[1][0],secao3[1][1],secao3[1][2]];  l3_resp = [secao1[2][0],secao1[2][1],secao1[2][2],secao2[2][0],secao2[2][1],secao2[2][2],secao3[2][0],secao3[2][1],secao3[2][2]]
        l4_resp = [secao4[0][0],secao4[0][1],secao4[0][2],secao5[0][0],secao5[0][1],secao5[0][2],secao6[0][0],secao6[0][1],secao6[0][2]];  l5_resp = [secao4[1][0],secao4[1][1],secao4[1][2],secao5[1][0],secao5[1][1],secao5[1][2],secao6[1][0],secao6[1][1],secao6[1][2]];  l6_resp = [secao4[2][0],secao4[2][1],secao4[2][2],secao5[2][0],secao5[2][1],secao5[2][2],secao6[2][0],secao6[2][1],secao6[2][2]]
        l7_resp = [secao7[0][0],secao7[0][1],secao7[0][2],secao8[0][0],secao8[0][1],secao8[0][2],secao9[0][0],secao9[0][1],secao9[0][2]];  l8_resp = [secao7[1][0],secao7[1][1],secao7[1][2],secao8[1][0],secao8[1][1],secao8[1][2],secao9[1][0],secao9[1][1],secao9[1][2]];  l9_resp = [secao7[2][0],secao7[2][1],secao7[2][2],secao8[2][0],secao8[2][1],secao8[2][2],secao9[2][0],secao9[2][1],secao9[2][2]]

        c1_resp = [secao1[0][0],secao1[1][0],secao1[2][0],secao4[0][0],secao4[1][0],secao4[2][0],secao7[0][0],secao7[1][0],secao7[2][0]];  c2_resp = [secao1[0][1],secao1[1][1],secao1[2][1],secao4[0][1],secao4[1][1],secao4[2][1],secao7[0][1],secao7[1][1],secao7[2][1]];  c3_resp = [secao1[0][2],secao1[1][2],secao1[2][2],secao4[0][2],secao4[1][2],secao4[2][2],secao7[0][2],secao7[1][2],secao7[2][2]]
        c4_resp = [secao2[0][0],secao2[1][0],secao2[2][0],secao5[0][0],secao5[1][0],secao5[2][0],secao8[0][0],secao8[1][0],secao8[2][0]];  c5_resp = [secao2[0][1],secao2[1][1],secao2[2][1],secao5[0][1],secao5[1][1],secao5[2][1],secao8[0][1],secao8[1][1],secao8[2][1]];  c6_resp = [secao2[0][2],secao2[1][2],secao2[2][2],secao5[0][2],secao5[1][2],secao5[2][2],secao8[0][2],secao8[1][2],secao8[2][2]]
        c7_resp = [secao3[0][0],secao3[1][0],secao3[2][0],secao6[0][0],secao6[1][0],secao6[2][0],secao9[0][0],secao9[1][0],secao9[2][0]];  c8_resp = [secao3[0][1],secao3[1][1],secao3[2][1],secao6[0][1],secao6[1][1],secao6[2][1],secao9[0][1],secao9[1][1],secao9[2][1]];  c9_resp = [secao3[0][2],secao3[1][2],secao3[2][2],secao6[0][2],secao6[1][2],secao6[2][2],secao9[0][2],secao9[1][2],secao9[2][2]]
        
        diag_resp = [secao1[0][0],secao1[1][1],secao1[2][2],secao5[0][0],secao5[1][1],secao5[2][2],secao9[0][0],secao9[1][1],secao9[2][2]]
        
        #realizando a soma dos elementos de cada linha(soma_lx) e coluna(soma_cx) da matriz usando sum
        soma_l1 = sum(l1_resp); soma_l2 = sum(l2_resp); soma_l3 = sum(l3_resp); soma_l4 = sum(l4_resp);soma_l5 = sum(l5_resp);soma_l6 = sum(l6_resp);soma_l7 = sum(l7_resp);soma_l8 = sum(l8_resp);soma_l9 = sum(l9_resp)
        soma_c1 = sum(c1_resp); soma_c2 = sum(c2_resp); soma_c3 = sum(c3_resp); soma_c4 = sum(c4_resp); soma_c5 = sum(c5_resp); soma_c6 = sum(c6_resp); soma_c7 = sum(c7_resp); soma_c8 = sum(c8_resp); soma_c9 = sum(c9_resp)

        sc_soma_pt1 = [soma_l1,soma_l2, soma_l3]; sc_soma_pt2 = [soma_l4,soma_l5,soma_l6]; sc_soma_pt3 = [soma_l7,soma_l8,soma_l9];soma_diag = sum(diag_resp)

        #indexando os números nas linhas(lx-sc) e nas colunas(cx_sc)
        l1_sc = [sc1_resp[0][0],sc1_resp[0][1],sc1_resp[0][2],sc2_resp[0][0],sc2_resp[0][1],sc2_resp[0][2],sc3_resp[0][0],sc3_resp[0][1],sc3_resp[0][2]];  l2_sc = [sc1_resp[1][0],sc1_resp[1][1],sc1_resp[1][2],sc2_resp[1][0],sc2_resp[1][1],sc2_resp[1][2],sc3_resp[1][0],sc3_resp[1][1],sc3_resp[1][2]];  l3_sc = [sc1_resp[2][0],sc1_resp[2][1],sc1_resp[2][2],sc2_resp[2][0],sc2_resp[2][1],sc2_resp[2][2],sc3_resp[2][0],sc3_resp[2][1],sc3_resp[2][2]]
        l4_sc = [sc4_resp[0][0],sc4_resp[0][1],sc4_resp[0][2],sc5_resp[0][0],sc5_resp[0][1],sc5_resp[0][2],sc6_resp[0][0],sc6_resp[0][1],sc6_resp[0][2]];  l5_sc = [sc4_resp[1][0],sc4_resp[1][1],sc4_resp[1][2],sc5_resp[1][0],sc5_resp[1][1],sc5_resp[1][2],sc6_resp[1][0],sc6_resp[1][1],sc6_resp[1][2]];  l6_sc = [sc4_resp[2][0],sc4_resp[2][1],sc4_resp[2][2],sc5_resp[2][0],sc5_resp[2][1],sc5_resp[2][2],sc6_resp[2][0],sc6_resp[2][1],sc6_resp[2][2]]
        l7_sc = [sc7_resp[0][0],sc7_resp[0][1],sc7_resp[0][2],sc8_resp[0][0],sc8_resp[0][1],sc8_resp[0][2],sc9_resp[0][0],sc9_resp[0][1],sc9_resp[0][2]];  l8_sc = [sc7_resp[1][0],sc7_resp[1][1],sc7_resp[1][2],sc8_resp[1][0],sc8_resp[1][1],sc8_resp[1][2],sc9_resp[1][0],sc9_resp[1][1],sc9_resp[1][2]];  l9_sc = [sc7_resp[2][0],sc7_resp[2][1],sc7_resp[2][2],sc8_resp[2][0],sc8_resp[2][1],sc8_resp[2][2],sc9_resp[2][0],sc9_resp[2][1],sc9_resp[2][2]]

        c1_sc = [sc1_resp[0][0],sc1_resp[1][0],sc1_resp[2][0],sc4_resp[0][0],sc4_resp[1][0],sc4_resp[2][0],sc7_resp[0][0],sc7_resp[1][0],sc7_resp[2][0]];  c2_sc = [sc1_resp[0][1],sc1_resp[1][1],sc1_resp[2][1],sc4_resp[0][1],sc4_resp[1][1],sc4_resp[2][1],sc7_resp[0][1],sc7_resp[1][1],sc7_resp[2][1]];  c3_sc = [sc1_resp[0][2],sc1_resp[1][2],sc1_resp[2][2],sc4_resp[0][2],sc4_resp[1][2],sc4_resp[2][2],sc7_resp[0][2],sc7_resp[1][2],sc7_resp[2][2]]
        c4_sc = [sc2_resp[0][0],sc2_resp[1][0],sc2_resp[2][0],sc5_resp[0][0],sc5_resp[1][0],sc5_resp[2][0],sc8_resp[0][0],sc8_resp[1][0],sc8_resp[2][0]];  c5_sc = [sc2_resp[0][1],sc2_resp[1][1],sc2_resp[2][1],sc5_resp[0][1],sc5_resp[1][1],sc5_resp[2][1],sc8_resp[0][1],sc8_resp[1][1],sc8_resp[2][1]];  c6_sc = [sc2_resp[0][2],sc2_resp[1][2],sc2_resp[2][2],sc5_resp[0][2],sc5_resp[1][2],sc5_resp[2][2],sc8_resp[0][2],sc8_resp[1][2],sc8_resp[2][2]]
        c7_sc = [sc3_resp[0][0],sc3_resp[1][0],sc3_resp[2][0],sc6_resp[0][0],sc6_resp[1][0],sc6_resp[2][0],sc9_resp[0][0],sc9_resp[1][0],sc9_resp[2][0]];  c8_sc = [sc3_resp[0][1],sc3_resp[1][1],sc3_resp[2][1],sc6_resp[0][1],sc6_resp[1][1],sc6_resp[2][1],sc9_resp[0][1],sc9_resp[1][1],sc9_resp[2][1]];  c9_sc = [sc3_resp[0][2],sc3_resp[1][2],sc3_resp[2][2],sc6_resp[0][2],sc6_resp[1][2],sc6_resp[2][2],sc9_resp[0][2],sc9_resp[1][2],sc9_resp[2][2]]
        #definição da matriz resposta final, ela serve para a verifiação das somas a serem indexadas nas pontuações dos jogadores.
        m_resp = [l1_sc, l2_sc, l3_sc, l4_sc, l5_sc, l6_sc, l7_sc, l8_sc, l9_sc]

        print('''=============================
        Nível Dificil
=============================\n''')

        while fim == True:

            #Nas entradas dos jogadores são processadas:
            #A m_resp ( matriz resposta) é atualizada depois de cada jogada de modo a permitir as somas dos pontos, 
            #A função num_e_secoes recebe as entrada do número e seção escolhidos pelo jogador.
            #A variável pont_jx recebe a pontação para o jogador caso ele complete uma linha e/ou coluna e a diagonal principal
            #A variável cont conta o número de jogadas para poder encerrar o jogo.
            #A função pontuacao_parcial exibe a pontuação parcial dos jogadores
            #Matriz resposta(m_resp) e as linhas e colunas  são atualizadas depois de cada jogada de modo a permitir as somas dos pontos.

            #nessa etapa são processadas as funções de acordo com a entrada do jogador1
            print("\nJOGADOR %s, SUA VEZ!\n" % jogador1.upper())
            #num_secao recebe o número verificado da secão que o jogador que escolher
            num_e_secoes()
            exibir_matriz(base)
            pont_dps = sum(l1_sc) + sum(l2_sc) + sum(l3_sc) + sum(l4_sc) + sum(l5_sc) + sum(l6_sc) + sum(l7_sc) + sum(l8_sc) + sum(l9_sc) + sum(c1_sc) + sum(c2_sc) + sum(c3_sc) + sum(c4_sc) + sum(c5_sc) + sum(c6_sc)+ sum(c7_sc)+ sum(c8_sc) + sum(c9_sc)
            if pont_dps > pont_ant: pont_j1 += somas_col_facil() + somas_lin_facil() + somas_diag_dif()
            pont_ant = pont_dps
            cont += 1
            pontuacao_parcial(pont_j1 , jogador1, pont_j2, jogador2)
            m_resp = [l1_sc, l2_sc, l3_sc, l4_sc, l5_sc, l6_sc, l7_sc, l8_sc, l9_sc]

            l1_sc = [sc1_resp[0][0],sc1_resp[0][1],sc1_resp[0][2],sc2_resp[0][0],sc2_resp[0][1],sc2_resp[0][2],sc3_resp[0][0],sc3_resp[0][1],sc3_resp[0][2]];  l2_sc = [sc1_resp[1][0],sc1_resp[1][1],sc1_resp[1][2],sc2_resp[1][0],sc2_resp[1][1],sc2_resp[1][2],sc3_resp[1][0],sc3_resp[1][1],sc3_resp[1][2]];  l3_sc = [sc1_resp[2][0],sc1_resp[2][1],sc1_resp[2][2],sc2_resp[2][0],sc2_resp[2][1],sc2_resp[2][2],sc3_resp[2][0],sc3_resp[2][1],sc3_resp[2][2]]
            l4_sc = [sc4_resp[0][0],sc4_resp[0][1],sc4_resp[0][2],sc5_resp[0][0],sc5_resp[0][1],sc5_resp[0][2],sc6_resp[0][0],sc6_resp[0][1],sc6_resp[0][2]];  l5_sc = [sc4_resp[1][0],sc4_resp[1][1],sc4_resp[1][2],sc5_resp[1][0],sc5_resp[1][1],sc5_resp[1][2],sc6_resp[1][0],sc6_resp[1][1],sc6_resp[1][2]];  l6_sc = [sc4_resp[2][0],sc4_resp[2][1],sc4_resp[2][2],sc5_resp[2][0],sc5_resp[2][1],sc5_resp[2][2],sc6_resp[2][0],sc6_resp[2][1],sc6_resp[2][2]]
            l7_sc = [sc7_resp[0][0],sc7_resp[0][1],sc7_resp[0][2],sc8_resp[0][0],sc8_resp[0][1],sc8_resp[0][2],sc9_resp[0][0],sc9_resp[0][1],sc9_resp[0][2]];  l8_sc = [sc7_resp[1][0],sc7_resp[1][1],sc7_resp[1][2],sc8_resp[1][0],sc8_resp[1][1],sc8_resp[1][2],sc9_resp[1][0],sc9_resp[1][1],sc9_resp[1][2]];  l9_sc = [sc7_resp[2][0],sc7_resp[2][1],sc7_resp[2][2],sc8_resp[2][0],sc8_resp[2][1],sc8_resp[2][2],sc9_resp[2][0],sc9_resp[2][1],sc9_resp[2][2]]

            c1_sc = [sc1_resp[0][0],sc1_resp[1][0],sc1_resp[2][0],sc4_resp[0][0],sc4_resp[1][0],sc4_resp[2][0],sc7_resp[0][0],sc7_resp[1][0],sc7_resp[2][0]];  c2_sc = [sc1_resp[0][1],sc1_resp[1][1],sc1_resp[2][1],sc4_resp[0][1],sc4_resp[1][1],sc4_resp[2][1],sc7_resp[0][1],sc7_resp[1][1],sc7_resp[2][1]];  c3_sc = [sc1_resp[0][2],sc1_resp[1][2],sc1_resp[2][2],sc4_resp[0][2],sc4_resp[1][2],sc4_resp[2][2],sc7_resp[0][2],sc7_resp[1][2],sc7_resp[2][2]]
            c4_sc = [sc2_resp[0][0],sc2_resp[1][0],sc2_resp[2][0],sc5_resp[0][0],sc5_resp[1][0],sc5_resp[2][0],sc8_resp[0][0],sc8_resp[1][0],sc8_resp[2][0]];  c5_sc = [sc2_resp[0][1],sc2_resp[1][1],sc2_resp[2][1],sc5_resp[0][1],sc5_resp[1][1],sc5_resp[2][1],sc8_resp[0][1],sc8_resp[1][1],sc8_resp[2][1]];  c6_sc = [sc2_resp[0][2],sc2_resp[1][2],sc2_resp[2][2],sc5_resp[0][2],sc5_resp[1][2],sc5_resp[2][2],sc8_resp[0][2],sc8_resp[1][2],sc8_resp[2][2]]
            c7_sc = [sc3_resp[0][0],sc3_resp[1][0],sc3_resp[2][0],sc6_resp[0][0],sc6_resp[1][0],sc6_resp[2][0],sc9_resp[0][0],sc9_resp[1][0],sc9_resp[2][0]];  c8_sc = [sc3_resp[0][1],sc3_resp[1][1],sc3_resp[2][1],sc6_resp[0][1],sc6_resp[1][1],sc6_resp[2][1],sc9_resp[0][1],sc9_resp[1][1],sc9_resp[2][1]];  c9_sc = [sc3_resp[0][2],sc3_resp[1][2],sc3_resp[2][2],sc6_resp[0][2],sc6_resp[1][2],sc6_resp[2][2],sc9_resp[0][2],sc9_resp[1][2],sc9_resp[2][2]]

            if cont == 81:
                fim = False
                pontuacao_final(pont_j1 , jogador1, pont_j2, jogador2)

            #nessa etapa são processadas as funções de acordo com a entrada do jogador2
            print("\nJOGADOR %s, SUA VEZ!" % jogador2.upper())
            num_e_secoes()
            exibir_matriz(base)
            pont_dps = sum(l1_sc) + sum(l2_sc) + sum(l3_sc) + sum(l4_sc) + sum(l5_sc) + sum(l6_sc) + sum(l7_sc) + sum(l8_sc) + sum(l9_sc) + sum(c1_sc) + sum(c2_sc) + sum(c3_sc) + sum(c4_sc) + sum(c5_sc) + sum(c6_sc)+ sum(c7_sc)+ sum(c8_sc) + sum(c9_sc)
            if pont_dps > pont_ant: pont_j2 += somas_col_facil() + somas_lin_facil() + somas_diag_dif()
            pont_ant = pont_dps
            cont += 1
            pontuacao_parcial(pont_j1 , jogador1, pont_j2, jogador2)
            m_resp = [l1_sc, l2_sc, l3_sc, l4_sc, l5_sc, l6_sc, l7_sc, l8_sc, l9_sc]

            l1_sc = [sc1_resp[0][0],sc1_resp[0][1],sc1_resp[0][2],sc2_resp[0][0],sc2_resp[0][1],sc2_resp[0][2],sc3_resp[0][0],sc3_resp[0][1],sc3_resp[0][2]];  l2_sc = [sc1_resp[1][0],sc1_resp[1][1],sc1_resp[1][2],sc2_resp[1][0],sc2_resp[1][1],sc2_resp[1][2],sc3_resp[1][0],sc3_resp[1][1],sc3_resp[1][2]];  l3_sc = [sc1_resp[2][0],sc1_resp[2][1],sc1_resp[2][2],sc2_resp[2][0],sc2_resp[2][1],sc2_resp[2][2],sc3_resp[2][0],sc3_resp[2][1],sc3_resp[2][2]]
            l4_sc = [sc4_resp[0][0],sc4_resp[0][1],sc4_resp[0][2],sc5_resp[0][0],sc5_resp[0][1],sc5_resp[0][2],sc6_resp[0][0],sc6_resp[0][1],sc6_resp[0][2]];  l5_sc = [sc4_resp[1][0],sc4_resp[1][1],sc4_resp[1][2],sc5_resp[1][0],sc5_resp[1][1],sc5_resp[1][2],sc6_resp[1][0],sc6_resp[1][1],sc6_resp[1][2]];  l6_sc = [sc4_resp[2][0],sc4_resp[2][1],sc4_resp[2][2],sc5_resp[2][0],sc5_resp[2][1],sc5_resp[2][2],sc6_resp[2][0],sc6_resp[2][1],sc6_resp[2][2]]
            l7_sc = [sc7_resp[0][0],sc7_resp[0][1],sc7_resp[0][2],sc8_resp[0][0],sc8_resp[0][1],sc8_resp[0][2],sc9_resp[0][0],sc9_resp[0][1],sc9_resp[0][2]];  l8_sc = [sc7_resp[1][0],sc7_resp[1][1],sc7_resp[1][2],sc8_resp[1][0],sc8_resp[1][1],sc8_resp[1][2],sc9_resp[1][0],sc9_resp[1][1],sc9_resp[1][2]];  l9_sc = [sc7_resp[2][0],sc7_resp[2][1],sc7_resp[2][2],sc8_resp[2][0],sc8_resp[2][1],sc8_resp[2][2],sc9_resp[2][0],sc9_resp[2][1],sc9_resp[2][2]]

            c1_sc = [sc1_resp[0][0],sc1_resp[1][0],sc1_resp[2][0],sc4_resp[0][0],sc4_resp[1][0],sc4_resp[2][0],sc7_resp[0][0],sc7_resp[1][0],sc7_resp[2][0]];  c2_sc = [sc1_resp[0][1],sc1_resp[1][1],sc1_resp[2][1],sc4_resp[0][1],sc4_resp[1][1],sc4_resp[2][1],sc7_resp[0][1],sc7_resp[1][1],sc7_resp[2][1]];  c3_sc = [sc1_resp[0][2],sc1_resp[1][2],sc1_resp[2][2],sc4_resp[0][2],sc4_resp[1][2],sc4_resp[2][2],sc7_resp[0][2],sc7_resp[1][2],sc7_resp[2][2]]
            c4_sc = [sc2_resp[0][0],sc2_resp[1][0],sc2_resp[2][0],sc5_resp[0][0],sc5_resp[1][0],sc5_resp[2][0],sc8_resp[0][0],sc8_resp[1][0],sc8_resp[2][0]];  c5_sc = [sc2_resp[0][1],sc2_resp[1][1],sc2_resp[2][1],sc5_resp[0][1],sc5_resp[1][1],sc5_resp[2][1],sc8_resp[0][1],sc8_resp[1][1],sc8_resp[2][1]];  c6_sc = [sc2_resp[0][2],sc2_resp[1][2],sc2_resp[2][2],sc5_resp[0][2],sc5_resp[1][2],sc5_resp[2][2],sc8_resp[0][2],sc8_resp[1][2],sc8_resp[2][2]]
            c7_sc = [sc3_resp[0][0],sc3_resp[1][0],sc3_resp[2][0],sc6_resp[0][0],sc6_resp[1][0],sc6_resp[2][0],sc9_resp[0][0],sc9_resp[1][0],sc9_resp[2][0]];  c8_sc = [sc3_resp[0][1],sc3_resp[1][1],sc3_resp[2][1],sc6_resp[0][1],sc6_resp[1][1],sc6_resp[2][1],sc9_resp[0][1],sc9_resp[1][1],sc9_resp[2][1]];  c9_sc = [sc3_resp[0][2],sc3_resp[1][2],sc3_resp[2][2],sc6_resp[0][2],sc6_resp[1][2],sc6_resp[2][2],sc9_resp[0][2],sc9_resp[1][2],sc9_resp[2][2]]

        #Ao final do jogo, pergunta se os jogadores querem iniciar um novo nivel.
        time.sleep(1)
        num_menu = verificar_menu()

# Mensagem de encerramento do jogo
time.sleep(1)
print('==='*26)
print('\n  OBRIGADO POR JOGAREM O JOGO DAS SOMAS 2.0, ESPERO QUE TENHAM SE DIVERTIDO!\n')
print('==='*26)
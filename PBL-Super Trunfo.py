#/*******************************************************************************
#Autor: Gabriel da Silva Barreto
#Componente Curricular: MI - Algoritmos
#Concluido em: 15/11/2019
#Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
#trecho de código de outro colega ou de outro autor, tais como provindos de livros e
#apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
#de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
#do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
#******************************************************************************************/

#OBSERVAÇÃO IMPORTANTE: Para evitar qualquer problema, esse é o arquivo sem cores e sem emojis.
#Caso o primeiro arquivo não funcione corretamente, por favor ultilizar este para os fins de avaliação.
#Desde já, agradeço a compreenção.

from terminaltables import AsciiTable
import random
import getpass
import os
import time
import sys

primary_player = 0
second_player = 1

jogadores = [] #lista que irá ser manipulada para obter as informações dos jogadores
cartas = [  #lista contendo as informações das cartas que irão ser manipuladas durante o jogo
    {'id': 0, 'nome': 'Ghast', 'atributo': [1, 1, 1], 'tipo': 'Monstros', 'peso': 0},
    {'id': 1, 'nome': 'Creeper', 'atributo': [1, 1, 1], 'tipo': 'Monstros', 'peso': 0},
    {'id': 2, 'nome': 'Vaca', 'atributo': [1, 1, 1], 'tipo': 'Animais', 'peso': 0},
    {'id': 3, 'nome': 'Cavalo', 'atributo': [1, 1, 1], 'tipo': 'Animais', 'peso': 0},
    {'id': 4, 'nome': 'Steve', 'atributo': [1, 1, 1], 'tipo': 'Pessoas', 'peso': 0},
    {'id': 5, 'nome': 'Villanger', 'atributo': [1, 1, 1], 'tipo': 'Pessoas', 'peso': 0},
    {'id': 6, 'nome': 'Zombie', 'atributo': [1, 1, 1], 'tipo': 'Monstros', 'peso': 0},
    {'id': 7, 'nome': 'Slime', 'atributo': [1, 1, 1], 'tipo': 'Monstros', 'peso': 0},
    {'id': 8, 'nome': 'Porco', 'atributo': [1, 1, 1], 'tipo': 'Animais', 'peso': 0},
    {'id': 9, 'nome': 'Galinha', 'atributo': [1, 1, 1], 'tipo': 'Animais', 'peso': 0},
    {'id': 10, 'nome': 'Alex', 'atributo': [1, 1, 1], 'tipo': 'Pessoas', 'peso': 0},
    {'id': 11, 'nome': 'Herobrine', 'atributo': [1, 1, 1], 'tipo': 'Pessoas', 'peso': 0}
]

# Funções do jogo:

def select_player():  # Função para selectionar o nick do jogador
    """
    Pede o nickname e a senha de cada jogador, atribuindo as informações em suas respectivas variáveis.
    :return: jogadores[]
    """
    global jogador1, jogador2
    jogador1 = str(input('Qual será o NICK do jogador 1? '))
    senha1 = getpass.getpass('Qual será o SENHA do jogador 1? ')
    jogador2 = str(input('Qual será o NICK do jogador 2? '))
    senha2 = getpass.getpass('Qual será o SENHA do jogador 2? ')
    if jogador1 == jogador2:
        print('Os nomes dos jogadores não podem ser iguais!')
        return select_player()
    jogadores.append(
        {'id': 0, 'nome': jogador1, 'senha': senha1, 'pontuacao': 0, 'cartas': [1, 2, 3], 'carta_selecionada': 0,
         'atributo_selecionado': 0})
    jogadores.append(
        {'id': 1, 'nome': jogador2, 'senha': senha2, 'pontuacao': 0, 'cartas': [1, 2, 3], 'carta_selecionada': 0,
         'atributo_selecionado': 0})


def select_rodadas(): #Função que define o número de rodadas que terá o jogo
    """
    Pergunta ao usuário quantas rodadas ele quer que o jogo tenha, fazendo o minimo de rodadas ser 3.
    :return: round_game.
    """
    global round_game
    try:
        round_game = int(input('Quantas rodadas você quer jogar? '))
        if round_game < 3:
            print('O número minímo de rodadas é 3, números de rodadas menores do que 3 são redefinidos para 3!')
            time.sleep(6)
            round_game = 3
    except:
        print('Você digitou uma opção inválida. Tente novamente')
        return select_rodadas()


def clear_terminal(): #Função que limpa a tela
    """
    Função para limpar a tela e fazer com que os jogadores vejam apenas suas próprias cartas.
    :return: True.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def sort_card(jogador_id): #Função que sorteia as cartas
    """
    Sorteia a carta para o jogador sem repeti-las.
    :return: jogadores[]
    """
    card_id = []
    while len(card_id) != 3:
        cartinha = random.randint(0, 11)
        if cartinha not in card_id:
            card_id.append(cartinha)
    jogadores[jogador_id]['cartas'] = card_id


def input_senha(jogador_id): #Função que pede a senha dos jogadores
    """
    Pede a senha para cada jogador.
    :para jogador_id: Pede para o jogador com o respectivo id a ser ultilizado no momento para que digite sua senha.
    :return: True ou False, onde True faz o jogo continuar e False mostra uma mensagem de erro e retorna input_senha.
    """
    senha = getpass.getpass('Vez de {} Digite sua senha'.format(jogadores[jogador_id]['nome']))
    if senha == jogadores[jogador_id]['senha']:
        clear_terminal()
        return True
    else:
        print('A senha está errada, digite novamente.')
        return input_senha(jogador_id)


def cards_player(jogador_id): #Função que mostra as cartas dos jogadores
    """
    Tabela que mostra as cartas dos jogadores.
    :param jogador_id: Recebe a informação de qual jogador está jogando e mostra as cartas do jogador com o respectivo id.
    :return: True
    """
    cards_ids = jogadores[jogador_id]['cartas']
    card_one = cartas[cards_ids[0]]
    card_two = cartas[cards_ids[1]]
    card_three = cartas[cards_ids[2]]
    table_data = [
        ['Nº#', 'Nome do jogador', 'Nome da carta:', 'Atributo:', 'Tipo:'],
        [str(card_one['id']), jogadores[jogador_id]['nome'], card_one['nome'],
         'Ataque {} | Defesa {} | Vida {}'.format(card_one['atributo'][0], card_one['atributo'][1],
                                                  card_one['atributo'][2]), card_one['tipo']],
        [str(card_two['id']), jogadores[jogador_id]['nome'], card_two['nome'],
         'Ataque {} | Defesa {} | Vida {}'.format(card_two['atributo'][0], card_two['atributo'][1],
                                                  card_two['atributo'][2]), card_two['tipo']],
        [str(card_three['id']), jogadores[jogador_id]['nome'], card_three['nome'],
         'Ataque {} | Defesa {} | Vida {}'.format(card_three['atributo'][0], card_three['atributo'][1],
                                                  card_three['atributo'][2]), card_three['tipo']]
    ]
    table = AsciiTable(table_data)
    print(table.table)


def rand_atributes(): #Função para sortear os atributos de cada carta
    """
    Sorteia os atributos de cada carta e adiciona à váriavel "atributo" na lista "cartas".
    :return: cartas[]
    """
    for i in range(0, 12):
        carta_1 = random.randint(1, 10)
        carta_2 = random.randint(1, 10)
        carta_3 = random.randint(1, 10)
        if carta_1 == carta_2 or carta_1 == carta_3 or carta_2 == carta_3:
            return rand_atributes()
        atributos = [carta_1, carta_2, carta_3]
        cartas[i]['atributo'] = atributos


def rand_peso(): #Função que sorteia o peso de cada tipo de carta
    """
    Sorteia o peso que cada tipo de carta terá, esse peso é um valor numérico que multiplica todos os atributos das
    cartas.
    :return:cartas[]
    """
    animais = random.randint(1, 5)
    monstros = random.randint(1, 5)
    pessoas = random.randint(1, 5)
    for i in range(0, 12):
        if list(cartas[i]['atributo']):
            list(cartas[i]['atributo']).clear()
        if cartas[i]['tipo'] == 'Animais':
            cartas[i]['peso'] = animais
            cartas[i]['atributo'][0] *= cartas[i]['peso']
            cartas[i]['atributo'][1] *= cartas[i]['peso']
            cartas[i]['atributo'][2] *= cartas[i]['peso']
        if cartas[i]['tipo'] == 'Monstros':
            cartas[i]['peso'] = monstros
            cartas[i]['atributo'][0] *= cartas[i]['peso']
            cartas[i]['atributo'][1] *= cartas[i]['peso']
            cartas[i]['atributo'][2] *= cartas[i]['peso']
        if cartas[i]['tipo'] == 'Pessoas':
            cartas[i]['peso'] = pessoas
            cartas[i]['atributo'][0] *= cartas[i]['peso']
            cartas[i]['atributo'][1] *= cartas[i]['peso']
            cartas[i]['atributo'][2] *= cartas[i]['peso']


def select_card(jogador_id): #Função que determina a escolha de carta dos jogadores
    """
    Pede ao jogador que escolha uma das cartas que ele tenha.
    :param jogador_id: recebe a informação de qual jogador está escolhendo as cartas.
    :return: select_valor, cards_have.
    """
    try:
        select_valor = int(input('Selecione a carta que você quer: Nº#'))
        cards_have = jogadores[jogador_id]['cartas']
        if select_valor not in cards_have:
            print('Escolha uma carta que você tem!')
            return select_card(jogador_id)
        jogadores[jogador_id]['carta_selecionada'] = select_valor
    except:
        print('Selecione apenas numeros!')
        return select_card(jogador_id)


def select_atribute(primary_player, second_player): #Função que determina o atributo selecionado por cada jogador
    """
    Pede ao jogador 1 que escolha o atributo que usará para competir.
    :param primary_player: jogador que escolhe o atributo.
    :param second_player: jogador que não escolhe o atributo.
    :return: 'ataque', 'defesa', 'vida'.
    """
    global select_valor
    select_valor = input('Digite o nome do atributo que você quer: ')
    if (select_valor.lower() == 'ataque'):
        jogadores[primary_player]['atributo_selecionado'] = 'ataque'
        print('O atributo selecionado foi: Ataque')
        jogadores[second_player]['atributo_selecionado'] = 'ataque'
        print('Alternando jogador...')
        time.sleep(5)
    elif (select_valor.lower() == 'defesa'):
        jogadores[primary_player]['atributo_selecionado'] = 'defesa'
        print('O atributo selecionado foi: Defesa')
        jogadores[second_player]['atributo_selecionado'] = 'defesa'
        print('Alternando jogador...')
        time.sleep(5)
    elif (select_valor.lower() == 'vida'):
        jogadores[primary_player]['atributo_selecionado'] = 'vida'
        print('O atributo selecionado foi: Vida')
        jogadores[second_player]['atributo_selecionado'] = 'vida'
        print('Alternando jogador...')
        time.sleep(5)
    else:
        print('Digite corretamente o nome de um atributo que você tem!')
        return select_atribute(primary_player, second_player)


def record(): #Função que salva o recorde do jogador com a maior pontuação
    """
    Atribui a maior pontuação feita no jogo e o nickname de quem a fez à lista recordes.
    :return: recordes
    """
    global recordes
    recordes = ['Não há recorde no momento', 0]
    primary_point = jogadores[primary_player]['pontuacao']
    second_point = jogadores[second_player]['pontuacao']
    if recordes[1] > primary_point and recordes[1] > second_point:
        return True
    else:
        if primary_point > second_point:
            recordes = [jogadores[primary_player]['nome']]
            recordes.append(jogadores[primary_player]['pontuacao'])
        elif second_point > primary_point:
            recordes = [jogadores[second_player]['nome']]
            recordes.append(jogadores[second_player]['pontuacao'])


def add_points(jogador_id, points): #Função que adiciona os pontos a cada jogador
    """
    Adiciona os pontos ao jogador que venceu a rodada.
    :param jogador_id: jogador que está recebendo os pontos.
    :param points: pontos atribuidos ao jogador que venceu a rodada.
    :return: jogadores[]
    """
    print('Adicionado ' + str(points) + ' ponto(s) ao ' + jogadores[jogador_id]['nome'] + '!')
    jogadores[jogador_id]['pontuacao'] += points


def victory(primary_player, second_player): #Função que determina o vencedor da rodada
    """
    Faz a comparação dos atributos e determina o jogador que venceu a rodada
    :param primary_player: jogador que seleciona o atributo
    :param second_player: jogador que não seleciona o atributo
    :return: add_points()
    """
    primary_select_card = jogadores[primary_player]['carta_selecionada']
    primary_select_atribute = jogadores[primary_player]['atributo_selecionado']
    second_select_card = jogadores[second_player]['carta_selecionada']
    if primary_select_atribute == 'ataque':
        primary_atribute_cards = cartas[primary_select_card]['atributo'][0]
        second_atribute_cards = cartas[second_select_card]['atributo'][0]
        if primary_atribute_cards > second_atribute_cards:
            add_points(primary_player, 1)
            print('{} ganhou!'.format(jogadores[primary_player]['nome']))
        elif primary_atribute_cards == second_atribute_cards:
            add_points(primary_player, 0.5)
            add_points(second_player, 0.5)
            print('Empatou')
        else:
            add_points(second_player, 1)
            print('{} ganhou!'.format(jogadores[second_player]['nome']))
    if primary_select_atribute == 'defesa':
        primary_atribute_cards = cartas[primary_select_card]['atributo'][1]
        second_atribute_cards = cartas[second_select_card]['atributo'][1]
        if primary_atribute_cards > second_atribute_cards:
            add_points(primary_player, 1)
            print('{} ganhou!'.format(jogadores[primary_player]['nome']))
        elif primary_atribute_cards == second_atribute_cards:
            add_points(primary_player, 0.5)
            add_points(second_player, 0.5)
            print('Empatou!')
        else:
            add_points(second_player, 1)
            print('{} ganhou!'.format(jogadores[second_player]['nome']))
    if primary_select_atribute == 'vida':
        primary_atribute_cards = cartas[primary_select_card]['atributo'][2]
        second_atribute_cards = cartas[second_select_card]['atributo'][2]
        if primary_atribute_cards > second_atribute_cards:
            add_points(primary_player, 1)
            print('{} ganhou!'.format(jogadores[primary_player]['nome']))
        elif primary_atribute_cards == second_atribute_cards:
            add_points(primary_player, 0.5)
            add_points(second_player, 0.5)
            print('Empatou!')
        else:
            add_points(second_player, 1)
            print('{} ganhou!'.format(jogadores[second_player]['nome']))
    time.sleep(5)


def alternate_round(primary_player, second_player): #Função encarregada de fazer a alternancia das rodadas
    """
    Alterna a rodada para que cada jogador tenha sua vez de jogar
    :param primary_player: primeiro jogador
    :param second_player: segundo jogador
    :return: victory()
    """
    round_player = 0
    print(round_game)
    for p in range(0, round_game):
        if round_player == 0:
            round_player += 1
            clear_terminal()
            print('Partida: #', p + 1)
            input_senha(primary_player)
            print('Partida: #', p + 1)
            rand_peso()
            rand_atributes()
            cards_player(primary_player)
            select_card(primary_player)
            select_atribute(primary_player, second_player)
            sort_card(primary_player)
        if round_player == 1:
            round_player -= 1
            clear_terminal()
            print('Partida: #', p + 1)
            input_senha(second_player)
            print('Partida: #', p + 1)
            if select_valor == 'ataque':
                print('O atributo selecionado foi: Ataque')
            elif select_valor == 'defesa':
                print('O atributo selecionado foi: Defesa')
            elif select_valor == 'vida':
                print('O atributo selecionado foi: Vida')
            rand_peso()
            rand_atributes()
            cards_player(second_player)
            select_card(second_player)
            sort_card(second_player)
            victory(primary_player, second_player)


def start(): #Função de inicio do jogo
    """
    Sorteia quem vai ser o primeiro e segundo jogador e inicia o jogo
    :return: alternate_round()
    """
    print('O novo SUPER TRUNFO versão MINECRAFT irá começar!')
    print('Iniciando jogo em 3 segundos...')
    time.sleep(3)
    primary_player = random.randint(0, 1)
    second_player = 0
    if primary_player == 0:
        second_player = 1
    elif primary_player == 1:
        second_player = 0
    sort_card(primary_player)
    sort_card(second_player)
    alternate_round(primary_player, second_player)


def new_start(): #Função que mostra um novo menu ao final do jogo
    """
    Mostra um pequeno menu ao final do jogo, com a opção de voltar ao menu principal ou sair do jogo
    :return: iniciando()
    """
    try:
        clear_terminal()
        novo_inicio = int(input(
            'Deseja iniciar uma nova jogo?\n[1] para voltar ao menu.\n[2] para sair do jogo.\nQual opção deseja escolher? '))
        if novo_inicio == 1:
            iniciando()
        elif novo_inicio == 2:
            print('')
    except:
        print('Você não escolheu uma opção válida, tente novamente!')
        return new_start()


def recordes_menu(): #Função para mostrar o recorde do jogador com maior pontuação
    """
    Mostra o recorde atual do jogo
    :return: recordes[]
    """
    record()
    if not recordes[1]:
        print('Não há recorde no momento!')
    else:
        print('O recorde é:')
        print('\nJogador: ' + recordes[0] + '\nPontuação: ' + str(recordes[1]) + '\n')
    print('Voltando ao menu em 5 segundos...')
    time.sleep(5)
    return iniciando()


def winner(): #Função que determina o vencedor do jogo
    """
    Compara a pontuação dos dois jogadores e determina quem venceu o jogo.
    :return: True
    """
    if jogadores[primary_player]['pontuacao'] > jogadores[second_player]['pontuacao']:
        print('{} venceu o jogo!'.format(jogadores[primary_player]['nome']))
    elif jogadores[primary_player]['pontuacao'] < jogadores[second_player]['pontuacao']:
        print('{} venceu o jogo!'.format(jogadores[second_player]['nome']))
    else:
        print('O jogo empatou!')


def iniciando(): #Função princinpal que inicia e administra as outras funções do jogo
    """
    Inicia todo o jogo e faz todas as funções funcionarem em sincronia e ordem.
    :return: True
    """
    global inicio
    try:
        clear_terminal()
        inicio = int(input(
            '[1] Para iniciar.\n[2] Para abrir os recordes.\n[3] Para sair do jogo.\nQual opção deseja escolher? '))
    except:
        print('Opção inválida. Tente novamente!')
        return iniciando()
    if inicio == 1:
        clear_terminal()
        print('Entrando na configuração...')
        select_rodadas()
        clear_terminal()
        start()
        winner()
        time.sleep(4)
        new_start()
    if inicio == 2:
        recordes_menu()
    if inicio == 3:
        clear_terminal()
        print('Até a proxima!')
        sys.exit(1)


select_player()
iniciando()

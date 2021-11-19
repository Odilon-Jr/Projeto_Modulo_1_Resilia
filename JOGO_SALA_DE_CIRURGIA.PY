print(f'\033[34m----------------------------------------\n***  BEM-VINDOS A SALA DE CIRURGIA!  *** \n----------------------------------------\n*** QUEM NUNCA PENSOU EM SER MÉDICO? ***')
print('\033[31m------------------------------------------------------\nNESSE JOGO VOCÊ CONTARA COM 3 MÉDICOS DISTINTOS, CADA UM COM SUA ESPECIALIDADE, ONDE REALIZARÁ \nUMA OPERAÇÃO DE EMERGÊNCIA')
print('\033[34m-------------------------------------------------------\nAS ESCOLHAS SÃO:\n 1. DR. COLD SHEEPMAN: FAMOSO NEUROLOGISTA, QUASE UM MAGO DO CÉREBRO HUMANO NUNCA PERDEU UMA CIRURGIA...ATÉ HOJE. SEU MAIOR \nPONTO FRACO É SUA PERSONALIDADE, POR SE SENTIR UM DEUS NÃO SABE SOLICITAR AJUDA.\n\n 2. DRA. CRISTINA JOVEM, é uma médica especializada em transplantes do coração. Muito eficaz e apaixonada por cardiologia, dedica atenção especial para cada paciente. Tenta conciliar a vida profissional com a pessoal, sem sucesso e tenta superar preconceitos enfrentados dentro do trabalho que é dominado por homens.\n\n 3. Uma das médicas mais talentosas do nosso hospital, Dra. Livía Wesley é uma médica extremamente competente e eficaz, intensa e confiante, não admite erros,e por isso tem uma cobrança interna muito grande. Solteira, se dedica totalmente ao seu trabalho.Tem uma relação próxima com a diretora Dra. Ana Mendes.\n------------------------------------------------------------')
escolha_personagem = int(input('Escolha um de nossos especialistas:'))

if escolha_personagem == 1:
    print('\033[31mVOCÊ ESCOLHEU O DR. COLD SHEEPMAN!')
    print('\n\033[97mVOCÊ CHEGA PARA MAIS UM PLANTÃO CONCENTRADO PARA REALIZAR QUALQUER MILAGRE QUE JOGUEM EM SUAS MÃOS (\033[34mafinal você é quase um Deus, \num semiDeus vai) \033[97mQUANDO UM ENFERMEIRO QUALQUER (\033[34mseja lá qual for,todos são iguais) \033[97mCORRE ATÉ SUA DIREÇÃO, COM A APARÊNCIA PÁLIDA\n\n\033[95mENFERMEIRO: Dr. Sheepman temos um paciênte que está tendo convulsões, devido a uma grave concussão cerebral!! Venha rápido! \n\n\033[34mDR.SHEEPMAN: Não me de ordens! Você sabe com quem está falando por acaso?! Eu que decido quem morre e quem vive aqui.\n Agora mostre-me o caminho.\n CHEGAMOS A SALA DE CIRURGIA, AO OLHAR PARA OS OUTROS MÉDICOS, TODOS ESTÃO ABATIDOS, SUJOS DE SANGUE, A SALA TEM CHEIRO DE MORTE...\nPUTREFAÇÃO \nVOCÊ OLHA PARA O PACIÊN...TEM UM GALHO ATRAVESSADO EM SEU CRÂNIO, ENTRANDO POR CIMA E SAINDO NA LATERAL NO LOCAL ONDE ERA \nPARA SER UMA ORELHA...VOCÊ SE PREPARA PARA OPERAR...MAIS NENHUM SEGUNDO PODER SER PERDIDO, OU SUA REPUTAÇÃO SERÁ MANCHADA\n')

    escolha_primeira_fase = int(input(
        '\033[31mESCOLHA UM PROCEDIMENTO ABAIXO\n1 - REALIZAR O PROCEDIMENTO DE ARRANCAR O GALHO DA CABEÇA DO PACIÊNTE\n2 - CORTAR UM DOS LADOS DO GALHO E PUXAR UTILIZANDO O OUTRO LADO AINDA EXPOSTO\n3 - CORTAR OS DOIS LADOS DO GALHO, DEIXANDO APENAS A PARTE QUE ESTA DENTRO E REALIZAR O PROCEDIMENTO DE RETIRADA\nPor onde deseja começar ?\n'))
    if escolha_primeira_fase == 1:
        print('VOCÊ REALIZA ALGUNS CORTES PARA AMPLIAR BURACO E FACILITAR A SAÍDA,\nVOCÊ PEGA A PINÇA ALLIS DENTRE AS FERRAMENTAS,\nDA O PRIMEIRO PUXÃO, O GALHO SAI UM POUCO,\nVOCÊ PUXA OUTRA VEZ O GALHO SAI POR COMPLETO.\nSANGUE JORRA POR TODA SALA, O PACIÊNTE COMEÇA A PERDER OS BATIMENTOS CARDIACOS.\nVOCÊ TENTA ESTANCAR OS FERIMENTOS, MAS É TARDE DEMAIS, O PACIÊNTE NÃO TEM CHANCE.\n')

        print('\033[97mDEPOIS DE REALIZAR UMA CIRURGIA PÉSSIMA, O DR. COLD NAO CONSEGUIU SE PERDOAR.\nCAIU EM DEPRESSÃO PROFUNDA, NÃO CONSEGUIA MAIS SE ACEITAR,\nLARGOU SEU EMPREGO NO HOSPITAL E VIVEU SEUS ULTIMOS ANOS DE VIDA ISOLADO EM SUA CASA.\nGAME OVER! ')

    elif escolha_primeira_fase == 2:
        print('VOCÊ REALIZA UM CORTE DE PODA NA PARTE EXPOSTA DO GALHO, COM TODO CUIDADO PARA NÃO DANIFICAR ALGUMA AREA DO CEREBRO DO PACIÊNTE (Como é possivel algo disso ser real...), VOCÊ PEGA A PINÇA ALLIS DENTRE AS FERRAMENTAS PARA AGARRAR A PARTE AINDA EXPOSTA DO GALHO, VOCÊ FIRMA SEUS MUSCULOS COMO UMA ESTÁTUA, VAGAROSAMENTE COMEÇA A REMOVER O GALHO DO PACIÊNTE. COMO SE ESTIVESSE SEGURANDO UM TORNEIRA FECHADA AO REMOVE-LO COMEÇA DESCER UMA QUANTIDADE ASSUSTADORA DE SANGUE...VOCÊ SABE QUE ALGO PRECISA SER FEITO E AGORA!\n')

        segunda_escolha_fase_1 = int(input(
            '\033[34mESCOLHA UM PROCEDIMENTO ABAIXO\n1 - VOCÊ DEIXA O SANGUE ESCORRER, O PRÓPRIO ORGANISMO VAI ESTANCAR O SANGRAMENTO\n2 - VOCÊ DECIDE QUE ESSE TRABALHO NÃO É SEU, AFINAL VOCÊ JÁ REMOVEU O GALHO, ORDENA QUE O AUXILIAR TERMINE A CIRURGIA \n3 - VOCÊ REALIZA O PROCEDIMENTO PARA ESTARCAR O SANGRAMENTO\nPor onde deseja começar ?\n'))
        if segunda_escolha_fase_1 == 1:
            print('\033[34mDR.SHEEPMAN: Acabamos por aqui, o organismo estancará o sangramento, deixe o sangue contaminado escorrer. \n\n\033[95mAUXILIAR: Doutor, se permitimos que o sangramento continue, ele vai morrer, o Dr. tem certeza? \n\n\033[34mDR.SHEEPMAN: Pense duas vezes antes de perguntar se eu tenho certeza, por esse incomodo vou recomendar a diretoria do hospital que \nvocê não esteja presente em mais nenhuma de minhas cirurgias. \n\n\033[97mASSIM QUE VOCÊ TERMINA DE PROFERIR SUAS PALAVRAS O PACIÊNTE COMEÇA A CONVULSIONAR NOVAMENTE, OS BATIMENTOS CARDIACOS SOBEM COMO SE A NASA HOUVESSE AUTORIZADO A DECOLAGEM DE UM FOGUETE. VOCÊ BUSCA EM SUA MENTE OQUE PODE OCASIONAR ISSO, MAS ANTES QUE QUALQUER PALAVRA SAIA DE SUA BOCA OS BATIMENTOS VÃO À ZERO, VOCÊ FICA PARALISADO \033[34m(Estou acabado...tudo esta acabado)\n\n')
            print('\033[97mDEPOIS DE REALIZAR UMA CIRURGIA PÉSSIMA, O DR. COLD NAO CONSEGUIU SE PERDOAR.\nCAIU EM DEPRESSÃO PROFUNDA, NÃO CONSEGUIA MAIS SE ACEITAR.\nLARGOU SEU EMPREGO NO HOSPITAL E VIVEU SEUS ULTIMOS ANOS DE VIDA ISOLADO EM SUA CASA.\nGAME OVER! ')

        elif segunda_escolha_fase_1 == 2:
            print('\033[34mDR.SHEEPMAN: Pronto, agora Auxiliar, se você não for tão inútil quanto me parece, realize os procedimentos para estancar o \nsangramento. Mantenha-me informado sobre o caso, melhor, irei agora mesmo relatar para a diretoria mais um de meus milagres. \n\033[95mAUXILIAR: OK Doutor, creio que sou tão capacitado quanto o senhor afinal nos formamos na mesma turma, Cold! \n\033[34mDR.SHEEPMAN: Claro...\033[97m(Sorri e da as costas). \n\n APÓS ALGUNS MESES VOCÊ ESCUTA QUE O PACIÊNTE DO GALHO TEVE ALTA, INFELIZMENTE NÃO CONSEGUIU SE RECUPERAR COMPLETAMENTE E NEM SE LEMBRA DE MAIS NADA DEPOIS DO ACIDENTE...VOCÊ O SALVOU, E SE CASO ALGUMA SEQUELA TENHA RESTADO A CULPA COM CERTEZA É DAQUELE AUXILIAR. \n\n BOM, PARABENS ! VOCÊ CONSEGUIU SALVAR O PACIÊNTE, MAS NÃO COMPLETAMENTE, MELHOR SORTE NA PRÓXIMA VEZ')
        elif segunda_escolha_fase_1 == 3:
            print(
                '\033[97mVOCÊ COMEÇA OS PROCEDIMENTOS PARA ESTANCAR O SANGRAMENTO \033[34m(afinal ninguem menos qualificado poderia faze-lo)\033[97m E DURANTE VOCÊ PERCEBE \nQUE DEVIDO A UM ERRO SEU O PACIÊNTE PODE TER SEQUELAS PERMANENTES \n\n')
            escolha_terceira_fase = int(input(
                'Diante dessa descoberta você pensa sobre oque pode ser feito: \n1 - IGNORA, AFINAL SOMENTE VOCÊ SABE DESSA INFORMAÇÃO E SUA REPUTAÇÃO NÃO PODE SER MANCHADA \n2 - VOCÊ SE LEMBRA QUE UM NEUROLOGISTA CONHECIDO SEU JÁ PUBLICOU UM ARTIGO SOBRE ESSA SEQUELA E ELE ESTA NO HOSPITAL, VOCÊ PODE \nPEDIR QUE ELE SEJA CONVOCADO E ASSUMA A OPERAÇÃO \033[34m(Porém significa perder o seu pedestal de Deus da cirurgia para alguém inferior) \n\033[97m3 - VOCÊ SE LEMBRA QUE UM NEUROLOGISTA CONHECIDO SEU JÁ PUBLICOU UM ARTIGO SOBRE ESSA SEQUELA E ELE ESTA NO HOSPITAL, VOCÊ SE RECORDA DO ARTIGO, E DEVIDO AS SUAS EXCELENTES HABILIDADES PODE \033[34m(tentar) \033[97mCOPIAR O PROCEDIMENTO \033[34m(mas você consegue, afinal estamos falando de você)  \n\033[97mOque você faz?'))

            if escolha_terceira_fase == 1:
                print('\033[31m VOCÊ IGNORA AS SEQUELAS, AFINAL ESSE CARA JÁ TEM A SORTE DE NÃO TER MORRIDO. \n APÓS ALGUNS MESES VOCÊ RECEBE A NOTICIA DE QUE O PACIÊNTE FOI LIBERADO NO ENTANTO ELE TEVE GRAVES SEQUELAS E NÃO PODERÁ MAIS ANDAR NOVAMENTE.\n\033[34mBOM JOGADOR, VOCÊ NÃO DEIXOU SEU PACIÊNTE MUITO BEM, NO ENTANTO É IMPORTANTE SABER QUE DR. SHEEPMAN VIVEU SUA VIDA COM PESO E REMORSO POR TODA SUA VIDA E NÃO CONSEGUIU REALIZAR OUTRA OPERAÇÃO COMPLEXA, COM O TEMPO SUA REPUTAÇÃO DE RENOMADO CIRURGIÃO CAIU EM ESQUECIMENTO...\n EM SEUS ULTIMOS ANOS DR. COLD MUDOU PARA UM HOSPITAL NO SUBURBIO E VIVEU UMA VIDA SEM EMOÇÕES ATÉ SEUS ULTIMOS DIAS. ')

            elif escolha_terceira_fase == 2:
                print('VOCÊ ESCOLHEU CONVOCAR UM COLEGA ESPECIALISTA NESSE ASSUNTO, OS DEMAIS MÉDICOS ATÉ SORRIEM COM OS OLHOS, \033[34m(Você pode até sentir \nque eles casoam de você) \033[37mO MÉDICO ESPECIALISTA CHEGA E TODA OPERAÇÃO É UM SUCESSO, O ESPECIALISTA NÃO ABRIU NENHUMA INVESTIGAÇÃO A RESPEITO DO SEU ERRO NA CIRURGIA. \033[34m(No entanto toda vez que vocês se cruzam no corredor ele te encara com olhar de superioridade). \n\033[37mAH! E O PACIÊNTE FICOU BEM, RESTARAM ALGUMAS SEQUELAS TEMPORÁRIAS, E COM O TRATAMENTO CORRETO ELE DEVE TER UM VIDA NORMAL\nPARABENS JOGADOR !')
            elif escolha_terceira_fase == 3:
                print('VOCÊ COMEÇA O PROCEDIMENTO PUBLICADO POR SEU COLEGA, LENTAMENTE VOCÊ ESTA REALIZANDO OS PASSOS, UM POR VEZ, SEM PRESSA, \033[34m(Eu consigo, tenho que conseguir) \033[37mVOCÊ TERMINA O PROCEDIMENTO ESTA TUDO OK, VOCÊ CONSEGUE RESPIRAR CONFORTAVELMENTE AGORA.\n\nAPÓS A CIRURGIA OS DEMAIS MEDICOS AUXILIARES NOTARAM O PROCEDIMENTO REALIZADO POR VOCÊ, APENAS ALGUNS DIAS DEPOIS VOCÊ TEM \nA NOTICIA QUE O PACIÊNTE TEVE UMA COMPLICAÇÃO INESPERADA E ACABOU FALECENDO, OS OUTROS MÉDICOS INICIAM UM PROCESSO DE INVESTIGAÇÃO \033[37m\nNA SUA CIRURGIA QUE RESULTADA NA SUSPENSÃO DA SUA HABILITAÇÃO DE MÉDICO. ISSO ACABA COM A CARREIRA DO DR. COLD. ENTREGUE AS BEBIDAS O DOUTOR ACABA PRECISANDO DE UM TRANSPLANTE DE FÍGADO QUE DA ERRADO E OCASIONA SUA MORTE. \033[31m\nGAME OVER!')

    elif escolha_primeira_fase == 3:
        print('VOCÊ REALIZA OS CORTES EM AMBOS OS LADOS DO GALHO, DEIXANDO APENAS A PARTE QUE ESTA DENTRO DO CRÂNIO, ANTES DE REALIZAR A REMOÇÃO DA PARTE QUE ESTA ALOJADA DENTRO DO CRÂNIO VOCÊ PEDE PARA QUE UMA EQUIPE FIQUE DE PRONTIDÃO ESTANCANDO O SANGRAMENTO QUE É INEVITAVEL.')

    escoha_primeira_segunda_fase = int(input(
        '\033[37mEXISTEM DOIS PROCEDIMENTOS PARA REMOÇÃO DO GALHO DENTRO DO CRÂNIO \n1 - INCISÃO DIRETA NO CRÂNIO PARA AUMENTAR A ABERTURA E REALIZAR A REMOÇÃO DO GALHO \n2 - COM UMA BROCA REALIZAR UM PEQUENO FURO NO GALHO E APÓS FURADO PUXAR UTILZANDO UM GANCHO NO BURACO \nQual procedimento você escoherá?'))
    if escoha_primeira_segunda_fase == 1:
        print('VOCÊ REALIZA O PROCEDIMENTO COM MANEJO PERFEITO, OS DEMAIS MÉDICOS AUXILIAM NO SANGRAMENTO CAUSADO PELA OPERAÇÃO. A OPERAÇÃO É UM SUCESSO ! (Nada que você já não soubesse) VOCÊ FICA SABENDO QUE O PACIÊNTE TERÁ ALTA AMANHÃ.')

        escolha_primeira_terceira_fase = int(input(
            '1 - VOCÊ PODE VISITA-LO E DESEJAR-LHE BOAS NOVAS \n2 - OU NÃO PERDER SEU TEMPO COM ALGUEM TÃO AZARADO (burro) ASSIM. \n Oque você decide?'))

        if escolha_primeira_terceira_fase == 1:
            print(
                'VOCÊ VISITA SEU PACIÊNTE, LHE DESEJA BOAS NOVAS! E ACABA DESCOBRINDO QUE O MESMO ACABOU SE ENVOLVENDO NUM ACIDENTE POR CONTA DE UM \nCAMINHONEIRO QUE ATIROU SEU CARRO PARA FORA DA ESTRADA QUANDO ELE ESTAVA INDO VISITAR SUA FILHA QUE HAVIA SE FORMADO RECENTEMENTE EM MEDICINA. ANTES DE SAIR DA SALA CARL, O PACIÊNTE, DIZ QUE LHE DEVE A VIDA. \033[34m(Se eu começar a receber em vida alcançaria a \nimortalidade rsrs) \n \033[37mAPÓS ALGUM TEMPO DR. COLD DEVIDO AO SEU CORPORTAMENTO EGOISTA ACABA SOZINHO E SE ENTREGA AS BEBIDAS CADA VEZ MAIS. ESSE HÁBITO \nDESTRÓI SEU FÍGADO, SEM ESPERANÇA DE UM DOADOR UMA JOVEM MÉDICA DESCONHECIDA SE OFERE PARA DOAR PARTE DE SEU FÍGADO. \033[31m\nPARABENS JOGADOR ! SALVOU O PACIÊNTE, E AINDA POR CIMA NOSSO MÉDICO DE SEU PRÓPRIO DESTINO ! ')
        elif escolha_primeira_terceira_fase == 2:

            print(
                'VOCÊ DECIDE EM NÃO PERDER SEU TEMPO, TEMPO É VIDA E ISSO NÃO TEM COMO RECUPERAR. \nDR. COLD CONTINUA REALIZANDO SEUS MILAGRES E O SEU GRAU DE PRESTIGIO NÃO TEM LIMITES, NO ENTANTO EM SEU PARTICULAR, QUANDO ESTA \nSOZINHO SOFRE DE DEPRESSÃO PROFUNDA E BEBE PARA AMENIZAR O VAZIO QUE TEM NO PEITO. INFELIZMENTE O HÁBITO DE BEBER SEM LIMITES \nCOMPROMETE SEU FÍGADO, E COMO NÃO ENCONTRA NENHUM DOADOR MORRE DURANTE UMA CIRURGIA EXPERIMENTAL DE TRANSPLANTE UTILIZANDO FÍGADOS DE ANIMAIS \n\033[33mGAME OVER!')

    elif escoha_primeira_segunda_fase == 2:
        print('VOCÊ PEGA A BROCA DE PRECISÃO E INICIA O PROCEDIMENTO DE PERFURAR O PEDAÇO DE GALHO DENTRO DA CABEÇA DO PACIÊNTE, A BROCA COMEÇA A PERFURAR O GALHO QUANDO VOCÊ COM SEUS OLHOS TREINADOS PERCEBE QUE O GALHO COMEÇA A SE MOVIMENTAR E ISSO PODE ACABAR COMPLICAR AS COISAS. ENTÃO VOCÊ PARA ESSE PROCEDIMENTO E PREFERE UTILIZAR TÉCNICA DE INCISÃO DIRETA\n')
        print('VOCÊ REALIZA O PROCEDIMENTO COM MANEJO PERFEITO, OS DEMAIS MÉDICOS AUXILIAM NO SANGRAMENTO CAUSADO PELA OPERAÇÃO. A OPERAÇÃO É UM SUCESSO ! (Nada que você já não soubesse) VOCÊ FICA SABENDO QUE O PACIÊNTE TERÁ ALTA AMANHÃ.')
        escolha_primeira_quarta_fase = int(input(
            '1 - VOCÊ PODE VISITA-LO E DESEJAR-LHE BOAS NOVAS \n2 - OU NÃO PERDER SEU TEMPO COM ALGUEM TÃO AZARADO (burro) ASSIM. \n Oque você decide?'))

        if escolha_primeira_quarta_fase == 1:
            print(
                'VOCÊ VISITA SEU PACIÊNTE, LHE DESEJA BOAS NOVAS! E ACABA DESCOBRINDO QUE O MESMO ACABOU SE ENVOLVENDO NUM ACIDENTE POR CONTA DE UM \nCAMINHONEIRO QUE ATIROU SEU CARRO PARA FORA DA ESTRADA QUANDO ELE ESTAVA INDO VISITAR SUA FILHA QUE HAVIA SE FORMADO RECENTEMENTE EM MEDICINA. ANTES DE SAIR DA SALA CARL, O PACIÊNTE, DIZ QUE LHE DEVE A VIDA. \033[34m(Se eu começar a receber em vida alcançaria a \nimortalidade rsrs) \n \033[37mAPÓS ALGUM TEMPO DR. COLD DEVIDO AO SEU CORPORTAMENTO EGOISTA ACABA SOZINHO E SE ENTREGA AS BEBIDAS CADA VEZ MAIS. ESSE HÁBITO \nDESTRÓI SEU FÍGADO, SEM ESPERANÇA DE UM DOADOR UMA JOVEM MÉDICA DESCONHECIDA SE OFERE PARA DOAR PARTE DE SEU FÍGADO. \033[31m\nPARABENS JOGADOR ! SALVOU O PACIÊNTE, E AINDA POR CIMA NOSSO MÉDICO DE SEU PRÓPRIO DESTINO ! ')
        elif escolha_primeira_quarta_fase == 2:
            print(
                'VOCÊ DECIDE EM NÃO PERDER SEU TEMPO, TEMPO É VIDA E ISSO NÃO TEM COMO RECUPERAR. \nDR. COLD CONTINUA REALIZANDO SEUS MILAGRES E O SEU GRAU DE PRESTIGIO NÃO TEM LIMITES, NO ENTANTO EM SEU PARTICULAR, QUANDO ESTA \nSOZINHO SOFRE DE DEPRESSÃO PROFUNDA E BEBE PARA AMENIZAR O VAZIO QUE TEM NO PEITO. INFELIZMENTE O HÁBITO DE BEBER SEM LIMITES \nCOMPROMETE SEU FÍGADO, E COMO NÃO ENCONTRA NENHUM DOADOR MORRE DURANTE UMA CIRURGIA EXPERIMENTAL DE TRANSPLANTE UTILIZANDO FÍGADOS DE ANIMAIS \n\033[33mGAME OVER!')

elif escolha_personagem == 2:
    print('\033[37mMAIS UM DIA DE PLANTÃO. VOCÊ ACABOU DE CHEGAR AO HOSPITAL E OLHA O QUADRO DE ENTRADA DO PACIENTE. \n\nQuadro clínico: Procurou a urgência com queixas de “forte dor no peito”. A dor em aperto em região precordial que iniciou há 10 dias com piora progressiva é agravada após moderado esforço físico como caminhar dois quarteirões planos, ou subir dois lances de escadas e dura pouco tempo, com melhora após repouso. No momento da consulta a intensidade é 8, numa escala de 0 a 10. Paciente referiu apresentar também desconforto em região de dorso e membro superior esquerdo. Refere ainda que sente palpitações, náuseas e tonturas. Em relação aos antecedentes pessoais, paciente é hipertenso, diabético, obeso e tabagista. Relata histórico familiar de infarto agudo do miocárdio (pai faleceu aos 50 anos) e de hipertensão (mãe hipertensa)')

    segunda_escolha_fase_1 = int(input(
        '\033[31mESCOLHA OQUE DEVEMOS FAZER: \n1 - SOLICITAR ECOCARDIOGRAMA \n2 - INDICAR MEDICAÇÃO DE DIAZEPAM 10MG \n3 - DISPENSAR PACIENTE INDICANDO QUE NÃO DEVE FAZER ESFORÇO FÍSICO \n'))
    if segunda_escolha_fase_1 == 1:
        print(
            '\033[34mDra., identificamos um desnivelamento supra do segmento ST de 2 mm na parede anterior.')

        segunda_escolha_fase_2 = int(input(
            'Escolha oque fazer agora: \n1 - ENCAMINHAR PACIENTE PARA SALA DE OBSERVAÇÃO \n2 - ENCAMINHAR PACIENTE PARA MEDICAÇÃO DE ESTATINAS \n3 - DISPENSAR PACIENTE COM MEDICAÇÃO RECOMENDADA \n'))
        if segunda_escolha_fase_2 == 1:
            print('\033[37mDra., o paciente sofreu infarto agudo do miocárdio e a família solicitou transferência de hospital. Devíamos ter nos atentado \nmelhor aos sinais. ')
        elif segunda_escolha_fase_2 == 2:
            print('\033[37mO Paciente apresentou melhora do quadro, com pressão arterial dentro da normalidade porém ainda reclama da dor no peito.')
            segunda_escolha_fase_3 = int(input('\033[37mESCOLHA OQUE DEVEMOS FAZER: \n1 - DISPENSAR PACIENTE COM ORIENTAÇÕES DOS CUIDADOS \n2 - ENCAMINHAR O PACIENTE PARA SALA DE OBSERVAÇÃO \n3 - ENCAMINHAR PACIENTE PARA CIRURGIA')
                                         )
            if segunda_escolha_fase_3 == 1:
                print('\033[34mSua falta de cuidado levou o paciente a falecer.')
            elif segunda_escolha_fase_3 == 2:
                print('\033[34mDra., o paciente sofreu infarto agudo do miocárdio e a família solicitou transferência de hospital. Devíamos ter nos atentado melhor aos sinais.')
            elif segunda_escolha_fase_3 == 3:
                print('\033[34mParabéns Dra., a cirurgia foi um sucesso! Você foi muito cuidadosa na leitura das respostas do paciente e tomou as melhores decisões, a família gostaria de fazer um agradecimento!')
        elif segunda_escolha_fase_2 == 3:
            print('\033[37mSua falta de cuidado levou o paciente a falecer.')

    elif segunda_escolha_fase_1 == 2:
        print('\033[34mDra. o paciente relata melhora da dor no peito, porém diz ter um sentimento de angústia, suspeitamos de efeito colateral da medicação.')
        rhayza_2_2 = int(input(
            'Oque faremos: \n1 - ENCAMINHAR PACIENTE PARA SALA DE OBSERVAÇÃO \n2 - DENTRO DO ESPERADO DISPENSE O PACIÊNTE \n3 - CODE BLUE! CODE BLUE! ENCAMINHAR PARA SALA DE CIRURGIA!'))
        if rhayza_2_2 == 1:
            print('\033[37mApós 6h, desenvolveu inversão na onda T, onda Q patológica, além da presença de onda U invertida transitória. Na pesquisa de marcadores bioquímicos de lesão miocárdica houve elevação das troponinas acima do percentil 99 do limite máximo de referência, porém a CK-MB massa estava dentro da normalidade.')
            rhayza_2_3 = int(input(
                'OQUE FAREMOS AGORA: \n1 - DISPENSAR PACIENTES COM ORIENTAÇÃO DE CUIDADOS \n2 - ENCAMINHAR PACIENTE PARA INICIAR MEDICAÇÃO DE ESTATINAS \n3 - ENCAMINHAR PACIENTE PARA CIRURGIA'))
            if rhayza_2_3 == 1:
                print('\033[34mSua falta de cuidado levou o paciente a falecer.')
            elif rhayza_2_3 == 2:
                print(
                    '\033[34mO Paciente apresentou melhora do quadro, com pressão arterial dentro da normalidade porém ainda reclama da dor no peito.')
                rhayza_2_4 = int(input(
                    'ESCOLHA OQUE DEVEMOS FAZER: \n1 - DISPENSAR PACIENTE COM ORIENTAÇÕES DOS CUIDADOS \n2 - ENCAMINHAR O PACIENTE PARA SALA DE OBSERVAÇÃO \n3 - ENCAMINHAR PACIENTE PARA CIRURGIA'))
                if rhayza_2_4 == 1:
                    print('Sua falta de cuidado levou o paciente a falecer.')
                elif rhayza_2_4 == 2:
                    print('Dra., o paciente sofreu infarto agudo do miocárdio e a família solicitou transferência de hospital. Devíamos ter nos atentado melhor aos sinais.')
                elif rhayza_2_4 == 3:
                    print('Parabéns Dra., a cirurgia foi um sucesso! Você foi muito cuidadosa na leitura das respostas do paciente e tomou as melhores decisões, a família gostaria de fazer um agradecimento!')
            elif rhayza_2_3 == 3:
                print('\033[34mParabéns Dra., a cirurgia foi um sucesso! Você foi muito cuidadosa na leitura das respostas do paciente e tomou as melhores decisões, a família gostaria de fazer um agradecimento!')

        elif rhayza_2_2 == 2:
            print('\033[37mSua falta de cuidado levou o paciente a falecer.')
        elif rhayza_2_2 == 3:
            print('\033[37mParabéns Dra., a cirurgia foi um sucesso! Você foi muito cuidadosa na leitura das respostas do paciente e tomou as melhores decisões, a família gostaria de fazer um agradecimento!')

    elif segunda_escolha_fase_1 == 3:
        print('\033[34mSua falta de cuidado levou o paciente a falecer. ')

elif escolha_personagem == 3:
    print('Paciente com 13 anos, deu entrada no hospital apresentando quadro de pneumonia bacteriana que inicialmente foi tratada com antibióticos mas quadro evoluiu para um derrame pleural.')
    opcao_inicio = int(input(
        '1 - SOLICITAR ULTRASSONOGRAFIA \n 2 - ENCAMINHAR PARA CIRURGIA \nOQUE FAREMOS AGORA: '))
    if opcao_inicio == 1:
        print('Dra. Lívia  a ultrassonografia constatou acumulo de liquido na região pleural. Oque faremos agora:')
        opcao_1_1 = int(
            input('1 - ENCAMINHAR PARA CIRURGIA \n2 - ENCAMINHAR PARA SALAR DE MEDICAÇÃO'))
        if opcao_1_1 == 1:
            print('É feita drenagem do liquido na cavidade pleural, paciente em observação após cirurgia, paciente evolui de forma satisfatória e concluímos com êxito a cirurgia. \nDeseja refazer os exames ?')
            opcao_1_2 = int(
                input('1 - REFAZER OS EXAMES \n2 - DAR ALTA AO PACIENTE \n'))
            if opcao_1_2 == 1:
                print(
                    'Constatados resquícios de inflamação, recomendado antibiótico. Alto no paciente.')
            elif opcao_1_2 == 2:
                print('Dar alta ao paciente \n\n\n Paciente morreu!')

        elif opcao_1_1 == 2:
            print('Mandar pra sala de medicação, dispensado por falta de embasamento do caso, a medicação não foi assertiva e paciente veio a óbito.')

    elif opcao_inicio == 2:
        print('Ao abrir a cavidade torácica, Dra. Livia percebeu que a situação era mais grave do que esperado \n Oque faremos agora?')
        opcao_2_1 = int(input(
            '1 - SOLICITAR EXAMES \n2 - FAZER A CIRURGIA MESMO ASSIM VISTO A URGÊNCIA DO CASO'))
        if opcao_2_1 == 1:
            print('Dra., Livia o exame contatou que o acumulo de liquido se concentra na parte superior esquerda. Oque faremos agora?')
            opcao_2_2 = int(
                input('1 - REFAZER A CIRURGIA \n 2 - MEDICAR E AGUARDAR '))
            if opcao_2_2 == 1:
                print(
                    'Cirurgia foi um sucesso,conseguimos drenar todo o liquido da cavidade e paciente se recupera bem.')
            elif opcao_2_2 == 2:
                print(
                    'Indicação da medicação foi equivocada e o paciente veio a óbito.')
        elif opcao_2_1 == 2:
            print('Paciente morreu! ')

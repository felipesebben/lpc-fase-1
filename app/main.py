# ### Professores: ###
#  **Marcelo Cohen** e **Sílvia Maria Wanderley Moraes**

# ## Enunciado da fase 1

# Implemente um programa que leia, valide e analise dados informados pelo usuário. Os dados são meteorológicos e referem-se aos dados de 2021 (de janeiro a dezembro) registrados em uma cidade.

# Toda entrada de dados deve ser validada. No caso de valor inválido, informe ao usuário o erro e permita que ele redigite o dado.

# Seu programa deve coletar os seguintes dados:
# -  Mês: use valor numérico de 1 a 12 (janeiro a dezembro) para se referir aos meses do ano.

# ---------------------------------------------------------------------------------------------------------------------------- #

# ## Código da fase 1

# Gerar instruções para o usuário.
print("Leitura e análise de dados meteorológicos.\nInstruções:")
print("- Informe a temperatura máxima de cada mês.")
print("- A temperatura deve ser informada em graus Celsius.")
print("- O intervalo de temperaturas válidas é de -60ºC a +50ºC.")
print("- Os meses devem ser informados usando valor numérico de 1 a 12.")
# ## Entrada: ##
# Booleano para controle do programa. Enquanto for `True`, o programa continua.
programa_continua = True
while programa_continua:
    # Criar dicionário vazio para armazenar dados.
    dados = {}

    # Criar lista de meses em formato numérico.
    list_meses = list(range(1, 13))

    # Criar lista de meses em formato string.
    list_meses_str = [
        "Janeiro",
        "Fevereiro",
        "Março",
        "Abril",
        "Maio",
        "Junho",
        "Julho",
        "Agosto",
        "Setembro",
        "Outubro",
        "Novembro",
        "Dezembro",
    ]
    # Criar dicionário com listas anteriores. Utilizar função `zip` para unir as listas `list_meses` e `list_meses_str` em um dicionário `list_meses_dict`.
    list_meses_dict = dict(zip(list_meses, list_meses_str))

    # Inicia loop baseado em `list_meses`. A cada iteração, remove o mês informado da lista. O loop continua até que a lista esteja vazia.
    while list_meses:
        mes_informado = int(input("\nInforme o mês usando valor numérico de 1 a 12: "))
        while mes_informado not in list_meses:
            if mes_informado in dados:
                dados_formatados = "\n".join(
                    f"{k} : {v}" for k, v in dados.items()
                )  # Formatação do dicionário para exibição.
                print(
                    f"\nErro: Mês {mes_informado} ({list_meses_dict[mes_informado]}) já informado. \nMeses informados (mês : temperatura): \n{dados_formatados}. \nPor favor, informe um mês que ainda não foi informado."
                )
            else:
                print("\nErro: Mês inválido. Por favor, informe um mês válido.")
            mes_informado = int(
                input("Informe o mês usando valor numérico de 1 a 12: ")
            )

        temperatura_maxima = float(input("\nInforme a temperatura máxima do mês: "))
        while temperatura_maxima < -60 or temperatura_maxima > 50:
            print("\nErro: Temperatura inválida.")
            temperatura_maxima = float(input("\nInforme a temperatura máxima do mês: "))

        # Armazenar os dados no dicionário.
        dados[mes_informado] = temperatura_maxima
        # Remover mês informado da lista.
        list_meses.remove(mes_informado)
        # Informar ao usuário que os dados foram inseridos.
        print(f"Dados inseridos para o mês {mes_informado}.")

    # Retorna dados para validação.
    # print(data)

    # ## Saída: ##
    # Temperatura média máxima anual: valor da maior temperatura máxima informada.
    print("\nAnálise de dados meteorológicos. Resultados:")
    temp_media_max = sum(dados.values()) / len(dados)
    print(
        f"\n- Temperatura média máxima anual: {temp_media_max:.2f}ºC."
    )  # Arredondar para 2 casas decimais.

    # Quantidade de meses escaldantes: meses com temperaturas máximas acima de 33ºC.
    meses_escaldantes = [
        mes for mes, temp in dados.items() if temp > 33
    ]  # Compreeensão de lista para criar lista de meses escaldantes se a temperatura máxima for maior que 33ºC.
    print(
        f"\n- Quantidade de meses escaldantes: {len(meses_escaldantes)}."
    )  # Contar a quantidade de meses escaldantes.
    print(
        f"\n- Mês/Meses escaldante(s): {', '.join([list_meses_dict[mes] for mes in meses_escaldantes])}."  # Utilizar compreensão de lista para criar lista de meses escaldantes em formato string.
    )

    # Mês mais escaldante do ano:
    mes_mais_escaldante = max(
        dados, key=dados.get
    )  # Utilizar função `max` para encontrar a chave (mês) com maior valor (temperatura máxima). `key=dados.get` é utilizado para comparar os valores do dicionário `dados` e retornar a chave correspondente ao maior valor.
    print(f"\n- Mês mais escaldante do ano: {list_meses_dict[mes_mais_escaldante]}.") # Retorna mês em string do dicionário.
    print(f"\n- Temperatura máxima: {dados[mes_mais_escaldante]}ºC.")

    # Mês menos quente do ano:
    mes_mais_ameno = min(dados, key=dados.get)
    print(f"\n- Mês menos quente do ano: {list_meses_dict[mes_mais_ameno]}.")

    print("\nFim da análise.")
    continuar = input("Deseja informar novos dados? (s/n): ") # Pergunta ao usuário se deseja continuar. 
    if continuar.lower() == "n": # Se a resposta for "n", o programa encerra.
        programa_continua = False
        print("Programa encerrado.")
    elif continuar.lower() == "s": # Se a resposta for "s", o programa continua.
        programa_continua = True
    else: # Se a resposta for diferente de "s" ou "n", o programa informa que a resposta é inválida e pergunta novamente.
        print("Resposta inválida. Por favor, informe 's' para sim ou 'n' para não.")
        continuar = input("Deseja informar novos dados? (s/n): ")
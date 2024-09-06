funcionario = {
    '01': {'cpf': 36721546957,
           'nome': 'Ariel Mendes',
           'email': 'ariel_mendes@oleoverde.com',
           'cargo': 'Engenheiro de Software',
           'projetos': ['Monitoramento do site', 'Monitoramento do aplicativo']
           },
    '02': {'cpf': 89781724749,
           'nome': 'Emanoel Cruz',
           'email': 'emanoel_cruz@oleoverde.com',
           'cargo': 'Desenvolvedor Mobile',
           'projetos': ['Criação do APP', 'Monitoramento do aplicativo']
           },
    '03': {'cpf': 28724432822,
           'nome': 'Caroline Ferraz Prado',
           'email': 'caroline_prado@oleoverde.com',
           'cargo': 'Desenvolvedor Web',
           'projetos': ['Criação do Site', 'Monitoramento do Site']
           },
    '04': {'cpf': 83313324070,
           'nome': 'Oséas Abreu de Faria',
           'email': 'oseas_faria@oleoverde.com',
           'cargo': 'Desenvolvedor Web',
           'projetos': ['Criação do Site', 'Monitoramento do Site']
           },
    '05': {'cpf': 37268117612,
           'nome': ' Jânio Colaço Sobrinho',
           'email': 'janio_sobrinho@oleoverde.com',
           'cargo': 'Analista de dados',
           'projetos': ['Analisar dados do Site', 'Analisar dados do aplicativo']
           },
    '06': {'cpf': 25189596370,
           'nome': 'Cristiano Bittencourt Carmona',
           'email': 'cristiano_carmona@oleoverde.com',
           'cargo': 'Assistente de TI',
           'projetos': ['Auxiliar no desenvolvimento do Site', 'Auxiliar no desenvolvimento do aplicativo']
           },
    '07': {'cpf': 45183865582,
           'nome': 'Milene Taís Lovato de Matias',
           'email': 'josue_maia@oleoverde.com',
           'cargo': 'Marketing',
           'projetos': ['Pesquisa de vendas', 'Estrategias de vendas']
           },
    '08': {'cpf': 72827685957,
           'nome': ' Josué Furtado de Maia',
           'email': 'milene_matias@oleoverde.com',
           'cargo': 'Assistente de TI',
           'projetos': ['Auxiliar no desenvolvimento do Site', 'Auxiliar no desenvolvimento do aplicativo']
           },
    '09': {'cpf': 21859922449,
           'nome': 'Elizabete Raquel Aragão de Pacheco',
           'email': 'elizabete_pacheco@oleoverde.com',
           'cargo': 'Assistente de produção',
           'projetos': ['Produção de biodiesel', 'Produção de sabão']
           },
    '10': {'cpf': 26548722540,
           'nome': 'Dário Ricardo de Casanova,',
           'email': 'dario_casanova@oleoverde.com',
           'cargo': 'Assistente de produção',
           'projetos': ['Produção de biodiesel', 'Produção de sabão']
           },

}


def buscar_por_cpf(cpf):
    for cpf_funcionario, info in funcionario.items():
        if info["cpf"] == cpf:
            return info
        return None


def buscar_por_nome(nome):
    for nome_funcionario, info in funcionario.items():
        if info["nome"].lower() == nome.lower():
            return info
        return None


def buscar_por_cargo(cargo):
    resultados = []
    for cpf_funcionario, info in funcionario.items():
        if info["cargo"] == cargo:
            resultados.append(info)
    return resultados if resultados else None


def exibir_infor(funcionario):
    if funcionario:
        print("informações do funcionario:")
        for chave, valor in funcionario.items():
            print(f"{chave}: {valor}")
    else:
        print("Funcionario nao encontrado")


def main():
    print("Funcionarios da Oleo Verde:")
    print("Digite 1 para buscar por CPF do funcionario:\n")
    print("Digite 2 para buscar pelo NOME do funcionario:\n")
    print("Digite 3 para buscar pelo CARGO do funcionario:\n")

    try:
        escolha = int(input("Digite o número da opção desejada:\n"))
        if escolha == 1:
            cpf = input("Digite o CPF do funcionario (FORMATO: xxx.xxx-xx)")
            funcionario = buscar_por_cpf(cpf)
            exibir_infor(funcionario)
        elif escolha == 2:
            nome = input("Digite o NOME COMPLETO do funcionario:\n")
            funcionario = buscar_por_nome(nome)
            exibir_infor(funcionario)
        elif escolha == 3:
            cargo = input("Digite o CARGO do funcionario:\n")
            funcionarios_por_cargo = buscar_por_cargo(cargo)
            if funcionarios_por_cargo:
                print("Funcionarios com o cargo especificado:\n")
                for funcionario in funcionarios_por_cargo:
                    exibir_infor(funcionario)
            else:
                print("Nenhum funcionario encontrado com o cargo especificado.\n")
        else:
            print("Opção imvalida. Por favor esoclha uma opçao valida.\n")
    except ValueError:
        print("Entrada inválida. Por favor digite um numero valido.\n")


if __name__ == "__main__":
    main()

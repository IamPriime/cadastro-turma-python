def ver_dados(turma):
    for categoria, nomes in turma.items():
        print(f"\n{categoria.upper()}")
        if not nomes:
            print("Nenhum cadastro.")
        for posicao, nome in enumerate(nomes, start=1):
            print(f"{posicao} - {nome}")


def adicionar(turma, categoria, nome):
    nome = nome.strip()
    if not nome:
        raise ValueError("O nome não pode ficar vazio.")
    turma[categoria].append(nome)


def remover(turma, categoria, posicao):
    if not 1 <= posicao <= len(turma[categoria]):
        raise ValueError("Posição inválida.")
    return turma[categoria].pop(posicao - 1)


def main():
    turma = {"professores": [], "alunos": []}
    while True:
        print("\n1 - Listar\n2 - Adicionar aluno\n3 - Adicionar professor\n4 - Remover aluno\n5 - Remover professor\n0 - Sair")
        escolha = input("Escolha: ")
        if escolha == "0":
            break
        try:
            if escolha == "1":
                ver_dados(turma)
            elif escolha in {"2", "3"}:
                categoria = "alunos" if escolha == "2" else "professores"
                adicionar(turma, categoria, input("Nome: "))
                ver_dados(turma)
            elif escolha in {"4", "5"}:
                categoria = "alunos" if escolha == "4" else "professores"
                ver_dados(turma)
                nome = remover(turma, categoria, int(input("Posição a remover: ")))
                print(f"Removido: {nome}")
            else:
                print("Opção inválida.")
        except ValueError as erro:
            print(erro)


if __name__ == "__main__":
    main()

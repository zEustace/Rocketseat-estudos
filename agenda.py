def adicionar_contato(contatos, nome, telefone, email):
    contato = {"nome": nome, "telefone": telefone, "email": email, "favorito": False}
    contatos.append(contato)
    print(f"O {contato} foi adicionado com sucesso")
    return

def editar_contato(contatos, indice_contato, novo_nome, novo_telefone, novo_email):
    indice_contato_ajustado = int(indice_contato) - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
        contatos[indice_contato_ajustado]["nome"] = novo_nome
        contatos[indice_contato_ajustado]["telefone"] = novo_telefone
        contatos[indice_contato_ajustado]["email"] = novo_email
        print(f"Contato {nome} alterado para {novo_nome}")
    else:
        print("Contato inválido")

def ver_contatos(contatos):
    print("\nLista de contatos:")
    for indice, contato in enumerate(contatos, start=1):
        status = "✓" if contato["favorito"] else " "
        nome_contato = contato["nome"]
        print(f"{indice}. [{status}] {nome_contato}")

def marcar_favorito(contatos):
    indice_contato_ajustado = int(indice_contato) - 1
    if contatos[indice_contato_ajustado]["favorito"] == False:
        contatos[indice_contato_ajustado]["favorito"] = True
        print(f"O contato {nome} foi marcado como favorito")
    elif contatos[indice_contato_ajustado]["favorito"] == True:
        contatos[indice_contato_ajustado]["favorito"] = False
        print(f"O contato {nome} foi removido dos favoritos")
    return

def contatos_favoritos(contatos):
    for contato in contatos:
        if contato["favorito"]:
            print(f"{contato}")

def deletar_contato(contatos):
    indice_contato_ajustado = int(indice_contato) - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
        contatos.pop(indice_contato_ajustado)
        print(f"O contato {nome} foi deletado com sucesso.")


contatos = []

while True:
    print("\nMenu da agenda:")
    print("1. Adicionar contato.")
    print("2. Editar contato.")
    print("3. Ver todos os contatos.")
    print("4. Marcar/Desmarcar como favorito.")
    print("5. Ver contatos favoritos.")
    print("6. Apagar contato.")
    print("7. Sair.")
    escolha = input("Digite a sua escolha: ")
    
    if escolha == "1":
        nome = input("Digite o nome do contato: ")
        telefone = input("Digite o telefone do contato: ")
        email = input("Digite o e-mail do contato: ")
        adicionar_contato(contatos, nome, telefone, email)
    
    if escolha == "2":
        ver_contatos(contatos)
        indice_contato = input("Digite o numero do contato: ")
        novo_nome = input("Digite o nome: ")
        novo_telefone = input ("Digite o novo telefone: ")
        novo_email = input ("Digite o novo email: ")
        editar_contato(contatos, indice_contato, novo_nome, novo_telefone, novo_email)
    
    if escolha == "3":
        ver_contatos(contatos)

    if escolha == "4":
        ver_contatos(contatos)
        indice_contato = input("Escolha o contato que quer favoritar: ")
        marcar_favorito(contatos)

    if escolha == "5":
        contatos_favoritos(contatos)

    if escolha == "6":
        ver_contatos(contatos)
        indice_contato = input ("Escolha o contato para deletar.")
        deletar_contato(contatos)    

    if escolha == "7":
        break
print("Programa finalizado.")

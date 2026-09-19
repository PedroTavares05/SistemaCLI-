#5 quartos fixos  for_pagamento= input('Digite a forma de pagamento: ')
status_quartos = ["livre", "ocupado", "em limpeza"]
quartos = [{
    "num_quarto": 1,
    "nome_hospede": "0",
    "idade_hospede": "",
    "status": status_quartos[2]
},{
    "num_quarto": 2,
    "nome_hospede": "0",
    "idade_hospede": "",
    "status": status_quartos[0]
},{
    "num_quarto": 3,
    "nome_hospede": "0",
    "idade_hospede": "",
    "status": status_quartos[1]
},{
    "num_quarto": 4,
    "nome_hospede": "0",
    "idade_hospede": "",
    "status": status_quartos[1]
}, {
    "num_quarto": 5,
    "nome_hospede": "0",
    "idade_hospede": "",
    "status": status_quartos[0]
}
]

# criar check-in  (hóspede)
print('============INSCRIÇÃO DO CHECK-IN============')


while True:

    print('''
[1] Realizar check-in
[2] Exibir mapa de quartos 
[3] Alterar status do quarto
[4] Realizar check-out 
[5] Liberar quarto após limpeza 
[0] Sair 
      ''')
    
    resposta= input('\nResposta:')
# CHECK-IN
    if resposta == '1':
        nome= input("Nome do hóspede: ")
        try:
            idade=int(input('Idade do hóspede: '))
        except ValueError:
            print("Fale uma idade válida!")
            continue
    
        print("====QUARTOS DISPONIVEIS====\n")
        
        for item in quartos:
            if item["status"] == status_quartos[0]:
                print(f"Quarto {item['num_quarto']} está {item['status']}")
    
        escolha = int(input("\nEscolha o quarto a ser hospedado: "))
        for item in quartos:
            if item["num_quarto"]== escolha:
                item['nome_hospede'] = nome
                item["idade_hospede"] = idade
                item["status"] = status_quartos[1]
                print(f"\nQuarto {item['num_quarto']} foi ocupado pelo hóspede: {item['nome_hospede']} e se encontra {item['status']} no momento.")
                continue
        
       #MAPA DE QUARTOS

    elif resposta == "2":
        print(" =============== MAPA DE QUARTOS =============\n")
        for item in quartos:
            if item["status"] == status_quartos[0] or item["status"] == status_quartos[2]:
                
                print(f"O Quarto {item['num_quarto']} está {item['status']}")
            
            else:
                print(f"O Quarto {item['num_quarto']} se encontra ocupado pelo hóspede: {item['nome_hospede']}")
    
    # STATUS DO QUARTO
    
    elif resposta == "3":
        print("\n =========== ALTERAR STATUS DO QUARTO ===============")

        for item in quartos:
            #if item["status"] == status_quartos[2]:
                print(f"Quarto {item['num_quarto']} - {item['status']}. ")
        try:
         escolha = int(input('\n Escolha o quarto que deseja alterar: '))
        except ValueError:
            print("Coloque um número de quarto válido!")
            continue
        for item in quartos:
            if item["num_quarto"] == escolha:
                print('''
                [1] Livre
                [2] Ocupado
                [3] Em Limpeza
                      ''')
                novo_status =input("Escolha o novo status: ")
                if novo_status == "1":
                    item["status"] = "livre"
                
                elif novo_status == "2":
                    item["status"] = "ocupado"
                
                elif novo_status == "3":
                    item["status"] = "em limpeza"
                
                else:
                    print("Opção Inválida!!")
                    

                print(f"O quarto {item['num_quarto']} agora está {item['status']}.")
            
            
        #CHECK-OUT
    elif resposta == "4":
        print("\n============= CHECK-OUT ============") 
        for item in quartos:
            if item["status"] == "ocupado":
                print(f'Quarto {item['num_quarto']} - Hóspede: {item['nome_hospede']}')
        try:     
            escolha = int(input("\n Escolha o número do quarto para realizar o Check-out: "))
        except ValueError:
            print("Digite um número de quarto válido!")

        for item in quartos:
            if item["num_quarto"] == escolha:
                if item["status"] == "ocupado":
                    print(
                        f"Check out do hóspede {item["nome_hospede"]} realizado."
                    )
                    item["nome_hospede"] = "0"
                    item["idade_hospede"] = ""
                    item["status"] = "em limpeza"
                else:
                    print("Esse quarto não está ocupado.")
        

    elif resposta == "5":
        print("\n============== LIBERAR QUARTO ================")
        for item in quartos:
            if item["status"] == "em limpeza":
                print(f"Quarto {item['num_quarto']} está em limpeza")
        try:
            escolha = int(input("Escolha o quarto para ser liberado: "))
        except ValueError:
            print("Digite um número de quarto válido!")
        for item in quartos:
            if item["num_quarto"] == escolha:
                if item["status"]  == "em limpeza":
                    item["status"] = "livre"
                    print(f"\n Quarto {item["num_quarto"]} foi liberado e está livre.")
                else:
                    print("\n Esse quarto não está em limpeza.")
    elif resposta == "0":
        print("Sistema Encerrado!")
               
        
    



    

        


        

        







    #[1] Realizar check-in → realizar_checkin()
    #[2] Exibir mapa de quartos → listar_quartos()
    #[3] Alterar status do quarto → atualizar_status()
    #[4] Realizar check-out → realizar_checkout()
    #[5] Liberar quarto após limpeza → liberar_quarto()
    #[0] Sair → salvar_dados()

    #if item["status"] == status_quartos[2]:
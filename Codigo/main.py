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
        idade=int(input('Idade do hóspede: '))
    
    print("\n====QUARTOS DISPONIVEIS====")
    for item in quartos:
        if item["status"] == status_quartos[0]:
            print(f"Quarto {item['num_quarto']} está {item['status']}")
    
    escolha = int(input("\nEscolha o quarto a ser hospedado: "))
    for item in quartos:
        if item["num_quarto"]== escolha:
             item['nome_hospede'] = nome
             item["idade_hospede"] = idade
             item["status"] = status_quartos[1]
             print(f"Quarto {item['num_quarto']} foi ocupado pelo hóspede: {item['nome_hospede']} e se encontra {item['status']} no momento.")
             continue
        
       # if escolha != item["num_quarto"]:
           # print("!ERROR! Escolha uma opção válida!")
           # continue
    if resposta == 2:
        for item in quartos:


    



    

        


        

        







#[1] Realizar check-in → realizar_checkin()
#[2] Exibir mapa de quartos → listar_quartos()
#[3] Alterar status do quarto → atualizar_status()
#[4] Realizar check-out → realizar_checkout()
#[5] Liberar quarto após limpeza → liberar_quarto()
#[0] Sair → salvar_dados()

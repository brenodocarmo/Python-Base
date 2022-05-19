email_tml = """
     Olá, %(nome)s
    
     Tem interesse em cpmprar  %(produto)s?
    
     Este produto é ótimo oara resolver %(texto)s
    
     Clique agora em %(link)s
    
     Apenas %(quantidade)d disponiveis!
    
     Preço promocional %(preco).2f
     """
clientes = ["Maria", "Breno", "João"]


for cliente in clientes:
        print(
            email_tml 
            % {
                "nome": cliente, 
                "produto": "caneta", 
                "texto": "Escrever muito bom", 
                "link": "http://caneta.com", 
                "quantidade": 1, 
                "preco": 50.5,
                })
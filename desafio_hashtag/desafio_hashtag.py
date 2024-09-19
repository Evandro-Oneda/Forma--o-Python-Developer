import pandas as pd
from twilio.rest import Client
account_sid =''
auth_token = ''
client = Client(account_sid, auth_token)

lista_meses = ["janeiro","fevereiro", "março", "abril", "maio", "junho"]

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f"C:\Formação Python Developer\desafio_hashtag\{mes}.xlsx")
    #print(tabela_vendas)
    if (tabela_vendas ["Vendas"] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas ["Vendas"] > 55000, "Vendedor"].values[0]
        vendas =  tabela_vendas.loc[tabela_vendas ["Vendas"] > 55000,"Vendas"].values[0]
        message = client.messages.create(
            body = f' no mes de {mes} o vendedor {vendedor} bateu a meta com o valor de {vendas}',
            from_= '+',
            to='+')
        print(message.sid)
        


                

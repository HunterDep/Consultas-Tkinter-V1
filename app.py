from tkinter import *
import requests
import phonenumbers
from phonenumbers import carrier, parse, geocoder

def iniciar():
	# Janela do Programa
	janela = Tk()
	janela.geometry("200x200")
	global dados, puxar, informações
	Label(text="Consultas Básicas Tkinter\nCriado Por: (HunterDep)\nGithub: https://github.com/HunterDep").pack()
	Label().pack()
	Button(text="Consultar IP", command=consulta.ip).pack()
	Button(text="Consultar CEP", command=consulta.cep).pack()
	Button(text="Consultar Número", command=consulta.número).pack()
	dados = Entry()
	puxar = Button()
	informações = Label(text="")
	janela.mainloop()
	
class consulta():
	def ip():
		dados.config()
		dados.pack()
		puxar.config(text="Obter Informações IP", command=consulta.ipinfo)
		puxar.pack()
	def ipinfo():
		ip = dados.get()
		api = requests.get(f"http://ip-api.com/json/{ip}")
		api_json = api.json()
		lista_de_informações = []
		for info in api_json:
			lista_de_informações.append(f"[{info[0].upper()+info[1:]}] {api_json[info]}")
		lista_de_informações = "\n".join(lista_de_informações)
		informações.config(text=lista_de_informações)
		informações.pack()
			
	def cep():
		dados.config()
		dados.pack()
		puxar.config(text="Obter Informações do CEP", command=consulta.cepinfo)
		puxar.pack()
	def cepinfo():
		cep = dados.get()
		cep = cep.replace("-", "")
		cep = cep.replace(".", "")
		url = f"https://viacep.com.br/ws/{cep}/json/"
		try:
			api = requests.get(url)
			api_json = api.json()
			lista_de_informações = []
			for informação in api_json:
				lista_de_informações.append(f"[{informação[0].upper() + informação[1:]}] {api_json[informação]}")
			lista_de_informações = "\n".join(lista_de_informações)
			informações.config(text=lista_de_informações)
			informações.pack()
			
		except:
			informações.config(text="Ops... Verifique se o CEP existe ou se digitou certo :/")
			informações.pack()
			
	def número():
		dados.config()
		dados.pack()
		puxar.config(text="Obter Informações do Número", command=consulta.puxar_número)
		puxar.pack()
	def puxar_número():
		número = dados.get()
		número = número.replace(" ", "")
		número = número.replace("-", "")
		número = número.replace("+", "")
		número = número.replace("(", "")
		número = número.replace(")", "")
		try:
			número_phone = phonenumbers.parse(número, "BR")
			número_nacional = phonenumbers.format_number(número_phone, phonenumbers.PhoneNumberFormat.NATIONAL)
			número_internacional = phonenumbers.format_number(número_phone, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
			estado = geocoder.description_for_number(número_phone, "pt-br")
			operadora = carrier.name_for_number(número_phone, "pt-br")
			texto = f"""
Número (Nacional): {número_nacional}
Número (Internacional): {número_internacional}
Estado: {estado}
Operadora: {operadora}
			"""
			informações.config(text=texto)
			informações.pack()
		except:
			informações.config(text="Verifique se digitou o número de forma correta!")
			informações.pack()
			
if __name__ == "__main__":
	iniciar()
else:
	pass

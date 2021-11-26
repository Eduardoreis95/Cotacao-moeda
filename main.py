# Criar nosso aplicativo

from kivy.app import App
from kivy.lang import Builder
import requests

GUI = Builder.load_file('tela.kv')

class MeuAplicativo(App):
    def build(self):
        return GUI

    def on_start(self):
        self.pegar_cotacao('USD')
        self.root.ids['moeda1'].text = 'Dolar: R$5,61'
        self.root.ids['moeda2'].text = 'Euro: R$6,28'
        self.root.ids['moeda3'].text = 'Bitcoin: R$325.979,85'
        self.root.ids['moeda4'].text = 'Ethereum: R$24.282,20'
        
    def pegar_cotacao(self, moeda):
        link = f'https://economia.awesomeapi.com.br/last/{moeda}-BRL'
        requisicao = requests.get(link)
        dic_requisicao = requisicao.json()
        cotacao = dic_requisicao[f'{moeda}BRL']['bid']
        return cotacao


MeuAplicativo().run()
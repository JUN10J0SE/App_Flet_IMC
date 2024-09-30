#para gerara o executavel do app:
#pip instal pyinstaççer --> para gerar o executavel
#pip instal pillow --> para poder gerar o icone
#flet pack NOME_ARQUIVO_PRINCIPAL.py --icon NOME_DO_ICONE.png

#biblioteca
import flet as ft

#def principal
def main(page: ft.Page):
    #def de acao
    def acao(e):
        peso.value = float(peso.value)
        altura.value = float(altura.value)

        imc = peso.value / (altura.value ** 2)

        if imc <= 16.9:
            resultado.value = 'Você está muito abaixo do peso, procure ajuda!'
        elif imc < 18.5:
            resultado.value = 'Você esta baixo do peso '
        elif imc < 25:
            resultado.value = 'Voce esta em seu peso ideal, parabens. '
        elif imc < 30:
            resultado.value = 'Voce esta acima do seu peso ideal '
        elif imc > 35:
            resultado.value = 'Você está obeso'
        elif imc < 40:
            resultado.value ='Atencao, voce esta com obsidade de nivel 2'
        else:
            resultado.value = 'Voce esta com obesidade Morbida, procure ajuda URGENTE!'

        resultado.value += f'{imc:.2f}'

        page.update()


    page.title = 'Indice de Massa Corporal'
    page.scroll = 'daptive'
    page.theme_mode = ft.ThemeMode.LIGHT

    #Variaveis
    nome = ft.TextField(label = 'Infrome o seu nome:', color='red')
    idade = ft.TextField(label = 'Informe a sua Idade:',color='red')
    altura = ft.TextField(label = 'Informe a sua Altura',color='red')
    peso = ft.TextField(label = 'Informe o seu Peso:',color='red')
    resultado = ft.Text(size = 20)
    
    page.add(
        ft.Row(
            [ft.Text('Calculadora de IMC',size = 40, weight='bold',color='purple')],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [nome],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [idade],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [altura],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [peso],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [ft.ElevatedButton('Calcular IMC',color='purple',on_click=acao)],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [resultado],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

    page.update()

ft.app(main)
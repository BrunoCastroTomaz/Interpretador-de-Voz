print ("preparando....")

import speech_recognition as sr

import os

#Função para ouvir e reconhecer a fala
def ouvir_microfone():
    #Habilita o microfone do usuário
    microfone = sr.Recognizer()

    #usando o microfone
    with sr.Microphone() as source:
        #chama um algoritmo de redução de ruídos no som
        microfone.adjust_for_ambient_noise(source)
        #Frase para o usuário dizer algo...
        print("Diga alguma coisa:")
        #Armazena o que foi dito numa variável
        audio = microfone.listen(source)

    try:
        #Passa a variável para o algoritmo reconhecedor de padrões
        frase = microfone.recognize_google(audio,language='pt-BR')
        if "navegador Firefox" in frase:
            os.system("start Firefox.exe")
            return False
        elif "navegador Chrome" in frase:
            os.system("start Chrome.exe")
            return False
        elif "fechar" in frase:
            print("Encerrando aplicação....")
            return True
        else:
            #retorna a frase pronunciada
            print("Você disse: " + frase)
    except sr.UnknownValueError:
        print("Não entendi!")
        return False

def main():
    while True:
        if ouvir_microfone():
            break
    os.system("exit")
main()

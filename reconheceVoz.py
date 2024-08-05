print ("testando....")

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
        if "navegador" in frase:
            os.system("start Firefox.exe")
            return False
        elif "Excel" in frase:
            os.system("start Excel.exe")
            return False
        elif "PowerPont" in frase:
            os.system("start POWERPNT.exe")
            return False
        elif "Edge" in frase:
            os.system("start msedge.exe")
            return False
        elif "Fechar" in frase:
            os.system("exit")
            return True
        #retorna a frase pronunciada
        print("Você disse: " + frase)
    except sr.UnknownValueError:
        print("Não entendi")

    return frase
while True:
    if ouvir_microfone():
        break

# Nome da aplicação
print("="*50)
print("       Programa em Python para calcular IMC")
print("="*50)

# Apresentação sobre IMC
print("\n   O Índice de Massa Corporal (IMC) é um cálculo matemático rápido usado para avaliar se uma pessoa está dentro do peso ideal em relação à sua altura [Organização Mundial da Saúde (OMS)].\n" + 
"   O cálculo divide o peso (em quilos) pela altura (em metros) elevada ao quadrado.\n")

# Entrada do programa
idade_tabela_imc = input("  Primeiramente, você quer fazer IMC para:\n 🧒Crianças e jovens (De 0 a 19 anos);\n 👩Adultos (De 20 a 59 anos)\n 👴Ou idosos (60 ou mais)?\nResposta: ")

nome = input("\n✏ Qual seu nome? ")
idade = int(input("\n🗓 Qual a sua idade? "))
peso = float(input("\n⚖️ Qual o seu peso? "))
altura = float(input("\n📏 Qual sua altura? (Ex.: 1.6 metros) "))

# Processamento 
imc = peso / (altura * altura)


# ===============================================
# Crianças e jovens 
# ===============================================

if idade_tabela_imc in ["crianças", "jovens", "crianças/jovens"]:
    sexo = input("\nVocê é do sexo (♀) feminino ou (♂) masculino? ")
# Área de crianças / jovens femininos
    if sexo == "feminino":
        if (idade == 5):
            if(imc >= 12.7 and imc <= 16.9):
                print(f"\nA criança {nome} tem o IMC equivalente a: {imc:.2f}, sendo classificado(a) com um peso saudável.")
            elif (imc < 12.7):
                print(f"\nA criança está em estado de alerta para risco de magreza!")
            else:
                print(f"\nA criança está em estado de alerta para risco de obesidade!")

        if (idade == 6):
            if(imc >= 12.7 and imc <= 17.1):
                print(f"\nA criança {nome} tem o IMC equivalente a: {imc:.2f}, sendo classificado(a) com um peso saudável.")
            elif (imc < 12.7):
                print(f"\nA criança está em estado de alerta para risco de magreza!")
            else:
                print(f"\nA criança está em estado de alerta para risco de obesidade!")

        if (idade == 7):
            if(imc >= 12.7 and imc <= 17.5):
                print(f"\nA criança {nome} tem o IMC equivalente a: {imc:.2f}, sendo classificado(a) com um peso saudável.")
            elif (imc < 12.7):
                print(f"\nA criança está em estado de alerta para risco de magreza!")
            else:
                print(f"\nA criança está em estado de alerta para risco de obesidade!")

        if (idade == 8):
            if(imc >= 12.9 and imc <= 18.0):
                print(f"\nA criança {nome} tem o IMC equivalente a: {imc:.2f}, sendo classificado(a) com um peso saudável.")
            elif (imc < 12.9):
                print(f"\nA criança está em estado de alerta para risco de magreza!")
            else:
                print(f"\nA criança está em estado de alerta para risco de obesidade!")

        if (idade == 9):
            if(imc >= 13.1 and imc <= 18.7):
                print(f"\nA criança {nome} tem o IMC equivalente a: {imc:.2f}, sendo classificado(a) com um peso saudável.")
            elif (imc < 13.1):
                print(f"\nA criança está em estado de alerta para risco de magreza!")
            else:
                print(f"\nA criança está em estado de alerta para risco de obesidade!")

        if (idade == 10):
            if(imc >= 13.5 and imc <= 19.4):
                print(f"\nA criança {nome} tem o IMC equivalente a: {imc:.2f}, sendo classificado(a) com um peso saudável.")
            elif (imc < 13.5):
                print(f"\nA criança está em estado de alerta para risco de magreza!")
            else:
                print(f"\nA criança está em estado de alerta para risco de obesidade!")

        if (idade == 11):
            if(imc >= 13.9 and imc <= 20.3):
                print(f"\nA criança {nome} tem o IMC equivalente a: {imc:.2f}, sendo classificado(a) com um peso saudável.")
            elif (imc < 13.9):
                print(f"\nA criança está em estado de alerta para risco de magreza!")
            else:
                print(f"\nA criança está em estado de alerta para risco de obesidade!")
        
        if (idade == 12):
            if(imc >= 14.4 and imc <= 21.3):
                print(f"\nA criança {nome} tem o IMC equivalente a: {imc:.2f}, sendo classificado(a) com um peso saudável.")
            elif (imc < 14.4):
                print(f"\nA criança está em estado de alerta para risco de magreza!")
            else:
                print(f"\nA criança está em estado de alerta para risco de obesidade!")
        
        if (idade == 13):
            if(imc >= 14.9 and imc <= 22.3):
                print(f"\nA criança {nome} tem o IMC equivalente a: {imc:.2f}, sendo classificado(a) com um peso saudável.")
            elif (imc < 14.9):
                print(f"\nA criança está em estado de alerta para risco de magreza!")
            else:
                print(f"\nA criança está em estado de alerta para risco de obesidade!")
        
        if (idade == 14):
            if(imc >= 15.4 and imc <= 23.1):
                print(f"\nA criança {nome} tem o IMC equivalente a: {imc:.2f}, sendo classificado(a) com um peso saudável.")
            elif (imc < 15.4):
                print(f"\nA criança está em estado de alerta para risco de magreza!")
            else:
                print(f"\nA criança está em estado de alerta para risco de obesidade!")
        
        if (idade == 15):
            if(imc >= 15.9 and imc <= 23.8):
                print(f"\nA criança {nome} tem o IMC equivalente a: {imc:.2f}, sendo classificado(a) com um peso saudável.")
            elif (imc < 15.9):
                print(f"\nA criança está em estado de alerta para risco de magreza!")
            else:
                print(f"\nA criança está em estado de alerta para risco de obesidade!")
        
        if (idade == 16):
            if(imc >= 16.2 and imc <= 24.3):
                print(f"\nA criança {nome} tem o IMC equivalente a: {imc:.2f}, sendo classificado(a) com um peso saudável.")
            elif (imc < 16.2):
                print(f"\nA criança está em estado de alerta para risco de magreza!")
            else:
                print(f"\nA criança está em estado de alerta para risco de obesidade!")

        if (idade == 17):
            if(imc >= 16.4 and imc <= 24.6):
                print(f"\nA criança {nome} tem o IMC equivalente a: {imc:.2f}, sendo classificado(a) com um peso saudável.")
            elif (imc < 16.4):
                print(f"\nA criança está em estado de alerta para risco de magreza!")
            else:
                print(f"\nA criança está em estado de alerta para risco de obesidade!")
                        
        if (idade == 18):
            if(imc >= 16.4 and imc <= 24.8):
                print(f"\nA criança {nome} tem o IMC equivalente a: {imc:.2f}, sendo classificado(a) com um peso saudável.")
            elif (imc < 16.4):
                print(f"\nA criança está em estado de alerta para risco de magreza!")
            else:
                print(f"\nA criança está em estado de alerta para risco de obesidade!")


# Área de crianças / jovens masculinos
    elif sexo == "masculino":
        if (idade == 5):
            if(imc >= 13.0 and imc <= 16.6):
                print(f"\nA criança {nome} tem o IMC equivalente a: {imc:.2f}, sendo classificado(a) com um peso saudável.")
            elif (imc < 13.0):
                print(f"\nA criança está em estado de alerta para risco de magreza!")
            else:
                print(f"\nA criança está em estado de alerta para risco de obesidade!")

        if (idade == 6):
            if(imc >= 13.0 and imc <= 16.9):
                print(f"\nA criança {nome} tem o IMC equivalente a: {imc:.2f}, sendo classificado(a) com um peso saudável.")
            elif (imc < 13.0):
                print(f"\nA criança está em estado de alerta para risco de magreza!")
            else:
                print(f"\nA criança está em estado de alerta para risco de obesidade!")

        if (idade == 7):
            if(imc >= 13.1 and imc <= 17.2):
                print(f"\nA criança {nome} tem o IMC equivalente a: {imc:.2f}, sendo classificado(a) com um peso saudável.")
            elif (imc < 13.1):
                print(f"\nA criança está em estado de alerta para risco de magreza!")
            else:
                print(f"\nA criança está em estado de alerta para risco de obesidade!")

        if (idade == 8):
            if(imc >= 13.3 and imc <= 17.7):
                print(f"\nA criança {nome} tem o IMC equivalente a: {imc:.2f}, sendo classificado(a) com um peso saudável.")
            elif (imc < 13.3):
                print(f"\nA criança está em estado de alerta para risco de magreza!")
            else:
                print(f"\nA criança está em estado de alerta para risco de obesidade!")

        if (idade == 9):
            if(imc >= 13.5 and imc <= 18.2):
                print(f"\nA criança {nome} tem o IMC equivalente a: {imc:.2f}, sendo classificado(a) com um peso saudável.")
            elif (imc < 13.5):
                print(f"\nA criança está em estado de alerta para risco de magreza!")
            else:
                print(f"\nA criança está em estado de alerta para risco de obesidade!")

        if (idade == 10):
            if(imc >= 13.7 and imc <= 18.8):
                print(f"\nA criança {nome} tem o IMC equivalente a: {imc:.2f}, sendo classificado(a) com um peso saudável.")
            elif (imc < 13.7):
                print(f"\nA criança está em estado de alerta para risco de magreza!")
            else:
                print(f"\nA criança está em estado de alerta para risco de obesidade!")

        if (idade == 11):
            if(imc >= 14.1 and imc <= 19.5):
                print(f"\nA criança {nome} tem o IMC equivalente a: {imc:.2f}, sendo classificado(a) com um peso saudável.")
            elif (imc < 14.1):
                print(f"\nA criança está em estado de alerta para risco de magreza!")
            else:
                print(f"\nA criança está em estado de alerta para risco de obesidade!")
        
        if (idade == 12):
            if(imc >= 14.5 and imc <= 20.4):
                print(f"\nA criança {nome} tem o IMC equivalente a: {imc:.2f}, sendo classificado(a) com um peso saudável.")
            elif (imc < 14.5):
                print(f"\nA criança está em estado de alerta para risco de magreza!")
            else:
                print(f"\nA criança está em estado de alerta para risco de obesidade!")
        
        if (idade == 13):
            if(imc >= 14.9 and imc <= 21.3):
                print(f"\nA criança {nome} tem o IMC equivalente a: {imc:.2f}, sendo classificado(a) com um peso saudável.")
            elif (imc < 14.9):
                print(f"\nA criança está em estado de alerta para risco de magreza!")
            else:
                print(f"\nA criança está em estado de alerta para risco de obesidade!")
        
        if (idade == 14):
            if(imc >= 15.5 and imc <= 22.2):
                print(f"\nA criança {nome} tem o IMC equivalente a: {imc:.2f}, sendo classificado(a) com um peso saudável.")
            elif (imc < 15.5):
                print(f"\nA criança está em estado de alerta para risco de magreza!")
            else:
                print(f"\nA criança está em estado de alerta para risco de obesidade!")
        
        if (idade == 15):
            if(imc >= 16.0 and imc <= 22.7):
                print(f"\nA criança {nome} tem o IMC equivalente a: {imc:.2f}, sendo classificado(a) com um peso saudável.")
            elif (imc < 16.0):
                print(f"\nA criança está em estado de alerta para risco de magreza!")
            else:
                print(f"\nA criança está em estado de alerta para risco de obesidade!")
        
        if (idade == 16):
            if(imc >= 16.3 and imc <= 23.1):
                print(f"\nA criança {nome} tem o IMC equivalente a: {imc:.2f}, sendo classificado(a) com um peso saudável.")
            elif (imc < 16.3):
                print(f"\nA criança está em estado de alerta para risco de magreza!")
            else:
                print(f"\nA criança está em estado de alerta para risco de obesidade!")

        if (idade == 17):
            if(imc >= 16.4 and imc <= 24.3):
                print(f"\nA criança {nome} tem o IMC equivalente a: {imc:.2f}, sendo classificado(a) com um peso saudável.")
            elif (imc < 16.4):
                print(f"\nA criança está em estado de alerta para risco de magreza!")
            else:
                print(f"\nA criança está em estado de alerta para risco de obesidade!")
                        
        if (idade == 18):
            if(imc >= 17.3 and imc <= 24.9):
                print(f"\nA criança {nome} tem o IMC equivalente a: {imc:.2f}, sendo classificado(a) com um peso saudável.")
            elif (imc < 17.3):
                print(f"\nA criança está em estado de alerta para risco de magreza!")
            else:
                print(f"\nA criança está em estado de alerta para risco de obesidade!") 
    else:
        print("\nDigite o seu gênero para que possamos realizar o cálculo infanto-juvenil")



# ===============================================
# Adultos 
# ===============================================
elif idade_tabela_imc in ["adultos", "adulto", "Adultos", "adultos"]:
    if imc < 18.5:
        print(f"\nA pessoa {nome} tem o IMC equivalente a: {imc:.2f}, sendo classificado com magreza.")
    elif (imc >=18.5 and imc <= 24.9):
        print(f"\nA pessoa {nome} tem o IMC equivalente a: {imc:.2f}, sendo classificado com peso normal.")
    elif (imc >=25.0 and imc <= 29.9):
        print(f"\nA pessoa {nome} tem o IMC equivalente a: {imc:.2f}, sendo classificado com pré-obesidade.")
    elif (imc >=30.0 and imc <= 34.9):
        print(f"\nA pessoa {nome} tem o IMC equivalente a: {imc:.2f}, sendo classificado com obesidade de grau I.")
    elif (imc >=35.0 and imc <= 39.9) :
        print(f"\nA pessoa {nome} tem o IMC equivalente a: {imc:.2f}, sendo classificado com obesidade de grau II.")
    else:
        print(f"\nA pessoa {nome} tem o IMC equivalente a: {imc:.2f}, sendo classificado com obesidade de grau III.")


# ===============================================
# Idosos
# ===============================================
elif idade_tabela_imc in ["idosos", "Idosos", "idoso", "Idoso"]:
    if imc <= 22.0:
        print(f"\nA pessoa {nome} tem o IMC equivalente a: {imc:.2f}, sendo classificado com magreza.")
    elif (imc > 22.0 and imc <= 27.0):
        print(f"\nA pessoa {nome} tem o IMC equivalente a: {imc:.2f}, sendo classificado com peso adequado.")
    elif (imc >=27.1 and imc <= 32.0):
        print(f"\nA pessoa {nome} tem o IMC equivalente a: {imc:.2f}, sendo classificado com pré-obesidade ou exesso de peso leve.")
    elif (imc >=32.1 and imc <= 37.0):
        print(f"\nA pessoa {nome} tem o IMC equivalente a: {imc:.2f}, sendo classificado com obesidade de grau I.")
    elif (imc >=37.1 and imc <= 32.1) :
        print(f"\nA pessoa {nome} tem o IMC equivalente a: {imc:.2f}, sendo classificado com obesidade de grau II.")
    else:
        print(f"\nA pessoa {nome} tem o IMC equivalente a: {imc:.2f}, sendo classificado com obesidade de grau III.")

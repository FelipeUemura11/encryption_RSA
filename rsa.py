def mod_pow(base, exp, mod):
    resultado = 1
    base = base % mod

    while exp > 0:
        if exp % 2 == 1:
            resultado = (resultado * base) % mod
        base = (base * base) % mod
        exp = exp // 2 
    
    return resultado

def criptografarCaractere(caractere, e, n):
    return mod_pow(ord(caractere), e, n)

def descriptografarCaractere(caractere, d, n):
    return chr(mod_pow(caractere, d, n))

def main():

    p = 17
    q = 23
    e = 17

    n = p * q
    phi = (p - 1) * (q - 1)

    d = 1
    while((d * e) % phi != 1):
        d = d + 1

    while True:
        print("========= RSA =========")
        print("[1] Criptografar    < ")
        print("[2] Descriptografar < ")
        print("[3] Sair            < ")
        print("========= RSA =========")

        opc = int(input(" >> Escolha uma das opcoes: "))

        if opc == 1:
            mensagem = input("Informe a mensagem: ")
            cripto = [0] * len(mensagem)

            print(f"Mensagem original: {mensagem}")
            print("Mensagem criptografada: ", end="")

            for i in range(len(mensagem)):
                cripto[i] = criptografarCaractere(mensagem[i], e, n)
                print(f"{cripto[i]}", end=" ")
            print()

        elif opc == 2:
            try:
                mensagem_cripto = input("Informe a mensagem criptografada (números separados por espaço): ")
                numeros = [int(x) for x in mensagem_cripto.split()]
                mensagem_original = ""

                for num in numeros:
                    mensagem_original += descriptografarCaractere(num, d, n)
                
                print(f"Mensagem descriptografada: {mensagem_original}")
            except ValueError:
                print("Erro: Por favor, insira números válidos separados por espaço.")
            except Exception as e:
                print(f"Erro ao descriptografar: {str(e)}")

        elif opc == 3:
            print("Saindo...")
            break

        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()

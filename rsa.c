#include<stdio.h>
#include<stdlib.h>
#include<time.h>

int verificar(int primo){
    // return 1 ---- primo
    // return 0 ---- nao primo
    if(primo < 2){
        return 0;
    }

    if(primo == 2){
        return 1;
    }

    if(primo % 2 == 0){
        return 0;
    }

    for(int i = 3; i < primo; i += 2){
        if(primo % i == 0){
            return 0;
        }
    }

    return 1;
}

// Função para calcular o MDC (Máximo Divisor Comum)
int mdc(int a, int b) {
    int temp;
    while (b != 0) {
        temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

int gerar_primo(int min_val, int max_val) {
    int primo;
    do {
        primo = rand() % (max_val - min_val + 1) + min_val;
    } while (verificar(primo) != 1);
    return primo;
}

int main(void){
    // Inicializa o gerador de números aleatórios
    srand(time(NULL));

    int p, q, n, phi, e, d;

    p = gerar_primo(2, 100);
    q = gerar_primo(2, 100);

    // Calcula n e phi(totiente de n)
    n = p * q;
    phi = (p - 1) * (q - 1);

    // Encontra um valor para e que seja coprimo com phi
    for(e = 2; e < phi; e++){
        if(mdc(e, phi) == 1){
            break;
        }
    }

    // Encontra o valor de d (inverso multiplicativo de e módulo phi)
    for(d = 2; d < phi; d++){
        if((e * d) % phi == 1){
            break;
        }
    }

    printf("p: %d\n", p);
    printf("q: %d\n", q);
    printf("n: %d\n", n);
    printf("phi: %d\n", phi);
    printf("e: %d\n", e);
    printf("d: %d\n", d);

    return 0;
}
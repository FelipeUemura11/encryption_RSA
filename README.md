# 🔐 RSA - Criptografia
## 📘 O que é o RSA?

O RSA é um algoritmo de **criptografia assimétrica**, ou seja, usa **duas chaves diferentes**:

- **Chave pública**: usada para criptografar.
- **Chave privada**: usada para descriptografar.

Esse sistema permite que uma mensagem seja enviada de forma segura, mesmo que todos conheçam a chave pública.

---

## 🛠️ Etapas do Algoritmo

### 1. **Geração das Chaves**

- Escolha dois números primos grandes: `p` e `q`
- Calcule `n = p * q`
- Calcule o totiente: `φ(n) = (p - 1)(q - 1)`
- Escolha um número `e` tal que `1 < e < φ(n)` e `mdc(e, φ(n)) = 1`
- Calcule `d`, o inverso modular de `e` em relação a `φ(n)`

> **Chave pública**: `(n, e)`  
> **Chave privada**: `(n, d)`

---

### 2. **Criptografia**

Para criptografar uma mensagem (já convertida em número `m`):

c = m^e mod n

O resultado `c` é a **mensagem criptografada**.

---

### 3. **Descriptografia**

Para recuperar a mensagem original:

m = c^d mod n


---

## 🔢 Conversão de texto para número

Antes de aplicar RSA, o texto deve ser transformado em número, normalmente por:

- **ASCII ou UTF-8**: cada caractere vira um número (ex: "A" → 65)
- Concatenar os números com tamanho fixo (ex: "AB" → "065066")

Depois da descriptografia, basta converter os números de volta para texto.

---

## ✅ Exemplo simples

- `p = 3`, `q = 11` → `n = 33`
- `φ(n) = 20`
- `e = 3`
- `d = 7`

Mensagem `m = 4`

Criptografar: c = 4^3 mod 33 = 31
Descriptografar: m = 31^7 mod 33 = 4

Mensagem recuperada com sucesso!

---

## 💡 Aplicações do RSA

- Criptografia de mensagens
- Assinaturas digitais
- Certificados SSL/TLS
- Autenticação de usuários

---

## 🚧 Observações

- O RSA é seguro pois **fatorar `n` em `p` e `q` é muito difícil** para números grandes.
- Em aplicações reais, bibliotecas como OpenSSL, PyCryptodome ou Crypto++ são usadas.
- Para dados grandes, o RSA costuma cifrar apenas **chaves de sessão**, enquanto os dados são protegidos com criptografia simétrica (como AES).


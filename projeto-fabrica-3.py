produto = input("Produto (ex.: Arroz 5kg): ")

mercado1 = input("Nome do supermercado 1: ")
preco1 = float(input(f"Preço no {mercado1} (use ponto, ex.: 27.90): "))

mercado2 = input("Nome do supermercado 2: ")
preco2 = float(input(f"Preço no {mercado2} (use ponto, ex.: 27.90): "))

mercado3 = input("Nome do supermercado 3: ")
preco3 = float(input(f"Preço no {mercado3} (use ponto, ex.: 27.90): "))

menor = min(preco1, preco2, preco3)

mercado_barato = []

if preco1 == menor:
    mercado_barato.append(mercado1)
if preco2 == menor:
    mercado_barato.append(mercado2)
if preco3 == menor:
    mercado_barato.append(mercado3)
    
print(f"\n=== Resultado ===\nProduto: {produto}\nMais barato em: {', '.join(mercado_barato)}\nPreço: {menor}")
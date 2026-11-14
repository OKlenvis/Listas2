livros = [
    [1, "O Senhor dos Anéis", "J.R.R. Tolkien", 1954],
    [2, "Harry Potter e a Pedra Filosofal", "J.K. Rowling", 1997],
    [3, "O Código Da Vinci", "Dan Brown", 2003],
]

titulo_procurado = "Harry Potter e a Pedra Filosofal"

for livro in livros:
    if livro[1] == titulo_procurado:
        print("Livro Encontrado!")
        break

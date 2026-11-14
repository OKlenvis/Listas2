livros = [
    [1, "O Senhor dos Anéis", "J.R.R. Tolkien", 1954],
    [2, "Harry Potter e a Pedra Filosofal", "J.K. Rowling", 1997],
    [3, "O Código Da Vinci", "Dan Brown", 2003],
]

id_procurado = bool(99)

for id in livros:
    print("\nProcurando livro com o ID 99...\n")
    if id[0] == id_procurado:
        print("Livro não encontrado")
        break

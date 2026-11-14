livros = [
    [1, "O Senhor dos Anéis", "J.R.R. Tolkien", 1954],
    [2, "Harry Potter e a Pedra Filosofal", "J.K. Rowling", 1997],
    [3, "O Código Da Vinci", "Dan Brown", 2003],
]

id_remover = 3

for indice, livro in enumerate(livros):
    if livro[0] == id_remover:
        livros.pop(indice)
        break

print(f"{livros}\n")
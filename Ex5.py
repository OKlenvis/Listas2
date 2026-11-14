livros = [
    [1, "O Senhor dos Anéis", "J.R.R. Tolkien", 1954],
    [2, "Harry Potter e a Pedra Filosofal", "J.K. Rowling", 1997],
    [3, "O Código Da Vinci", "Dan Brown", 2003],
]

livros[0][3] = 2024


for i in livros:
    print(f"\nID: {i[0]} | O livro {i[1]} foi escrito por {i[2]} e lançado em {i[3]}")
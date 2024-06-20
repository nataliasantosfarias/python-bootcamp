contatos = {
    "eliene.farias.aju@gmail.com" : {"nome" : "Eliene", "Telefone" : "3333-2221"},
    "alisson.farias.aju@gmail.com" : {"nome" : "Alisson", "Telefone" : "3333-2222"},
    "priscila.farias.aju@gmail.com" : {"nome" : "Priscila", "Telefone" : "3333-2223"},
    "juliana.farias.aju@gmail.com" : {"nome" : "Juliana", "Telefone" : "3333-2224" , "extra": {"a": 1}},
}

telefone = contatos["eliene.farias.aju@gmail.com"],["telefone"]
print(telefone)

extra = contatos["juliana.farias.aju@gmail.com"],["extra"],["a"] # type: ignore
print(extra)

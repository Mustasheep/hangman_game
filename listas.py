import unicodedata

lista1 = [
    "Cachorro",
    "Gato",
    "Elefante",
    "Leão",
    "Tigre",
    "Girafa",
    "Macaco",
    "Zebra",
    "Cavalo",
    "Vaca",
    "Porco",
    "Ovelha",
    "Galinha",
    "Pato",
    "Ganso",
    "Peru",
    "Coelho",
    "Hamster",
    "Rato",
    "Cobra",
    "Lagarto",
    "Tartaruga",
    "Crocodilo",
    "Tubarão",
    "Baleia",
    "Golfinho",
    "Pinguim",
    "Águia",
    "Coruja",
    "Papagaio",
    "Canário",
    "Abelha",
    "Formiga",
    "Borboleta",
    "Joaninha",
    "Aranha",
    "Escorpião",
    "Caranguejo",
    "Camarão",
    "Polvo",
    "Estrela-do-mar",
    "Água-viva",
]

animais_processo = [
    unicodedata.normalize('NFKD', animal).encode('ASCII', 'ignore').decode('ASCII')
    for animal in lista1
]

frutas = [
    "abacaxi",
    "abacate",
    "acerola",
    "ameixa",
    "banana",
    "caja",
    "carambola",
    "cereja",
    "framboesa",
    "goiaba",
    "graviola",
    "jabuticaba",
    "laranja",
    "lima",
    "limao",
    "maçã",
    "mamao",
    "manga",
    "maracuja",
    "melancia",
    "melao",
    "morango",
    "pera",
    "pessego",
    "pitanga",
    "tangerina",
    "uva"
]

cor_processo = [
    "Preto",
    "Branco",
    "Cinza",
    "Vermelho",
    "Verde",
    "Azul",
    "Amarelo",
    "Laranja",
    "Marrom",
    "Rosa",
    "Roxo",
    "Violeta",
    "Turquesa",
    "Bege",
    "Dourado",
    "Prateado",
    "Ciano",
    "Magenta",
    "Indigo",
    "Salmao",
    "Carmim",
    "Coral",
    "Esmeralda",
    "Rubi",
    "Safira",
    "Ametista",
    "Jade",
    "Ambar"
]

cor = [item.lower() for item in cor_processo]
animais = [item.lower() for item in animais_processo]

listas = frutas, animais, cor
print(listas)
import random

def create_large_file(filename):
    vocab = ["кавун", "ананс", "банан", "океан", "туман", "небо", "сонце",
             "планета", "антена", "кант", "букву", "на", "у", "ангар"]

    with open(filename, 'w', encoding='utf-8') as f:
        for _ in range(105):
            line = []
            while sum(len(w) for w in line) < 110:
                line.append(random.choice(vocab))
            f.write(" ".join(line) + "\n")


create_large_file('large_text.txt')
print("Файл успішно створено!")
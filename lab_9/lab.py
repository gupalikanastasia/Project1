import string

def pair_counter_generator(filename, target_pairs):
    with open(filename, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            counts = {pair: 0 for pair in target_pairs}

            words = line.lower().split()

            for word in words:
                word = word.strip(string.punctuation)
                for i in range(len(word) - 1):
                    current_pair = word[i] + word[i + 1]

                    if current_pair in counts:
                        counts[current_pair] += 1

            yield line_num, counts
pairs_to_find = ['ан', 'на', 'не']
file_path = 'large_text.txt'

total_stats = {pair: 0 for pair in pairs_to_find}

try:
    gen = pair_counter_generator(file_path, pairs_to_find)

    print(f"{'Рядок':<10} | {'Результати по рядку'}")

    for line_number, result in gen:
        res_str = ", ".join([f"{k}: {v}" for k, v in result.items()])
        print(f"{line_number:<10} | {res_str}")

        for pair, count in result.items():
            total_stats[pair] += count

    print("ЗАГАЛЬНА КІЛЬКІСТЬ У ВСЬОМУ ФАЙЛІ:")
    for pair, count in total_stats.items():
        print(f"Пара '{pair}': {count}")

except FileNotFoundError:
    print("Файл не знайдено.")
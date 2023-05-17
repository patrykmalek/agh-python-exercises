import re


def count_bigrams_and_trigrams(filename):
    bigram_counts = {}
    trigram_counts = {}

    with open(filename, 'r', encoding='utf-8') as file:
        file_content = file.read()  # zły pomysł; proszę to zrobić z Wikipedią
        file_content = re.sub(r'[^\w\s]|_', ' ', file_content)
        file_content = file_content.lower()

        words = file_content.split()
        # bigrams, utworzenie bigramu, każde dwa następne słowa tworzą bigram
        for i, word in enumerate(words[:-1]):  # do przedostatniego słowa
            bigram = f'{word} {words[i + 1]}'
            if bigram in bigram_counts:
                bigram_counts[bigram] += 1
            else:
                bigram_counts[bigram] = 1

        # trigrams
        for i, word in enumerate(words[:-2]):  # do przed przedostatniego słowa  # szkoda, że w poleceniu nie było n-gramów od 2 do 10
            trigram = f'{word} {words[i + 1]} {words[i + 2]}'
            if trigram in trigram_counts:
                trigram_counts[trigram] += 1
            else:
                trigram_counts[trigram] = 1
    sorted_bigram_counts_list = sorted(bigram_counts.items(), key=lambda x: (-x[1], x[0]))
    sorted_trigram_counts_list = sorted(trigram_counts.items(), key=lambda x: (-x[1], x[0]))
    sorted_bigram_counts_dict = {bigram: count for bigram, count in sorted_bigram_counts_list}
    sorted_trigram_counts_dict = {trigram: count for trigram, count in sorted_trigram_counts_list}
    return sorted_bigram_counts_dict, sorted_trigram_counts_dict


def display_n_most_common_bi_tri_gram(n_grams, n):
    n_grams_to_display = list(n_grams.items())
    for i, (n_gram, count) in enumerate(n_grams_to_display):
        if i >= n and count != n_grams_to_display[i - 1][1]:
            break
        print(f'{i + 1}. {n_gram}: {count}')


FILE_NAME = "potop.txt"
bigrams, trigrams = count_bigrams_and_trigrams(FILE_NAME)
print(f'\nZnaleziono {sum(bigrams.values())} wszystkich bigramów.')
N_MOST_COMMON_BIGRAMS = int(input('Ile najczęściej występujących bigramów wypisać?\n'))
display_n_most_common_bi_tri_gram(bigrams, N_MOST_COMMON_BIGRAMS)
print(f'\nZnaleziono {sum(trigrams.values())} wszystkich trigramów.')
N_MOST_COMMON_TRIGRAMS = int(input('Ile najczęściej występujących trigramów wypisać?\n'))
display_n_most_common_bi_tri_gram(trigrams, N_MOST_COMMON_TRIGRAMS)

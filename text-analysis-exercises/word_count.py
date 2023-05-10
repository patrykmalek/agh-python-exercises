import re


def count_words(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        word_counts = {}
        # czytanie linia po linii
        for line in file:
            # wyczyszczenie linii ze wszystkich znaków, które nie są literą,
            # cyfrą ani znakami białymi (podkreślenia, spacje)
            line = re.sub(r'[^\w\s]', '', line)
            line = line.lower()

            words = line.split()

            for word in words:
                if word in word_counts:
                    word_counts[word] += 1
                else:
                    word_counts[word] = 1

    #  Sortowanie najpierw malejąco po ilości wystąpień, a jeśli ilość wystąpień będzie taka sama,
    #  to sortowanie alfabetycznie po słowach
    sorted_word_counts_list = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))
    sorted_word_counts_dict = {word: count for word, count in sorted_word_counts_list}
    return sorted_word_counts_dict


def display_n_most_common_words(sorted_words, n):
    words_and_counts_tuples = list(sorted_words.items())
    for i, (word, count) in enumerate(words_and_counts_tuples):
        if i >= n and count != words_and_counts_tuples[i - 1][1]:
            break
        print(f'{i + 1}. {word}: {count}')


FILE_NAME = "potop.txt"
N_MOST_COMMON = int(input('Ile najczęściej występujących słów wypisać?\n'))
words_dict = count_words(FILE_NAME)
total_words = sum(words_dict.values())
print(f'Znaleziono {total_words} wszystkich różnych słów.')
print(f'Poniżej {N_MOST_COMMON} najczęściej występujących słów.')
display_n_most_common_words(words_dict, N_MOST_COMMON)

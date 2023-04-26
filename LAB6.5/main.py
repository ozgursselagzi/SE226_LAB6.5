def common_elements():
    list1 = list(map(int, input("\nEnter the elements of first list separated by space: ").split()))
    list2 = list(map(int, input("\nEnter the elements of second list separated by space: ").split()))
    set1 = set(list1)
    set2 = set(list2)
    common = set1.intersection(set2)
    return list(common)


def palindrome_words():
    string_list = input("\nEnter the list of strings separated by space: ").split()
    palindromes = [string for string in string_list if string == string[::-1]]
    return palindromes


def prime_numbers():
    num_list = list(map(int, input("\nEnter the list of integers separated by space: ").split()))
    primes = []
    is_prime = [True] * (max(num_list) + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(max(num_list) ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, max(num_list) + 1, i):
                is_prime[j] = False
    for num in num_list:
        if is_prime[num]:
            primes.append(num)
    return primes


def find_anagrams(word, word_list):
    word_chars = sorted(word.lower().replace(" ", ""))
    anagrams = []
    for w in word_list:
        w_chars = sorted(w.lower().replace(" ", ""))
        if w_chars == word_chars:
            anagrams.append(w)
    return anagrams


common = common_elements()
print("\nCommon elements are:", common)

palindromes = palindrome_words()
print("\nPalindrome words are:", palindromes)

primes = prime_numbers()
print("\nPrime numbers are:", primes)

word = "listen"
word_list = ["enlists", "google", "inlets", "banana"]
anagrams = find_anagrams(word, word_list)
print()
print(anagrams)

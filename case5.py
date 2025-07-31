def word_length(words):
    wl = {w: len(w) for w in words}
    return wl


from math import inf


def shortest_actual_words(words):
    data = word_length(words)
    shortest = None  # initial value for shortest word length
    second_shortest = None  # initial value for next shortest word length
    shortest_word = ""  # initial value for shortest actual word
    next_shortest_word = ""  # initial value for next shortest actual word
    for key in data:
        length = data[key]

        if shortest is None or length < data[shortest]:
            second_shortest = shortest
            shortest = key
        elif (
            second_shortest is None or length < data[second_shortest]
        ) and key != shortest:
            second_shortest = key

    return [shortest, second_shortest] if second_shortest else [shortest]


print(shortest_actual_words(["cc", "cc"]))  # should return ["cc", "cc"]
print(shortest_actual_words(["x", "long", "y"]))  # should return ["x", "y"]
print(shortest_actual_words(["water", "sun", "vim"]))
print(shortest_actual_words(["aha", "blue", "ha"]))  # should return ["aha", "ha"]
print(shortest_actual_words(["a", "b", "ccc", ""]))  # should return ["a", "b"]
print(shortest_actual_words(["ccc", ""]))  # should return [""]
print(shortest_actual_words([]))  # should return [""]

print(shortest_actual_words(["a", "b", "c", "d"]))  # should return ["a", "b"]
print(shortest_actual_words(["hello", "", "world", ""]))  # should return ["", ""]

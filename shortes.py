from math import inf


def word_length(words):
    wl = {w: len(w) for w in words}
    return wl


def shortest_actual_words(words):
    wl = word_length(words)
    s = inf  # initial value for shortest word length
    ns = inf  # initial value for next shortest word length
    sw = ""  # initial value for shortest actual word
    nsw = ""  # initial value for next shortest actual word
    if not wl:
        return [""]
    if len(wl) == 1:
        return [wl.pop()]
    if len(wl) == 2:
        return [k for k, v in wl.items() if v == min(wl.values())]
    else:
        values_list = list(wl.values())
        keys_list = list(wl.keys())
        s = min(wl.values())
        s_index = values_list.index(s)
        key_to_remove = keys_list[s_index]
        del wl[key_to_remove]
        ns = min(v for v in wl.values() if v >= s)
        wl[key_to_remove] = s
        sn_index = values_list.index(ns)
        sw = next(k for k, v in wl.items() if v == values_list[-1])
        nsw = next(k for k, v in wl.items() if v == values_list[sn_index])
    return [sw, nsw]


print(shortest_actual_words(["cc", "cc"]))  # should return ["cc", "cc"]
print(shortest_actual_words(["x", "long", "y"]))  # should return ["x", "y"]
print(shortest_actual_words(["water", "sun", "vim"]))
print(shortest_actual_words(["aha", "blue", "ha"]))  # should return ["aha", "ha"]
print(shortest_actual_words(["a", "b", "ccc", ""]))  # should return ["a", "b"]
print(shortest_actual_words(["ccc", ""]))  # should return [""]
print(shortest_actual_words([]))  # should return [""]

print(shortest_actual_words(["a", "b", "c", "d"]))  # should return ["a", "b"]
print(shortest_actual_words(["hello", "", "world", ""]))  # should return ["", ""]

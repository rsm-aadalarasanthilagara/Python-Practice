def word_length(words):
    wl = {w: len(w) for w in words}
    return wl


def mean_word_length(words):
    wl = word_length(words)
    wl_sum = 0
    wl_mean = 0.0
    if len(words) == 0:
        return 0.0
    else:
        val_lst = [v for v in wl.values()]
        for i in val_lst:
            wl_sum += i
    wl_mean = wl_sum / len(val_lst)
    return wl_mean  # mean word length


print(mean_word_length(["mouse", "king", "on"]))  # should return 3.666667
print(mean_word_length(["tax", "house", "blue"]))  # should return 4
print(mean_word_length(["purple", "red", "turquoise"]))  # should return 6

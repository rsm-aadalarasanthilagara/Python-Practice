from math import floor


def word_length(words):
    wl = {w: len(w) for w in words}
    return wl


def median_word_length(words):
    wl = list({w: len(w) for w in words}.values())
    len_wl = len(wl)
    wl.sort()
    if len_wl == 0:
        return 0.0
    elif len_wl % 2 == 1:
        return wl[floor(len_wl / 2)]
    else:
        mid_index = len_wl // 2
        return (wl[mid_index - 1] + wl[mid_index]) / 2.0


print(median_word_length(["mouse", "on"]))  # should return 3.5
print(median_word_length(["tax", "house", "blue"]))  # should return 4
print(median_word_length(["purple", "red", "turquoise"]))  # should return 6

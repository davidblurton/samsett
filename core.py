word_list = set(x.strip() for x in open("./ordmyndalisti.txt"))


def is_word(word):
    return word in word_list


def partitions(s, k):
    if k == 0:
        yield [s]
        return
    for i in range(1, len(s)):
        for tail in partitions(s[i:], k - 1):
            yield [s[:i]] + tail


def valid(partitions):
    for i in partitions:
        if all(is_word(word.lower()) for word in i):
            yield i


def split(input, count=1):
    result = list(valid(partitions(input, count)))

    if result or count == len(input):
        return result
    else:
        return split(input, count + 1)

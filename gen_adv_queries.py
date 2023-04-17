import random
number_per_variation = 5
rf = open("../pcap_filter_with_gpt/NL_queries/english_query_base.txt", 'r')
wf = open("../pcap_filter_with_gpt/NL_queries/adversarials.txt", 'w')

# remove letters
def removeLetters(query):
    min_word_len = 4
    l = []
    for k in range(number_per_variation):
        words = query.replace("?", "").split(" ")
        for i in range(len(words)):
            word = words[i]
            if len(word) > min_word_len:
                idx = random.randint(0, len(word) - 1)
                words[i] = word[:idx] + word[idx+1:]
        new_query = " ".join(words)
        if query[-1] == "?":
            new_query += "?"
        new_query += '\n'
        l.append(new_query)
    return l

# find neighbor keys
def get_neighbor_keys(key):
    lines = 'qwertyuiop', 'asdfghjkl', 'zxcvbnm'
    line_index, index = [(i, l.find(key)) for i, l in enumerate(lines) if key in l][0]
    lines = lines[line_index-1: line_index+2] if line_index else lines[0: 2]
    return [
        line[index + i] for line in lines for i in [-1, 0, 1]
        if len(line) > index + i and line[index + i] != key and index + i >= 0]

def neighbor_keys(query):
    min_word_len = 4
    l = []
    for k in range(number_per_variation):
        words = query.replace("?", "").split(" ")
        for i in range(len(words)):
            word = words[i]
            if len(word) > min_word_len:
                idx = random.randint(0, len(word) - 1)
                var = get_neighbor_keys(word[idx])
                v = var[random.randint(0, len(var) -1)]
                words[i] = word[:idx] + v + word[idx+1:]
        new_query = " ".join(words)
        if query[-1] == "?":
            new_query += "?"
        new_query += '\n'
        l.append(new_query)
    return l


# replace letter with number
def let2num(query):
    s = query
    max_swaps = 3
    d = {'e':'3', 'l':'1', 'o':'0', 'a':'4', 's':'5', 'b':'8', 't':'7'}
    l = []
    for k in range(number_per_variation):
        query = s
        i = 0
        while i < max_swaps:
            idx = random.randint(0, len(query[:-1]) - 1)
            if query[idx] in d:
                query = query[:idx] + d[query[idx]] + query[idx+1:]
                i+=1
                print(i)
        query += '\n'
        l.append(query)
    return l

for query in rf.readlines():
    wf.write(query)
    query = query.replace('\n', "")
    l1 = removeLetters(query)
    l2 = let2num(query)
    l3 = neighbor_keys(query)

    for adv_queries in [l1, l2, l3]:
        for aq in adv_queries:
            wf.write(aq.replace('\n', ''))
            wf.write('\n')
    wf.write('\n')





word_list = ['Sunday', 'Monday', 'Tuseday', 'Wedensday', 'Thursday', 'Friday', 'Shabbos']

def for_loop_length(your_list):
    for_loop_result = []
    for word in your_list:
        for_loop_result.append(len(word))
    return for_loop_result

map_result = list(map(len, word_list))

print(for_loop_length(word_list))
print(map_result)
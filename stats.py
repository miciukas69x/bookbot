def number_of_words(text):
    words = text.split()
    return len(words)

def characters_count(text):
    char_counts = {}
    for char in text:
        lowercase_char = char.lower()
        if lowercase_char in char_counts:
            char_counts[lowercase_char] += 1
        else:
            char_counts[lowercase_char] = 1
    return char_counts

def sorted_list (char_counts):
    list_of_dicts = [{"char": key, "count": value} for key, value in char_counts.items() if key.isalpha()]
    list_of_dicts.sort(key=lambda x: x["count"], reverse=True)
    return list_of_dicts
    
   

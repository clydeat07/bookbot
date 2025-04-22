def get_num_words(text): 
    words = text.split()
    return len(words)
def count_characters(text):
    character_count = {}
    
    lowered_text = text.lower()
    
    for char in lowered_text:
        
        if char in character_count:
            character_count[char] += 1
        
        else:
            character_count[char] = 1
     
    return character_count

def sort_dict(character_count):
    chars_list = []
    
    for char, count in character_count.items():
        char_dict = {"char": char, "count": count}
        chars_list.append(char_dict)
    
    def sort_on(dict):
        return dict["count"]
    
    chars_list.sort(reverse=True, key=sort_on)
    
    return chars_list

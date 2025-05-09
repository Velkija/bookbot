def sort_character_counts(char_dict):
    
    chars_list = []
    for char, count in char_dict.items():
        chars_list.append({"char": char, "count": count})
    
   
    def sort_on(dict):
        return dict["count"]
    
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list

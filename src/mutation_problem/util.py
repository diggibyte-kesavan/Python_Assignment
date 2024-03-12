def mutate_string(string, position, character):
    string_list = list(string)  # convert the string into list
    string_list[position] = character
    mutated_string = ''.join(string_list)  # join the list back into string
    return mutated_string

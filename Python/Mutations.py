def mutate_string(string, position, character):
    new_string = list(string)
    new_string[position] = character
    another_new_string_for_godssake = ''.join(new_string)
    return another_new_string_for_godssake

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

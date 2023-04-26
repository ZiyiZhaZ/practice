def create_list(phrase):
    return phrase.split(' ')

def get_first_letters(word_list):
    x = []
    for i in word_list:
       x.append(i[0]) 
    return "".join(x)

print(create_list("California State University"))
print(get_first_letters(["California", "State", "University"]))

phrase = "Self Contained Underwater Breathing Apparatus"
word_list = create_list(phrase)
acronym = get_first_letters(word_list)
print(acronym)
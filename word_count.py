

# text = 'The Marvel Cinematic Universe (MCU) a  centers Marvel a Cinematic a series of American superhero films produced by Marvel Studios based on characters that appear in publications by Marvel Comics. which became the highest-grossing film of all time at the time of its release.'
paragraph = input('Enter paragraph:')

count = 0
#count_word = text.split(' ')
count_word = paragraph.split(' ')
counting_word = input('Enter counting word:')
for every_word in count_word:
    if counting_word == every_word:
        count =count+1
print(f'The "{counting_word}" word is {count} times in the paragraph.')
# Write a Python program that calculates a "love score" between two people based on the letters in their names.
# The program should:
# Ask the user to enter two names.
# Count the total occurrences of the letters T, R, U, E (from the word "TRUE") and L, O, V, E (from the word "LOVE").
# Combine the two totals to form the love score (e.g., if TRUE total is 5 and LOVE total is 8, then the love score is 58).
# Finally, print a summary the total scores.


print('Welcome to the love calculator')
name1 = input('Enter your name:')
name2 = input('Enter their name:')

combined_string = name1.lower() + name2.lower()

t = combined_string.count('t')
r = combined_string.count('r')
u = combined_string.count('u')
e = combined_string.count('e')

l = combined_string.count('l')
o = combined_string.count('o')
v = combined_string.count('v')

true = t+r+u+e
love = l+o+u+e

love_score = int(str(true)+str(love))

if love_score<10 or love_score>=90:
    print(f'your love score is {love_score}')
elif love_score >= 40 and love_score <= 50:
    print(f'love{love_score}')
else:
    print(f'love{love_score}')

print(f'T occurs {t} times \nR occurs {r} times \nU occurs {u} times \nE occurs {e} times \n'
      f'Total={true}\n\n'
      f'L occurs {l} times \nO occurs {o} times \nV occurs {v} times \nE occurs {e} times \n Total={love}')
print(f'Love score is:{love_score}%')
# •   Count the number of occurrences of the numeric number '0' to '9' in a single string and you can either explain 
# it by words, psedocode or any other languages

def count_number(str):
    result = 0
    check = ['0','1','2','3','4','5','6','7','8','9']
    for each in str:
        if each in check:
            result += 1

    return result


print(count_number('adetge6882kfh4'))



str = 'ahdfoe89'

for each in str:
    print(each, end=' ')



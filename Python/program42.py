# An input string can be completed if additional letters can be added and no letters need to be taken away to match 
# the word.Furthermore,the order of the letters in the input string must be the same as the order of lettters in 
# the final word 

# create a function that,given as input string ,determines if the word can be completed

def canComplete(pw,cw):
    found=''
    for letter in pw:
        letter_found=False
        while cw and not letter_found:
            if letter==cw[0]:
                cw=cw[1:]
                found+=letter
                letter_found=True
            else:
                cw=cw[1:]
                letter_found=False

    if found==pw:
        return True
    else:
        return False
    
complete_word=input()
partial_word=input()
print(canComplete(partial_word,complete_word))

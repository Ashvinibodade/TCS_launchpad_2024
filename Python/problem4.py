#Write a program to take a input from console and another input named as pattern .If the input starts and ends 
# with the pattern then print {input string} contains {pattern} else {input string} does not contains {pattern}

input_str=input()
pattern=input()

if (input_str.lower().startswith(pattern.lower())):
    print("{} contains {}".format(input_str,pattern))
else:
    print("{} does not contains {}".format(input_str,pattern))
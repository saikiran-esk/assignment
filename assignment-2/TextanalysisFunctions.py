def count_words(text):
    words=text.split()
    print(f"words:{len(words)}")
def count_vowels(text):
    count=0
    for ch in text:
        if ch in "AaEeIiOoUu":
            count+=1
    print(f"Vowels:{count}")
def count_consonants(text):
    count=0
    for ch in text:
        if ch not in "AaEeIiOoUu" and not ch==" ":
            count+=1
    print(f"Consonants:{count}")
def reverse_text(text):
    words=text.split()
    revStr=""
    for word in words:
        temp=""
        for ch in word:
            temp=ch+temp
        revStr+=temp+" "
    print(f"Reversed:{revStr.strip()}")
def is_palindrome(text):
    words=text.split()
    revStr=""
    for word in words:
        temp=""
        for ch in word:
            temp=ch+temp
        revStr+=temp+" "
    if revStr==text:
        print(f"Palindrome:Yes")
    else:
        print(f"Palindrome:No")
def remove_vowels(text):
    result=""
    for ch in text:
        if ch not in"AaEeIiOoUu":
            result+=ch
    print(f"without vowels:{result}")
def word_frequency(text):
    words=text.split()
    f={}
    for ch in words:
        if ch not in f:
            f[ch]=1
        else:
            f[ch]+=1
    print("Word Frequency",end=" ")
    for key,value in f.items():
        print(f"{key}:{value},",end="")
def longestword(text):
    words=text.split()
    longest=words[0]
    for word in words:
        if len(word)>len(longest):
            longest=word
    print(f"\nLongest word:{longest}({len(longest)} letters)")
text=input("Enter text:")
print("====text analysis===")
count_words(text)
count_vowels(text)
count_consonants(text)
reverse_text(text)
is_palindrome(text)
remove_vowels(text)
word_frequency(text)
longestword(text)
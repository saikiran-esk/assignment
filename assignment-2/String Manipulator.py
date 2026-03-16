def StringManipulator(Sentence):
    print(f"Original Sentence:{Sentence}")
    print(f"Total Characters(with Spaces):{len(Sentence)}")
    print(f"Total Characters(without Spaces):{len(Sentence.replace(' ',''))}")
    word_count=len(Sentence.split())
    print(f"Words:{word_count}")
    print(f"UPPERCASE:{Sentence.upper()}")
    print(f"lowercase: {Sentence.lower()}")
    print(f"Title Case: {Sentence.title()}")
    words=Sentence.split()
    print(f"First word:{words[0]}")
    print(f"last word :{words[-1]}")
    print(f"reversed:{Sentence[::-1]}")


s=input("Enter Sentence:")
StringManipulator(s)

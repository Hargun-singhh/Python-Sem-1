def cap(sentence):
    words = sentence.split()
    cap_se = [word.capitalize() for word in words]
    return ' '.join(cap_se)
sentence=input("Enter a Sentence:")
res=cap(sentence)
print("_________RESULT____________")
print(res)
print("___________________________")
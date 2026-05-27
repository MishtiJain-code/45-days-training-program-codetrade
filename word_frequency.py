def fun(sentence):
    words=sentence.lower().split()
    freq={}

    for word in words:
    
        if word in freq:
            freq[word]+=1
        else:
            freq[word]=1

    return freq

text="Python is a easy and python is powerfull programming language"
result = fun(text)
print(result)
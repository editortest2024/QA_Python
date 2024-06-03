def word_frequency(text):


    text  = text.lower()




    for i in "!\'#%$^&()*+,-./;:<=>?@[\\]_`{|}~":
        text = text.replace(i,' ')


    words = text.split()


    freq = {}


    for word in words:
        if word in freq:
            freq[word] +=1
        else:
            freq[word] = 1
    return freq




print(word_frequency('Hello, World, How World world mir'))


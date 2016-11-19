# Define a word as any sequence of one or more lower-case letters(no numbers, no punctuation)
# words are separated by white space. Read all words(on every line)from standard input, and to produce,
# in order, on separate lines: -the count of words in input -the word “words” -each unique word, and the
# count of times it occurs in the input(listed in alphabetical order) -the word “letters” -for every letter
# from a to z, the letter, the count of times it occured IN A WORD(listed in alphabetical order)

def parsing(input):
    words = input.split();
    for i in input.split():
        for c in i:
            if not c.islower():
                words.remove(i)
                break
    print(len(words))
    print('words')
    words.sort();
    init_word=words[0];
    number = 1;
    for i in list(range(1,len(words))):
        if(init_word != words[i]):
            print(init_word+' '+str(number));
            init_word = words[i];
            number = 1;
        else:
            number+=1;
        if(i == len(words)-1):
            print(init_word + ' ' + str(number));
    print('letters')
    lowercase=list('abcdefghijklmnopqrstuvwxyz')
    for i in lowercase:
        number = 0;
        for j in words:
            if i in j:
                number+=1;
        print (i+' '+str(number));


input='# Define a word as any sequence of one or more lower-case letters(no numbers, no punctuation)'
parsing(input)
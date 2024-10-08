answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower().replace(' ','')
answers = ['42', 'forty-two', 'fortytwo']
if answer in answers:
    print('Yes')
else:
    print('No')

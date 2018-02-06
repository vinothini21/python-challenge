import os
import csv

# data sets
paragraph = ['1', '2']


#loop thru different data sets
for texting in paragraph:
    
    # Grab the electiondata csv
    paragraphtxt = os.path.join('paragraph_' + texting + '.txt')
    #print(paragraphtxt)
    num_words = 0
    num_sents = 0
    avg_sents_len =[]
    #num_chars = 0
    numb_chars_wo_space = 0  
    avg_lett_count = []  

    # open the txt file
    with open(paragraphtxt,'r') as f:

        for line in f:
            # for number of words splitting by space 
            words = line.split()
            num_words += len(words)

            # for number of characters
            # num_chars += len(line)

            # removing whitespaces
            numb_chars_wo_space += len(line) - line.count(' ')
            #for number of sentence 
            num_sents += line.count(".")
            # for average sentence length
            avg_sents_len = (num_words/num_sents)

            # for average letter count(per word)
            avg_lett_count = (numb_chars_wo_space/num_words)

            
    print("Paragraph Analysis")
    print("-"*80)
    print ("Approximate Word count:  %i \nApproximate Sentences Count: %i \nAverage sentence length: %f \nAverage letter count: %f "\
    % (num_words, num_sents, avg_sents_len, avg_lett_count))
    
    with open("Output.txt", "w") as text_file:
        text_file.write("Approximate Word count:  %i \nApproximate Sentences Count: %i \nAverage sentence length: %f \nAverage letter count: %f "\
        % (num_words, num_sents, avg_sents_len, avg_lett_count))
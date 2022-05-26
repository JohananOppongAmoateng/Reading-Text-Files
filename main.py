# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}


def read_file_content(filename):
    # [assignment] Add your code here 
    with open(filename) as f:
        lines = f.read()
    
    return lines

def count_words():
    count = {}
    text = read_file_content("./story.txt")
    text = text.split()
    for i in text:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    # print(count)
    return count

# count_words()
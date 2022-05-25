""" 
Collocation tool
"""
""" Import relevant packages """
import math, os, spacy, re
import pandas as pd
import argparse

""" Basic functions """
# Argument parser
def parse_args():
    ap = argparse.ArgumentParser()
    # REQUIRED ARGUMENTS
    # argument that decides whether the input is a single text or a whole directory
    ap.add_argument("-i",
                    "--input",
                    required = True,
                    help = "Whether you want to work with a single text or the whole directory")
    # user-defined search term argument
    ap.add_argument("-t", 
                    "--term",
                    type=str,
                    required = True,
                    help="The user-defined search term")
    # OPTIONAL ARGUMENTS
    # name of target text (if relevant) (default = "Anon_Clara_1864.txt")
    ap.add_argument("-x",
                    "--text_name",
                    type=str,
                    default="Anon_Clara_1864.txt",
                    help = "The name of the text you want to work with")
    # window size argument (default = 5)
    ap.add_argument("-w",
                    "--window_size",
                    type=int,
                    default=5,
                    help="The user-defined window-size")
    args = vars(ap.parse_args())
    return args 

# Read the text
def read_text(text_name):
    # define filepath
    filepath = os.path.join("in",
                            "100_english_novels",
                            "corpus",
                            f"{text_name}")
    # read the text
    with open(filepath, "r") as file:
        text = file.read()
    return text

# A quick regex tokenizer for splitting files
def tokenize(input_string):
    tokenizer = re.compile(r"\W+")
    return tokenizer.split(input_string)

# MI function
def MI(A, B, AB, span, corpus_size):
    score = math.log((AB * corpus_size) / (A * B * span)) / math.log(2)
    return score


""" Collocation tool """
def collocation_tool(term, text_name, window_size):
    # define parameters
    term = term.lower()
    window_size = window_size
    span = window_size*2
    # read the text
    text = read_text(text_name)
    # tokenise the text and remove punctuation
    tokenized_text = []
    for word in tokenize(text):
        # lowercase
        lowercase = word.lower()
        # cleanup punctuation etc
        cleaned = re.sub(r'[^\w\s]', '', lowercase)
        tokenized_text.append(cleaned)
    # create temporary list
    tmp = []
    # for the target word 
    for idx,word in enumerate(tokenized_text):
        # if it's the user-defined keyword
        if word == term:
            # define left and right context windows
            left_context = max(0, idx-window_size)
            right_context = idx+window_size+1
            # extract all words ± 5
            full_context = tokenized_text[left_context:idx] + tokenized_text[idx+1:right_context]
            # append the words to tmp list
            tmp.append(full_context)
    # flatten list
    flattened_list = []
    # for each sublist in list of lists
    for sublist in tmp:
        # for each item in the sublist
        for item in sublist:
            # append to flattened list
            flattened_list.append(item)
    # create a list of collocate counts
    collocate_counts = []
    # for every collocate 
    for word in set(flattened_list):
        # count how often each word appears as a collocate
        count = flattened_list.count(word)
        # append tuple of word and count to list
        collocate_counts.append((word, count))
    # size of corpus (in this case, the number of words in the text)
    corpus_size = len(tokenized_text)
    # frequency of the user-defined term
    keyword_freq = tokenized_text.count(term)
    # create a list of all the information
    out_list = []
    for tup in collocate_counts:
        coll_text = tup[0]
        coll_count = tup[1]
        total_occurrences = tokenized_text.count(coll_text)
        score = MI(keyword_freq, coll_count, total_occurrences, span, corpus_size)
        out_list.append((coll_text, coll_count, total_occurrences, score))
    # create a pandas dataframe out of the results
    output_df = pd.DataFrame(out_list, columns = ["collocation", "collocate_count", "total_count", "MI"])
    # sort ascending by the MI score
    output_df = output_df.sort_values(by=['MI'], ascending=False)
    # remove ".txt" from the text name to use it for saving
    outname = text_name.rsplit('.',1)[0]
    return output_df, outname
    

""" Main function """
def main():
    # parse arguments
    args = parse_args()
    # if the input is marked as a single text
    if args["input"] == "single_text":
        # define parameters
        term = args["term"]
        text_name = args["text_name"]
        window_size = args["window_size"]
        # run the collocation tool function
        output_df, outname = collocation_tool(term, text_name, window_size)
        # save output CSV
        output_df.to_csv(os.path.join("out", "user-defined",
                                      f"collocates_{term}_{outname}_windowsize{window_size}.csv"), index=False)
        # print message
        print("[INFO] FINISHED!")
    # otherwise, if the input is a directory
    elif args["input"] == "directory":
        # define filepath
        filepath = os.path.join("in", "100_english_novels", "corpus")
        # get list of the contents of the directory
        text_names = os.listdir(filepath)
        # get list of TXT files
        text_names_clean = []
        for name in text_names:
            if name.endswith(".txt"):
                text_names_clean.append(name)
            else:
                pass
        # count the number of texts in list
        count_texts = len(text_names_clean)
        # start counter
        counter = 0
        # for text in list of texts
        for name in text_names_clean:
            # add 1 to counter
            counter += 1
            # define parameters
            term = args["term"]
            text_name = name
            window_size = args["window_size"]
            # run the collocation tool
            output_df, outname = collocation_tool(term, text_name, window_size)
            # save output CSV
            output_df.to_csv(os.path.join("out", "all", 
                                          f"collocates_{term}_{outname}_windowsize{window_size}.csv"), index=False)
            # print message
            print(f"[INFO] {(counter):03}/{count_texts} - {text_name}")
        # when everything has run, print final message
        return print("[INFO] FINISHED!")

if __name__=="__main__":
    main()
            
        
    
 
# Assignment 1 – Collocation tool
The portfolio for __Language Analytics S22__ consists of 5 projects (4 class assignments and 1 self-assigned project). This is the __first assignment__ in the portfolio. 

## 1. Contribution
The initial assignment was made partly in collaboration with others from the course, but the final code is my own. I made several adjustments to the code since I first handed it in.

## 2. Assignment description by Ross
### Main task
For this assignment, you will write a small Python program to perform collocational analysis using the string processing and NLP tools you've already encountered. Your script should do the following:

- Take a user-defined search term and a user-defined window size.
- Take one specific text which the user can define.
- Find all the context words which appear ± the window size from the search term in that text.
- Calculate the mutual information score for each context word.
- Save the results as a CSV file with (at least) the following columns: the collocate term; how often it appears as a collocate; how often it appears in the text; the mutual information score.

### Bonus task
- Create a program which does the above for every novel in the corpus, saving one output CSV per novel
- Create a program which does this for the whole dataset, creating a CSV with one set of results, showing the mutual information scores for collocates across the whole set of texts
- Create a program which allows a user to define a number of different collocates at the same time, rather than only one.

## 3. Methods
### Main task


### Bonus task



## 4. Usage
### Install packages
Before running the script, you have to install the relevant packages. To do this, run the following from the command line:
```
sudo apt update
pip install --upgrade pip
# required packages
pip install pandas numpy scipy spacy tqdm spacytextblob vaderSentiment networkx scikit-learn tensorflow gensim textsearch contractions nltk beautifulsoup4 transformers autocorrect pytesseract opencv-python
# install spacy model
python -m spacy download en_core_web_sm
# ocr tools
sudo apt install -y tesseract-ocr
sudo apt install -y libtesseract-dev
```

### Get the data

### Main task


### Bonus task


## 5. Discussion of results

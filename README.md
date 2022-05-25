# Assignment 1 – Collocation tool
The portfolio for __Language Analytics S22__ consists of 5 projects (4 class assignments and 1 self-assigned project). This is the __first assignment__ in the portfolio. 

## 1. Contribution
The initial assignment was made partly in collaboration with others from the course, but the final code is my own. I made several adjustments to the code since I first handed it in.

After the initial hand-in, Ross posted a [possible solution](https://github.com/CDS-AU-DK/cds-language/blob/main/notebooks/assignment1_possible_solution.ipynb) which I found useful in writing the code for the final portfolio.

## 2. Assignment description by Ross
### Main task
For this assignment, you will write a small Python program to perform collocational analysis using the string processing and NLP tools you've already encountered. Your script should do the following:

- Take a user-defined search term and a user-defined window size.
- Take one specific text which the user can define.
- Find all the context words which appear ± the window size from the search term in that text.
- Calculate the mutual information score for each context word.
- Save the results as a CSV file with (at least) the following columns: the collocate term; how often it appears as a collocate; how often it appears in the text; the mutual information score.

### Bonus task
1. Create a program which does the above for every novel in the corpus, saving one output CSV per novel
2. Create a program which does this for the whole dataset, creating a CSV with one set of results, showing the mutual information scores for collocates across the whole set of texts
3. Create a program which allows a user to define a number of different collocates at the same time, rather than only one.

## 3. Methods
### Main task


### Bonus task
As for the bonus tasks, I managed to do 1/3. By tweaking the code from the main task, I allowed for the user to specify whether they want to run the collocational analysis on a single file or the whole dataset, saving one output CSV per novel.

I did not have time to finish the other two but the provided code could be used as a stepping stone towards solving these problems.


## 4. Usage
### Install packages
Before running the script, you have to install the relevant packages. To do this, run the following from the command line:
```
sudo apt update
pip install --upgrade pip
# required packages
pip install pandas numpy spacy tqdm spacytextblob
# install spacy model
python -m spacy download en_core_web_sm
```

### Get the data
- Download the data from: https://github.com/computationalstylistics/100_english_novels.
- Unzip and place the folder in the [`in`](https://github.com/agnesbn/LANG_assignment1/tree/main/in) folder.
- Make sure the path from `LANG_assignment1` to the data is `in/100_english_novels/corpus`.
    - You may have to rename the input folder from `100_english_novels-main` to just `100_english_novels`. Alternatively, you can change the filepath defined in `collocation_tool.py` [line 44](https://github.com/agnesbn/LANG_assignment1/blob/2163cdfc70d9a736591afe3bfdea83cd33cd9340/src/collocation_tool.py#L44) and [150](https://github.com/agnesbn/LANG_assignment1/blob/2163cdfc70d9a736591afe3bfdea83cd33cd9340/src/collocation_tool.py#L150) to match your path.

### Main task
Make sure your current directory is the `LANG_assignment1` folder. Then from the command line, run:
```
python src/collocation_tool.py --input single_file --term <USER-DEFINED TERM> (--text_name <TEXT> --window_size <USER-DEFINED WINDOW SIZE>)
```
__Required input:__
- `<USER-DEFINED TERM>`: the target word or user-defined search term, you wish to work with. I used the word `man`.

__Optional input:___
- `<TEXT>`: the text you want to use for the collocational analysis. The default is the first text in the data, `Anon_Clara_1864.txt`.
- `<USER-DEFINED WINDOW SIZE>`: the desired number of context words before and after your target word. The default is `5` – so five words before and five words after.

The results will be saved in [`out/user-defined`](https://github.com/agnesbn/LANG_assignment1/tree/main/out/user-defined).

### Bonus task
Make sure your current directory is the `LANG_assignment1` folder. Then from the command line, run:
```
python src/collocation_tool.py --input directory --term <USER-DEFINED TERM> (--window_size <USER-DEFINED WINDOW SIZE>)
```
__Required input:__
- `<USER-DEFINED TERM>`: the target word or user-defined search term, you wish to work with. I used the word `man`.

__Optional input:__
- `<USER-DEFINED WINDOW SIZE>`: the desired number of context words before and after your target word. The default is `5` – so five words before and five words after.

The results will be saved in [`out/all`](https://github.com/agnesbn/LANG_assignment1/tree/main/out/all).

## 5. Discussion of results

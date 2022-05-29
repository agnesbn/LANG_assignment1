# Assignment 1 – Collocation tool
The portfolio for __Language Analytics S22__ consists of 5 projects (4 class assignments and 1 self-assigned project). This is the __first assignment__ in the portfolio. 

## 1. Contribution
The initial assignment was made partly in collaboration with others from the course, but the final code is my own. I made several adjustments to the code since I first handed it in. However, I found this [possible solution](https://github.com/CDS-AU-DK/cds-language/blob/main/notebooks/assignment1_possible_solution.ipynb) posted by Ross after the initial hand-in useful in writing the code for the final portfolio.

## 2. Assignment description by Ross
### Main task
For this assignment, you will write a small Python program to perform collocational analysis using the string processing and NLP tools you've already encountered. Your script should do the following:

- Take a __user-defined search term__ and a __user-defined window size__.
- Take one __specific text__ which the user can define.
- Find all the __context words__ which appear ± the window size from the search term in that text.
- Calculate the __mutual information score__ for each context word.
- Save the results as a CSV file with (at least) the following columns: the collocate term; how often it appears as a collocate; how often it appears in the text; the mutual information score.

### Bonus task
1. Create a program which does the above for __every novel in the corpus__, saving one output CSV per novel
2. Create a program which does this for the __whole dataset__, creating a CSV with one set of results, showing the mutual information scores for collocates across the whole set of texts
3. Create a program which allows a user to define __a number of different collocates at the same time__, rather than only one.

## 3. Methods
### Main task
The [`collocation_tool.py`](https://github.com/agnesbn/LANG_assignment1/blob/main/src/collocation_tool.py) script reads a given text and tokenises it. Then taking a user-defined window size, it extracts all the words which appear ± the window size from a user-defined search term. It then calculates the mutual information score between the contexts words and the given search term. Finally, the information (i.e. the mutual information score, the number of times the context word occurs as a collocate, and the number of times it occurs in general in the text) is converted into a `pandas` dataframe and saved as a CSV in which the results are sorted in descending order by the mutual information score.

### Bonus task
As for the bonus tasks, I managed to do 1/3. By tweaking the code from the main task, I allowed for the user to specify whether they want to run the collocational analysis on a single file or the whole dataset, saving one output CSV per novel.

I did not have time to finish the other two but the provided code could be used as a stepping stone towards solving these problems.


## 4. Usage
### Install packages
Before running the script, you have to install the relevant packages. To do this, run the following from the command line:
```
sudo apt update
pip install --upgrade pip
pip install pandas numpy spacy tqdm spacytextblob
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
python src/collocation_tool.py --input single_file --term <TERM> (--text_name <TEXT> --window_size <WINDOW SIZE>)
```
__Required input:__
- `<TERM>`: the target word or user-defined search term, you wish to work with. I used the word `man`.

__Optional input:___
- `<TEXT>`: the text you want to use for the collocational analysis. The default is the first text in the data, `Anon_Clara_1864.txt`.
- `<WINDOW SIZE>`: the desired number of context words before and after your target word. The default is `5` – so five words before and five words after the search term.

The results will be saved in [`out/user-defined`](https://github.com/agnesbn/LANG_assignment1/tree/main/out/user-defined).

### Bonus task
Make sure your current directory is the `LANG_assignment1` folder. Then from the command line, run:
```
python src/collocation_tool.py --input directory --term <TERM> (--window_size <WINDOW SIZE>)
```
__Required input:__
- `<TERM>`: the target word or user-defined search term, you wish to work with. I used the word `man`.

__Optional input:__
- `<WINDOW SIZE>`: the desired number of context words before and after your target word. The default is `5` – so five words before and five words after the search term.

The results will be saved in [`out/all`](https://github.com/agnesbn/LANG_assignment1/tree/main/out/all).

## 5. Discussion of results
The results can be seen in the two output folders in [`out`](https://github.com/agnesbn/LANG_assignment1/tree/main/out). At the top of each output CSV is the word with the highest mutual information score. An in-depth analysis of the results is beyond the scope of this exam but I noticed that many of the high-scoring words were feminine, like [`she`, `mrs`, `mother`](https://github.com/agnesbn/LANG_assignment1/blob/main/out/all/collocates_man_Anon_Clara_1864_windowsize5.csv), [`prioress`, `sister`](https://github.com/agnesbn/LANG_assignment1/blob/main/out/all/collocates_man_Barclay_Ladies_1917_windowsize5.csv), [`miss`](https://github.com/agnesbn/LANG_assignment1/blob/main/out/all/collocates_man_Barclay_Postern_1911_windowsize5.csv) etc. but this was not the case for all texts.

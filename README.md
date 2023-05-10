# Pencil Durability Kata
The Pencil Durability Kata is a larger-than-trivial exercise that can be used to practice test-driven development. The purpose of this kata is to write code to simulate an ordinary graphite pencil. Basic functionality includes writing and editing text; additional future features include wearing down the point/eraser, sharpening the pencil, and overwriting text.

## Value Stories

### Write
> **AS A** writer,  
**I WANT** to be able to use a pencil to write text on a sheet of paper  
**SO THAT** I can better remember my thoughts.  

When the pencil is instructed to write a string of text on a sheet of paper, the paper should reflect the text that was written.

Text written by the pencil should always be appended to existing text on the paper. Thus, given a piece of paper with the text ```"She sells sea shells"```, when a pencil is instructed to write ```" down by the sea shore"``` on the paper, the paper will then contain the entire string (i.e. ```"She sells sea shells down by the sea shore"```).

### Erase
> **AS A** writer,  
**I WANT** to be able to erase previously written text  
**SO THAT** I can remove my mistakes.  

When the pencil is instructed to erase text from the paper, the last occurrence of that text on the paper will be replaced with empty spaces.  

Given a piece of the paper containing the string:
```
"How much wood would a woodchuck chuck if a woodchuck could chuck wood?"
```  
when the string "chuck" is erased, the paper should read:  
```
"How much wood would a woodchuck chuck if a woodchuck could       wood?"
```    
and if the string "chuck" is erased again, the paper should read:  
```
"How much wood would a woodchuck chuck if a wood      could       wood?"
```  

## Setup

### Environment setup
1. Install `pip` and `pipenv`
2. Clone this repository
3. In root folder (`kata-pencil-durability/`), run:
   ```
   pipenv install
   ```

**pipenv installation for Windows:**
1. Run Windows Power Shell as Administrator
2. Run the following command in PowerShell:
   ```
   pip install pipenv
   ```
3. Execute the following command (replace `<YOUR USER NAME>` with the appropriate directory):
   ```
   set PATH=%PATH%;set PATH=%PATH%;'c:\users\<YOUR USER NAME>\appdata\local\programs\python\python36-32\Scripts'
   ```

*Instructions found in [this tutorial](https://thinkdiff.net/how-to-use-python-pipenv-in-mac-and-windows-1c6dc87b403e)*

### Run tests
After running `pipenv install` (above), you can run tests with:
```
pytest -f --color=yes
```
Explanation of options:
- `-f`: Rerun tests after saving changes to any file
- `--color=yes`: Color-code test output in terminal (i.e. green for pass, red for fail)
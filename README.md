# Fluency-Fact-Quizzer
## Getting set up
1. Go to the Terminal app, or open a terminal in VSCode if you have that
2. Run `git clone https://github.com/yasen5/Fluency-Fact-Quizzer.git` (this will clone this repository)
3. You will need Python to run this program. If you do not have it (you can check by running `python3 --version`) you can install it using the instructions in this article: https://realpython.com/installing-python/

## Generating the JSON
Copy-paste the fluency facts from the google doc into ff.txt
Run `python3 txt_to_json.py`
This will export the FFs into a readable json format

### Running the quiz
Run `python3 quiz.py`
- If you would like to test only one category, run `python3 quiz.py <Categoryname>
- If you choose the "When" (or "when") option, it will prompt you to enter dates. If you enter an answer that doesn't have a start and end when one is expected, it will notify you
- If you get an answer incorrect in the "When" mode, it will ask you about it later
- For the other modes you will just have to confirm whether your answer was correct (it will give you the prompt, and then the answer after you press enter)

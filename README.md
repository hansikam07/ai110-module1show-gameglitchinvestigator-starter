# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
The purpose of the game is to show teh various type of bugs that can occur in any programming project and how to approach these issues using AI. Game helped us use ClaudeCode to understand error, find solution and verify and test the code after solutions were implememted.
- [ ] Detail which bugs you found.
I found a bug with wrong hints(backwards), wrong number of guess attempts, miscalcution of score and issue starting a new game.
- [ ] Explain what fixes you applied.
i applied fixes so the game will produce the right hints, and so teh game allowed teh correct 8 number of guesses for the user. 

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. Game starts with 8 guesses and an option to see a hint, hints are on
2. User starts by enetering 50
3. Game return a hint of "📉 Go HIGHER!"
4. User enters 80 -> a hint of "📉 Go HIGHER!"
5. User enters 90 -> game returns "Win", "🎉 Correct!"

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]

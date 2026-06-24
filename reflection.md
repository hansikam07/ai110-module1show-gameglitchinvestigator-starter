# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
The hints are both backwards anbd the hint is not being updated with changing guesses by the user. I expected teh hint to update with the guess and actually point me in teh right direction. the new game button doesn't refresh teh game and so you can't play a new game. The game says out of attempts and reveals the answer when there is still one attempt left, so only at 7 instead of 8. The socrinmg function is also off and generating inaccrurate reuslts. 
-hints
-new game
-guess on odd vs even attempts:on even guesses the secret is passed as a string so number comparison is off


**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| 21    | Go Lower          |   Go Higher     |   wrong hint 
| 40    | Go Lower          |   Go HIGHER!    |   wrong hint
| 1     | Go Higher         |    Go LOWER!    |   wrong hint

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used Claude Code, Claude
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
An AI suggestion was that the guess counter started at the wrong number of 1 terefore the number of guesses a user was allowed was ending earlier that expected. AI suggested a change to initial guess = 0; and I verified that thsi was right and made the change, now a user can make 8 guesses. Another AI suggestion was to remove the try catch block in the check_guess function because it was reading in the number input as a string skewing teh hints. Calude suggested removing it, I didn't quite understand how teh try catch would work, however i learned through claude that it was still wrong for reading in a string and would skew hints so I verified and removed it. 

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
The AI suggested that "since the new check_guess no longer has the TypeError fallback, the string-conversion in the submit block would now crash on even attempts… I have to remove it for the app to work." This was incorrect as I had previosuly just changed the string conversion so I was wondering hwo it still was crashing so I double checked calude with all the changes made and claudecode caught this error.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

I had the test cases specifically checking for teh bug we caught and after ran teh gaem and played it my slef to check that teh bug was actually fixed. 

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  I went and played the game, after fixing the string/wrong hinst error. I saw the secret and made dilebrate even and odd guesses to make sure that the lower/higher hint was based on number camprison and not string. The correct hints given by the game regardless of even or odd inputs revelead that the bug was fixed. 

- Did AI help you design or understand any tests? How?
Yes I asked AI to check that the game was giving users te right amount fo guess and it explained that the inital guess count was off and designed a test and explained it woudl stimulate teh guess loop on teh game and cheked if it got the right attempt limit number we had set. 

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

# Number of guesses already made at the start of a game. Must be 0 so the
# player gets the full attempt_limit — starting at 1 ends the game a guess early.

#FIXME - worked with AI to let user act have 8 guesses instead of stopping one early, did that by setting teh first guess to 0 instead of 1 liek it was
INITIAL_ATTEMPTS = 0


def is_out_of_attempts(attempts: int, attempt_limit: int) -> bool:
    """Return True when no guesses remain. `attempts` counts guesses made so far."""
    return attempts >= attempt_limit


def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


#FIXME - worked with AI to refactor teh check_guess code and into logic_utils.py
def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"

    Both arguments are expected to be ints. A guess larger than the secret
    is "Too High", so the hint tells the player to go LOWER.
    """
    if guess == secret:
        return "Win", "🎉 Correct!"
    if guess > secret:
        return "Too High", "📈 Go LOWER!"
    return "Too Low", "📉 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")

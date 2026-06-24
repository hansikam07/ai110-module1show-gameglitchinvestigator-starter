from logic_utils import check_guess

# check_guess returns a tuple: (outcome, message)

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, outcome should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, outcome should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"


# --- Regression test for the high/low hint bug ---
# The bug: when the guess was higher than the secret, the hint told the
# player to go HIGHER (backwards), and vice versa. The hint message must
# point in the direction that moves the player TOWARD the secret.

def test_hint_direction_matches_comparison():
    # Guess too high -> the hint must tell the player to go LOWER
    outcome, message = check_guess(70, 50)
    assert outcome == "Too High"
    assert "LOWER" in message.upper()
    assert "HIGHER" not in message.upper()

    # Guess too low -> the hint must tell the player to go HIGHER
    outcome, message = check_guess(30, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message.upper()

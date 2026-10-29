
from password_policy import check_password, strength, suggest_fix


def test_password_short_branch():
    assert "too short" in check_password("Ab1!")


def test_password_normal_length_branch():
    assert "too short" not in check_password("Abcdef1!")


def test_password_long_branch():
    assert "too long" in check_password("A" + "b" * 63 + "1!")


def test_password_max_length_boundary():
    assert "too long" not in check_password("A" + "b" * 61 + "1!")


def test_common_password_branch():
    assert "common" in check_password("password")


def test_not_common_password_branch():
    assert "common" not in check_password("Abcdef1!")


def test_all_character_categories():
    assert check_password("Abcdef1!") == []


def test_no_uppercase_branch():
    assert "no uppercase" in check_password("abcdef1!")


def test_no_lowercase_branch():
    assert "no lowercase" in check_password("ABCDEF1!")


def test_no_digit_branch():
    assert "no digit" in check_password("Abcdefgh!")


def test_no_special_branch():
    assert "no special" in check_password("Abcdef12")


def test_strength_strong_branch():
    assert strength("Abcdefgh1234!@") == "strong"


def test_strength_good_branch():
    assert strength("Abcdef1!") == "good"


def test_strength_weak_branch():
    assert strength("Abcdefgh") == "weak"


def test_strength_very_weak_branch():
    assert strength("abc") == "very weak"


def test_suggest_fix_empty_branch():
    assert suggest_fix([]) == "none needed"


def test_suggest_fix_short_branch():
    assert suggest_fix(["too short"]) == "add more characters"


def test_suggest_fix_common_branch():
    assert suggest_fix(["common"]) == "avoid common passwords"


def test_suggest_fix_missing_character_branch():
    assert suggest_fix(["no digit"]) == "add digit"


def test_suggest_fix_fallback_branch():
    assert suggest_fix(["too long"]) == "shorten it"

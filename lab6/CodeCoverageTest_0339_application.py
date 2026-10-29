
from password_policy import check_password, strength, suggest_fix


def test_valid_password():
    assert check_password("Abcdef1!") == []


def test_password_too_short():
    assert "too short" in check_password("Ab1!")


def test_password_too_long():
    assert "too long" in check_password("Abcdef1!" + "x" * 65)


def test_common_password_case_insensitive():
    assert "common" in check_password("PASSWORD")


def test_password_without_uppercase():
    assert "no uppercase" in check_password("abcdef1!")


def test_password_without_lowercase():
    assert "no lowercase" in check_password("ABCDEF1!")


def test_password_without_digit():
    assert "no digit" in check_password("Abcdefgh!")


def test_password_without_special_character():
    assert "no special" in check_password("Abcdef12")


def test_empty_password():
    issues = check_password("")
    assert "too short" in issues
    assert "no uppercase" in issues
    assert "no lowercase" in issues
    assert "no digit" in issues
    assert "no special" in issues


def test_good_strength():
    assert strength("Abcdef1!") == "good"


def test_strong_strength():
    assert strength("Abcdefgh1234!@") == "strong"


def test_weak_strength():
    assert strength("Abcdefgh") == "weak"


def test_very_weak_strength():
    assert strength("abc") == "very weak"


def test_suggest_fix_no_issues():
    assert suggest_fix([]) == "none needed"


def test_suggest_fix_too_short():
    assert suggest_fix(["too short"]) == "add more characters"


def test_suggest_fix_common():
    assert suggest_fix(["common"]) == "avoid common passwords"


def test_suggest_fix_missing_character_type():
    assert suggest_fix(["no uppercase"]) == "add uppercase"


def test_suggest_fix_too_long():
    assert suggest_fix(["too long"]) == "shorten it"

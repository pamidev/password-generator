import string
from io import StringIO
from unittest.mock import patch

from password_generator import password_generator, main


def test_password_generator_length():
    for pass_length in range(13, 100):
        assert len(password_generator(pass_length)) == pass_length


def test_password_generator_default_length():
    pwd = password_generator()
    assert len(pwd) == 12


def test_password_generator_expected_characters():
    for _ in range(100):
        generated_password = password_generator()
        assert any(char in string.punctuation for char in generated_password)
        assert sum(char in string.digits for char in generated_password) >= 3
        assert sum(char in string.ascii_lowercase for char in generated_password) >= 3
        assert sum(char in string.ascii_uppercase for char in generated_password) >= 3


def test_password_generator_randomness():
    generated_password_1 = password_generator(12)
    generated_password_2 = password_generator(12)
    assert generated_password_1 != generated_password_2


def test_main_valid_input():
    with patch('builtins.input', return_value='18'):
        with patch('sys.stdout', new=StringIO()) as output:
            main()
            assert "Your strong password is: " in output.getvalue()


def test_main_invalid_input():
    with patch('builtins.input', return_value='11'):
        with patch('sys.stdout', new=StringIO()) as output:
            main()
            assert "Check password length. Must be at least 12 characters." in output.getvalue()


def test_main_non_numeric_input():
    with patch('builtins.input', return_value='abc'):
        with patch('sys.stdout', new=StringIO()) as output:
            main()
            assert "Entered bad data. Try again." in output.getvalue()

from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    name = 'patricia'
    numbers = [40, 2, 3, 1]
    validateInverter = encrypt_message(name, numbers[0])
    assert (validateInverter) == "aicirtap"

    validatePair = encrypt_message(name, numbers[1])
    assert (validatePair) == "aicirt_ap"

    validateOdd = encrypt_message(name, numbers[2])
    assert (validateOdd) == "tap_aicir"

    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message(name, "")

    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(numbers[3], numbers[1])

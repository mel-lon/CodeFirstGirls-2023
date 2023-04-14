def test_isogram_checker():
    # Testing for a word that is an isogram
    assert isogram_checker("hello") == True

    # Test for a word that isnt an isogram
    assert isogram_checker("apple") == False

    # Test for a word with a mixture of upper and lower cases
    assert isogram_checker("aBcDeFg") == True

    # Test for a word that uses special characters
    assert isogram_checker("hello!") == True

    # Test for a string that's empty
    assert isogram_checker("") == True

    # Test for a string with only spaces
    assert isogram_checker("  ") == True

    # Test for a string with a mix of letters and spaces
    assert isogram_checker("abc def") == True



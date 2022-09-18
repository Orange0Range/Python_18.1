def print_upper_words(words, must_start_with):
    """For list of words, 
       print each on separate line in uppercase
       Also accepts letters to gate words

       Should return:
       HELLO
       HEY
       YO
       YES
    """  

    # Python has a built-in function `sum()` for this, but we don't
    # want you to use it. Please write this by hand.

    # YOUR CODE HERE
    for let in must_start_with:
        for word in words:
            if word[0].lower() == let.lower():
                print(word.upper())

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], must_start_with={"h", "y"})
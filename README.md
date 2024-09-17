[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/5UIWQGVJ)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=16001508)
# Lab: N-Grams

## Overview

An *n-gram* -- in the context of parsing natural languages such as English -- is a sequence of *n* consecutive *tokens* (which we might define as characters separated by whitespace) from some passage of text. Based on the following passage:

> I really really like cake.

We have the following 2-grams:

    [('I', 'really'), ('really', 'really'), ('really', 'like'), ('like', 'cake.')]

And the following 3-grams:

    [('I', 'really', 'really'),
     ('really', 'really', 'like'),
     ('really', 'like', 'cake.')]

Note that we omit a 1-gram listing because it would merely be a list of all tokens in the original text.

Among other things, n-grams are useful for describing the vocabulary of and statistical correlation between tokens in a sample body of text (e.g., as taken from a book). We can use an n-gram model to determine the likelihood of finding
a particular sequence of words after another. This information, in turn, can be used to generate passages of text that statistically mimic the sample.

We can convert the above 3-gram list into the following lookup structure (i.e., a dictionary mapping strings to lists of 2-tuples), where the first token of each n-gram maps to all sequences that follow it in the text:

    {'I': [('really', 'really')],
     'really': [('really', 'like'), ('like', 'cake.')]}

We can now generate passages of text using the following method:

1. Select a random key and use it as the start token of the passage. It will also serve as the current token for the next step.
2. Select a random tuple from the list associated with the current token and append the sequence to the passage. The last token of the selected sequence will be the new current token.
3. If the current token is a key in the dictionary then simply repeat step 2, otherwise select another random key from the dictionary as the current token and append it to the passage before repeating step 2.

E.g., we might start by selecting `'I'` in step (1), which gives us `('really', 'really')` as our only choice in (2). The second `'really'` in that tuple is the new current token (which is a valid key), which takes us back to (2) and gives us a choice between two tuples. If we choose `('like', 'cake.')`, then we have `'cake.'` as our new current token --- it is not a key in the map, however, so we'd have to choose a new random key if we wanted to generate a longer passage. Either way, the passage we've generated thus far is `'I really really like cake.'` (which also happens to be the original passage).

Here's a lengthier passage that could be generated from the 3-gram dictionary above -- note that for clarity I've added `*`'s every time a new random key is selected (i.e., when the previous token isn't a key in the dictionary):

> \* really like cake. \* I really really really like \* really like cake. \* I really really really like \* really

This gets more interesting when we build n-gram dictionaries from lengthier bodies of text. For instance, the following text was generated (with a little programmed embellishment for prettier capitalization and punctuation) from a 3-gram dictionary extracted from Romeo's famous balcony monologue:

> Lamp her eyes were there they in their spheres till they in her eyes in all the fairest stars in all the heaven having some business do wear it is my love! O it is envious her cheek would through the heaven having some business do entreat her eyes were there they in their spheres till they in her eyes to.

For reference, here is the dictionary entry for the token `'her'` used to generate the above:

    'her': [('maid', 'art'),
            ('maid', 'since'),
            ('vestal', 'livery'),
            ('eyes', 'to'),
            ('eyes', 'were'),
            ('head?', 'The'),
            ('cheek', 'would'),
            ('eyes', 'in'),
            ('cheek', 'upon'),
            ('hand!', 'O')],

Your assignment is to implement a function that constructs an n-gram dictionary from a list of strings (tokens), and another that returns a passage of text generated from a given n-gram dictionary.

## Details

All your code will go into the `ngrams.py` source file.

### Exercise 1 (15 points)

Your first task is to implement `compute_ngrams`, which will take a list of tokens, a value `n` indicating the n-gram length (e.g., 3 for 3-grams), and return an n-gram dictionary. The keys in the returned dictionary should all be strings, whose values will be lists of one or more tuples. Note that even in the case of `n`=2 (which would be the minimum value) the dictionary should map strings to lists of 1-tuples (i.e., instead of to lists of individual tokens).


### Exercise 2 (10 points)

Next, you will implement `gen_passage`, which will take an n-gram dictionary and a length for the passage to generate (as a token count). 

As described earlier, it will work as follows:

1. Select a random key from the dictionary and use it as the start token of the passage. It will also serve as the current token for the next step.
2. Select a random tuple from the list associated with the current token and append the sequence to the passage. The last token of the selected sequence will be the new current token.
3. If the current token is a key in the dictionary then simply repeat step 2, otherwise select another random key from the map as the current token and append it to the passage before repeating step 2.

You will use [`random.choice`](https://docs.python.org/3/library/random.html#random.choice) whenever a random selection needs to be made. In order for your results to be reproduceable, be sure to sort the dictionary's keys (which, recall, are in no discernible order) before selecting a random one, like this (assuming `ngram_dict` is the dictionary):

    random.choice(sorted(ngram_dict.keys()))

For the test cases to pass, it is *critical* that you do not invoke `random.choice` more than is absolutely necessary, and only as prescribed in the steps described above!

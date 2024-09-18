import random

ROMEO_SOLILOQUY = """
        But, soft! what light through yonder window breaks?
        It is the east, and Juliet is the sun.
        Arise, fair sun, and kill the envious moon,
        who is already sick and pale with grief, 
        That thou her maid art far more fair than she:
        be not her maid, since she is envious;
        her vestal livery is but sick and green
        and none but fools do wear it; cast it off.
        It is my lady, O, it is my love! 
        O, that she knew she were!
        She speaks yet she says nothing: what of that?
        Her eye discourses; I will answer it.
        I am too bold, 'tis not to me she speaks:
        two of the fairest stars in all the heaven, 
        having some business, do entreat her eyes
        to twinkle in their spheres till they return.
        What if her eyes were there, they in her head?
        The brightness of her cheek would shame those stars,
        as daylight doth a lamp; her eyes in heaven 
        would through the airy region stream so bright
        that birds would sing and think it were not night.
        See, how she leans her cheek upon her hand!
        O, that I were a glove upon that hand,
        that I might touch that cheek!"""


def compute_ngrams(toks, n=2):
    """Returns an n-gram dictionary based on the provided list of tokens."""
        ngrams = {}
        for i in range(len(tokens)-n+1):
                gram = ' '.join(tokens[i:i+n])
                if gram not in ngrams.keys():
                        ngrams[gram] = []
                ngrams[gram].append(tuple(tokens[i+1:i+n]))
return ngrams


def gen_passage(ngram_dict, length=100):
    """Generates a passage of the specified length using the given n-grams."""
        current_token = random.choice(list(ngram_dict.keys()))
        passage = [current_token]
        while len(passage) < length:
                if current_token in ngram_dict.keys():
                        next_token = random.choice(ngram_dict[current_token])
                        passage.append(' '.join(next_token))
                        current_token = next_token[-1]
                else:
                        current_token = random.choice(list(ngram_dict.keys()))
                        passage.append(current_token)
        return ' '.join(passage)

import pytest
import ngrams
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


@pytest.mark.points(5)
def test_compute_ngrams_simple():
    simple_toks = 'i really really like cake.'.split()

    assert ngrams.compute_ngrams(simple_toks) == {
                'i': [('really',)], 
                'like': [('cake.',)], 
                'really': [('really',), ('like',)]
            }
    assert ngrams.compute_ngrams(simple_toks, n=3) == {
                'i': [('really', 'really')],
                'really': [('really', 'like'), ('like', 'cake.')]
            }


@pytest.mark.points(5)
def test_compute_ngrams_romeo():
    romeo_toks = [t.lower() for t in ROMEO_SOLILOQUY.split()]

    dct = ngrams.compute_ngrams(romeo_toks, n=4)
    assert set(dct['but']) == set([('sick', 'and', 'green'), 
                                   ('fools', 'do', 'wear')])
    assert set(dct['it'])  == set([('is', 'the', 'east,'),
                                   ('off.', 'it', 'is'),
                                   ('is', 'my', 'lady,'),
                                   ('is', 'my', 'love!'),
                                   ('were', 'not', 'night.')])


@pytest.mark.points(5)
def test_compute_ngrams_peterpan():
    with open('peterpan.txt') as f:
        pp_toks = [t.lower() for t in f.read().split()]
        
    dct = ngrams.compute_ngrams(pp_toks, n=3)
    assert set(dct['crocodile']) == set([('passes,', 'but'),
                    ('that', 'happened'),
                    ('would', 'have'),
                    ('was', 'in'),
                    ('passed', 'him,'),
                    ('is', 'about'),
                    ('climbing', 'it.'),
                    ('that', 'was'),
                    ('pass', 'by'),
                    ('and', 'let'),
                    ('was', 'among'),
                    ('was', 'waiting')])
    assert len(dct['wendy']) == 202
    assert len(dct['peter']) == 243


@pytest.mark.points(5)
def test_gen_passage_simple():
    random.seed(1234)
    simple_toks = [t.lower() for t in 'I really really like cake.'.split()]
    assert ngrams.gen_passage(ngrams.compute_ngrams(simple_toks), 10) == \
                'like cake. i really really really really like cake. i'


@pytest.mark.points(5)
def test_gen_passage_romeo():
    random.seed(1234)
    romeo_toks = [t.lower() for t in ROMEO_SOLILOQUY.split()]
    assert ngrams.gen_passage(ngrams.compute_ngrams(romeo_toks), 10) == \
                'too bold, \'tis not night. see, how she leans her'

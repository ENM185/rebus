#!/usr/bin/env python3

import nltk
import patterns

nltk.download('punkt')

impl_binary_terminators = {
        "around": patterns.r_around,
        }

impl_unary_terminators = {}

impl_binary = {
        # TODO function aliases happen here
        "above": patterns.r_above,
        "after": patterns.r_after,
        "before": patterns.r_before,
        "against": patterns.r_against,
        "under": patterns.r_under,
        "below": patterns.r_below,
        "in": patterns.r_in
        }

impl_unary = {}

def get_rebus(sentence):
    articles = { "the", "a", "an" }
    tokens = nltk.word_tokenize(sentence)
    tokens[:] = (value for value in tokens if value not in articles)
    return rebus_magic(tokens, True)

def rebus_magic(tokens, terminators_allowed=False):
    for t in tokens:
        i = tokens.index(t)

        # binary terminator functions
        if terminators_allowed:
            if (t in impl_binary_terminators.keys()):
                if (i == 0) or (i == len(tokens) - 1):
                    pass
                else:
                    leftSide = " ".join(tokens[:i])
                    rightSide = " ".join(tokens[i + 1:])
                    result = impl_binary[word](leftSide, rightSide)
                    return rebus_magic(result)

        # unary terminator functions
        if terminators_allowed:
            if (t in impl_unary_terminators.keys()):
                if i == len(tokens) - 1:
                    pass
                else:
                    rightSide = " ".join(tokens[i + 1:])
                    result = impl_unary[word](rightSide)
                    return rebus_magic(result)

        # binary functions
        if t in impl_binary.keys():
            if (i == 0) or (i == len(tokens) - 1):
                pass
            else:
                leftSide = " ".join(tokens[:i])
                rightSide = " ".join(tokens[i + 1:])
                result = impl_binary[word](leftSide, rightSide)
                return rebus_magic(result)

        # unary functions
        if t in impl_unary.keys():
            if i == len(tokens) - 1:
                pass
            else:
                rightSide = " ".join(tokens[i + 1:])
                result = impl_unary[word](leftSide, rightSide)
                return rebus_magic(result)

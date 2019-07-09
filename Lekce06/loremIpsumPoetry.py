
def lorem_ipsum(num_rows):
    import random
    articles = ["the", "a", "an"]
    determiners = ["another", "this", "every", "many"]
    subjects = ["cat", "dog", "man", "woman"]
    verbs = ["sang", "ran", "jumped"]
    adverbs = ["loudly", "quietly", "well", "badly"]

    for i in range(num_rows):
        order = random.randint(1, 3)

        if order == 1:
            print(random.choice(articles) + " " + random.choice(subjects) +\
            " " + random.choice(verbs) + " " + random.choice(adverbs))
        elif order == 2:
            print(random.choice(determiners) + " " + random.choice(subjects) +\
            " " + random.choice(verbs))
        else:
            print(random.choice(determiners) + " " + random.choice(subjects) +\
            " " + random.choice(verbs) + " " + random.choice(adverbs))




lorem_ipsum(5)

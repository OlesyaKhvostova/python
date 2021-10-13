from random import choice


def get_jokes(number, **kwargs):
    nouns = ["автомобиль","лес","огонь","город","дом"]
    adverbs = ["сегодня","вчера","завтра","позавчера","ночью"]
    adjectives = ["веселый","яркий","зеленый","утопичный","мягкий"]

    jokes = list()
    cur_index = 0
    while cur_index < number:
        noun = choice(nouns)
        adv = choice(adverbs)
        adj = choice(adjectives)

        add_to_jokes = True

        if kwargs["check_exist_word"]:
            search_item = filter(lambda x: x.count(noun) or x.count(adv) or x.count(adj), jokes)
            _ = list(search_item)
            if len(_):
                add_to_jokes = False

        if add_to_jokes:
            jokes.append(f'{noun} {adv} {adj}')
            cur_index += 1

    return jokes


print(get_jokes(4, check_exist_word=True))

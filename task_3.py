'''
В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
Не учитывать знаки препинания и регистр символов. 
За основу возьмите любую статью из википедии или из документации к языку.
'''

essay = "After the attack on Pearl Harbor, \
    the feelings of animosity in America against Japan increased. \
    By late 1945, the Allied leaders met in Germany with news of a secret new weapon, \
        called the atomic bomb, created by American scientists,\
              that was powerful enough to destroy an entire city.\
                  However, there were some feelings that the bomb was too powerful, \
                    and the leaders chose instead to send the Potsdam Declaration to Japan \
                        warning them to surrender. The Japanese military did not know about the \
                            atomic bomb and ignored the warning, so on August 6th 1945,\
                                  an American bomber called the Enola Gay was dropped on Hiroshima, Japan.\
                                      This blast killed an approximated 70,000 people and destroyed more than eighty percent of the city,\
                                          but the Japanese still did not surrender. The US dropped a second atomic bomb,\
                                              and after a furious debate in the Japanese cabinet, \
                                                the emperor of Japan announced a surrender. \
                                                    This day on the 14th of August became known as V-J Day, for Victory over Japan."

dublicates = []

words =  essay.split()

word_counts = {}

for word in words:
    if word in word_counts:
        word_counts[word] += 1

    else:
        word_counts[word] = 1


sorted_word_counts = dict(sorted(word_counts.items(), key=lambda item: item[1], reverse=True))

top_10_sorted_word_counts = dict(list(sorted_word_counts.items())[:10])

for word, count in top_10_sorted_word_counts.items():
    print(f'{word}: {count}')
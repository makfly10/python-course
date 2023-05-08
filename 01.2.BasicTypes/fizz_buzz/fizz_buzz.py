import typing as tp


def get_fizz_buzz(n: int) -> list[tp.Union[int, str]]:
    """
    If value divided by 3 - "Fizz",
       value divided by 5 - "Buzz",
       value divided by 15 - "FizzBuzz",
    else - value.
    :param n: size of sequence
    :return: list of values.
    """

    answer = []
    for figure in range(1, n + 1, 1):
        if figure % 15 == 0:
            answer.append('FizzBuzz')
        elif figure % 3 == 0:
            answer.append('Fizz')
        elif figure % 5 == 0:
            answer.append('Buzz')
        else:
            answer.append(figure)
    return answer

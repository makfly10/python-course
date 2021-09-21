import copy
import dataclasses
import itertools
import random
import string
import sys

import pytest

from .alphabet import get_alphabet, build_graph


@dataclasses.dataclass
class Case:
    words: list[str]
    result: dict[str, set[str]]

    def __str__(self) -> str:
        return str(self.words)


TEST_CASES = [
    Case(words=[],
         result={}),
    Case(words=["aa", "aab"],
         result={"a": set(), "b": set()}),
    Case(words=["aabcde"],
         result={"a": set(), "b": set(), "c": set(), "d": set(), "e": set()}),
    Case(words=["aa", "aab", "acb"],
         result={"a": {"c"}, "b": set(), "c": set()}),
    Case(words=["aaa", "bbb", "cccc"],
         result={"a": {"b"}, "b": {"c"}, "c": set()}),
    Case(words=["aa", "aa", "aa"],
         result={"a": set()}),
    Case(words=["aab", "aac", "aad"],
         result={"b": {"c"}, "c": {"d"}, "a": set(), "d": set()}),
    Case(words=["aa", "aac", "aab"],
         result={"c": {"b"}, "a": set(), "b": set()}),
    Case(words=["aab", "aac", "dee", "deeer"],
         result={"b": {"c"}, "a": {"d"}, "c": set(), "d": set(), "e": set(), "r": set()}),
    Case(words=["aawq", "aad", "aade"],
         result={"w": {"d"}, "q": set(), "a": set(), "d": set(), "e": set()}),
    Case(words=["aawq", "aad", "aadf", "fdaa", "ffdd"],
         result={"w": {"d"}, "a": {"f"}, "d": {"f"}, "f": set(), "q": set()}),
    Case(words=["aawq", "bced", "bcddd"],
         result={"a": {"b"}, "e": {"d"}, "b": set(), "c": set(), "d": set(), "q": set(), "w": set()}),
    Case(words=["aa", "aab", "aacb", "aacf", "aacc", "dacdf", "dfghr", "dfchr", "zfdcf", "zxdcf", "zxdcr"],
         result={"b": {"c", "f"}, "a": {"d", "f"}, "d": {"z"}, "z": set(), "x": set(),
                 "f": {"c", "x", "r"}, "g": {"c"}, "c": set(), "h": set(), "r": set()}),
    Case(words=["agc", "bha", "ebc", "ebe", "eeb"],
         result={"a": {"b"}, "b": {"e"}, "c": {"e"}, "h": set(), "g": set(), "e": set()}),
    Case(words=["a", "b", "ba", "bc", "bca", "bcd", "bcda", "bcde"],
         result={"a": {"b", "c", "d", "e"}, "b": set(), "c": set(), "d": set(), "e": set()})
]


def _generate_words(n: int) -> set[str]:

    words: set[str] = set()

    while len(words) != n:
        word_len = random.choice(range(3, 6))
        words.add("".join(random.choices(string.ascii_letters, k=word_len)))

    return words


def test_banned_modules() -> None:
    banned_modules = ['graphlib']

    for module_name in banned_modules:
        assert module_name not in sys.modules, f'You have imported the {module_name} module'


def test_random_stress() -> None:
    alphabet = "".join(random.sample(string.ascii_letters, len(string.ascii_letters)))
    words = sorted(_generate_words(100000), key=lambda word: tuple([alphabet.index(c) for c in word]))
    graph = build_graph(words)

    words_copy = copy.deepcopy(words)

    result_alphabet = get_alphabet(words_copy)

    assert words_copy == words, "You shouldn't change inputs"

    assert sorted(result_alphabet) == sorted(alphabet)

    for i, letter in enumerate(result_alphabet):
        if letter in graph:
            for c in graph[letter]:
                assert result_alphabet.index(c) > i


@pytest.mark.parametrize("t", TEST_CASES, ids=str)
def test_build_graph(t: Case) -> None:
    words_copy = copy.deepcopy(t.words)

    graph = build_graph(words_copy)
    assert t.words == words_copy, "You shouldn't change inputs"

    assert graph == t.result


@pytest.mark.parametrize("t", TEST_CASES, ids=str)
def test_get_alphabet(t: Case) -> None:
    words_copy = copy.deepcopy(t.words)

    graph = build_graph(words_copy)
    answer = get_alphabet(words_copy)

    assert t.words == words_copy, "You shouldn't change inputs"

    all_letters = sorted(set(itertools.chain(*t.words)))

    assert sorted(answer) == all_letters

    for i, letter in enumerate(answer):
        if letter in graph:
            for c in graph[letter]:
                assert answer.index(c) > i
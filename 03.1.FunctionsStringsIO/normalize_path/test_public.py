import dataclasses

import pytest

from .normalize_path import normalize_path


@dataclasses.dataclass
class Case:
    path: str
    result: str


TEST_CASES = [
    Case(path='foo', result='foo'),
    Case(path='./bar', result='bar'),
    Case(path='', result='.'),
    Case(path='.', result='.'),
    Case(path='zog/..', result='.'),
    Case(path='./config/../etc', result='etc'),
    Case(path='foo/./bar', result='foo/bar'),
    Case(path='a/..///../b', result='../b'),
    Case(path='./../../../zog', result='../../../zog'),
    Case(path='/////documents/root/.././../etc', result='/etc'),
    Case(path='/../../../zog', result='/zog'),
    Case(path='/foo/bar//baz/asdf/quux/..', result='/foo/bar/baz/asdf'),
    Case(path='/h/../a/..' * 1_000_000, result='/'),
    Case(path='/a/b//c/d/..//../..//..' * 1_000_000, result='/'),
]


@pytest.mark.parametrize('case', TEST_CASES)
def test_normalize(case: Case) -> None:
    answer = normalize_path(case.path)

    assert answer == case.result

import sys
import typing as tp

import pytest

# pls don't use `inspect` and `FunctionType`
from . import function_type_ban  # noqa
from . import cases  # noqa
from . import vm_scorer  # noqa
from . import vm_runner  # noqa

sys.modules['inspect'] = None  # type: ignore # noqa

from . import vm  # noqa


IDS = [test.name for test in cases.TEST_CASES]
TESTS = [test.text_code for test in cases.TEST_CASES]
SCORER = vm_scorer.Scorer(TESTS)
SCORES = [SCORER.score(test) for test in TESTS]


class Scorer:
    def __init__(self) -> None:
        self._score: float = 0.
        self._blocking_error: bool = False

    def add_blocking_error(self) -> None:
        self._blocking_error = True

    def add_score(self, score: float) -> None:
        self._score += score

    @property
    def score(self) -> float:
        if self._blocking_error:
            return 0.
        else:
            return self._score

    def __str__(self) -> str:
        return f'\nSummary score is: {self.score}'


def test_version() -> None:
    """
    To do this task you need python=3.9.7
    """
    assert '3.9.7' == sys.version.split(' ', maxsplit=1)[0]


@pytest.fixture(scope="module")
def task_scorer() -> tp.Generator[Scorer, None, None]:
    scorer = Scorer()
    yield scorer
    # vm_scorer.dump_tests_stat(sys.stdout, SCORER)
    print(scorer)


@pytest.mark.parametrize("test,score", zip(cases.TEST_CASES, SCORES), ids=IDS)
def test_all_cases(test: cases.Case, score: float, task_scorer: Scorer) -> None:
    """
    Compare all test cases with etalon
    :param test: test case to check
    :param score: score for test if passed
    """
    code = vm_runner.compile_code(test.text_code)
    globals_context: dict[str, tp.Any] = {}
    vm_out, vm_err, vm_exc = vm_runner.execute(code, vm.VirtualMachine().run)
    py_out, py_err, py_exc = vm_runner.execute(code, eval, globals_context, globals_context)

    assert vm_out == py_out

    if py_exc is not None:
        assert vm_exc == py_exc
    else:
        assert vm_exc is None

    # Write score into scorer
    task_scorer.add_score(score)

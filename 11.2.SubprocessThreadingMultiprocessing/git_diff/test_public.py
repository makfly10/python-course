import zipfile
from dataclasses import dataclass
from pathlib import Path
import typing as tp

import pytest

from .git_diff import get_changed_dirs


GIT_REPO_DIR = Path(__file__).parent / 'testdata'


def rmtree(path: Path) -> None:
    for child in path.iterdir():
        if child.is_file():
            child.unlink()
        else:
            rmtree(child)
    path.rmdir()


@pytest.fixture(scope="session", autouse=True)
def unzip_git_repo() -> tp.Generator[None, None, None]:
    with zipfile.ZipFile(Path(__file__).parent / 'testdata.zip', 'r') as zip_ref:
        zip_ref.extractall(Path(__file__).parent)
    yield
    rmtree(GIT_REPO_DIR)


tasks = {
    1: GIT_REPO_DIR / 'task1',
    2: GIT_REPO_DIR / 'task2',
    3: GIT_REPO_DIR / 'task3',
    4: GIT_REPO_DIR / 'task4',
    5: GIT_REPO_DIR / 'task5',
    6: GIT_REPO_DIR / 'task6',
    7: GIT_REPO_DIR / 'task7',
}


@dataclass
class Case:
    from_commit_hash: str
    to_commit_hash: str
    expected_dirs: tp.Set[Path]


TEST_CASES = [
    Case(
        from_commit_hash='e9bd09aed488b562df0116174ec4feb973e9eb1a',
        to_commit_hash='f8f989433f0d0445070fbee045e93953bce7ba59',
        expected_dirs={tasks[5], tasks[7]}
    ),
    Case(
        from_commit_hash='14356e546a6841cea7132f60c2a5d9bf36dea660',
        to_commit_hash='e9bd09aed488b562df0116174ec4feb973e9eb1a',
        expected_dirs={tasks[3], tasks[6]}
    ),
    Case(
        from_commit_hash='4a9ed009a7e82d6c1c600093c67bea8b990659d3',
        to_commit_hash='ca0a45e88fa9f2b045a5c58636c4041a047ccaf3',
        expected_dirs={tasks[2], tasks[3]}
    ),
    Case(
        from_commit_hash='22ac60faec7b38c68e7a740557e3864dbae1689d',
        to_commit_hash='4a9ed009a7e82d6c1c600093c67bea8b990659d3',
        expected_dirs={tasks[1]}
    ),
]


@pytest.mark.parametrize('case', TEST_CASES, ids=str)
def test_git_diff(case: Case) -> None:
    dirs = get_changed_dirs(
        GIT_REPO_DIR,
        case.from_commit_hash,
        case.to_commit_hash
    )
    assert case.expected_dirs == dirs

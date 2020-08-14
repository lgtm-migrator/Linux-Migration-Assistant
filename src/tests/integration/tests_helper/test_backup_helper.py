from pathlib import Path

from helpers.backup_helper import get_different_blocks

import pytest

CURRENT_FOLDER = Path(__file__).resolve().parent


@pytest.mark.parametrize('file_to_compare,is_diff',[
    (f'{CURRENT_FOLDER}/test_file/same.txt', []),
    (f'{CURRENT_FOLDER}/test_file/diff.txt', [16]),
])
def test_has_different_blocks(file_to_compare, is_diff):
    original_file_path = f'{CURRENT_FOLDER}/test_file/original.txt'
    assert get_different_blocks(src=original_file_path, dst=file_to_compare) == is_diff

import pytest

from utils.dicts import get_val


@pytest.mark.parametrize('collection, key, default, expected', [
    ({"vcs": "mercurial"}, "vcs", None, "mercurial"),
    ({"vcs": "mercurial"}, "vcs", "git", 'mercurial'),
    ({}, "vcs", "git", 'git'),
    ({}, "vcs", "bazaar", 'bazaar')
])
def test_getval1(collection, key, default, expected):
    assert get_val(collection, key, default) == expected

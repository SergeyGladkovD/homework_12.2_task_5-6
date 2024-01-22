from utils.dicts import get_val


def test_getval1():
	assert get_val({"vcs": "mercurial"}, "vcs") == "mercurial"


def test_getval2():
	assert get_val({"vcs": "mercurial"}, "vcs", default="git") == "mercurial"


def test_getval3():
	assert get_val({}, "vcs", default='git') == "git"


def test_getval4():
	assert get_val({}, "vcs", default="bazaar") == "bazaar"

# SPDX-License-Identifier: GPL-3.0-or-later
"""The release this handbook documents, in both languages.

./VERSION mirrors iso/VERSION, where the number is decided. README.md says
the release once, in English and in French, and no page repeats it -- a
number written in seven chapters is a number that drifts in six of them.

English says "Beta", French says "Bêta". That is not a typo on either
side: it is the rule the website already follows (tools/build_pages.py
renders the French title by replacing Beta with Bêta), so the handbook
follows it too.

    python3 -I -B tests/test_version.py

Running it runs every other test file of tests/ too, each one by path --
see SIDECARS at the bottom and the comment with it.
"""
import importlib.util
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
VERSION = (ROOT / "VERSION").read_text().strip()
README = (ROOT / "README.md").read_text()

PRODUCT = "Raye Linux"
FRENCH = VERSION.replace("Beta", "Bêta")
PAGES = sorted(p for p in ROOT.rglob("*.md") if p.name != "README.md")


def test_version_is_the_beta():
    assert re.fullmatch(r"\d+(?:\.\d+)+ Beta(?: \d+)?", VERSION), VERSION


def test_readme_says_the_release_in_english():
    assert f"{PRODUCT} {VERSION}" in README, (
        f"README.md never says {PRODUCT} {VERSION}")


def test_readme_says_the_release_in_french():
    assert f"{PRODUCT} {FRENCH}" in README, (
        f"README.md never says {PRODUCT} {FRENCH} (French spells it Bêta)")


def test_the_two_languages_are_the_same_release():
    """A French page left on an older release is the drift this prevents."""
    english = re.findall(r"%s (\d+(?:\.\d+)+) Beta" % PRODUCT, README)
    french = re.findall(r"%s (\d+(?:\.\d+)+) Bêta" % PRODUCT, README)
    assert english and french, (english, french)
    assert set(english) == set(french) == {VERSION.split()[0]}, (english, french)


def test_no_chapter_repeats_the_number():
    """The release lives in README.md and nowhere else, so there is one
    line to edit next time."""
    number = re.escape(VERSION.split()[0])
    spelt = re.compile(r"%s[ _-]+B[eê]ta" % number, re.I)
    for page in PAGES:
        rel = page.relative_to(ROOT)
        for line in page.read_text().splitlines():
            assert not spelt.search(line), (
                f"{rel}: the release is repeated here, keep it in README.md: {line.strip()}")


def test_both_languages_have_the_same_pages():
    """A chapter in one language only is a handbook that lies to half its
    readers about what it covers."""
    en = {p.name.split("-", 1)[0] for p in (ROOT / "en").glob("*.md")}
    fr = {p.name.split("-", 1)[0] for p in (ROOT / "fr").glob("*.md")}
    assert en == fr, f"only in en: {sorted(en - fr)}, only in fr: {sorted(fr - en)}"


def test_mirrors_the_iso_version():
    """iso/VERSION decides the number; this repo only follows it. The image
    is built with every repo checked out side by side, so this compares for
    real there. A lone clone says so out loud rather than passing quietly.
    """
    source = ROOT.parent / "iso" / "VERSION"
    if not source.is_file():
        print(f"no sibling {source}: cross-check skipped, ./VERSION not compared")
        return
    assert source.read_text() == (ROOT / "VERSION").read_text(), (
        f"./VERSION is {VERSION!r}, iso/VERSION is {source.read_text().strip()!r}")


# The launcher of the tree runs ONE command for this repo
# (raye_tests_suites.py: handbook/version), and that table is in another
# repo. A second test file left to be registered there is a second file
# nobody runs, so this one runs them all.
#
# Named one by one, never globbed. A glob that matched nothing would
# drop a whole suite out of the gate without a line of output -- the same
# silence as a test that skips itself. A file in tests/ that is missing
# here fails below, so the list cannot fall behind either.
#
# And loaded by PATH, not by name: python3 -I implies -P, which keeps
# the script's own directory out of sys.path, so `import test_promises`
# raises ModuleNotFoundError (measured, CPython 3.13.5).
SIDECARS = ("test_promises.py", "test_hyprland_guide.py")


def run(cases):
    """Every test_* of a namespace; returns how many failed."""
    bad = 0
    for name, case in sorted(cases.items()):
        if not name.startswith("test_"):
            continue
        try:
            case()
        except AssertionError as error:
            bad += 1
            print(f"FAIL - {name}: {error}")
        except Exception as error:
            # Not an assertion -- a file that is not there, a source read
            # the wrong way. It still has to print a red line: a traceback
            # on its own counts as nothing at all.
            bad += 1
            print(f"FAIL - {name}: {type(error).__name__}: {error}")
        else:
            print(f"ok - {name}")
    return bad


def sidecars():
    """The other test files of tests/, loaded by path."""
    here = pathlib.Path(__file__).resolve().parent
    mine = pathlib.Path(__file__).name
    on_disk = {p.name for p in here.glob("test_*.py")} - {mine}
    missing = sorted(on_disk - set(SIDECARS))
    assert not missing, (
        f"tests/{', tests/'.join(missing)} would not be run: add it to "
        f"SIDECARS in tests/{mine}")
    out = []
    for name in SIDECARS:
        path = here / name
        assert path.is_file(), f"{path} is in SIDECARS and not on disk"
        spec = importlib.util.spec_from_file_location(path.stem, path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        out.append(module)
    return out


if __name__ == "__main__":
    bad = run(dict(globals()))
    # Wrapped so a broken list prints a red LINE and not only a traceback:
    # the launcher counts "ok -" and "FAIL -" lines, and a traceback alone
    # would leave a tally of nothing but passes next to a non-zero exit.
    try:
        found = sidecars()
    except Exception as error:
        bad += 1
        found = []
        print(f"FAIL - sidecars: {type(error).__name__}: {error}")
    for module in found:
        bad += run(vars(module))
    sys.exit(1 if bad else 0)

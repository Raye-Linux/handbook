# SPDX-License-Identifier: GPL-3.0-or-later
"""The Hyprland chapter (en/12, fr/12) stays true.

A guide to editing a config is worth what its examples are worth: an
example that Hyprland refuses sends the reader to a red error bar. So every
line of Hyprland written in the chapter is given to `Hyprland
--verify-config`, the commands it names are looked up in the tool that
implements them, and both languages must carry the same examples.

    python3 -I -B tests/test_hyprland_guide.py

RAYE_SRC points at another checkout of the tree (default: the parent of
this repo). Without Hyprland on PATH the parse check says so and is not run.
"""
import os
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
import textwrap

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = pathlib.Path(os.environ.get("RAYE_SRC", ROOT.parent))
PAGES = {"en": ROOT / "en" / "12-hyprland.md", "fr": ROOT / "fr" / "12-hyprland.md"}
LONE = not (SRC / "theme" / "hyprland").is_dir()

LINE = re.compile(r"^\s*(\}|[\w.:\-]+\s*(=|\{))")


def hypr_lines(path):
    """The Hyprland lines of the indented examples, dedented, in order."""
    out, run = [], []
    for raw in path.read_text(encoding="utf-8").splitlines() + [""]:
        if raw.startswith("    ") or (run and not raw.strip()):
            run.append(raw)
            continue
        text = textwrap.dedent("\n".join(run))
        out += [l for l in text.splitlines() if LINE.match(l)]
        run = []
    return out


def test_both_languages_have_the_same_examples():
    en, fr = hypr_lines(PAGES["en"]), hypr_lines(PAGES["fr"])
    assert len(en) > 30, "the examples were not found: has the chapter's layout changed?"
    assert en == fr, "the English and French examples differ"


def test_every_example_parses_in_hyprland():
    hyprland = shutil.which("Hyprland")
    if not hyprland:
        print("-- every_example_parses: no Hyprland on PATH, not run")
        return
    lines = hypr_lines(PAGES["en"])
    with tempfile.TemporaryDirectory() as runtime:
        os.chmod(runtime, 0o700)
        conf = pathlib.Path(runtime) / "guide.conf"
        # the curve the animation example names is Raye's, defined in its file
        conf.write_text("bezier = rayeIn, 0, 0, 0, 1\n" + "\n".join(lines) + "\n")
        args = [hyprland, "--verify-config", "-c", str(conf)]
        if os.geteuid() == 0:
            args.insert(1, "--i-am-really-stupid")
        run = subprocess.run(args, capture_output=True, text=True, timeout=60,
                             env=dict(os.environ, XDG_RUNTIME_DIR=runtime))
    out = run.stdout + run.stderr
    assert run.returncode == 0 and "config ok" in out, out


def test_a_wrong_example_would_be_caught():
    hyprland = shutil.which("Hyprland")
    if not hyprland:
        print("-- wrong_example: no Hyprland on PATH, not run")
        return
    with tempfile.TemporaryDirectory() as runtime:
        os.chmod(runtime, 0o700)
        conf = pathlib.Path(runtime) / "bad.conf"
        conf.write_text("bind = SUPER, T, notadispatcher,\n")
        args = [hyprland, "--verify-config", "-c", str(conf)]
        if os.geteuid() == 0:
            args.insert(1, "--i-am-really-stupid")
        run = subprocess.run(args, capture_output=True, text=True, timeout=60,
                             env=dict(os.environ, XDG_RUNTIME_DIR=runtime))
    assert run.returncode != 0


def test_the_commands_named_exist():
    if LONE:
        print("-- commands_named: handbook cloned on its own, nothing to compare")
        return
    tool = (SRC / "theme/hyprland/tools/raye-hyprland-config").read_text()
    for page in PAGES.values():
        text = page.read_text(encoding="utf-8")
        for sub in re.findall(r"raye-hyprland-config (dots \w+|open|reload|reset)", text):
            word = sub.split()[-1]
            assert re.search(rf"\b{word}\)|\b{word}\b\s*\)|\b{word}\)", tool) or f"{word})" in tool, \
                f"{page.name} names `{sub}`, the tool has no such command"
    conf = (SRC / "theme/hyprland/config/hyprland.conf").read_text()
    assert "bind = SUPER, M," in conf, "the guide shows `unbind = SUPER, M`: Raye no longer binds it"
    session = (SRC / "theme/hyprland/session/raye-hyprland-session").read_text()
    for name in ("user.conf", "keyboard.conf", "monitors.conf", "hyprlock.conf"):
        assert name in session, f"the session no longer writes {name}"


def test_the_settings_buttons_are_named_as_on_screen():
    if LONE:
        print("-- settings_buttons: handbook cloned on its own, nothing to compare")
        return
    po = (SRC / "settings/po/fr/raye-settings.po").read_text(encoding="utf-8")
    for en, fr in (("Open my Hyprland settings", "Ouvrir mes réglages Hyprland"),
                   ("Hyprland guide", "Guide Hyprland")):
        assert re.search(rf'^msgid "{en}"\nmsgstr "{fr}"$', po, re.M), f"Settings has no {en!r}/{fr!r}"
    assert "Open my Hyprland settings" in PAGES["en"].read_text(encoding="utf-8")
    assert "Ouvrir mes réglages Hyprland" in PAGES["fr"].read_text(encoding="utf-8")


def test_the_guide_is_listed_in_the_readme():
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    assert "en/12-hyprland.md" in readme and "fr/12-hyprland.md" in readme


if __name__ == "__main__":
    bad = 0
    for name, case in sorted(dict(globals()).items()):
        if name.startswith("test_"):
            try:
                case()
                print(f"ok - {name}")
            except AssertionError as error:
                bad += 1
                print(f"FAIL - {name}: {error}")
    sys.exit(1 if bad else 0)

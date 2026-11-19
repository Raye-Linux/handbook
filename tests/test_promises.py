# SPDX-License-Identifier: GPL-3.0-or-later
"""Keeps the handbook's checkable claims tied to what they come from.

A manual rots in one direction: the system changes, the page does not, and
nobody notices because prose has nothing to compile. These checks pin the
few facts that CAN be pinned -- a link, a figure, an address, the number of
known problems -- to the file that decides them, so a page that has become
false goes red instead of growing old quietly.

What it cannot do, and no analysis can: it does not read. It cannot tell
whether an explanation is clear, whether the order helps, or whether a true
sentence is the one a frightened reader needs. It only says that a fact is
still a fact.

    python3 -I -B tests/test_promises.py

Sources outside this repo are read, never written. In the full /srv/raye
tree every one of them must be there: a renamed or deleted source is a
failure, not a quiet pass. A handbook cloned on its own (no sibling repo at
all) runs the checks that need nothing else and says so on the line.
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
RAYE = ROOT.parent

PAGES = sorted(p for p in (ROOT / "en").glob("*.md")) + \
        sorted(p for p in (ROOT / "fr").glob("*.md"))
README = ROOT / "README.md"
LINKED = PAGES + [README]
# the notes of the release in VERSION: "0.5 Beta" -> release-notes-0.5-beta.md
SLUG = (ROOT / "VERSION").read_text().strip().lower().replace(" ", "-")
NOTES_EN = f"iso/docs/release-notes-{SLUG}.md"
NOTES_FR = f"iso/docs/release-notes-{SLUG}.fr.md"

# Every file outside this repo that a check below reads, with the claim it
# answers for. Keep the two in step: a check that reads a file missing from
# this table is a check whose source can vanish unnoticed.
SOURCES = {
    NOTES_EN: "the known problems, in English",
    NOTES_FR: "the known problems, in French",
    "installer/etc/calamares/modules/welcomeq.conf": "the free space the installer demands",
    "installer/etc/calamares/settings.conf": "which modules the installer runs",
    "installer/usr/lib/calamares/modules/rayedisk/rayedisk_core.py": "whether partitions can be carved by hand",
    "installer/etc/calamares/branding/raye/strings.js": "what the installer says before a dual boot",
    "settings/po/fr/raye-settings.po": "the names of the two kinds of account, and Settings' labels",
    "theme/config/kglobalshortcutsrc": "what Ctrl+Shift+Esc opens",
    "apps/taskmanager/src/org.raye.taskmanager.desktop": "the Task Manager's name",
    "update/src/raye_update.py": "whether updates install while you work",
    "update/src/raye-update-notify": "the button of the update notification",
    "wine/third-party/sources.txt": "what the Windows layer carries for DirectX and .NET",
    "theme/shell/po/fr/raye_shell_start.po": "the Start menu's Update and restart",
    "files/po/fr/raye-files.po": "the archive commands of File Explorer",
    "settings/portal/units/raye-device-portal.socket": "the port of Device Portal",
    "wine/release/windows/titles/00-upstream.titles": "games their publisher keeps off this system",
    "wine/release/windows/titles/50-raye.titles": "what Raye says about some Windows programs",
}

# Labels a page tells the reader to click or look for, with the file that
# shows them. A renamed button turns a page into a hunt for a word the
# screen no longer has.
LABELS = (
    ("03-updates.md", "03-mises-a-jour.md", "settings/po/fr/raye-settings.po",
     (("Install now", "Installer maintenant"), ("Restart now", "Redémarrer maintenant"),
      ("Restart required", "Redémarrage requis"), ("Pause", "Suspendre"),
      ("Resume updates", "Reprendre les mises à jour"))),
    ("03-updates.md", "03-mises-a-jour.md", "theme/shell/po/fr/raye_shell_start.po",
     (("Update and restart", "Mettre à jour et redémarrer"),)),
    ("02-first-steps.md", "02-premiers-pas.md", "files/po/fr/raye-files.po",
     (("Extract all…", "Extraire tout…"), ("Extract here", "Extraire ici"),
      ("Extract to a new folder", "Extraire dans un nouveau dossier"),
      ("Compress to", "Compresser en"), ("Additional options…", "Options supplémentaires…"),
      ("Add to archive", "Ajouter à l'archive"))),
    ("10-for-developers.md", "10-pour-les-developpeurs.md", "settings/po/fr/raye-settings.po",
     (("Advanced", "Avancé"), ("For developers", "Pour les développeurs"),
      ("Developer Mode", "Mode développeur"), ("Device Portal", "Portail d'appareil"),
      ("OpenSSH server", "Serveur OpenSSH"), ("Device discovery", "Découverte d'appareil"),
      ("Sign in with a key only", "Connexion par clé uniquement"), ("Address", "Adresse"),
      ("Certificate fingerprint", "Empreinte du certificat"), ("Set", "Définir"),
      ("Pair a device", "Appairer un appareil"), ("Connection log", "Journal des connexions"))),
    ("04-windows-programs.md", "04-programmes-windows.md", "settings/po/fr/raye-settings.po",
     (("Installed apps", "Applications installées"),)),
)

# What the layer carries, and how a paragraph of the beta page would say,
# wrongly, that it is missing.
CARRIED = (
    ("dxvk-src", "DirectX", re.compile(r"DirectX|Vulkan")),
    ("mono", ".NET", re.compile(r"\.NET")),
)
MISSING = re.compile(r"not in this image|nothing supplies|pas dans cette image|rien ne fournit", re.I)

# Games the Windows chapter says will not run, and why it says so.
BLOCKED = ("Roblox", "Valorant", "Fortnite")
# A lone clone of the handbook: no sibling repo of the tree at all.
LONE = not any((RAYE / name).is_dir() for name in ("iso", "installer", "settings"))

# The layer that runs Windows programs is never named to a reader, in any
# language. Settings, the dialogs and the menus say "Windows programs"; a
# page that names the project behind it teaches a word the system never
# uses, and that the person would then look for in vain.
UNNAMEABLE = re.compile(r"\bwine\b", re.I)

# Raye speaks Linux about rights: root, a sudo user, a standard user.
ADMINISTRATOR = re.compile(r"administrat|\badmin\b", re.I)

MD_LINK = re.compile(r"\]\(([^)\s]+)\)")
ANCHOR = re.compile(r'<a id="([^"]+)"></a>')
HANDBOOK_URL = re.compile(
    r"https://github\.com/Raye-Linux/handbook/blob/main/([A-Za-z0-9/._-]+\.md)")
FRAGMENT = re.compile(r'"#([A-Za-z0-9][A-Za-z0-9-]*)"')
HEX_COLOUR = re.compile(r"^[0-9a-fA-F]{3,8}$")
# Not worth walking: history, and what the builds leave behind.
SKIP_DIRS = {".git", "out", "build", "target", "node_modules", "__pycache__"}


def source(rel):
    """The text of a file this repo does not own, or None on a lone clone."""
    assert rel in SOURCES, f"{rel} is read but not declared in SOURCES"
    path = RAYE / rel
    if LONE:
        return None
    assert path.is_file(), (
        f"{path} is gone or renamed. {SOURCES[rel]} is checked against it; "
        f"find where it moved rather than dropping the check")
    return path.read_text(encoding="utf-8")


def lone(name):
    """Say so, without printing a second verdict.

    ⚠️ The launcher counts lines: anything starting with "ok" is a pass and
    anything starting with "FAIL" a failure, leading blanks included. A note
    here that began with either word would be counted on top of the verdict
    run() prints, and the suite would report more tests than it ran.
    """
    print(f"-- {name}: handbook cloned on its own, nothing to compare")


def known_issues(text):
    """The top-level bullets under the known-problems heading."""
    body = re.search(r"^## (?:Known issues|Problèmes connus)[ \t]*\n(.*?)(?=^## )",
                     text, re.S | re.M)
    assert body, "the release notes have no known-problems section under a known heading"
    return [line for line in body.group(1).splitlines() if line.startswith("- ")]


def test_no_page_link_goes_nowhere():
    """A link to a chapter that was never written is the one mistake a
    reader cannot work around: it reads as "the answer is elsewhere"."""
    bad = []
    for page in LINKED:
        for target in MD_LINK.findall(page.read_text(encoding="utf-8")):
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            path, _, fragment = target.partition("#")
            if not path:
                continue
            if not (page.parent / path).resolve().is_file():
                bad.append(f"{page.relative_to(ROOT)} -> {target}")
                continue
            if fragment:
                text = (page.parent / path).read_text(encoding="utf-8")
                if fragment not in ANCHOR.findall(text):
                    bad.append(f"{page.relative_to(ROOT)} -> {target} (no such anchor)")
    assert not bad, "links that lead nowhere: " + ", ".join(bad)


def test_the_windows_layer_is_never_named():
    """Raye calls it "Windows programs" everywhere a person can see."""
    bad = [f"{p.relative_to(ROOT)}:{n}"
           for p in LINKED
           for n, line in enumerate(p.read_text(encoding="utf-8").splitlines(), 1)
           if UNNAMEABLE.search(line)]
    assert not bad, ("the layer that runs Windows programs is named here, and a "
                     "reader never sees that word: " + ", ".join(bad))


def test_rights_are_root_and_sudo():
    """No page says administrator, and the account kinds are the ones
    Settings shows."""
    bad = [f"{p.relative_to(ROOT)}:{n}"
           for p in LINKED
           for n, line in enumerate(p.read_text(encoding="utf-8").splitlines(), 1)
           if ADMINISTRATOR.search(line)]
    assert not bad, "the handbook says administrator: " + ", ".join(bad)
    po = source("settings/po/fr/raye-settings.po")
    if po is None:
        lone("test_rights_are_root_and_sudo")
        return
    en = (ROOT / "en/05-security.md").read_text(encoding="utf-8").lower()
    fr = (ROOT / "fr/05-securite.md").read_text(encoding="utf-8").lower()
    for english, french in (("Sudo user", "Utilisateur sudo"), ("Standard user", "Utilisateur standard")):
        assert re.search(rf'^msgid "{english}"\nmsgstr "{french}"$', po, re.M), (
            f"Settings no longer names the account kind {english!r} / {french!r}")
        assert english.lower() in en and french.lower() in fr, (
            f"the security page does not name the account kind {english!r} / {french!r}")


def test_the_beta_pages_number_their_problems_the_same_way():
    """English and French must carry the same list, item for item: the two
    pages are the same promise made twice."""
    ids = {}
    for lang, name in (("en", "07-this-beta.md"), ("fr", "07-cette-beta.md")):
        page = ROOT / lang / name
        assert page.is_file(), f"{page.relative_to(ROOT)} is missing"
        found = [a for a in ANCHOR.findall(page.read_text(encoding="utf-8"))
                 if a.startswith("known-")]
        numbers = sorted(int(a.removeprefix("known-")) for a in found)
        assert numbers == list(range(1, len(numbers) + 1)), (
            f"{page.relative_to(ROOT)}: the known-N anchors are {numbers}, "
            f"they have to run from 1 with no gap")
        ids[lang] = numbers
    assert ids["en"] == ids["fr"], (
        f"English lists {len(ids['en'])} problems, French {len(ids['fr'])}")
    assert ids["en"], "the beta page lists no known problem at all"


def test_every_known_problem_of_the_release_has_a_paragraph():
    """The release notes decide how many there are. One more there and this
    goes red, which is the whole point: the page people read when something
    is broken must not be the short version.

    It compares COUNTS, not wording: it cannot tell that paragraph 5 is
    about the right problem, only that there are as many as there are.
    """
    english = source(NOTES_EN)
    french = source(NOTES_FR)
    if english is None:
        return lone("test_every_known_problem_of_the_release_has_a_paragraph")
    wanted = len(known_issues(english))
    assert wanted == len(known_issues(french)), (
        f"the release notes themselves disagree: {wanted} problems in English, "
        f"{len(known_issues(french))} in French")
    page = (ROOT / "en" / "07-this-beta.md").read_text(encoding="utf-8")
    got = len([a for a in ANCHOR.findall(page) if a.startswith("known-")])
    assert got == wanted, (
        f"the release notes list {wanted} known problems, en/07-this-beta.md "
        f"has {got} known-N paragraphs")


def test_the_free_space_figure_is_the_one_the_installer_demands():
    """Setup refuses to go on below it, so a smaller number in the handbook
    sends someone to buy nothing and a larger one scares them off."""
    text = source("installer/etc/calamares/modules/welcomeq.conf")
    if text is None:
        return lone("test_the_free_space_figure_is_the_one_the_installer_demands")
    m = re.search(r"^\s*requiredStorage:\s*([0-9.]+)\s*$", text, re.M)
    assert m, "welcomeq.conf no longer declares requiredStorage"
    gb = str(int(float(m.group(1))))
    for lang, name, unit in (("en", "01-installing.md", "GB"),
                             ("fr", "01-installer.md", "Go"),
                             ("en", "11-chromebooks.md", "GB"),
                             ("fr", "11-chromebooks.md", "Go")):
        page = (ROOT / lang / name).read_text(encoding="utf-8")
        assert f"{gb} {unit}" in page, (
            f"{lang}/{name} never says {gb} {unit}, which is what the installer "
            f"requires (requiredStorage: {m.group(1)})")


def test_manual_partitioning_really_is_off():
    """The dual-boot chapter tells the reader there is no hand-carving in
    this installer. The day it is turned on, that sentence is a lie.

    Since 2026-11-07 Raye writes the disk itself: the stock partition module,
    the one that could be told to allow it, is out of the sequence, and the
    disk module takes only the choices the chapter lists."""
    settings = source("installer/etc/calamares/settings.conf")
    core = source("installer/usr/lib/calamares/modules/rayedisk/rayedisk_core.py")
    if settings is None or core is None:
        return lone("test_manual_partitioning_really_is_off")
    assert not re.search(r"^\s*-\s*partition\s*$", settings, re.M), (
        "settings.conf runs the partition module again, so the dual-boot "
        "chapter may be wrong about carving partitions by hand")
    modes = re.search(r"^MODES\s*=\s*\(([^)]*)\)", core, re.M)
    assert modes, ("rayedisk_core.py no longer declares MODES, so what the "
                   "disk page can be told to do was not read")
    names = re.findall(r"\"([a-z-]+)\"", modes.group(1))
    assert names and set(names) <= {"erase", "shrink", "free", "replace", "keep"}, (
        f"the disk module takes {names}: a choice the dual-boot chapter does "
        f"not describe")


def test_the_installer_really_warns_about_fast_startup():
    """The chapter says Raye tells you itself when Windows was not shut
    down. If that warning goes, the chapter is promising a safety net that
    is not there -- and the reader would shrink a half-open disk."""
    text = source("installer/etc/calamares/branding/raye/strings.js")
    if text is None:
        return lone("test_the_installer_really_warns_about_fast_startup")
    found = re.findall(r"^\s*hibernated:\s*\"(.+)\",\s*$", text, re.M)
    assert len(found) >= 2, (
        f"the installer has {len(found)} hibernated warning(s); one per language "
        f"is what makes the chapter true in both")
    assert any("fast startup" in s.lower() for s in found), found
    assert any("démarrage rapide" in s.lower() for s in found), found


def test_the_address_to_write_to_is_the_release_one():
    """A tester who writes to the wrong place is a tester lost. The release
    notes and the handbook have to send people to the same door."""
    english = source(NOTES_EN)
    french = source(NOTES_FR)
    if english is None:
        return lone("test_the_address_to_write_to_is_the_release_one")
    pages = [(ROOT / "en" / "06-report-a-bug.md"),
             (ROOT / "fr" / "06-signaler-un-probleme.md")]
    for page in pages:
        assert page.is_file(), f"{page.relative_to(ROOT)} is missing"
        text = page.read_text(encoding="utf-8")
        urls = set(re.findall(r"https://github\.com/Raye-Linux/\S*?/issues", text))
        mails = set(re.findall(r"[a-z0-9.]+@rayelinux\.com", text))
        assert urls, f"{page.relative_to(ROOT)} gives no issue tracker"
        assert mails, f"{page.relative_to(ROOT)} gives no e-mail address"
        for where in urls | mails:
            assert where in english and where in french, (
                f"{page.relative_to(ROOT)} sends people to {where}, which the "
                f"release notes of this release do not mention")


def test_the_links_the_system_opens_still_land_somewhere():
    """Settings opens handbook pages by URL, with an anchor: four places in
    Raye Settings today. Renaming a page or dropping an <a id> breaks a
    button in the system, and nothing in the system can tell."""
    if LONE:
        return lone("test_the_links_the_system_opens_still_land_somewhere")
    seen = 0
    for path in sorted(RAYE.rglob("*.qml")):
        if SKIP_DIRS & set(path.relative_to(RAYE).parts):
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            # The whole tree is read, and the tree is worked on. A file that
            # moves between the listing and the read is not a handbook
            # defect, and a red here would be noise that gets a useful check
            # deleted.
            continue
        targets = set(HANDBOOK_URL.findall(text))
        if not targets:
            continue
        seen += 1
        fragments = {f for f in FRAGMENT.findall(text) if not HEX_COLOUR.match(f)}
        for rel in sorted(targets):
            page = ROOT / rel
            assert page.is_file(), (
                f"{path.relative_to(RAYE)} opens {rel}, which this repo does not "
                f"have. Settings would show a 404 to someone looking for help")
            ids = set(ANCHOR.findall(page.read_text(encoding="utf-8")))
            for fragment in sorted(fragments):
                assert fragment in ids, (
                    f"{path.relative_to(RAYE)} opens {rel}#{fragment}, and that "
                    f"page has no <a id=\"{fragment}\"></a>")
    assert seen, ("no QML in the tree links to the handbook any more; either the "
                  "links moved or this check stopped looking where they are")


def page(lang, name):
    """A page as one line: Markdown wraps a phrase or a bold label anywhere."""
    path = ROOT / lang / name
    assert path.is_file(), f"{lang}/{name} is missing"
    return " ".join(path.read_text(encoding="utf-8").split())


def bold(text):
    """What a page puts in bold, a path like Settings → System split up."""
    return {part for span in re.findall(r"\*\*(.+?)\*\*", text)
            for part in [span] + span.split(" → ")}


def test_the_labels_the_pages_name_are_on_screen():
    """Every button a page names exists, in both languages, in the file
    that draws it."""
    for en_name, fr_name, rel, pairs in LABELS:
        po = source(rel)
        if po is None:
            return lone("test_the_labels_the_pages_name_are_on_screen")
        en, fr = page("en", en_name), page("fr", fr_name)
        for english, french in pairs:
            assert re.search(rf'^msgid "{re.escape(english)}"\nmsgstr "{re.escape(french)}"$',
                             po, re.M), (
                f"{rel} no longer shows {english!r} / {french!r}")
            for lang, name, text, label in (("en", en_name, en, english),
                                            ("fr", fr_name, fr, french)):
                assert label in bold(text), f"{lang}/{name} does not name **{label}**"


def test_ctrl_shift_esc_opens_what_the_page_says():
    """The shortcut table names the app the key really starts."""
    keys = source("theme/config/kglobalshortcutsrc")
    desktop = source("apps/taskmanager/src/org.raye.taskmanager.desktop")
    if keys is None or desktop is None:
        return lone("test_ctrl_shift_esc_opens_what_the_page_says")
    bound = re.findall(r"^\[services\]\[([^\]]+)\]\n_launch=(.*)$", keys, re.M)
    owners = [name for name, chord in bound if "Ctrl+Shift+Esc" in chord.split("\\t")]
    assert owners == ["org.raye.taskmanager.desktop"], (
        f"Ctrl+Shift+Esc starts {owners}; the shortcut tables say Task Manager")
    names = dict(re.findall(r"^(Name|Name\[fr\])=(.+)$", desktop, re.M))
    for lang, name, row in (("en", "02-first-steps.md", f"| Ctrl + Shift + Esc | {names['Name']} |"),
                            ("fr", "02-premiers-pas.md", f"| Ctrl + Maj + Échap | {names['Name[fr]']} |")):
        assert row in page(lang, name), f"{lang}/{name} has no row {row!r}"


def test_the_chromebook_pages_give_the_same_commands():
    """Someone types these on a machine that may not start again if a line
    is wrong. The French page is a translation, so its commands are the
    English ones, character for character, in the same order."""
    blocks = {}
    for lang in ("en", "fr"):
        text = (ROOT / lang / "11-chromebooks.md").read_text(encoding="utf-8")
        blocks[lang] = [line.strip() for line in text.splitlines()
                        if line.startswith("    ") and not line.startswith("     ")]
        ids = set(ANCHOR.findall(text))
        # the sound notice of a Chromebook opens the page at #sound
        assert {"keyboard", "sound"} <= ids, f"{lang}/11-chromebooks.md lacks {{'keyboard', 'sound'}} - {ids}"
    assert blocks["en"], "the Chromebook page has no command at all"
    assert blocks["en"] == blocks["fr"], (
        "the two Chromebook pages do not give the same commands: "
        f"{set(blocks['en']) ^ set(blocks['fr'])}")
    script = [b for b in blocks["en"] if "firmware-util.sh" in b]
    assert script == ["cd; curl -LOf https://mrchromebox.tech/firmware-util.sh "
                      "&& sudo bash firmware-util.sh"], script


def test_updates_are_said_to_install_while_you_work():
    """Raye Update installs what needs no restart right away. A page that
    says everything waits for the restart teaches the opposite."""
    code = source("update/src/raye_update.py")
    if code is None:
        return lone("test_updates_are_said_to_install_while_you_work")
    assert "raye-update-live@" in code, (
        "Raye Update no longer installs in use; the update pages say it does")
    for lang, name, said, never in (
            ("en", "03-updates.md", "while you work", "never while you work"),
            ("fr", "03-mises-a-jour.md", "pendant que vous travaillez", "jamais pendant"),
            ("en", "02-first-steps.md", "while you work", "never while you work"),
            ("fr", "02-premiers-pas.md", "pendant que vous travaillez", "jamais pendant")):
        text = page(lang, name)
        assert said in text and never not in text, (
            f"{lang}/{name} has to say that most updates install {said!r}")


def test_the_device_portal_address_is_the_one_it_listens_on():
    unit = source("settings/portal/units/raye-device-portal.socket")
    if unit is None:
        return lone("test_the_device_portal_address_is_the_one_it_listens_on")
    port = re.search(r"^ListenStream=(?:.*:)?(\d+)\s*$", unit, re.M)
    assert port, "the Device Portal socket no longer says where it listens"
    for lang, name in (("en", "10-for-developers.md"), ("fr", "10-pour-les-developpeurs.md")):
        assert f":{port.group(1)}" in page(lang, name), (
            f"{lang}/{name} does not give port {port.group(1)}")


def test_the_games_said_not_to_run_are_blocked():
    """A game the Windows chapter calls blocked is one Raye refuses."""
    upstream = source("wine/release/windows/titles/00-upstream.titles")
    raye = source("wine/release/windows/titles/50-raye.titles")
    if upstream is None:
        return lone("test_the_games_said_not_to_run_are_blocked")
    states = dict(re.findall(r"^name\s*=\s*(.+?)\s*\nstate\s*=\s*(\S+)", upstream + raye, re.M))
    for game in BLOCKED:
        assert states.get(game) == "blocked", f"{game} is {states.get(game)} in the titles"
        for lang, name in (("en", "04-windows-programs.md"), ("fr", "04-programmes-windows.md")):
            assert game in page(lang, name), f"{lang}/{name} does not name {game}"


def test_the_notification_button_is_named():
    """The update notification has one button, and it is not the Start
    menu's."""
    script = source("update/src/raye-update-notify")
    if script is None:
        return lone("test_the_notification_button_is_named")
    shown = {"fr": re.search(r'fr\*\).*?now="([^"]+)"', script, re.S),
             "en": re.search(r'^\s*\*\)\s+title=.*?now="([^"]+)"', script, re.S | re.M)}
    for lang, name, where in (("en", "03-updates.md", r"in the notification"),
                              ("fr", "03-mises-a-jour.md", r"dans la notification")):
        assert shown[lang], f"raye-update-notify no longer has a {lang} button label"
        said = re.search(rf"\*\*([^*]+)\*\* {where}", page(lang, name))
        assert said, f"{lang}/{name} does not name the notification's button"
        assert said.group(1) == shown[lang].group(1), (
            f"{lang}/{name} says the notification shows {said.group(1)!r}; "
            f"it shows {shown[lang].group(1)!r}")


def test_the_beta_page_does_not_deny_what_the_layer_carries():
    """Once the Windows layer brings DirectX through Vulkan and .NET, a
    known problem saying they are missing sends people away for nothing."""
    carried = source("wine/third-party/sources.txt")
    if carried is None:
        return lone("test_the_beta_page_does_not_deny_what_the_layer_carries")
    names = {line.split()[0] for line in carried.splitlines()
             if line.strip() and not line.startswith("#")}
    for lang, name in (("en", "07-this-beta.md"), ("fr", "07-cette-beta.md")):
        text = (ROOT / lang / name).read_text(encoding="utf-8")
        for block in re.split(r"\n\s*\n", text):
            for component, what, topic in CARRIED:
                if component in names and topic.search(block):
                    assert not MISSING.search(block), (
                        f"{lang}/{name} says {what} is missing, and the "
                        f"Windows layer carries {component}: "
                        f"{' '.join(block.split())[:90]!r}")


if __name__ == "__main__":
    bad = 0
    for name, case in sorted(globals().items()):
        if not name.startswith("test_"):
            continue
        try:
            case()
        except AssertionError as error:
            bad += 1
            print(f"FAIL - {name}: {error}")
        except Exception as error:
            # Not an assertion: a source read the wrong way, a page that is
            # not there. It still has to be a red line and not a traceback
            # the launcher would count as nothing at all.
            bad += 1
            print(f"FAIL - {name}: {type(error).__name__}: {error}")
        else:
            print(f"ok - {name}")
    sys.exit(1 if bad else 0)

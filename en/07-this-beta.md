# What this beta still gets wrong

The list below is the whole list, in the order the release notes give it.
It is here because this is the page you open when something does not work,
and finding your problem already written down is faster than reporting it.

<a id="known-1"></a>
**The screen goes black for a moment before the sign-in screen.** For 3
to 5 seconds, between the Raye picture and the sign-in screen. Nothing is
wrong: wait, and the sign-in screen comes.

<a id="known-2"></a>
**A few apps do not look like Raye.** The terminal, the screenshot tool
and some dialogs wear Raye's colors but have not been redrawn yet.

<a id="known-3"></a>
**The Start menu and the taskbar are close to Windows 11, not identical.**
The search field and the recommended section are the parts still missing.

<a id="known-4"></a>
**The sign-in and lock screens disagree about your picture.** The default
account picture is not the same on both. A lone **OK** button also shows
under "Wrong password".

<a id="known-5"></a>
**Not every Windows program runs.** The first one you open after setup
takes a while, some installers show a gray old-style window, and some
programs do not start at all. When a program also exists for Raye - 
Discord, Steam - install it from the Raye Store instead; see
[Windows programs](04-windows-programs.md).

<a id="known-6"></a>
**Microsoft's fonts come later.** Arial, Times New Roman and Verdana
are Microsoft's, so the image does not carry them: Raye fetches them in
the background the first time the PC is online after setup, with the
Visual C++ runtimes, and puts them in every Windows space. A program
opened before that uses the system's fonts, and its text can come out in
different type, or the wrong size for its box.

<a id="known-7"></a>
**3D games have hardly been tried.** Windows programs now draw through
Vulkan, but the only game played so far is an old Direct3D 9 one,
Chocolate Doom. No Direct3D 11 or 12 game has been tried on a real
graphics card, so how well they run is not known yet.

<a id="known-8"></a>
**Programs built on .NET have hardly been tried.** Raye now brings .NET
and the web engine some programs embed, but only one such program has
been tested. Paint.NET's installer gets past its graphics check now,
then stops on an error about its color output. Nothing has been tried
on a real graphics card yet.

<a id="known-9"></a>
**Roblox Studio cannot be signed in to from its own window.** Typing
does not reach its sign-in page yet. Use Login via Browser instead,
which opens the page in your web browser.

<a id="known-10"></a>
**Updates need the internet before they can say anything.** Raye looks for
its own packages on rayelinux.com and on GitHub. Until you are online,
Settings says it could not check, which is true and not a fault.

<a id="known-11"></a>
**Nothing has been measured against Windows on a real computer.** If you
read anywhere that Raye is faster or slower, nobody has weighed it yet.

<a id="known-12"></a>
**`add-apt-repository -c` and `-p` can break Raye's own package source.**
They may pick it and rewrite it; `apt` then answers 404 for Raye's
packages, and because the file belongs to a package it is replaced again
at the next update. Add a PPA with plain `add-apt-repository ppa:...`,
which writes its own file. If it already happened:
`sudo apt install --reinstall raye-archive-keyring`.

<a id="known-13"></a>
**Source packages are declared but switched off**, so `apt update` does
not fetch 18 MB of source indexes on every computer. To build a package
from source, turn them on first:
`sudo sed -i 's/^Enabled: no$/Enabled: yes/' /etc/apt/sources.list.d/ubuntu.sources && sudo apt update`.

<a id="known-14"></a>
**The ring around the focused control is faint**, on a few dark surfaces
and more so with a very light or very dark accent color. Text and
controls keep their contrast; it is the thin focus ring that does not
always reach the 3:1 a keyboard user needs.

## And setup has one page in English only

Every screen of setup is translated except the one where you choose the
disk. That page comes from the installer Raye builds on, and this image
carries no French for it: it shows in English even when you picked
French. It is also the page where a wrong click costs the most, so
[Installing next to Windows](09-windows-alongside.md) names its buttons.

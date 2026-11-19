# What this beta still gets wrong

The list below is the whole list, in the order the release notes give it.
It is here because this is the page you open when something does not work,
and finding your problem already written down is faster than reporting it.

<a id="known-1"></a>
**Older AMD cards can start at a low resolution.** Some RX 400 and 500
series cards show a low resolution with low frame rates on some PCs. When
the desktop fails to show twice in a row, Raye switches to a simpler display
mode by itself, which helps some cards but not all. If it happens to you,
say so in #bugs on Discord: the team is still working on it.

<a id="known-2"></a>
**No Raye kernel with NVIDIA's driver.** NVIDIA's prebuilt modules only
load on the standard kernel, so Settings does not offer the Raye kernel on
a PC that uses them, and says why.

<a id="known-3"></a>
**The Graphics Card panel is new.** Its fan curve and power limit have been
checked on test data, not yet on every generation of AMD card. Restore
defaults puts the card back the way it came.

<a id="known-4"></a>
**Not every Windows program runs.** Apps built only for the Microsoft Store
cannot run at all. Programs that also exist for Raye (Discord, Steam) are
better installed from the Raye Store.

<a id="known-5"></a>
**Alarms ring only while the PC is on.** Clock cannot wake the PC from
sleep yet: an alarm missed while it slept shows as missed when it wakes.

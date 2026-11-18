# Installing next to Windows

Raye can take part of the disk and leave Windows where it is. The one
thing that goes wrong, goes wrong before you ever start Raye.

## First, in Windows: shut it down for real

Windows ships with **Fast Startup** on. With it, "Shut down" does not shut
down: it saves the running system to the disk and stops. The disk is left
half-open, and the tool that makes room for Raye **refuses to touch a disk
in that state**. That refusal is on purpose. Forcing a resize onto a
half-open Windows is how people lose files.

So, in Windows: **Control Panel → Power Options → Choose what the power
buttons do**, untick **Turn on fast startup**, then shut the computer
down. Hibernation leaves the same trace, so do not come back from
hibernation either.

Raye checks this itself. If Windows was not shut down properly, the very
first screen of setup says so, before anything is written.

The same screen warns about two other things:

- **BitLocker.** Start Windows, open **Manage BitLocker**, choose
  **Suspend protection**, then come back - and keep your BitLocker
  recovery key at hand.
- **Another Linux on the same disk.** Raye would replace the way it
  starts. Erase the disk on purpose, or pick a different one.

## Room

At least **25 GB** free: setup refuses to go on below that. It is the
floor, not a comfortable figure - how much Raye itself ends up using has
not been measured.

## The disk page

This page of setup is in English even if you chose French - see
[What this beta still gets wrong](07-this-beta.md). Three choices:

- **Erase disk** - Raye alone. Already selected, so do not leave it by
  accident.
- **Install alongside** - the one you want. Raye shrinks a partition to
  make room. Pick the Windows partition, then drag the bar at the bottom
  to decide how much Windows keeps and how much Raye gets.
- **Replace a partition** - puts Raye in place of one partition and
  deletes what was on it.

You cannot carve partitions by hand here: this installer does not offer
it. If the layout you need is not one of those three, it is not a Raye
thing to do yet.

Raye uses the EFI partition Windows already made rather than adding one.
Shrinking, though, does rewrite the size of the Windows partition - which
is the whole reason Windows has to have been shut down properly first.

## Afterwards

With two systems on the computer, a menu shows for **three seconds** at
every start, with Raye and Windows in it. Pick one, or wait and Raye
starts. With Raye alone that menu stays hidden, which is why you may
never have seen it.

From inside Raye, **Restart to Windows** in the Start menu restarts
straight into Windows, that once, without the menu.

For the disk password and the recovery key, see
[Security](05-security.md).

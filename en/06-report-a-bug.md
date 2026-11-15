# Reporting a problem

This is a beta, so the most useful thing you can do with it is say what
went wrong. Two doors, both read:

- an issue at **https://github.com/Raye-Linux/releases/issues**
- an e-mail to **bonjour@rayelinux.com**

## What to write

Four lines are enough, and they are the four that save a round trip:

1. what computer you have,
2. what you did,
3. what you expected,
4. what happened instead.

A photo of the screen says more than a paragraph. Take one with your
phone if the computer is stuck.

## The two blocks worth pasting in

**Settings → System → About** has a **Copy** button next to each of its
two blocks. The first copies the computer - processor, memory, graphics,
storage, model. The second copies Raye's own side, including the
**Version** line, which says exactly which build you are on. Paste both
into the report and nobody has to ask.

## After the violet screen

When the screen turns violet and the computer restarts by itself, Raye
writes a report of it. The notification that follows has a **Details**
button, which opens the report; it also sits in
`~/.local/share/raye/crash-reports/`, one text file per restart, named
after the date and the time. Attach the newest one.

The details of some problems can only be read as root. The notification
says so and gives the path when that happens.

## If the installation itself failed

Once Raye is installed, setup leaves its own log in
`/var/log/installer/session.log`, readable only as root. On a
computer where setup never finished there is no such file: write down
what the last screen said, and at which step.

## One thing not to send

Nothing here needs a password, and nothing here needs your **recovery
key**. No Raye report contains either. If you are copying files out of
your home folder to attach them, leave `.local/share/raye/recovery-key` where it
is - see [Security](05-security.md).

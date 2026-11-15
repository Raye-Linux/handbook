# Security: encryption, recovery key, startup

## The encrypted disk

If you ticked **Encrypt the system** when installing, the whole disk is
encrypted: a stolen computer gives nothing away without the password.

On most recent computers the **security chip** (TPM) opens the disk by
itself at startup, and you only type your account password. If the chip
does not answer (firmware update, disk moved to another computer), the
startup screen asks for the disk password.

## The recovery key

Installing creates a **recovery key**: eight groups of six digits, shown by the
window that opens the first time you sign in. Raye keeps it in
**.local/share/raye/recovery-key**, in your home folder. It opens the disk if
you forget its password: type it instead of the password at startup.

**Write it down** on paper or in a password manager, keep it somewhere
other than the computer, then **delete the file**. **Settings → Privacy &
security → Device security** reminds you while the file is there.

## If the computer crashes

The screen turns violet and shows the Raye eye: your files are safe and the
computer restarts by itself after 30 seconds.

## The Raye kernel (optional)

**Settings → Drivers → Raye kernel** offers the same kernel with the Raye
crash screen. With Secure Boot, the Raye key has to be enrolled once: at
the restart a blue screen shows. Press a key **within 10 seconds**, choose
**Enroll MOK**, **Continue**, **Yes**, type the six-digit code Settings
showed, then **Reboot**. The original kernel stays installed as a fallback.

## Starting Windows

If Windows is installed alongside, **Restart to Windows** in the menu
restarts straight into it, once.

## Root and sudo

Changes to the whole system (installing for everyone, the firewall, the
start-up menu) run as **root**, the system account. Raye asks first: a
window names the program and asks for a password.

- A **sudo user** types their own password. The account made when
  installing is one.
- A **standard user** cannot make these changes alone: the window asks
  for the password of a sudo user of the PC.

**Settings → Accounts → Other users → Account type** switches between
the two.

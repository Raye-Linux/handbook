# Installing Raye Linux

## What you need

- A 64-bit PC (Intel or AMD) that starts in UEFI mode, 4 GB of memory (8 GB
  recommended) and 25 GB of free disk space.
- A USB stick of 8 GB or more. Everything on it will be erased.
- About 20 minutes, and a backup of your important files: installing can
  erase the disk you pick.

## 1. Download the image

Download the Raye image (the `.iso` file, about 2.9 GB) from
rayelinux.com. To be sure the download is complete, its size must match the
one on the download page, and its SHA-256 must match the one shown there.

## 2. Make the USB stick

Copying the file onto the stick is not enough: a tool has to make it
bootable.

- **On Windows:** Rufus (rufus.ie). Pick the stick under Device, click
  SELECT and choose the image, click START, and when it asks, choose
  **DD mode**. Wait until it says READY.
- **On Windows, Mac or Linux:** balenaEtcher. Flash from file (the image),
  Select target (the stick), Flash. On Windows, if it fails, right-click it
  and start it with full rights.
- **On Linux Mint:** right-click the image and choose "Make bootable USB
  stick". Fedora Media Writer and GNOME Disks ("Restore Disk Image") work too.
- Ventoy is not tested yet. It may work (with Secure Boot it asks once to
  enroll its key), but Rufus in DD mode is the surest.

If the tool says the write failed, try another USB port, start the tool
with full rights, or use another stick: cheap no-name sticks often fail on
large writes.

## 3. Start from the stick

Plug the stick in, restart, and open your computer's boot menu right when
it powers on. The key depends on the brand: F12 (Dell, Lenovo, Acer), F9
(HP, then pick the USB device), F8 (ASUS), F11 (MSI) or Esc. Pick the USB
stick, the UEFI entry if there are two.

Raye starts with Secure Boot on, there is nothing to change in the
computer's settings.

The stick shows a menu: **Install Raye Linux** (English), **Installer Raye
Linux** (French) and **Safe graphics**. Trying Raye without installing it is
not available yet: it is coming in a future update.

## 4. The installer, step by step

1. **Region**: your language and keyboard.
2. **Network**: if the computer has no cable, pick your Wi-Fi. Raye uses it
   to set the clock and the time zone by itself.
3. **Disk**: pick the disk, then how Raye uses it.
   - **Install next to Windows**: Raye takes part of the free space and keeps
     Windows. At each start you choose which one to use.
   - **Erase this disk**: Raye is alone on that disk. Everything on it is
     deleted.
   - **Encrypt Raye with a password** protects your files if the computer
     is stolen.
   Read the summary at the bottom: it shows what each system will get.
4. **Account**: your name, a login and a password. You can also sign in to a
   Raye account (optional) to sync your settings.
5. **Privacy**: your choices, all off by default.
6. **Install**: it takes about ten minutes.

When it is done, restart and take the stick out when the screen asks. The
computer then starts on Raye.

## If something goes wrong

- **Black screen** when starting the stick: choose **Safe graphics** in its
  menu. If the screen goes black after installing: at power on, tap Esc
  until the Raye menu shows, pick **Raye Linux (safe graphics)** if it is
  there, or press `e`, add `nomodeset` after `quiet splash` and press F10.
  Some older AMD graphics cards are affected; a fix is on the way.
- **"you need to load the kernel first"**: download the image again (the
  fixed one is dated November 15) and rewrite the stick.
- **The stick does not show in the boot menu**: rewrite it in DD mode, try
  another USB port, and check that the computer starts in UEFI mode.
- Still stuck? Ask on the Raye Linux Discord, in #help, with your computer's
  model and a photo of the screen.

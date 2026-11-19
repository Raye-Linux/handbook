# Installing on a Chromebook

Many Chromebooks with an **Intel or AMD** processor can run Raye. It takes
more work than a regular PC, and one step is not Raye's: the Chromebook
needs a new firmware (the program that starts the computer), made by a
community project called **MrChromebox**. Raye does not write it and
cannot support it; this page tells you how to use it and what to expect.

Chromebooks with an **ARM** processor (MediaTek, Qualcomm Snapdragon,
Rockchip) cannot run Raye, and the firmware below does not exist for them.

This page follows MrChromebox's own guide (docs.mrchromebox.tech) and the
community notes at docs.chrultrabook.com. When the two disagree with this
page, they are right: they are updated more often. Raye has not been tried
on every Chromebook, and some have never been tried at all.

Before anything: **if the Chromebook belongs to a school or a company, stop
here.** A managed Chromebook cannot be changed this way, and you need the
owner's written permission anyway.

## 1. Check that your Chromebook is supported

Support depends on the **board name**, not on the brand or the model you
bought: the same board name is sold under several model names.

1. In ChromeOS, open the browser and go to `chrome://system`, then search
   for **HWID**. The board name is the first word of it, before the first
   space or dash.
2. Open MrChromebox's list of supported devices,
   docs.mrchromebox.tech/docs/supported-devices.html, and look for that
   board name. The list is grouped by processor generation and only has
   Intel and AMD machines. **If your board name is not in the list, it is
   not supported.** Do not try with a "close" model.
3. Note the two columns that matter for the next steps: **RW_LEGACY** and
   **UEFI Firmware (Full ROM)**, and the **WP Method**.

Raye also needs **25 GB** of free space and 4 GB of memory (8 GB
recommended). A Chromebook with 32 GB of storage is just enough, one with
16 GB is not.

## 2. Back up, and get two USB sticks ready

The next step erases everything stored on the Chromebook itself. Files in
Google Drive stay in Google Drive; the **Downloads** folder and anything not
synced is lost. Copy what you want to keep to a USB stick or to the cloud.

You also need:

- the **Raye USB stick**, made on another computer as in
  [Installing Raye Linux](01-installing.md), steps 1 and 2;
- a second USB stick for the backup of the Chromebook's firmware (step 5);
- the charger, plugged in for the whole time. MrChromebox insists on it:
  some steps refuse to run, or go wrong, on battery.

## 3. Turn on Developer Mode

1. Turn the Chromebook off. Hold **Esc** and **Refresh** (the round arrow
   in the top row), then press **Power**. Release when the
   recovery screen shows. It has to be the built-in keyboard.
   On a tablet: hold **Volume up + Volume down + Power** for 10 seconds.
2. On that screen press **Ctrl + D**, and confirm.
3. The Chromebook erases itself and restarts. This takes a few minutes.

From now on, every start shows a screen saying that OS verification is
off. That is expected: it is how you know Developer Mode is on.

To type the commands of the next steps you need ChromeOS's shell. At the
ChromeOS sign-in screen, press **Ctrl + Alt** and the second key of the top
row (ChromeOS calls it F2; on most models it shows →), then sign in as
`chronos`, no password. On a ChromeOS older
than version 117, open the browser instead, press **Ctrl + Alt + T** and
type `shell`.

## 4. Choose the firmware

MrChromebox offers two kinds. Choose before you start the next step.

**UEFI Full ROM** - recommended, when the list shows it for your board.
The Chromebook then starts like a regular PC: no warning screen, Raye
starts by itself, the boot order is remembered, and Secure Boot exists.
What it costs:

- ChromeOS is removed. It can be put back, with the backup of step 5.
- You must first turn off the firmware's **write protection** (step 5).
- If the flash is interrupted (power cut, crash), the Chromebook may no
  longer start, and bringing it back needs a special cable or programmer.
  MrChromebox calls this a small risk. It is not zero.

**RW_LEGACY** - keeps the firmware Google installed and only adds a way to
start something else. It cannot break the Chromebook and needs no change
to the write protection. What it costs:

- Every start shows the Developer Mode screen, and you press **Ctrl + L**
  to start Raye (the firmware script can make that the default, see step 6).
- The Chromebook remembers no boot order and has no Secure Boot. Raye
  still starts: it keeps a copy of its boot loader in the place a firmware
  looks at when it remembers nothing.
- Raye's installer cannot share the internal disk with ChromeOS. Installing
  Raye on it with **Erase this disk** removes ChromeOS, even with RW_LEGACY.
  Do not use **Install next to Windows** on a Chromebook: it was made for
  Windows and has not been tried with ChromeOS.
- On older generations (the list says **EOL** in the RW_LEGACY column),
  RW_LEGACY can no longer be installed: only Full ROM is offered.
- MrChromebox lists two generations where RW_LEGACY works badly: **Gemini
  Lake** (the start menu shows no list of disks, so you cannot pick the
  USB stick) and **AMD Stoney Ridge** (it does not start on most models).
  Use Full ROM there.

## 5. Full ROM only: turn off write protection

How you do it depends on your board: the **WP Method** column of the list
says which. Follow MrChromebox's page for it exactly,
docs.mrchromebox.tech/docs/firmware/wp/disabling.html. In short:

- **screw, jumper or switch** (models from 2016 and earlier): you open the
  Chromebook and remove a screw or change a jumper.
- **CR50** (about 2017 to 2022): unplug the battery inside, or use a
  special USB-C cable (SuzyQ).
- **Ti50** (most models sold from 2023): **do not open it.** It is done
  with a command in ChromeOS's shell, and the guide also has you allow the
  firmware to start without its usual check, before anything else. Skip
  that part and the Chromebook may not start again.

Only use commands from that page. Commands found elsewhere for turning off
write protection by hand are, in MrChromebox's words, not needed, and the
firmware script handles the rest itself.

## 6. Run the firmware script

In ChromeOS's shell (step 3), type, all on one line:

    cd; curl -LOf https://mrchromebox.tech/firmware-util.sh && sudo bash firmware-util.sh

A menu shows. Options marked **[WP]** need write protection off.

- **Full ROM:** choose **Install/Update UEFI (Full ROM) Firmware**. When the
  script offers to **back up the stock firmware to USB**, say yes and use
  the second stick. Keep that file: it is the only exact copy of what came
  with your Chromebook, and you need it to go back to ChromeOS. Copy it to
  another computer too. When the script is done, use its menu to **power
  off**; do not restart right away.
- **RW_LEGACY:** choose **Install/Update the RW_LEGACY Firmware**. To skip
  pressing Ctrl + L at every start, choose **Set Boot Options (GBB Flags)**
  afterwards and pick a short delay with Legacy Boot as the default.

The first start after a Full ROM flash can stay black for up to a minute
or so: the firmware is testing the memory. Wait 90 seconds before you
think something is wrong.

## 7. Start the Raye stick

Plug in the Raye stick.

- **Full ROM:** turn the Chromebook on and press **Esc** when the logo
  (a hare) shows. Choose **Boot Menu**, then the USB stick.
- **RW_LEGACY:** on the Developer Mode screen press **Ctrl + L**, then
  **Esc** when the logo shows, **Boot Menu**, and the USB stick.

If the stick is not in the list, go back, unplug it, plug it in again,
wait three seconds and open the Boot Menu again. Try another port if it
still does not show. If you end up at a text prompt (the EFI shell), type
`exit` and press Enter.

The Raye stick shows its menu: choose **Install Raye Linux**, or **Safe
graphics** if the screen stays black. Raye starts with Secure Boot on or
off; there is nothing to change.

## 8. Install

The installer works as in [Installing Raye Linux](01-installing.md), step 4.
On the disk page, pick the **internal** disk (often called eMMC, or an
NVMe drive), not the USB stick, and choose **Erase this disk**.

About **Encrypt Raye with a password**: the security chip of a Chromebook
only does what ChromeOS needs, and MrChromebox says it cannot hold a disk
key for other systems. Encryption still works; expect Raye to ask for the
disk password at every start.

When the installer is done, restart and take the stick out.

<a id="keyboard"></a>
## 9. The keyboard

Raye sees that it runs on a Chromebook and sets the top row of keys to do
what the icons on them say:

| Key | What it does |
|---|---|
| Back, Forward | back and forward in the browser and in File Explorer |
| Refresh | reloads the page |
| Full screen | full screen (the same as F11) |
| Overview | shows all windows (⊞ + Tab) |
| Brightness, volume | as printed on the key |
| Lock (top right, on most models) | locks the screen |
| **Search** alone | opens the Start menu, like the ⊞ key |
| **Search** + a top-row key | F1, F2, F3... in order from the left |
| **Alt + Backspace** | Delete |
| **Ctrl + Alt + Backspace** | Ctrl + Alt + Delete |
| **Alt + brightness** | keyboard backlight, when there is one |

Newer Chromebooks do not all have the same top row. Raye reads its order
from the firmware, so Search + the first key is always F1. If you already
set up your keys yourself with keyd, Raye leaves your settings alone.

<a id="sound"></a>
## 10. Sound

On many Chromebooks the speakers or the microphone do not work right after
installing. This is not a Raye fault: the sound chips of Chromebooks need
settings that only ChromeOS carries. Raye shows a notice the first time it
finds no sound output.

A community script, **chromebook-linux-audio**, fixes most models. It
writes into the system's sound settings, so use it knowing that, and only
on your own installed Raye (not from the stick). It has not been tried on
Raye. Open a terminal (Konsole) and type, one line at a time:

    sudo apt install git
    git clone --depth 1 https://github.com/WeirdTreeThing/chromebook-linux-audio
    cd chromebook-linux-audio
    ./setup-audio

Then restart. Updates of the system's sound package can undo the fix; if
the sound goes away after an update, run `./setup-audio` again.

**Protect your speakers.** On some **Skylake**, **Kaby Lake** and **Apollo
Lake** Chromebooks, the speaker amplifier (max98357a) has no volume limit
with the driver the script picks. The script warns you and asks first.
Turning the volume up too far can damage the speakers for good: keep it
low, or say no.

What the community notes list for each generation, as of this writing:

| Generation | Known problems |
|---|---|
| Apollo Lake | microSD cards may not be detected; no headphone jack with one of the two sound drivers |
| Kaby Lake | the camera does not work on some models |
| Comet Lake | the fingerprint reader does not work; some wake up with the lid closed |
| Tiger Lake, Alder Lake | USB-C may not work (fix below); no fingerprint reader |
| Alder Lake-N | sound may not work |
| AMD Stoney Ridge | sound needs a recent kernel; Raye's is recent enough |
| AMD Picasso | needs `iommu=pt` added to the kernel's start line (below) |
| AMD Cezanne | the speakers do not work yet |
| any | fingerprint readers do not work |

**USB-C on Tiger Lake and Alder Lake.** In a terminal:

    echo cros-ec-typec | sudo tee -a /etc/initramfs-tools/modules
    echo intel-pmc-mux | sudo tee -a /etc/initramfs-tools/modules
    sudo update-initramfs -u -k all

**AMD Picasso.** In a terminal, then restart:

    echo 'GRUB_CMDLINE_LINUX="$GRUB_CMDLINE_LINUX iommu=pt"' | sudo tee /etc/default/grub.d/60-chromebook.cfg
    sudo update-grub

## Going back to ChromeOS

- **With RW_LEGACY:** your firmware is still Google's. Make a ChromeOS
  recovery stick on another computer (Google's **Chromebook Recovery
  Utility**, in Chrome), then start the Chromebook with **Esc + Refresh +
  Power** and plug the stick in when the screen asks.
- **With Full ROM:** first put the original firmware back. Start Raye, open
  a terminal and run the same firmware script as in step 6. Choose
  **Restore Stock Firmware**, then the USB backup made in step 5. Then make
  the recovery stick as above.

Two warnings from MrChromebox: once Google has stopped updating a model
(end of life), it cannot go back to ChromeOS at all; and on **Ti50** models
going back carries more risk, so keep the backup and read their page
before you start.

## If something goes wrong

- **Black screen after flashing:** wait 90 seconds. Then hold Power for 10
  seconds and start again.
- **A text menu or a black screen instead of Raye's menu** right after a
  Full ROM flash: the old ChromeOS loader is still on the disk. Turn the
  Chromebook off and on and press **Esc** at the logo.
- **The firmware itself is broken:** MrChromebox's guide explains how to
  recover with a SuzyQ cable or a programmer. Raye cannot help with that
  part.
- Ask on the Raye Linux Discord, in #help. Give the **board name** (step 1),
  which firmware you chose, and a photo of the screen.

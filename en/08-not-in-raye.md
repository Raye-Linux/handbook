# What Raye does not do (yet)

A few Windows features have no match in Raye. Rather than a button that
does nothing, Settings says **Not available on Raye** and links here.
Each part below says what Windows does, why Raye does not, and what to
use instead.

<a id="voice-typing"></a>

## Voice typing

**On Windows:** Windows + H opens a microphone bar and what you say is
typed wherever the cursor is. Voice access goes further and controls
the whole PC by voice.

**Why not on Raye:** good dictation needs a large speech model. The
ones that run on your own PC are not yet good enough in every language
to come with the system, and sending your voice to a company's servers
is not something Raye does behind your back.

**Instead:**

- **Speech Note**, in the Store, turns speech into text on your PC,
  without the internet. Speak, then copy the text where you need it.
- Your phone's keyboard has a microphone button. Dictate on the phone,
  then send the text to the PC with **Settings → Bluetooth & devices →
  Phone** (shared clipboard).

<a id="dynamic-lighting"></a>

## Dynamic lighting

**On Windows:** Settings → Personalization → Dynamic lighting sets the
color and effects of RGB keyboards, mice and PC cases from one place.

**Why not on Raye:** each brand drives its lights its own way, and Raye
has no common way to reach all of them from Settings.

**Instead:** **OpenRGB**, in the Store, controls the lights of most
keyboards, mice, memory, graphics cards and motherboards. If it does not
find your devices, restart the PC once after installing it.

<a id="cast"></a>

## Cast to a wireless screen

**On Windows:** Windows + K looks for TVs and screens that accept
Miracast and shows your screen on them without a cable.

**Why not on Raye:** wireless display support on Linux does not work
well enough yet: many TVs are not found or the picture drops.

**Instead:**

- Plug the screen in with an **HDMI** or **USB-C** cable, then press
  **Windows + P** to choose Duplicate or Extend.
- For a video or a web page, a browser that can cast, such as **Google
  Chrome** from the Store, sends it to a TV with Chromecast or Google TV.

<a id="quick-assist"></a>

## Quick Assist

**On Windows:** Quick Assist lets a friend see and control your PC over
the internet after you give them a short code.

**Why not on Raye:** a code like that only works through a service on
the internet that puts the two computers in touch. Raye does not run
such a service.

**Instead:**

- In the same house or office, use **Settings → System → Remote
  Desktop**.
- Over the internet, both people can install the same remote help app
  from the Store, such as **RustDesk**, and follow its steps.

Only let someone you know and trust control your PC. Microsoft, your
bank and Raye never call you to ask for remote access.

## Other Windows features not in Raye

| On Windows | On Raye |
|---|---|
| Live captions | Not available. Videos in Firefox often have captions of their own. |
| Find my device | Not available: it works through a Microsoft account and Microsoft's servers. |
| Family accounts and Microsoft parental controls | Not available. Create a standard account for each child in **Settings → Accounts → Other users**. |
| Windows backup to OneDrive | Not available. **Settings → System → Recovery** can take the system back to an earlier state, but it does not save your files: copy them to a USB drive or a cloud app. |

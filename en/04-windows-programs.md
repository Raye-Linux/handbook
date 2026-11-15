# Windows programs

Double-click an **.exe** or **.msi** file: it opens, like on Windows.
Nothing to install first, no questions.

- Each program gets **its own space**, so one that misbehaves cannot
  break the others.
- A couple of minutes after your first login, Raye prepares that space in
  the background: Raye's colors, Inter in place of Segoe UI, the display
  scale, and your own Documents, Pictures, Music, Videos and Downloads. A
  program's desktop shortcut lands inside the space, not on your desktop:
  Raye makes its own launcher for it. From then on a program opens in a
  second or two.
- An installed program gets its entry in Start, and you remove it from
  **Settings → Apps → Installed apps**, like any other app.
- When a program also exists for Raye (Steam, Discord, OBS Studio...),
  Raye offers that version first: it fits in better.
- Microsoft's fonts and Visual C++ runtimes are fetched in the background
  once the PC is online; until then some text comes out in another
  typeface. See [What this beta still gets wrong](07-this-beta.md).

## What has been tried

**Works:** 7-Zip and WinRAR install with a double-click, open from Start
and do real work. 7-Zip uninstalls from Settings. An older Direct3D 9
game, Chocolate Doom, runs full screen with its sound.

**Does not work, on purpose:**

- Games protected by an anti-cheat that refuses this system: Roblox,
  Fortnite, Valorant, several Battlefield games, Call of Duty: Black Ops
  7... Their publisher has to allow Linux. When you double-click the
  Roblox installer, Raye says so and installs nothing. Raye never works around an
  anti-cheat: it would get your account banned.
- Minecraft's Windows launcher and Bedrock Edition need the Microsoft
  Store. Raye says so and opens the Minecraft Java Edition launcher in
  the Store instead.

**Does not work yet:** Roblox Studio installs and opens its sign-in page,
but that page does not take typing.

**Not tried yet:** heavy 3D games (Direct3D 11 and 12) on a real graphics
card. For games you bought on Steam, use **Steam** from the Store.

For creative software, try **ArtCraft** in the Store: open-source apps
for photos, illustration, video and PDF.

To free space: **Settings → Gaming** lists the Windows programs and can
remove their space.

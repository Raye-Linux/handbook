# Hyprland on Raye: change everything

Hyprland is the tiling desktop of Raye: windows line up side by side on
their own, and you do most things with the keyboard. This page shows how to
change nearly anything, without ever breaking Raye's own settings.

You can change what you like in **one file**, and go back at any time.

## Two kinds of files

| File | Whose | What to do |
|---|---|---|
| `/usr/share/raye/hyprland/hyprland.conf` | Raye's settings, for every account | Read it, never edit it: an update replaces it |
| `~/.config/raye-hyprland/user.conf` | **Yours** | Edit it. Raye never changes it |

Hyprland reads Raye's settings first and your file **last**, so a line of
yours always wins. The other files in `~/.config/raye-hyprland/`
(`hyprland.conf`, `keyboard.conf`, `monitors.conf`, `hyprlock.conf`) are
written by Raye at each sign-in: leave them alone.

## Open your file, apply it, go back

Open a terminal and use the `raye-hyprland-config` command, or in
**Settings → Personalization → Desktop environment** press **Open my
Hyprland settings**.

    raye-hyprland-config open     # makes the file if needed, opens it
    raye-hyprland-config reload   # applies it now
    raye-hyprland-config reset    # back to Raye's settings

Hyprland applies a change **as soon as you save**: no need to sign out. If
a line is wrong, a red bar shows the problem at the top of the screen; fix
the line and save again. **reset** keeps a copy of your file next to it
(`user.conf.<date>.bak`) before emptying it.

## Examples to copy

Put them in `user.conf`. Each one replaces only the value you name.

**Gaps and borders**

    general {
        gaps_in = 2
        gaps_out = 4
        border_size = 2
        col.active_border = rgba(ff8800ff)
    }

**Square corners, no shadow**

    decoration {
        rounding = 0
        shadow {
            enabled = false
        }
    }

**Blur** (Raye blurs only the taskbar and Start; to blur behind one app)

    windowrule {
        name = my-terminal-blur
        match:class = ^(konsole)$
        no_blur = off
    }
    decoration {
        blur {
            size = 6
        }
    }

**Animations**: faster, or none

    animations {
        enabled = false
    }

To keep them but speed up windows opening:

    animation = windowsIn, 1, 1.5, rayeIn, popin 94%

(the number after `1,` is the time in tenths of a second).

**Your own shortcuts**

    bind = SUPER, T, exec, konsole
    bind = SUPER SHIFT, B, exec, firefox
    unbind = SUPER, M

`SUPER` is the Windows key. `bind` is for one press, `bindm` for the mouse,
`bindel` for keys that repeat (volume). Raye's own shortcuts are at the
end of `/usr/share/raye/hyprland/hyprland.conf`; `unbind` frees one of them.

**Window rules** (an app always floats, or always opens on a desktop)

    windowrule {
        name = calculator-floats
        match:class = ^(org\.kde\.kcalc)$
        float = yes
        center = yes
    }
    windowrule {
        name = browser-on-2
        match:class = ^(firefox)$
        workspace = 2
    }

To learn an app's class, open it and run `hyprctl clients`: the line
`class:` is what goes after `match:class`.

**Screens**: a second screen, and the size of things

    raye-hyprland-config open   # then add:
    monitor = DP-1, 2560x1440@144, 0x0, 1
    monitor = HDMI-A-1, preferred, 2560x0, 1.25

List your screens with `hyprctl monitors`. The last number is the scale
(1.25 is 125 %). Raye writes the scale you pick in Settings into
`monitors.conf`; a `monitor =` line in your file wins over it.

**Keyboard and mouse**

    input {
        kb_layout = ca
        repeat_rate = 40
        sensitivity = -0.3
        touchpad {
            natural_scroll = false
        }
    }

**Programs at sign-in**

    exec-once = discord --start-minimized
    exec-once = nm-applet

**Wallpaper**: pick it in **Settings → Personalization → Background**; the
Raye shell draws it. Nothing to write in the file.

**Taskbar and Start**: **Settings → Personalization → Taskbar** (size,
position, hide by itself). The shell is `raye-hypr-shell`; restart it with
`hyprctl dispatch exec raye-hypr-shell` if you ever close it.

## Lock and sleep

Win+L, and closing the lid, lock the screen (`hyprlock`). The screen turns
off after 10 minutes and locks a minute later (`hypridle`). To change the
times, copy Raye's file and make your own:

    mkdir -p ~/.config/hypr
    cp /usr/share/raye/hyprland/hypridle.conf ~/.config/hypr/hypridle.conf

then edit the `timeout =` numbers (in seconds). A file in
`~/.config/hypr/` is used instead of Raye's.

## Make the Raye apps look right

Raye's apps (Settings, Files, Store, Task Manager, Clock...) follow the
Raye style, colours and icons on Hyprland the same way as on KDE Plasma.
The session sets it for you; this is what it does and where to change it.

- **Theme and colours.** Qt and KDE apps use the Raye style
  (`QT_QPA_PLATFORMTHEME=kde`). Change the colours and the light or dark
  mode in **Settings → Personalization → Colors**, not in Hyprland.
- **GTK apps** (Firefox, GIMP...) read the same choice. If one looks wrong,
  run `gsettings set org.gnome.desktop.interface color-scheme prefer-dark`
  (or `default`).
- **Icons and cursor.** **Settings → Personalization**. The cursor is
  `Raye`, size 24; to change the size add to `user.conf`:

        env = XCURSOR_SIZE, 32
        env = HYPRCURSOR_SIZE, 32

- **Fonts** and text size: **Settings → Personalization → Fonts**.
- **Scale.** Set it per screen in **Settings → System → Display**, or with
  a `monitor =` line (see above). Programs that still run through X11 stay
  sharp: Raye turns off their blurry scaling.
- **Title bars.** Hyprland draws none; Raye's Qt apps draw their own. GTK
  apps draw theirs.
- **Where the apps keep their settings** (to copy or reset them):

  | App | File in `~/.config/` |
  |---|---|
  | Settings | `raye-settingsrc` |
  | Taskbar, Start, shell | `rayeshellrc` |
  | Raye style and title bars | `rayerc` |
  | Files | `dolphinrc` |

  Delete a file to give an app its defaults again (close the app first).
- **Window rules for the Raye apps.** Find the class with `hyprctl clients`
  while the app is open, then use the `windowrule` examples above. The
  Task Manager and dialogs already float; Settings and Files tile.
- **An app looks wrong?** Try, in order: close and open it again; sign out
  and in; delete its file from the table; make sure no line of your
  `user.conf` touches it (move the file aside with
  `mv ~/.config/raye-hyprland/user.conf ~/user.conf.test`, sign out and in,
  and look). Still wrong: see *Reporting a problem*.

## Other people's setups (dots)

The Hyprland community shares complete setups ("dotfiles") such as
Caelestia. Raye can try one and bring you back:

    raye-hyprland-config dots install https://github.com/<who>/<repo>

It **saves all your Hyprland and shell settings first** in a dated archive
under `~/.local/share/raye-hyprland/backups/`, downloads the repository,
shows you what its install script will do and **asks you to type `yes`**.
That script is somebody else's code: it can install programs and replace
your settings. Read it, and use only setups you trust.

    raye-hyprland-config dots restore   # exactly what you had before
    raye-hyprland-config dots off       # use Raye's settings again, keep theirs
    raye-hyprland-config reset          # also goes back to Raye's settings

If the setup does not start, Raye comes back by itself at the next sign-in.
From the sign-in screen you can also choose **KDE Plasma**; from a text
console (Ctrl+Alt+F3) run `raye-hyprland-config dots restore`.

## Go further

The whole Hyprland manual, with every setting:
[wiki.hypr.land](https://wiki.hypr.land/Configuring/). Start with *Variables*
(every setting and its values), *Binds*, *Window Rules* and *Monitors*.

# For developers

**Settings → System → Advanced** ends with a **For developers** section.
Nothing in it is on until you turn it on.

- **Developer Mode** unlocks the rest. From your next sign-in, Raye's own
  apps also write detailed logs. Turning it off turns Device Portal off.
- **Device Portal** lets you manage this PC from a browser on the same
  network. See below.
- **Device discovery** lets devices on the network find Device Portal by
  this PC's name.
- **OpenSSH server** lets you sign in to this PC from another computer
  with `ssh`. **Sign in with a key only** is on by default: passwords are
  refused, so put your public key in `~/.ssh/authorized_keys` before you
  connect.

## Device Portal

1. Turn on **Developer Mode**, then **Device Portal**.
2. Settings shows the **Address**, such as `https://192.168.1.20:50443`,
   and the **Certificate fingerprint**.
3. Open that address in a browser on another device of the same network.
   The browser warns about the page the first time: go on only if it
   shows the same fingerprint.
4. Sign in with the user name and password you **Set** in Settings, or
   choose **Pair a device**: Settings shows a code that works once, for
   10 minutes, and that browser then stays paired for 30 days.

The portal shows the PC at a glance: performance, processes, apps, logs,
network, and the files of your home folder, which you can download and
add to. It only answers devices on the networks this PC is connected to,
and after five wrong tries a device has to wait 15 minutes. Settings
keeps a **Connection log** of who came in.

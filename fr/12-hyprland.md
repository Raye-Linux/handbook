# Hyprland sur Raye : tout changer

Hyprland est le bureau en mosaïque de Raye : les fenêtres se rangent côte à
côte toutes seules, et on fait presque tout au clavier. Cette page montre
comment changer presque tout, sans jamais abîmer les réglages de Raye.

Ce que vous changez tient dans **un seul fichier**, et vous pouvez revenir en
arrière à tout moment.

## Deux sortes de fichiers

| Fichier | À qui | Que faire |
|---|---|---|
| `/usr/share/raye/hyprland/hyprland.conf` | Les réglages de Raye, pour tous les comptes | À lire, jamais à modifier : une mise à jour le remplace |
| `~/.config/raye-hyprland/user.conf` | **Le vôtre** | À modifier. Raye n'y touche jamais |

Hyprland lit les réglages de Raye d'abord et votre fichier **en dernier** :
une ligne de vous gagne toujours. Les autres fichiers de
`~/.config/raye-hyprland/` (`hyprland.conf`, `keyboard.conf`,
`monitors.conf`, `hyprlock.conf`) sont réécrits par Raye à chaque connexion :
n'y touchez pas.

## Ouvrir son fichier, l'appliquer, revenir

Dans un terminal, utilisez la commande `raye-hyprland-config`, ou allez dans
**Paramètres → Personnalisation → Environnement de bureau** et appuyez sur
**Ouvrir mes réglages Hyprland**. Le bouton **Guide Hyprland** juste à côté
ouvre cette page.

    raye-hyprland-config open     # crée le fichier si besoin, l'ouvre
    raye-hyprland-config reload   # l'applique tout de suite
    raye-hyprland-config reset    # retour aux réglages de Raye

Hyprland applique un changement **dès l'enregistrement** : inutile de se
déconnecter. Si une ligne est fausse, une barre rouge en haut de l'écran
indique le problème ; corrigez la ligne et enregistrez de nouveau. **reset**
garde une copie de votre fichier à côté (`user.conf.<date>.bak`) avant de le
vider.

## Exemples à copier

À mettre dans `user.conf`. Chacun ne remplace que la valeur nommée.

**Écarts et bordures**

    general {
        gaps_in = 2
        gaps_out = 4
        border_size = 2
        col.active_border = rgba(ff8800ff)
    }

**Coins carrés, sans ombre**

    decoration {
        rounding = 0
        shadow {
            enabled = false
        }
    }

**Flou** (Raye ne floute que la barre des tâches et Démarrer ; pour flouter
derrière une appli)

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

**Animations** : plus rapides, ou aucune

    animations {
        enabled = false
    }

Pour les garder mais accélérer l'ouverture des fenêtres :

    animation = windowsIn, 1, 1.5, rayeIn, popin 94%

(le nombre après `1,` est la durée en dixièmes de seconde).

**Vos propres raccourcis**

    bind = SUPER, T, exec, konsole
    bind = SUPER SHIFT, B, exec, firefox
    unbind = SUPER, M

`SUPER` est la touche Windows. `bind` sert pour un appui, `bindm` pour la
souris, `bindel` pour les touches qui se répètent (volume). Les raccourcis de
Raye sont à la fin de `/usr/share/raye/hyprland/hyprland.conf` ; `unbind`
libère l'un d'eux.

**Règles de fenêtres** (une appli flotte toujours, ou s'ouvre toujours sur un
bureau)

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

Pour connaître la classe d'une appli, ouvrez-la et lancez `hyprctl clients` :
la ligne `class:` est ce qui va après `match:class`.

**Écrans** : un second écran, et la taille des choses

    raye-hyprland-config open   # puis ajoutez :
    monitor = DP-1, 2560x1440@144, 0x0, 1
    monitor = HDMI-A-1, preferred, 2560x0, 1.25

Listez vos écrans avec `hyprctl monitors`. Le dernier nombre est l'échelle
(1,25 vaut 125 %). Raye écrit dans `monitors.conf` l'échelle choisie dans
les Paramètres ; une ligne `monitor =` de votre fichier l'emporte.

**Clavier et souris**

    input {
        kb_layout = ca
        repeat_rate = 40
        sensitivity = -0.3
        touchpad {
            natural_scroll = false
        }
    }

**Programmes à la connexion**

    exec-once = discord --start-minimized
    exec-once = nm-applet

**Fond d'écran** : choisissez-le dans **Paramètres → Personnalisation →
Arrière-plan** ; le shell de Raye le dessine. Rien à écrire dans le fichier.

**Barre des tâches et Démarrer** : **Paramètres → Personnalisation → Barre
des tâches** (taille, position, masquage automatique). Le shell s'appelle
`raye-hypr-shell` ; relancez-le avec `hyprctl dispatch exec raye-hypr-shell`
si vous l'avez fermé.

## Verrouillage et veille

Win+L, et la fermeture du capot, verrouillent l'écran (`hyprlock`). L'écran
s'éteint après 10 minutes et se verrouille une minute plus tard (`hypridle`).
Pour changer les durées, copiez le fichier de Raye et faites le vôtre :

    mkdir -p ~/.config/hypr
    cp /usr/share/raye/hyprland/hypridle.conf ~/.config/hypr/hypridle.conf

puis modifiez les nombres `timeout =` (en secondes). Un fichier dans
`~/.config/hypr/` est utilisé à la place de celui de Raye.

## Que les applis de Raye s'affichent bien

Les applis de Raye (Paramètres, Fichiers, Store, Gestionnaire des tâches,
Horloge...) suivent le style, les couleurs et les icônes de Raye sous
Hyprland comme sous KDE Plasma. La session s'en charge ; voici ce qu'elle
fait et où le changer.

- **Thème et couleurs.** Les applis Qt et KDE utilisent le style Raye
  (`QT_QPA_PLATFORMTHEME=kde`). Changez les couleurs et le mode clair ou
  sombre dans **Paramètres → Personnalisation → Couleurs**, pas dans Hyprland.
- **Applis GTK** (Firefox, GIMP...) lisent le même choix. Si l'une est de
  travers, lancez
  `gsettings set org.gnome.desktop.interface color-scheme prefer-dark`
  (ou `default`).
- **Icônes et curseur.** **Paramètres → Personnalisation**. Le curseur est
  `Raye`, taille 24 ; pour changer la taille, ajoutez à `user.conf` :

        env = XCURSOR_SIZE, 32
        env = HYPRCURSOR_SIZE, 32

- **Polices** et taille du texte : **Paramètres → Personnalisation →
  Polices**.
- **Échelle.** Réglez-la par écran dans **Paramètres → Système → Écran**, ou
  avec une ligne `monitor =` (voir plus haut). Les programmes qui passent
  encore par X11 restent nets : Raye coupe leur mise à l'échelle floue.
- **Barres de titre.** Hyprland n'en dessine pas ; les applis Qt de Raye
  dessinent la leur. Les applis GTK dessinent la leur.
- **Où les applis gardent leurs réglages** (pour les copier ou les
  réinitialiser) :

  | Appli | Fichier dans `~/.config/` |
  |---|---|
  | Paramètres | `raye-settingsrc` |
  | Barre des tâches, Démarrer, shell | `rayeshellrc` |
  | Style Raye et barres de titre | `rayerc` |
  | Fichiers | `dolphinrc` |

  Supprimez un fichier pour rendre ses réglages d'origine à une appli
  (fermez-la d'abord).
- **Règles de fenêtres pour les applis de Raye.** Trouvez la classe avec
  `hyprctl clients` pendant que l'appli est ouverte, puis servez-vous des
  exemples `windowrule` ci-dessus. Le Gestionnaire des tâches et les boîtes
  de dialogue flottent déjà ; Paramètres et Fichiers se rangent en mosaïque.
- **Une appli s'affiche mal ?** Essayez dans l'ordre : la fermer et la rouvrir ;
  se déconnecter puis se reconnecter ; supprimer son fichier du tableau ;
  vérifier qu'aucune ligne de votre `user.conf` ne la touche (écartez le
  fichier avec `mv ~/.config/raye-hyprland/user.conf ~/user.conf.test`,
  reconnectez-vous et regardez). Toujours de travers : voir *Signaler un
  problème*.

## Les réglages des autres (dots)

La communauté Hyprland partage des réglages complets (« dotfiles »), comme
Caelestia. Raye peut en essayer un et vous ramener en arrière :

    raye-hyprland-config dots install https://github.com/<qui>/<depot>

La commande **sauvegarde d'abord tous vos réglages Hyprland et du shell** dans
une archive datée sous `~/.local/share/raye-hyprland/backups/`, télécharge le
dépôt, vous montre ce que son script d'installation va faire et **vous
demande de taper `yes`**. Ce script est du code d'un tiers : il peut installer
des programmes et remplacer vos réglages. Lisez-le, et n'utilisez que des
réglages en qui vous avez confiance.

    raye-hyprland-config dots restore   # exactement ce que vous aviez
    raye-hyprland-config dots off       # les réglages de Raye, on garde les leurs
    raye-hyprland-config reset          # revient aussi aux réglages de Raye

Si le réglage ne démarre pas, Raye revient tout seul à la connexion suivante.
Depuis l'écran de connexion vous pouvez aussi choisir **KDE Plasma** ; depuis
une console texte (Ctrl+Alt+F3) lancez `raye-hyprland-config dots restore`.

## Aller plus loin

Le manuel complet de Hyprland, avec chaque réglage :
[wiki.hypr.land](https://wiki.hypr.land/Configuring/). Commencez par
*Variables* (chaque réglage et ses valeurs), *Binds*, *Window Rules* et
*Monitors*.

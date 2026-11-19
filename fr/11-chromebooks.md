# Installer sur un Chromebook

Beaucoup de Chromebooks à processeur **Intel ou AMD** peuvent faire tourner
Raye. C'est plus long que sur un PC ordinaire, et une étape ne dépend pas
de Raye : le Chromebook a besoin d'un nouveau micrologiciel (le programme
qui démarre l'ordinateur), fait par un projet communautaire appelé
**MrChromebox**. Raye ne l'écrit pas et ne peut pas en assurer le suivi ;
cette page explique comment s'en servir et à quoi s'attendre.

Les Chromebooks à processeur **ARM** (MediaTek, Qualcomm Snapdragon,
Rockchip) ne peuvent pas faire tourner Raye, et le micrologiciel décrit
ici n'existe pas pour eux.

Cette page suit le guide de MrChromebox (docs.mrchromebox.tech) et les notes
de la communauté sur docs.chrultrabook.com. Si les deux disent autre chose
que cette page, ce sont eux qui ont raison : ils sont mis à jour plus
souvent. Raye n'a pas été essayé sur tous les Chromebooks, et certains ne
l'ont jamais été.

Avant tout : **si le Chromebook appartient à une école ou à une entreprise,
arrêtez-vous ici.** Un Chromebook géré ne peut pas être modifié ainsi, et il
vous faut de toute façon l'accord écrit de son propriétaire.

## 1. Vérifier que votre Chromebook est pris en charge

Tout dépend du **nom de carte** (board name), pas de la marque ni du modèle
acheté : un même nom de carte est vendu sous plusieurs noms de modèle.

1. Dans ChromeOS, ouvrez le navigateur, allez à `chrome://system` et
   cherchez **HWID**. Le nom de carte en est le premier mot, avant le
   premier espace ou tiret.
2. Ouvrez la liste des appareils pris en charge par MrChromebox,
   docs.mrchromebox.tech/docs/supported-devices.html, et cherchez ce nom de
   carte. La liste est classée par génération de processeur et ne contient
   que des machines Intel et AMD. **Si votre nom de carte n'y est pas, il
   n'est pas pris en charge.** N'essayez pas avec un modèle « proche ».
3. Notez les deux colonnes utiles pour la suite : **RW_LEGACY** et **UEFI
   Firmware (Full ROM)**, ainsi que **WP Method**.

Raye a aussi besoin de **25 Go** d'espace libre et de 4 Go de mémoire
(8 Go conseillés). Un Chromebook de 32 Go de stockage suffit tout juste,
un de 16 Go non.

## 2. Sauvegarder, et préparer deux clés USB

L'étape suivante efface tout ce qui est stocké sur le Chromebook lui-même.
Les fichiers de Google Drive restent dans Google Drive ; le dossier
**Téléchargements** et tout ce qui n'est pas synchronisé est perdu. Copiez
ce que vous voulez garder sur une clé USB ou dans le cloud.

Il vous faut aussi :

- la **clé USB de Raye**, préparée sur un autre ordinateur comme dans
  [Installer Raye Linux](01-installer.md), étapes 1 et 2 ;
- une deuxième clé USB pour la sauvegarde du micrologiciel du Chromebook
  (étape 5) ;
- le chargeur, branché tout du long. MrChromebox y tient : certaines étapes
  refusent de se lancer, ou tournent mal, sur batterie.

## 3. Activer le mode développeur

1. Éteignez le Chromebook. Maintenez **Échap** et **Actualiser** (la
   flèche en rond de la rangée du haut), puis appuyez sur **Marche**.
   Relâchez quand l'écran de récupération s'affiche. Il faut le clavier
   intégré.
   Sur une tablette : maintenez **Volume haut, Volume bas et Marche**
   pendant 10 secondes.
2. Sur cet écran, appuyez sur **Ctrl + D** et confirmez.
3. Le Chromebook s'efface et redémarre. Cela prend quelques minutes.

Désormais, chaque démarrage affiche un écran disant que la validation de
l'OS est désactivée. C'est normal : c'est le signe que le mode développeur
est actif.

Pour taper les commandes des étapes suivantes, il vous faut le terminal de
ChromeOS. À l'écran de connexion de ChromeOS, appuyez sur **Ctrl + Alt** et
la deuxième touche de la rangée du haut (ChromeOS l'appelle F2 ; sur la
plupart des modèles elle montre →), puis connectez-vous en tant que
`chronos`, sans mot de passe. Sur un ChromeOS antérieur à la version 117,
ouvrez plutôt le navigateur, appuyez sur **Ctrl + Alt + T** et tapez
`shell`.

## 4. Choisir le micrologiciel

MrChromebox en propose deux sortes. Choisissez avant l'étape suivante.

**UEFI Full ROM** - conseillé, quand la liste l'indique pour votre carte.
Le Chromebook démarre alors comme un PC ordinaire : plus d'écran
d'avertissement, Raye démarre tout seul, l'ordre de démarrage est
mémorisé, et le Secure Boot existe. Ce que ça coûte :

- ChromeOS est supprimé. On peut le remettre, avec la sauvegarde de
  l'étape 5.
- Il faut d'abord couper la **protection en écriture** du micrologiciel
  (étape 5).
- Si l'écriture est interrompue (coupure de courant, plantage), le
  Chromebook peut ne plus démarrer, et le ramener demande un câble ou un
  programmateur spécial. MrChromebox parle d'un petit risque. Il n'est pas
  nul.

**RW_LEGACY** - garde le micrologiciel installé par Google et ajoute
seulement un moyen de démarrer autre chose. Il ne peut pas abîmer le
Chromebook et ne touche pas à la protection en écriture. Ce que ça coûte :

- Chaque démarrage affiche l'écran du mode développeur, et vous appuyez sur
  **Ctrl + L** pour démarrer Raye (le script peut en faire le choix par
  défaut, voir l'étape 6).
- Le Chromebook ne mémorise aucun ordre de démarrage et n'a pas de Secure
  Boot. Raye démarre quand même : il garde une copie de son chargeur de
  démarrage à l'endroit où un micrologiciel regarde quand il ne se souvient
  de rien.
- L'installation de Raye ne sait pas partager le disque interne avec
  ChromeOS. Installer Raye dessus avec **Effacer ce disque** supprime
  ChromeOS, même avec RW_LEGACY. N'utilisez pas **Installer à côté de
  Windows** sur un Chromebook : c'est fait pour Windows et n'a pas été
  essayé avec ChromeOS.
- Sur les générations anciennes (la liste indique **EOL** dans la colonne
  RW_LEGACY), RW_LEGACY ne s'installe plus : seul Full ROM est proposé.
- MrChromebox signale deux générations où RW_LEGACY marche mal : **Gemini
  Lake** (le menu de démarrage n'affiche pas la liste des disques, on ne
  peut donc pas choisir la clé USB) et **AMD Stoney Ridge** (il ne démarre
  pas sur la plupart des modèles). Prenez Full ROM dans ces cas-là.

## 5. Full ROM seulement : couper la protection en écriture

La méthode dépend de votre carte : la colonne **WP Method** de la liste
dit laquelle. Suivez exactement la page de MrChromebox,
docs.mrchromebox.tech/docs/firmware/wp/disabling.html. En bref :

- **screw, jumper ou switch** (modèles de 2016 et avant) : on ouvre le
  Chromebook et on retire une vis ou on déplace un cavalier.
- **CR50** (environ 2017 à 2022) : débrancher la batterie à l'intérieur, ou
  utiliser un câble USB-C spécial (SuzyQ).
- **Ti50** (la plupart des modèles vendus depuis 2023) : **ne l'ouvrez
  pas.** Cela se fait par une commande dans le terminal de ChromeOS, et le
  guide vous fait aussi autoriser le micrologiciel à démarrer sans sa
  vérification habituelle, avant tout le reste. Sautez cette partie et le
  Chromebook risque de ne plus démarrer.

N'utilisez que les commandes de cette page. Les commandes trouvées ailleurs
pour couper la protection à la main sont, selon MrChromebox, inutiles, et
le script s'occupe du reste lui-même.

## 6. Lancer le script du micrologiciel

Dans le terminal de ChromeOS (étape 3), tapez, sur une seule ligne :

    cd; curl -LOf https://mrchromebox.tech/firmware-util.sh && sudo bash firmware-util.sh

Un menu s'affiche, en anglais. Les options marquées **[WP]** demandent que
la protection en écriture soit coupée.

- **Full ROM :** choisissez **Install/Update UEFI (Full ROM) Firmware**.
  Quand le script propose de **sauvegarder le micrologiciel d'origine sur
  une clé USB**, acceptez et prenez la deuxième clé. Gardez ce fichier :
  c'est la seule copie exacte de ce qui était livré avec votre Chromebook,
  et il vous le faut pour revenir à ChromeOS. Copiez-le aussi sur un autre
  ordinateur. Quand le script a fini, passez par son menu pour **éteindre**
  (power off) ; ne redémarrez pas tout de suite.
- **RW_LEGACY :** choisissez **Install/Update the RW_LEGACY Firmware**.
  Pour ne plus appuyer sur Ctrl + L à chaque démarrage, choisissez ensuite
  **Set Boot Options (GBB Flags)** et prenez un délai court avec Legacy
  Boot par défaut.

Le premier démarrage après une écriture Full ROM peut rester noir une
minute environ : le micrologiciel teste la mémoire. Attendez 90 secondes
avant de croire que quelque chose ne va pas.

## 7. Démarrer sur la clé de Raye

Branchez la clé de Raye.

- **Full ROM :** allumez le Chromebook et appuyez sur **Échap** quand le
  logo (un lièvre) s'affiche. Choisissez **Boot Menu**, puis la clé USB.
- **RW_LEGACY :** sur l'écran du mode développeur, appuyez sur **Ctrl + L**,
  puis **Échap** quand le logo s'affiche, **Boot Menu**, et la clé USB.

Si la clé n'est pas dans la liste, revenez en arrière, débranchez-la,
rebranchez-la, attendez trois secondes et rouvrez le Boot Menu. Essayez un
autre port si elle n'apparaît toujours pas. Si vous tombez sur une invite
de texte (le shell EFI), tapez `exit` et appuyez sur Entrée.

La clé de Raye affiche son menu : choisissez **Installer Raye Linux**, ou
**Safe graphics** si l'écran reste noir. Raye démarre avec ou sans Secure
Boot ; il n'y a rien à changer.

## 8. Installer

L'installation se passe comme dans [Installer Raye Linux](01-installer.md),
étape 4. Sur la page du disque, prenez le disque **interne** (souvent
appelé eMMC, ou un disque NVMe), pas la clé USB, et choisissez **Effacer ce
disque**.

À propos de **Chiffrer Raye avec un mot de passe** : la puce de sécurité
d'un Chromebook ne fait que ce dont ChromeOS a besoin, et MrChromebox
indique qu'elle ne peut pas garder une clé de disque pour d'autres
systèmes. Le chiffrement marche quand même ; attendez-vous à ce que Raye
demande le mot de passe du disque à chaque démarrage.

Quand l'installation est finie, redémarrez et retirez la clé.

<a id="keyboard"></a>
## 9. Le clavier

Raye voit qu'il tourne sur un Chromebook et règle la rangée du haut pour
qu'elle fasse ce que montrent ses icônes :

| Touche | Ce qu'elle fait |
|---|---|
| Précédent, Suivant | page précédente et suivante dans le navigateur et l'Explorateur de fichiers |
| Actualiser | recharge la page |
| Plein écran | plein écran (comme F11) |
| Vue d'ensemble | affiche toutes les fenêtres (⊞ + Tab) |
| Luminosité, volume | comme indiqué sur la touche |
| Verrouillage (en haut à droite, sur la plupart des modèles) | verrouille l'écran |
| **Rechercher** seule | ouvre le menu Démarrer, comme la touche ⊞ |
| **Rechercher** + une touche du haut | F1, F2, F3... dans l'ordre depuis la gauche |
| **Alt + Retour arrière** | Suppr |
| **Ctrl + Alt + Retour arrière** | Ctrl + Alt + Suppr |
| **Alt + luminosité** | rétroéclairage du clavier, s'il y en a un |

Les Chromebooks récents n'ont pas tous la même rangée du haut. Raye lit son
ordre dans le micrologiciel, donc Rechercher + la première touche donne
toujours F1. Si vous avez déjà réglé vos touches vous-même avec keyd, Raye
ne touche pas à vos réglages.

<a id="sound"></a>
## 10. Le son

Sur beaucoup de Chromebooks, les haut-parleurs ou le micro ne marchent pas
juste après l'installation. Ce n'est pas un défaut de Raye : les puces son
des Chromebooks ont besoin de réglages que seul ChromeOS contient. Raye
affiche une notification la première fois qu'il ne trouve aucune sortie
son.

Un script de la communauté, **chromebook-linux-audio**, répare la plupart
des modèles. Il écrit dans les réglages son du système : utilisez-le en le
sachant, et seulement sur votre Raye installé (pas depuis la clé). Il n'a
pas été essayé sur Raye. Ouvrez un terminal (Konsole) et tapez, une ligne
après l'autre :

    sudo apt install git
    git clone --depth 1 https://github.com/WeirdTreeThing/chromebook-linux-audio
    cd chromebook-linux-audio
    ./setup-audio

Puis redémarrez. Les mises à jour du paquet son du système peuvent défaire
la réparation ; si le son disparaît après une mise à jour, relancez
`./setup-audio`.

**Protégez vos haut-parleurs.** Sur certains Chromebooks **Skylake**, **Kaby
Lake** et **Apollo Lake**, l'amplificateur des haut-parleurs (max98357a)
n'a pas de limite de volume avec le pilote que choisit le script. Le script
vous prévient et demande d'abord. Monter le volume trop haut peut abîmer
les haut-parleurs pour de bon : gardez-le bas, ou répondez non.

Ce que les notes de la communauté signalent pour chaque génération, au
moment où ces lignes sont écrites :

| Génération | Problèmes connus |
|---|---|
| Apollo Lake | les cartes microSD peuvent ne pas être détectées ; pas de prise casque avec l'un des deux pilotes son |
| Kaby Lake | la caméra ne marche pas sur certains modèles |
| Comet Lake | le lecteur d'empreintes ne marche pas ; certains se réveillent écran rabattu |
| Tiger Lake, Alder Lake | l'USB-C peut ne pas marcher (réparation plus bas) ; pas de lecteur d'empreintes |
| Alder Lake-N | le son peut ne pas marcher |
| AMD Stoney Ridge | le son demande un noyau récent ; celui de Raye l'est assez |
| AMD Picasso | il faut ajouter `iommu=pt` à la ligne de démarrage du noyau (plus bas) |
| AMD Cezanne | les haut-parleurs ne marchent pas encore |
| tous | les lecteurs d'empreintes ne marchent pas |

**USB-C sur Tiger Lake et Alder Lake.** Dans un terminal :

    echo cros-ec-typec | sudo tee -a /etc/initramfs-tools/modules
    echo intel-pmc-mux | sudo tee -a /etc/initramfs-tools/modules
    sudo update-initramfs -u -k all

**AMD Picasso.** Dans un terminal, puis redémarrez :

    echo 'GRUB_CMDLINE_LINUX="$GRUB_CMDLINE_LINUX iommu=pt"' | sudo tee /etc/default/grub.d/60-chromebook.cfg
    sudo update-grub

## Revenir à ChromeOS

- **Avec RW_LEGACY :** votre micrologiciel est toujours celui de Google.
  Préparez une clé de récupération ChromeOS sur un autre ordinateur
  (l'**Utilitaire de récupération Chromebook** de Google, dans Chrome), puis
  démarrez le Chromebook avec **Échap + Actualiser + Marche** et branchez la
  clé quand l'écran le demande.
- **Avec Full ROM :** remettez d'abord le micrologiciel d'origine. Démarrez
  Raye, ouvrez un terminal et lancez le même script qu'à l'étape 6.
  Choisissez **Restore Stock Firmware**, puis la sauvegarde USB faite à
  l'étape 5. Préparez ensuite la clé de récupération comme ci-dessus.

Deux avertissements de MrChromebox : quand Google a cessé de mettre à jour
un modèle (fin de vie), il ne peut plus du tout revenir à ChromeOS ; et sur
les modèles **Ti50**, revenir en arrière comporte plus de risque, alors
gardez la sauvegarde et lisez leur page avant de commencer.

## En cas de problème

- **Écran noir après l'écriture :** attendez 90 secondes. Puis maintenez
  Marche 10 secondes et rallumez.
- **Un menu en texte ou un écran noir au lieu du menu de Raye** juste après
  une écriture Full ROM : l'ancien chargeur de ChromeOS est encore sur le
  disque. Éteignez et rallumez le Chromebook, et appuyez sur **Échap** au
  logo.
- **Le micrologiciel lui-même est cassé :** le guide de MrChromebox explique
  comment le récupérer avec un câble SuzyQ ou un programmateur. Raye ne peut
  pas aider pour cette partie.
- Demandez sur le Discord de Raye Linux, dans #help. Donnez le **nom de
  carte** (étape 1), le micrologiciel choisi et une photo de l'écran.

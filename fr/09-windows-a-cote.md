# Installer à côté de Windows

Raye peut prendre une partie du disque et laisser Windows où il est. La
seule chose qui tourne mal, tourne mal avant même que vous démarriez Raye.

## D'abord, dans Windows : l'éteindre pour de vrai

Windows est livré avec le **démarrage rapide** activé. Avec lui,
« Arrêter » n'arrête pas : il enregistre le système en cours sur le disque
et s'arrête là. Le disque reste à moitié ouvert, et l'outil qui fait de la
place pour Raye **refuse de toucher un disque dans cet état**. Ce refus
est volontaire. Forcer le redimensionnement d'un Windows à moitié
ouvert, c'est comme ça qu'on perd des fichiers.

Donc, dans Windows : **Panneau de configuration → Options d'alimentation
→ Choisir l'action des boutons d'alimentation**, décochez **Activer le
démarrage rapide**, puis arrêtez l'ordinateur. La veille prolongée laisse
la même trace : ne revenez pas d'une veille prolongée non plus.

Raye le vérifie lui-même. Si Windows n'a pas été arrêté correctement, le
tout premier écran de l'installation le dit, avant que rien ne soit écrit.

Le même écran prévient de deux autres choses :

- **BitLocker.** Démarrez Windows, ouvrez **Gérer BitLocker**, choisissez
  **Suspendre la protection**, puis revenez - et gardez votre clé de
  récupération BitLocker sous la main.
- **Un autre Linux sur le même disque.** Raye remplacerait sa façon de
  démarrer. Effacez le disque en le voulant, ou choisissez-en un autre.

## La place

Au moins **25 Go** de libre : l'installation refuse d'aller plus loin en
dessous. C'est le plancher, pas un chiffre confortable - ce que Raye
lui-même finit par occuper n'a pas été mesuré.

## La page du disque

Cette page de l'installation est en anglais même si vous avez choisi le
français - voir [Ce que cette bêta fait encore mal](07-cette-beta.md).
Trois choix :

- **Erase disk** (effacer le disque) - Raye tout seul. Déjà sélectionné :
  ne le laissez pas par distraction.
- **Install alongside** (installer à côté) - celui que vous voulez. Raye
  rétrécit une partition pour faire de la place. Choisissez la partition
  de Windows, puis tirez la barre du bas pour décider ce que Windows garde
  et ce que Raye reçoit.
- **Replace a partition** (remplacer une partition) - met Raye à la place
  d'une partition et efface ce qu'elle contenait.

Vous ne pouvez pas découper les partitions à la main ici : cet
installateur ne le propose pas. Si la disposition dont vous avez besoin
n'est pas l'un de ces trois choix, Raye ne sait pas encore la faire.

Raye utilise la partition EFI que Windows a déjà créée au lieu d'en
ajouter une. Le rétrécissement, lui, réécrit bien la taille de la
partition Windows - c'est toute la raison pour laquelle Windows doit
avoir été arrêté correctement d'abord.

## Ensuite

Avec deux systèmes sur l'ordinateur, un menu s'affiche **dix secondes** à
chaque démarrage, avec Raye et Windows. Choisissez, ou attendez et Raye
démarre. Avec Raye seul, ce menu reste caché : c'est pourquoi vous ne
l'avez peut-être jamais vu.

Depuis Raye, **Redémarrer sur Windows** dans le menu Démarrer redémarre
directement sur Windows, cette fois-là seulement, sans le menu.

Pour le mot de passe du disque et la clé de récupération, voir
[Sécurité](05-securite.md).

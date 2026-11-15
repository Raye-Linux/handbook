# Installer Raye Linux

## Ce qu'il vous faut

- Un PC 64 bits (Intel ou AMD) qui démarre en mode UEFI, 4 Go de mémoire
  (8 Go conseillés) et 25 Go d'espace libre.
- Une clé USB de 8 Go ou plus. Tout ce qu'elle contient sera effacé.
- Une vingtaine de minutes, et une sauvegarde de vos fichiers importants :
  l'installation peut effacer le disque choisi.

## 1. Télécharger l'image

Téléchargez l'image de Raye (le fichier `.iso`, environ 2,9 Go) sur
rayelinux.com. Pour être sûr que le téléchargement est complet, sa taille
doit correspondre à celle de la page de téléchargement, et son SHA-256 à
celui qui y est indiqué.

## 2. Préparer la clé USB

Copier le fichier sur la clé ne suffit pas : un outil doit la rendre
démarrable.

- **Sous Windows :** Rufus (rufus.ie). Choisissez la clé sous Périphérique,
  cliquez sur SÉLECTION et choisissez l'image, cliquez sur DÉMARRER, puis
  choisissez **le mode DD** quand il le demande. Attendez « PRÊT ».
- **Sous Windows, Mac ou Linux :** balenaEtcher. Flash from file (l'image),
  Select target (la clé), Flash. Sous Windows, si ça échoue, faites un clic
  droit dessus et lancez-le avec tous les droits.
- **Sous Linux Mint :** clic droit sur l'image, « Créer une clé USB
  démarrable ». Fedora Media Writer et GNOME Disques (« Restaurer l'image
  disque ») fonctionnent aussi.
- Ventoy n'est pas encore testé. Il peut fonctionner (avec le Secure Boot,
  il demande une fois d'enregistrer sa clé), mais Rufus en mode DD reste le
  plus sûr.

Si l'outil dit que l'écriture a échoué, essayez un autre port USB, lancez
l'outil avec tous les droits, ou prenez une autre clé : les clés sans marque
échouent souvent sur les gros fichiers.

## 3. Démarrer sur la clé

Branchez la clé, redémarrez, et ouvrez le menu de démarrage de l'ordinateur
dès qu'il s'allume. La touche dépend de la marque : F12 (Dell, Lenovo, Acer),
F9 (HP, puis choisissez le périphérique USB), F8 (ASUS), F11 (MSI) ou Échap.
Choisissez la clé USB, l'entrée UEFI s'il y en a deux.

Raye démarre avec le Secure Boot activé, vous n'avez rien à changer dans les
réglages de l'ordinateur.

La clé affiche un menu : **Install Raye Linux** (anglais), **Installer Raye
Linux** (français) et **Safe graphics**. Essayer Raye sans l'installer n'est
pas encore possible : ça arrive dans une prochaine mise à jour.

## 4. Les étapes de l'installation

1. **Région** : votre langue et votre clavier.
2. **Réseau** : si l'ordinateur n'est pas branché par câble, choisissez votre
   Wi-Fi. Raye s'en sert pour régler l'heure et le fuseau tout seul.
3. **Disque** : choisissez le disque, puis comment Raye l'utilise.
   - **Installer à côté de Windows** : Raye prend une partie de l'espace
     libre et garde Windows. À chaque démarrage, vous choisissez lequel.
   - **Effacer ce disque** : Raye est seul sur ce disque. Tout ce qu'il
     contient est supprimé.
   - **Chiffrer Raye avec un mot de passe** protège vos fichiers si
     l'ordinateur est volé.
   Lisez le résumé en bas : il montre ce que chaque système obtiendra.
4. **Compte** : votre nom, un identifiant et un mot de passe. Vous pouvez
   aussi vous connecter à un compte Raye (facultatif) pour synchroniser vos
   réglages.
5. **Confidentialité** : vos choix, tous désactivés par défaut.
6. **Installation** : une dizaine de minutes.

À la fin, redémarrez et retirez la clé quand l'écran vous le demande.
L'ordinateur démarre alors sur Raye.

## En cas de problème

- **Écran noir** au démarrage de la clé : choisissez **Safe graphics** dans
  son menu. Si l'écran devient noir après l'installation : à l'allumage,
  appuyez sur Échap jusqu'au menu Raye, choisissez **Raye Linux (safe
  graphics)** s'il est là, ou appuyez sur `e`, ajoutez `nomodeset` après
  `quiet splash` et appuyez sur F10. Certaines cartes graphiques AMD plus
  anciennes sont concernées ; un correctif arrive.
- **« you need to load the kernel first »** : retéléchargez l'image (la
  version corrigée date du 15 novembre) et réécrivez la clé.
- **La clé n'apparaît pas dans le menu de démarrage** : réécrivez-la en mode
  DD, essayez un autre port USB, et vérifiez que l'ordinateur démarre en
  mode UEFI.
- Toujours bloqué ? Demandez sur le Discord de Raye Linux, dans #help, avec
  le modèle de votre ordinateur et une photo de l'écran.

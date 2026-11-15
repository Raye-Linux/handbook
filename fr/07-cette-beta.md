# Ce que cette bêta fait encore mal

La liste ci-dessous est la liste complète, dans l'ordre où les notes de
version la donnent. Elle est ici parce que c'est la page qu'on ouvre quand
quelque chose ne marche pas, et trouver son problème déjà écrit est plus
rapide que de le signaler.

<a id="known-1"></a>
**L'écran devient noir un instant avant l'écran de connexion.** Pendant 3
à 5 secondes, entre l'image de Raye et l'écran de connexion. Rien n'est
cassé : attendez, l'écran de connexion arrive.

<a id="known-2"></a>
**Quelques applis n'ont pas l'allure de Raye.** Le terminal, l'outil de
capture et certaines boîtes de dialogue portent les couleurs de Raye mais
ne sont pas encore redessinés.

<a id="known-3"></a>
**Le menu Démarrer et la barre des tâches sont proches de Windows 11, pas
identiques.** Le champ de recherche et la section Recommandé sont les
parties qui manquent encore.

<a id="known-4"></a>
**Les écrans de connexion et de verrouillage ne s'accordent pas sur votre
image.** L'image de compte par défaut n'est pas la même des deux côtés. Un
bouton **OK** isolé s'affiche aussi sous « Mot de passe incorrect ».

<a id="known-5"></a>
**Tous les programmes Windows ne fonctionnent pas.** Le premier que vous
ouvrez après l'installation prend du temps, certains installateurs
montrent une fenêtre grise à l'ancienne, et certains programmes ne
démarrent pas du tout. Quand un programme existe aussi pour Raye - 
Discord, Steam - installez-le plutôt depuis le Raye Store ; voir
[Les programmes Windows](04-programmes-windows.md).

<a id="known-6"></a>
**Les polices de Microsoft arrivent plus tard.** Arial, Times New Roman
et Verdana sont à Microsoft, donc l'image ne les emporte pas : Raye les
télécharge en arrière-plan la première fois que le PC est en ligne
après l'installation, avec les bibliothèques Visual C++, et les met dans
chaque espace Windows. Un programme ouvert avant utilise les polices du
système, et son texte peut sortir dans une autre fonte, ou à une taille
qui déborde de son cadre.

<a id="known-7"></a>
**Les jeux en 3D n'ont presque pas été essayés.** Les programmes
Windows dessinent maintenant par Vulkan, mais le seul jeu joué jusqu'ici
est un vieux jeu Direct3D 9, Chocolate Doom. Aucun jeu Direct3D 11 ou 12
n'a été essayé sur une vraie carte graphique : on ne sait pas encore
s'ils tournent bien.

<a id="known-8"></a>
**Les programmes faits en .NET n'ont presque pas été essayés.** Raye
apporte maintenant .NET et le moteur web que certains programmes
embarquent, mais un seul de ces programmes a été testé. L'installateur
de Paint.NET passe maintenant sa vérification de la carte graphique,
puis s'arrête sur une erreur de sortie des couleurs. Rien n'a encore été
essayé sur une vraie carte graphique.

<a id="known-9"></a>
**Roblox Studio ne permet pas encore de se connecter depuis sa propre
fenêtre.** Ce qu'on tape n'arrive pas à sa page de connexion. Passez par
Login via Browser, qui ouvre la page dans votre navigateur.

<a id="known-10"></a>
**Les mises à jour ont besoin d'Internet avant de pouvoir dire quoi que ce
soit.** Raye cherche ses propres paquets sur rayelinux.com et sur GitHub.
Tant que vous n'êtes pas connecté, les Paramètres indiquent que la
recherche n'a pas pu se faire : c'est exact, ce n'est pas une panne.

<a id="known-11"></a>
**Rien n'a été mesuré face à Windows sur un vrai ordinateur.** Si vous
lisez quelque part que Raye est plus rapide ou plus lent, personne ne l'a
encore pesé.

<a id="known-12"></a>
**`add-apt-repository -c` et `-p` peuvent casser la source des paquets de
Raye.** Ils risquent de la choisir et de la réécrire ; `apt` répond alors
404 pour les paquets Raye, et comme le fichier appartient à un paquet, il
est remplacé à la mise à jour suivante. Ajoutez un PPA avec
`add-apt-repository ppa:...` tout court, qui écrit son propre fichier. Si
c'est déjà arrivé : `sudo apt install --reinstall raye-archive-keyring`.

<a id="known-13"></a>
**Les paquets source sont déclarés mais éteints**, pour qu'`apt update` ne
télécharge pas 18 Mo d'index de sources sur chaque ordinateur. Pour
compiler un paquet depuis ses sources, allumez-les d'abord :
`sudo sed -i 's/^Enabled: no$/Enabled: yes/' /etc/apt/sources.list.d/ubuntu.sources && sudo apt update`.

<a id="known-14"></a>
**Le liseré autour de l'élément actif est peu visible**, sur quelques
surfaces sombres et davantage avec une couleur d'accent très claire ou
très foncée. Le texte et les commandes gardent leur contraste ; c'est le
fin anneau de focus qui n'atteint pas toujours le 3:1 qu'attend quelqu'un
qui navigue au clavier.

## Et une page de l'installation n'existe qu'en anglais

Tous les écrans de l'installation sont traduits, sauf celui où vous
choisissez le disque. Cette page vient de l'installateur sur lequel Raye
s'appuie, et cette image n'en porte aucune traduction française : elle
s'affiche en anglais même si vous avez choisi le français. C'est aussi la
page où un mauvais clic coûte le plus cher, donc
[Installer à côté de Windows](09-windows-a-cote.md) nomme ses boutons.

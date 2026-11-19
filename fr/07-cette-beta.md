# Ce que cette bêta fait encore mal

La liste ci-dessous est la liste complète, dans l'ordre où les notes de
version la donnent. Elle est ici parce que c'est la page qu'on ouvre quand
quelque chose ne marche pas, et trouver son problème déjà écrit est plus
rapide que de le signaler.

<a id="known-1"></a>
**Les anciennes cartes AMD peuvent démarrer en basse résolution.** Certaines
cartes des séries RX 400 et 500 affichent une basse résolution avec peu
d'images par seconde sur certains PC. Quand le bureau ne s'affiche pas deux
fois de suite, Raye passe tout seul à un mode d'affichage plus simple, ce qui
aide certaines cartes mais pas toutes. Si cela vous arrive, dites-le dans
#bugs sur Discord : l'équipe y travaille encore.

<a id="known-2"></a>
**Pas de noyau Raye avec le pilote NVIDIA.** Les modules précompilés de
NVIDIA ne se chargent qu'avec le noyau standard : Paramètres ne propose donc
pas le noyau Raye sur un PC qui les utilise, et dit pourquoi.

<a id="known-3"></a>
**L'appli Carte graphique est nouvelle.** Sa courbe de ventilateur et sa
limite de puissance ont été vérifiées sur des données de test, pas encore
sur chaque génération de carte AMD. Rétablir les valeurs par défaut remet
la carte comme elle était.

<a id="known-4"></a>
**Tous les programmes Windows ne fonctionnent pas.** Les applis faites
uniquement pour le Microsoft Store ne peuvent pas fonctionner du tout. Les
programmes qui existent aussi pour Raye (Discord, Steam) s'installent mieux
depuis le Raye Store.

<a id="known-5"></a>
**Les alarmes ne sonnent que lorsque le PC est allumé.** Horloge ne peut pas
encore sortir le PC de la veille : une alarme manquée pendant la veille
s'affiche comme manquée au réveil.

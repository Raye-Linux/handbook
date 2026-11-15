# Les programmes Windows

Double-cliquez sur un fichier **.exe** ou **.msi** : il s'ouvre, comme sous
Windows. Rien à installer avant, aucune question.

- Chaque programme a **son propre espace** : un programme qui se comporte
  mal ne peut pas abîmer les autres.
- Deux minutes après votre première connexion, Raye prépare cet espace en
  arrière-plan : les couleurs de Raye, Inter à la place de Segoe UI,
  l'échelle de l'affichage, et vos propres dossiers Documents, Images,
  Musique, Vidéos et Téléchargements. Le raccourci qu'un programme pose
  sur le bureau atterrit dans l'espace, pas sur votre bureau : Raye lui
  fabrique son propre lanceur. Ensuite, un programme s'ouvre en une
  seconde ou deux.
- Un programme installé a son entrée dans Démarrer, et se désinstalle
  depuis **Paramètres → Applications → Applications installées**, comme
  n'importe quelle application.
- Quand un programme existe aussi pour Raye (Steam, Discord, OBS
  Studio…), Raye vous propose d'abord cette version : elle s'intègre mieux.
- Les polices et les bibliothèques Visual C++ de Microsoft sont
  téléchargées en arrière-plan dès que le PC est en ligne ; avant cela,
  certains textes s'affichent dans une autre police. Voir
  [Ce que cette bêta fait encore mal](07-cette-beta.md).

## Ce qui a été essayé

**Fonctionne :** 7-Zip et WinRAR s'installent d'un double-clic, s'ouvrent
depuis Démarrer et font leur travail. 7-Zip se désinstalle depuis les
Paramètres. Un jeu Direct3D 9 plus ancien, Chocolate Doom, tourne en
plein écran avec son son.

**Ne fonctionne pas, et c'est voulu :**

- Les jeux protégés par un anti-triche qui refuse ce système : Roblox,
  Fortnite, Valorant, plusieurs Battlefield, Call of Duty: Black Ops 7…
  C'est à leur éditeur d'autoriser Linux. Quand vous double-cliquez sur
  l'installateur de Roblox, Raye le dit et n'installe rien. Raye ne
  contourne jamais un anti-triche : cela ferait bannir votre compte.
- Le lanceur Windows de Minecraft et l'édition Bedrock exigent le
  Microsoft Store. Raye le dit et ouvre plutôt dans le Store le lanceur de
  Minecraft Java Edition.

**Ne fonctionne pas encore :** Roblox Studio s'installe et ouvre sa page
de connexion, mais cette page ne prend pas ce que vous tapez.

**Pas encore essayé :** les jeux 3D exigeants (Direct3D 11 et 12) sur une
vraie carte graphique. Pour les jeux achetés sur Steam, passez par
**Steam** dans le Store.

Pour les logiciels de création, essayez **ArtCraft** dans le Store : des
applis libres pour la photo, l'illustration, la vidéo et le PDF.

Pour faire de la place : **Paramètres → Jeux** liste les programmes Windows
et permet d'effacer leur espace.

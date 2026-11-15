# Ce que Raye ne fait pas (encore)

Quelques fonctions de Windows n'ont pas d'équivalent dans Raye. Plutôt
qu'un bouton qui ne fait rien, les Paramètres affichent **Non disponible
sur Raye** et renvoient ici. Chaque partie dit ce que fait Windows,
pourquoi Raye ne le fait pas et quoi utiliser à la place.

<a id="voice-typing"></a>

## Saisie vocale

**Sous Windows :** Windows + H ouvre une barre avec un micro, et ce que
vous dites s'écrit là où se trouve le curseur. L'accès vocal va plus
loin et pilote tout le PC à la voix.

**Pourquoi pas sur Raye :** une bonne dictée demande un gros modèle de
reconnaissance vocale. Ceux qui tournent sur votre PC ne sont pas encore
assez bons dans toutes les langues pour être livrés avec le système, et
envoyer votre voix aux serveurs d'une entreprise n'est pas une chose que
Raye fait dans votre dos.

**À la place :**

- **Speech Note**, dans le Store, transforme la parole en texte sur
  votre PC, sans Internet. Parlez, puis copiez le texte là où vous en
  avez besoin.
- Le clavier de votre téléphone a un bouton micro. Dictez sur le
  téléphone, puis envoyez le texte au PC avec **Paramètres → Bluetooth et
  appareils → Téléphone** (presse-papiers partagé).

<a id="dynamic-lighting"></a>

## Éclairage dynamique

**Sous Windows :** Paramètres → Personnalisation → Éclairage dynamique
règle au même endroit la couleur et les effets des claviers, souris et
boîtiers RGB.

**Pourquoi pas sur Raye :** chaque marque pilote ses lumières à sa
façon, et Raye n'a pas de moyen commun de toutes les atteindre depuis
les Paramètres.

**À la place :** **OpenRGB**, dans le Store, pilote les lumières de la
plupart des claviers, souris, barrettes de mémoire, cartes graphiques et
cartes mères. S'il ne trouve pas vos appareils, redémarrez le PC une
fois après l'avoir installé.

<a id="cast"></a>

## Caster vers un écran sans fil

**Sous Windows :** Windows + K cherche les téléviseurs et les écrans
compatibles Miracast et y affiche votre écran, sans câble.

**Pourquoi pas sur Raye :** l'affichage sans fil ne marche pas encore
assez bien sous Linux : beaucoup de téléviseurs ne sont pas trouvés ou
l'image coupe.

**À la place :**

- Branchez l'écran avec un câble **HDMI** ou **USB-C**, puis appuyez
  sur **Windows + P** pour choisir Dupliquer ou Étendre.
- Pour une vidéo ou une page web, un navigateur qui sait caster, comme
  **Google Chrome** dans le Store, l'envoie vers un téléviseur avec
  Chromecast ou Google TV.

<a id="quick-assist"></a>

## Assistance rapide

**Sous Windows :** l'Assistance rapide permet à un proche de voir et de
piloter votre PC par Internet, une fois que vous lui avez donné un code
court.

**Pourquoi pas sur Raye :** un tel code ne marche qu'en passant par un
service sur Internet qui met les deux ordinateurs en contact. Raye ne
fait pas tourner ce genre de service.

**À la place :**

- Dans la même maison ou le même bureau, utilisez **Paramètres →
  Système → Bureau à distance**.
- Par Internet, les deux personnes peuvent installer la même appli
  d'aide à distance depuis le Store, comme **RustDesk**, et suivre ses
  étapes.

Ne laissez piloter votre PC que par quelqu'un que vous connaissez et en
qui vous avez confiance. Microsoft, votre banque et Raye ne vous
appellent jamais pour demander un accès à distance.

## Autres fonctions de Windows absentes de Raye

| Sous Windows | Sur Raye |
|---|---|
| Sous-titres en direct | Non disponible. Les vidéos dans Firefox ont souvent leurs propres sous-titres. |
| Localiser mon appareil | Non disponible : cela passe par un compte Microsoft et les serveurs de Microsoft. |
| Comptes Famille et contrôle parental de Microsoft | Non disponible. Créez un compte standard pour chaque enfant dans **Paramètres → Comptes → Autres utilisateurs**. |
| Sauvegarde Windows vers OneDrive | Non disponible. **Paramètres → Système → Récupération** peut ramener le système à un état antérieur, mais n'enregistre pas vos fichiers : copiez-les sur une clé USB ou dans une appli de stockage en ligne. |

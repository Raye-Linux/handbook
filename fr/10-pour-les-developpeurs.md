# Pour les développeurs

**Paramètres → Système → Avancé** se termine par une section
**Pour les développeurs**. Rien n'y est activé tant que vous ne l'activez
pas.

- Le **Mode développeur** donne accès au reste. À partir de votre
  prochaine connexion, les applications de Raye écrivent aussi des
  journaux détaillés. Le désactiver éteint le portail d'appareil.
- Le **Portail d'appareil** permet de gérer ce PC depuis un navigateur sur
  le même réseau. Voir plus bas.
- La **Découverte d'appareil** permet aux appareils du réseau de trouver
  le portail par le nom de ce PC.
- Le **Serveur OpenSSH** permet de se connecter à ce PC depuis un autre
  ordinateur avec `ssh`. **Connexion par clé uniquement** est activé par
  défaut : les mots de passe sont refusés, alors placez votre clé publique
  dans `~/.ssh/authorized_keys` avant de vous connecter.

## Le portail d'appareil

1. Activez le **Mode développeur**, puis le **Portail d'appareil**.
2. Les Paramètres affichent l'**Adresse**, par exemple
   `https://192.168.1.20:50443`, et l'**Empreinte du certificat**.
3. Ouvrez cette adresse dans un navigateur, sur un autre appareil du même
   réseau. Le navigateur met en garde la première fois : continuez
   seulement s'il affiche la même empreinte.
4. Connectez-vous avec le nom d'utilisateur et le mot de passe choisis
   avec **Définir** dans les Paramètres, ou choisissez
   **Appairer un appareil** : les Paramètres affichent un code qui ne sert
   qu'une fois, pendant 10 minutes, et ce navigateur reste ensuite appairé
   30 jours.

Le portail montre le PC d'un coup d'œil : performances, processus,
applications, journaux, réseau, et les fichiers de votre dossier
personnel, que vous pouvez télécharger et compléter. Il ne répond qu'aux
appareils des réseaux où ce PC est branché, et après cinq essais ratés,
un appareil doit attendre 15 minutes. Les Paramètres gardent un
**Journal des connexions** de qui est venu.

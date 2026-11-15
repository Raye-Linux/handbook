# Sécurité : chiffrement, clé de récupération, démarrage

## Le disque chiffré

Si vous avez coché **Chiffrer le système** à l'installation, tout le disque
est chiffré : sans le mot de passe, un ordinateur volé ne livre rien.

Sur la plupart des ordinateurs récents, la **puce de sécurité** (TPM) ouvre
le disque toute seule au démarrage, et vous n'entrez que votre mot de passe
de session. Si la puce ne répond pas (mise à jour du micrologiciel, disque
déplacé dans un autre ordinateur), l'écran de démarrage demande le mot de
passe du disque.

## La clé de récupération

L'installation crée une **clé de récupération** : huit groupes de six
chiffres, affichés par la fenêtre qui s'ouvre à votre première connexion.
Raye la garde dans **.local/share/raye/recovery-key**, dans votre dossier
personnel. Elle ouvre le disque si vous oubliez son mot de passe : tapez-la
à la place du mot de passe, à l'écran de démarrage.

**Notez-la** sur papier ou dans un gestionnaire de mots de passe, rangez-la
ailleurs que dans l'ordinateur, puis **supprimez le fichier**.
**Paramètres → Confidentialité et sécurité → Sécurité de l'appareil** vous
le rappelle tant que le fichier est là.

## Si l'ordinateur plante

L'écran devient violet et l'œil Raye s'affiche : vos fichiers sont en
sécurité et l'ordinateur redémarre seul après 30 secondes.

## Le noyau Raye (facultatif)

**Paramètres → Pilotes → Noyau Raye** propose le même noyau, avec l'écran de
plantage Raye. Avec le démarrage sécurisé, il faut enregistrer la clé Raye
une fois : au redémarrage, un écran bleu apparaît. Appuyez sur une touche
**dans les 10 secondes**, choisissez **Enroll MOK**, **Continue**, **Yes**,
tapez le code à 6 chiffres affiché par Paramètres, puis **Reboot**. Le noyau
d'origine reste installé en secours.

## Démarrer sur Windows

Si Windows est installé à côté, **Redémarrer sur Windows** dans le menu
redémarre directement dessus, une seule fois.

## Root et sudo

Les changements qui touchent tout le système (installer pour tout le
monde, le pare-feu, le menu de démarrage) s'exécutent en tant que
**root**, le compte du système. Raye demande d'abord : une fenêtre nomme
le programme et demande un mot de passe.

- Un **utilisateur sudo** tape son propre mot de passe. Le compte créé à
  l'installation en est un.
- Un **utilisateur standard** ne peut pas faire ces changements seul : la
  fenêtre demande le mot de passe d'un utilisateur sudo du PC.

**Paramètres → Comptes → Autres utilisateurs → Type de compte** passe de
l'un à l'autre.

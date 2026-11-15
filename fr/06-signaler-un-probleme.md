# Signaler un problème

C'est une version bêta : la chose la plus utile que vous puissiez en
faire, c'est dire ce qui a mal tourné. Deux portes, lues toutes les deux :

- un ticket sur **https://github.com/Raye-Linux/releases/issues**
- un courriel à **bonjour@rayelinux.com**

## Quoi écrire

Quatre lignes suffisent, et ce sont les quatre qui évitent un
aller-retour :

1. quel ordinateur vous avez,
2. ce que vous avez fait,
3. ce que vous attendiez,
4. ce qui s'est passé à la place.

Une photo de l'écran en dit plus qu'un paragraphe. Prenez-la avec votre
téléphone si l'ordinateur est bloqué.

## Les deux blocs à coller

**Paramètres → Système → Informations système** a un bouton **Copier** à
côté de chacun de ses deux blocs. Le premier copie l'ordinateur :
processeur, mémoire, carte graphique, stockage, modèle. Le second copie le
côté Raye, dont la ligne **Version**, qui dit exactement sur quelle
version vous êtes. Collez les deux dans le signalement et personne n'aura
besoin de demander.

## Après l'écran violet

Quand l'écran devient violet et que l'ordinateur redémarre seul, Raye en
écrit un compte rendu. La notification qui suit a un bouton **Détails**
qui l'ouvre ; il est aussi dans
`~/.local/share/raye/crash-reports/`, un fichier texte par redémarrage,
nommé d'après la date et l'heure. Joignez le plus récent.

Les détails de certains problèmes ne se lisent qu'en tant que root. La
notification le dit et donne le chemin quand c'est le cas.

## Si c'est l'installation qui a échoué

Une fois Raye installé, l'installation laisse son propre journal dans
`/var/log/installer/session.log`, lisible seulement en tant que root. Sur un
ordinateur où l'installation n'est jamais allée au bout, ce fichier
n'existe pas : notez ce qu'affichait le dernier écran, et à quelle étape.

## Une chose à ne pas envoyer

Rien ici ne demande de mot de passe, et rien ici ne demande votre **clé
de récupération**. Aucun compte rendu de Raye n'en contient. Si vous
copiez des fichiers de votre dossier personnel pour les joindre, laissez
`.local/share/raye/recovery-key` où il est - voir [Sécurité](05-securite.md).

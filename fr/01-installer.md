# Installer Raye Linux

Il vous faut une clé USB d'au moins 8 Go et 25 Go de libre sur
l'ordinateur. Tout ce qui est sur la clé sera effacé.

## 1. Préparer la clé

Téléchargez l'image de Raye (le fichier `.iso`), puis copiez-la sur la
clé avec un outil comme balenaEtcher ou Rufus (mode « image DD »). Ce
n'est pas un simple copier-coller : l'outil rend la clé démarrable.

## 2. Démarrer sur la clé

Branchez la clé, redémarrez, et ouvrez le menu de démarrage de votre
ordinateur. La touche dépend de la marque : souvent F12 (Dell, Lenovo),
F9 (HP), F8 (ASUS) ou Échap. Choisissez la clé USB.

Raye démarre avec le Secure Boot activé, vous n'avez rien à changer
dans les réglages de l'ordinateur.

## 3. Installer

La clé lance l'installation. Essayer Raye sans l'installer n'est pas
encore possible : ça arrive dans une prochaine mise à jour.

## 4. Les étapes de l'installation

1. **Wi-Fi** : si l'ordinateur n'est pas branché par câble, choisissez
   votre réseau. Raye s'en sert pour régler l'heure toute seule.
2. **Langue** et **clavier**.
3. **Fuseau horaire** : déjà rempli si vous êtes connecté.
4. **Disque** : « Effacer le disque » installe Raye seul sur
   l'ordinateur. Cochez « Chiffrer » pour protéger vos fichiers par un
   mot de passe si l'ordinateur est volé.
5. **Votre compte** : votre nom, votre identifiant et un mot de passe.

Comptez une dizaine de minutes. À la fin, redémarrez : l'ordinateur
démarre directement sur Raye, même si la clé est encore branchée. Vous
pouvez la retirer.

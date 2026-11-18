# Pages légales

Chaque dossier de site contient sa politique de confidentialité, ses mentions légales, le logo et une feuille de style commune aux deux pages. Les fichiers HTML sont autonomes : ils ne nécessitent ni WordPress, ni Webflow, ni JavaScript pour afficher leur contenu.

| Site | Mentions légales | Politique de confidentialité |
|---|---|---|
| ComparateurPro | [HTML](comparateurpro.fr/mentions-legales.html) | [HTML](comparateurpro.fr/politique-de-confidentialite-donnees-personnelles.html) |
| HelloDevis | [HTML](hellodevis.fr/mentions-legales.html) | [HTML](hellodevis.fr/politique-de-confidentialite-donnees-personnelles.html) |
| Ubepro | [HTML](ubepro.fr/mentions-legales.html) | [HTML](ubepro.fr/politique-de-confidentialite-donnees-personnelles.html) |

## Mettre à jour les fichiers

Modifier les sources dans `modeles/` et les paramètres par site dans `outils/generer-pages-legales.py`, puis régénérer les six pages et leurs feuilles de style :

```sh
python3 outils/generer-pages-legales.py
python3 outils/generer-pages-legales.py --check
```

La deuxième commande vérifie que les fichiers livrés correspondent aux modèles, sans modifier le dépôt. Aucun paquet Python externe n’est nécessaire. Pour vérifier une page en local, ouvrir le fichier HTML dans un navigateur en gardant le CSS et le logo dans le même dossier.

## Avant la mise en ligne

- Les exemples fournis sont des exports WordPress qui affichent en iframe les [mentions légales](https://www.hellodevis.fr/mentions-legales/) et la [politique de confidentialité](https://www.hellodevis.fr/politique-de-confidentialite-donnees-personnelles/) de HelloDevis. Les pages livrées reprennent leur organisation, pas les dépendances WordPress.
- Valider les adresses de contact et les coordonnées de l’hébergeur du **site**, distinct de la conservation des données. Pour HelloDevis, Plug & Tel est mentionné comme prestataire historique à confirmer ; la politique de référence indique OVH pour la conservation des données personnelles.
- En cas d’intégration CMS, adapter les chemins du logo, du CSS et des liens aux URL réelles. Les exports HTML statiques ne remplacent pas la configuration du CMS, sa gestion du consentement ou les scripts du reste du site.

Voir le [rapport de vérification](rapport-confidentialite.md) pour le détail et l’ancien paragraphe conservé pour un éventuel retour arrière.

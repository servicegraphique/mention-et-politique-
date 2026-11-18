# Rapport — Pages légales, 18 novembre 2026

Les deux exemples fournis sont des enveloppes WordPress. Leur contenu est chargé depuis les [mentions légales](https://www.hellodevis.fr/mentions-legales/) et la [politique de confidentialité](https://www.hellodevis.fr/politique-de-confidentialite-donnees-personnelles/) de HelloDevis. Les fichiers du dépôt reprennent l’organisation de ces pages, sans recopier les iframes ni les dépendances des exports.

| Site | Mentions légales | Politique de confidentialité | Publié |
|---|---|---|---|
| ComparateurPro | [Optimisées](comparateurpro.fr/mentions-legales.html) | [Optimisée](comparateurpro.fr/politique-de-confidentialite-donnees-personnelles.html) | Non |
| HelloDevis | [Optimisées](hellodevis.fr/mentions-legales.html) | [Créée à partir de la page chargée par l’exemple](hellodevis.fr/politique-de-confidentialite-donnees-personnelles.html) | Non |
| Ubepro | [Optimisées](ubepro.fr/mentions-legales.html) | [Optimisée](ubepro.fr/politique-de-confidentialite-donnees-personnelles.html) | Non |

## Corrections et vérifications

- Les six pages ont un sommaire cliquable, des rubriques numérotées, les coordonnées et le logo du bon site. Les liens de confidentialité Twilio et de désactivation Google Analytics ont été corrigés. Les deux paragraphes B2C et B2B restent **mot pour mot** ceux fournis, chacun sous un H3. Aucune référence à Bloctel ne figure dans les fichiers HTML.
- Les fichiers livrés pèsent **46 % de moins** (HTML et CSS hors logos : 203 600 → 109 583 octets), malgré l’ajout d’une sixième page. Au chargement, chaque page ne demande que son CSS et son logo, tous deux locaux. Les [modèles partagés](modeles/) évitent de recopier les changements entre sites.
- Validation HTML5 et contrôle Chromium à **320, 390, 768 et 1 440 px** : logos et navigation chargés, aucune section ne déborde, sommaire et lien d’accès au contenu fonctionnels. L’analyse automatisée axe n’a signalé aucune violation dans les règles WCAG 2.1 A/AA testées à 390 et 1 440 px.
- **Avant publication :** confirmer l’hébergeur web et les contacts. Pour HelloDevis, Plug & Tel figure dans les [mentions spécifiques indexées](https://hellodevis.fr/mentions-legales/) ; OVH est indiqué pour la conservation des données personnelles dans la politique de référence. La page distingue ces deux informations au lieu de présumer qu’elles désignent le même hébergement.

## Historique de la recherche Bloctel

La première vérification a trouvé le même ancien paragraphe dans les exports ComparateurPro et Ubepro et une version indexée pour HelloDevis. Elle n’a pas révélé d’autre occurrence dans les fichiers et pages consultables. Le [formulaire Fiat Pro](https://www.ubepro.fr/fiat-pro/) et sa [politique partenaire Stellantis](https://www.ubepro.fr/fiat-politique-de-confidentialite/) sont distincts et n’ont pas été modifiés. La recherche n’était pas exhaustive : certaines pages publiques, dont Ubepro Sécu, étaient inaccessibles.

### Ancien texte — pour un retour arrière

**ComparateurPro et Ubepro — texte identique dans les deux exports :**

> Par ailleurs, les utilisateurs du site sont informés, en application de l’article Article L121-34 du code de la consommation tel que modifié par la loi n° 2014-344 du 17 mars 2014 dite loi Hamon sur la consommation en son article 9, de la possibilité d’inscrire leur numéro de téléphone sur une liste d’opposition au démarchage téléphonique en dehors des cas de relations contractuelles préexistantes. Ce service est disponible à l’adresse [http://www.bloctel.gouv.fr](http://www.bloctel.gouv.fr/).

**HelloDevis — extraits de l’ancienne version indexée [1](https://hellodevis.fr/politique-de-confidentialite-donnees-personnelles/) ; le balisage et les sauts de ligne d’origine n’ont pas pu être vérifiés :**

> Par ailleurs, les utilisateurs du site sont informés, en application de l’article Article L121-34 du code de la consommation tel que modifié par la loi n° 2014-344 du 17 mars 2014 dite loi Hamon sur la consommation en son article 9, de la possibilité d’inscrire leur numéro de téléphone sur une liste d’opposition au démarchage téléphonique en dehors des cas de relations contractuelles préexistantes.

> Ce service est disponible à l’adresse http://www.bloctel.gouv.fr.

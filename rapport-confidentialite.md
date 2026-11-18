# Politique de confidentialité et mentions légales — 18 novembre 2026

La colonne « Publié » indique si **les changements de cette branche** ont été mis en ligne. Les trois URL publiques de la politique sont accessibles ; elles affichent déjà une section « Prospection téléphonique » sans renvoi vers Bloctel, dans une version différente des exports du dépôt.

| Site | URL modifiée | Paragraphe remplacé | Autres occurrences de « Bloctel » trouvées | Publié | Remarques |
|---|---|---|---|---|---|
| ComparateurPro | [HTML modifié](comparateurpro.fr/politique-de-confidentialite-donnees-personnelles.html) · [URL publique](https://www.comparateurpro.fr/politique-de-confidentialite-donnees-personnelles/) | Oui, dans le dépôt | Aucune autre repérée | Non | Les deux H3 reprennent la classe des titres voisins. |
| HelloDevis | [URL publique](https://www.hellodevis.fr/politique-de-confidentialite-donnees-personnelles/), non modifiée | Non | Ancien renvoi retrouvé dans l’index de recherche de cette même politique ; aucune autre occurrence repérée | Non | Aucun fichier source de la politique dans le dépôt. La page publique consultée ne contient pas le bloc à remplacer. |
| Ubepro | [HTML modifié](ubepro.fr/politique-de-confidentialite-donnees-personnelles.html) · [URL publique](https://www.ubepro.fr/politique-de-confidentialite-donnees-personnelles/) | Oui, dans le dépôt | Aucune autre repérée | Non | Les deux H3 reprennent la classe et la graisse des titres voisins. |

## Vérifications

- Comme sur [HelloLead](https://www.hellolead.pro/politique-de-confidentialite-donnees-personnelles/), les blocs B2C et B2B se trouvent après les droits de l’utilisateur et avant « Nous contacter ». Le diff confirme que seul l’ancien bloc a été remplacé dans les deux politiques HTML. Le reste du contenu, des liens et des métadonnées est inchangé.
- Chromium : blocs visibles et sans débordement à 1 440, 390 et 320 px ; mise en page identique hors du bloc, à l’exception du décalage vertical attendu de ce qui suit. Les feuilles Webflow d’origine ne sont pas fournies dans le dépôt : le rendu graphique de production reste à valider.
- Aucun doublon desktop/mobile ou de landing page dans les fichiers fournis. Le [formulaire Fiat Pro](https://www.ubepro.fr/fiat-pro/) renvoie à la politique générale en pied de page et à une [politique partenaire Stellantis](https://www.ubepro.fr/fiat-politique-de-confidentialite/) distincte dans le formulaire ; ces deux pages n’ont pas été modifiées. La recherche a porté sur les fichiers du dépôt et les pages publiques consultables ou indexées. Sans sitemap et avec certaines pages inaccessibles (dont Ubepro Sécu), elle ne garantit pas une couverture exhaustive des sites.

## Mentions légales

Trois pages ont été préparées, sur le modèle des [mentions légales de HelloLead](https://www.hellolead.pro/mentions-legales/) : [ComparateurPro](comparateurpro.fr/mentions-legales.html), [HelloDevis](hellodevis.fr/mentions-legales.html) et [Ubepro](ubepro.fr/mentions-legales.html). Elles reprennent les rubriques Éditeur, Marques, Hébergement et Contact, les logos du dépôt et les liens propres à chaque site. Logos, sommaire et mise en page ont été vérifiés localement aux trois largeurs. Elles n’ont pas été publiées.

**À confirmer avant publication pour HelloDevis :** les mentions spécifiques indexées indiquent Plug & Tel [2](https://hellodevis.fr/mentions-legales/), tandis que l’URL publique consultée reprend le contenu de HelloLead, qui indique OVH. La page préparée reprend Plug & Tel sans présenter ce point comme vérifié pour la version actuelle.

## Ancien texte — pour un retour arrière

**ComparateurPro et Ubepro — texte identique dans les deux exports :**

> Par ailleurs, les utilisateurs du site sont informés, en application de l’article Article L121-34 du code de la consommation tel que modifié par la loi n° 2014-344 du 17 mars 2014 dite loi Hamon sur la consommation en son article 9, de la possibilité d’inscrire leur numéro de téléphone sur une liste d’opposition au démarchage téléphonique en dehors des cas de relations contractuelles préexistantes. Ce service est disponible à l’adresse [http://www.bloctel.gouv.fr](http://www.bloctel.gouv.fr/).

**HelloDevis — extraits de l’ancienne version indexée [1](https://hellodevis.fr/politique-de-confidentialite-donnees-personnelles/) ; le balisage et les sauts de ligne d’origine n’ont pas pu être vérifiés :**

> Par ailleurs, les utilisateurs du site sont informés, en application de l’article Article L121-34 du code de la consommation tel que modifié par la loi n° 2014-344 du 17 mars 2014 dite loi Hamon sur la consommation en son article 9, de la possibilité d’inscrire leur numéro de téléphone sur une liste d’opposition au démarchage téléphonique en dehors des cas de relations contractuelles préexistantes.

> Ce service est disponible à l’adresse http://www.bloctel.gouv.fr.

Pour terminer HelloDevis sans réécrire le reste de la page, il faut la source qui fait foi (export du CMS, HTML ou Code Embed). Pour la mise en ligne, appliquer les changements dans les sources CMS/Webflow des pages publiques plutôt que remplacer leurs pages entières par les anciens exports.

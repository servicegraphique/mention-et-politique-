#!/usr/bin/env python3
"""Génère les deux pages HTML statiques et leur CSS pour chacun des trois sites."""

from argparse import ArgumentParser
from dataclasses import dataclass
from html import escape
from pathlib import Path
from string import Template
from textwrap import indent


ROOT = Path(__file__).resolve().parents[1]
MODELES = ROOT / 'modeles'
POLITIQUE = 'politique-de-confidentialite-donnees-personnelles.html'
MENTIONS = 'mentions-legales.html'
CSS = 'pages-legales.css'
DATE_ISO = '2026-11-18'
DATE_LONGUE = '18 novembre 2026'


@dataclass(frozen=True)
class Site:
    nom: str
    domaine: str
    theme: str
    logo: str
    largeur: int
    hauteur: int
    clients: str
    marques: tuple[str, ...]

    @property
    def url(self) -> str:
        return f'https://www.{self.domaine}/'

    @property
    def dpo(self) -> str:
        return f'dpo@{self.domaine}'


SITES = (
    Site('ComparateurPro', 'comparateurpro.fr', 'site-comparateurpro', 'logo_comparateurpro.png',
         2000, 431, 'de ComparateurPro', ('ComparateurPro', 'HelloLead')),
    Site('HelloDevis', 'hellodevis.fr', 'site-hellodevis', 'logo-hellodevis.png',
         274, 50, 'de Hellodevis', ('HelloLead', 'ComparateurPro', 'Ubepro')),
    Site('Ubepro', 'ubepro.fr', 'site-ubepro', 'logo-ubepro.png',
         800, 204, 'd’Ubepro', ('Ubepro', 'HelloLead')),
)

MARQUES = {
    'HelloLead': ('hellolead.pro', 'Marque commerciale dédiée à la mise en relation.'),
    'ComparateurPro': ('comparateurpro.fr', 'Recueil et gestion des demandes de devis et d’information.'),
    'Ubepro': ('ubepro.fr', 'Recueil et gestion des demandes de devis et d’information.'),
}

ADRESSE_OVH = '''<address>
  <strong>OVH</strong><br>
  ZI Les Huttes, route de la Ferme Masson<br>
  59820 Gravelines<br>
  Tél. <a href="tel:+33320192000">03 20 19 20 00</a> — <a href="https://www.ovhcloud.com/">ovhcloud.com</a>
</address>'''

# Cette adresse décrit l’ancien hébergeur du site HelloDevis, pas le lieu
# de conservation des données personnelles indiqué dans la politique actuelle.
ADRESSE_HISTORIQUE_HELLODEVIS = '''<h3>Hébergement du site HelloDevis</h3>
<p>Les anciennes mentions propres à HelloDevis indiquaient le prestataire ci-dessous. Ces coordonnées restent à confirmer avant publication.</p>
<address>
  <strong>Plug &amp; Tel</strong><br>
  8 rue des Champs Odés<br>
  78200 Buchelay<br>
  Tél. <a href="tel:+33172897101">01 72 89 71 01</a> — <a href="https://www.plugandtel.com/">plugandtel.com</a>
</address>'''

DESINSCRIPTION_HELLODEVIS = ('<p>Pour ne plus recevoir de courriels d’HelloLead, un '
                            '<a href="https://www.hellolead.pro/desinscription/">formulaire de désinscription</a> '
                            'est disponible sur ce site.</p>')


def lire_modele(nom: str) -> Template:
    return Template((MODELES / nom).read_text(encoding='utf-8'))


def lien_email(email: str) -> str:
    return f'<a href="mailto:{escape(email)}">{escape(email)}</a>'


def liste_contacts(site: Site) -> str:
    return f'''<dl class="detail-list">
  <dt>Données personnelles</dt>
  <dd>{lien_email(site.dpo)}</dd>
  <dt>Contact général</dt>
  <dd>{lien_email(f'contact@{site.domaine}')}</dd>
  <dt>Courrier</dt>
  <dd>Hellodevis, 5 avenue de la République, 75011 Paris</dd>
  <dt>Téléphone</dt>
  <dd><a href="tel:+33756986082">07 56 98 60 82</a></dd>
</dl>'''


def carte_marque(nom: str) -> str:
    domaine, description = MARQUES[nom]
    return f'''<div class="brand-card">
  <h3>{escape(nom)}</h3>
  <p>{escape(description)}</p>
  <p><a href="https://www.{escape(domaine)}/">www.{escape(domaine)}</a><br>
    {lien_email(f'contact@{domaine}')}</p>
</div>'''


def document(coque: Template, modele: Template, site: Site, politique: bool) -> str:
    est_hellodevis = site.domaine == 'hellodevis.fr'
    titre = 'Politique de confidentialité' if politique else 'Mentions légales'
    nom = escape(site.nom)
    editeur = ('Ce site est édité par la société <strong>Hellodevis</strong>.' if est_hellodevis else
               f'<strong>{nom}</strong> est une marque de la société <strong>Hellodevis</strong>, qui édite le présent site.')
    introduction = (
        f'Cette page décrit comment {nom} collecte, utilise et conserve vos données personnelles, et comment exercer '
        'vos droits au titre du règlement général sur la protection des données (règlement (UE) n°&nbsp;2016/679, RGPD).'
        if politique else
        f'Identité de l’éditeur, marques, conservation des données et coordonnées pour le site {nom}.'
    )
    resume = (
        ('Mise à jour', f'<time datetime="{DATE_ISO}">{DATE_LONGUE}</time>'),
        ('Responsable des traitements', 'Pierre Bénateau'),
        ('Éditeur', 'Hellodevis — RCS Paris B 798 043 634'),
    ) if politique else (
        ('Éditeur', 'Hellodevis — SAS au capital de 30 000 €'),
        ('Immatriculation', 'RCS Paris — B 798 043 634'),
        ('Conservation des données', 'OVH — Gravelines, France'),
    )
    contexte = {
        'nom': nom, 'domaine': escape(site.domaine), 'site': escape(site.url), 'theme': escape(site.theme),
        'logo': escape(site.logo), 'largeur': site.largeur, 'hauteur': site.hauteur,
        'dpo': escape(site.dpo), 'clients': escape(site.clients), 'texte_editeur': editeur,
        'adresse_ovh': indent(ADRESSE_OVH, '      '), 'contacts': indent(liste_contacts(site), '      '),
    }
    if politique:
        contexte['desinscription'] = indent(DESINSCRIPTION_HELLODEVIS, '      ') if est_hellodevis else ''
    else:
        contexte['marques'] = '\n'.join(indent(carte_marque(marque), '        ') for marque in site.marques)
        contexte['hebergeur_site'] = indent(ADRESSE_HISTORIQUE_HELLODEVIS, '      ') if est_hellodevis else ''

    return coque.substitute(
        contexte,
        titre=titre,
        description=escape(f'{titre} de {site.nom} : informations et coordonnées.'),
        rubrique='Données personnelles' if politique else 'Informations légales',
        introduction=introduction,
        resume='\n'.join(f'          <div><dt>{libelle}</dt><dd>{valeur}</dd></div>' for libelle, valeur in resume),
        mentions_courante='' if politique else ' aria-current="page"',
        politique_courante=' aria-current="page"' if politique else '',
        contenu=indent(modele.substitute(contexte).rstrip(), '    '),
        date_iso=DATE_ISO,
        date_longue=DATE_LONGUE,
        annee=DATE_ISO[:4],
    )


def main() -> int:
    parser = ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='signale les fichiers à régénérer sans les modifier')
    check = parser.parse_args().check
    coque = lire_modele('document.html')
    mentions, politique = lire_modele(MENTIONS), lire_modele(POLITIQUE)
    css = (MODELES / CSS).read_bytes()
    divergent = False
    for site in SITES:
        livrables = {
            MENTIONS: document(coque, mentions, site, politique=False).encode('utf-8'),
            POLITIQUE: document(coque, politique, site, politique=True).encode('utf-8'),
            CSS: css,
        }
        for fichier, contenu in livrables.items():
            chemin = ROOT / site.domaine / fichier
            if chemin.is_file() and chemin.read_bytes() == contenu:
                continue
            if check:
                print(f'À régénérer : {chemin.relative_to(ROOT)}')
                divergent = True
            else:
                chemin.write_bytes(contenu)
                print(chemin.relative_to(ROOT))
    return int(divergent)


if __name__ == '__main__':
    raise SystemExit(main())

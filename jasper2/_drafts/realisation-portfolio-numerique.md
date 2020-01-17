---
layout: post
current: post
cover: assets/images/typewriter-801921_1280.jpg
navigation: True
title: Réalisation d'un portfolio numérique avec Jekyll
date: 2020-01-17 10:18:00
tags: coulisses
class: post-template
subclass: 'post tag-coulisses'
author: quentin
---

Cet article présentera brièvement comment ce site a été construit en utilisant des technologies libres et open sources.

## Hébergement
GitHub permet d'héberger des sites via son service [Pages](https://pages.github.com/).
L'une des méthodes pour l'activer consiste à créer un dossier ```docs``` dans le dépôt du projet.
En allant ensuite dans les options (*Settings*), de descendre jusqu'à l'encart ```GitHub Pages``` et de sélectionner la source ```master branch /docs folder```.
Le site sera immédiatement disponible à l'adresse https://```nom d'utilisateur```.github.io/```nom du projet```,
comme par exemple [https://parastuffs.github.io/esnu/](https://parastuffs.github.io/esnu/)

## Générer un site web statique
GitHub Pages se contente d'afficher des pages web statiques, c'est-à-dire dont le contenu est généré à l'avance et ne peut pas être modifier par les visiteurs.
Pour générer un tel site, on peut utiliser [Jekyll](https://jekyllrb.com/) fonctionnant avec [Ruby](https://www.ruby-lang.org/fr/) en utilisant la commande suivante pour l'installer : ```gem install bundler jekyll```

Mais au lieu de créer un site entier à partir de rien, il est plus simple et rapide de partir d'un theme existant.
Par exemple, on peut utiliser [jasper2](https://github.com/jekyller/jasper2) dont il suffit de télécharger l'archive dans le dépôt du projet.
Depuis le dossier ```jasper2```, une seule commande permet de générer le site : ```bundle exec jekyll serve```.
Cette opération génère tous les fichiers du site web dans le dossier ```jasper2-pages``` par défaut et héberge une version locale du site à l'adresse ```http://127.0.0.1:4000/jasper2/```

## Configuration de jasper2
Le premier fichier de configuration à mettre à jour est le principal : [```_config.yml```](https://github.com/parastuffs/esnu/blob/master/jasper2/_config.yml).
Toutes les options sont commentées dans le fichier, mais l'une des essentielles est le dossier de destination à changer en ```../docs/``` ainsi que l'option ```baseurl```.

### Gérer les tags

### Gérer les auteurs

### Modifier l'en-tête

### Écrire un article

#### Brouillons
Les brouillons doivent être écrits dans un dossier ```_drafts``` et ne nécessite pas de date dans leur nom de fichier.
Ensuite, si vous souhaitez les voir sur la version locale de votre site, il faut compiler le site en ajoutant une option à la commande : ```bundle exec jekyll serve ---draft```.

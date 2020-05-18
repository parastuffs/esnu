---
layout: post
current: post
cover: assets/images/code-h5p-custom.jpg
navigation: True
title: Tester la maîtrise d'un logiciel, sans ce dernier
date: 2020-04-15 10:18:00
tags: projet
class: post-template
subclass: 'post tag-projet'
author: quentin
---

Comment aider les étudiants à tester leur maîtrise du logiciel en vue de l'examen de laboratoire ?

Ce questionnement découle de la [problématique mise en évidence]({{site.baseurl}}{% link _posts/2020-03-10-nouveau-public-nouvelle-problematique.md %}) et ce billet en présentera quelques réponses.


Le but de ces activités est de permettre aux étudiants de mettre leur maîtrise à l'épreuve sans devoir directement utiliser le logiciel, éliminant ainsi une source de problèmes et de frustration.
Ils auront tout de même déjà manipulé ce dernier, comme expliqué dans la [scénarisation du dispositif]({{site.baseurl}}{% link _posts/2020-04-05-scenarisation.md %}}).

La solution retenue a été d'exploiter à nouveau Moodle au travers de modules [H5P](https://h5p.org/), permettant de créer des contenus dynamiques et interactifs variés.
Trois volets ont ainsi été développés : (1) [la navigation dans l'interface du logiciel](#maîtrise-de-la-navigation), (2) [la connaissance des différents types de simulation](#maîtrise-des-types-de-simulation) et (3) [la gestion des erreurs de manipulation](#maîtrise-des-erreurs).


### Maîtrise de la navigation

Les étudiants peuvent ici vérifier qu'ils savent afficher la courbe de Bode d'une réponse en fréquence en naviguant dans l'interface de PSpice.
L'activité consiste en une suite de modules « **Find the Hotspot** », chacun avec une zone sensible correspondant au bouton ou menu à activer.

Idéalement, j'aurais préféré n'avoir qu'une seule image affichée à la fois, la suivante apparaissant losque le *hotspot* aurait été trouvé.
La solution la plus proche que j'ai trouvée était d'attribuer des points à la complétion d'une image, la suivante ne s'affichant que losqu'un certain seuil de points était atteint.
Le problème étant néanmoins qu'il fallait rafraîchir la page après chaque image afin que les points soient comptabilisés. De plus, l'activité n'aurait pu être réalisée qu'une seule fois, l'étudiant ne pouvant remettre ses points à zéro.

Ci-suit une animation de la réalisation de l'activité.

![Animation du projet de la quête de la courbe de Bode](assets/images/H5P/quete-bode.gif)


### Maîtrise des types de simulation

Un autre aspect essentiel à maîtriser est de savoir choisir le bon type de simualtion afin d'obtenir des résultats pertinents.

Un nouveau module H5P est adapté : la scénarisation (***Branching Scenario***).
L'étudiant est ici maître de son destin et l'évolution de l'activité dépend de ses réponses.

Pour ce premire essai, je suis resté bref, comme vous pouvez le voir sur l'aperçu du scénario.

![Overview H5P du projet de simulation](assets/images/H5P/simu_overview.png)

Je propose une situation requérant une simulation particulière.
Les quatres types de simulation sont proposés et pour chacun, le résultat de cette simulation est affiché, accompagné d'un feedback leur expliquant pourquoi la réponse est bonne ou mauvaise.
En cas de mauvaise réponse, ils sont renvoyés vers la question afin de donner une autre réponse.


![Animation du projet de la recherche de la bonne simulation](assets/images/H5P/bonne-simu.gif)


### Maîtrise des erreurs

Le dernier aspect testé dans ce projet n'est pas le plus anodin : d'où viennent les erreurs qu'il est possible de rencontrer dans le logiciel ?

Quatre erreurs typiques sont ainsi présentées dans ce nouveau scénario.

![Overview H5P du projet où il faut trouver l'erreur](assets/images/H5P/error_overview.png)

En cas de mauvaise réponses, l'utilisateur est à nouveau renvoyé vers le début de l'erreur afin qu'il puisse en ré-analyser les messages et mieux en diagnostiquer la cause.


![Animation du projet où il faut trouver l'erreur](assets/images/H5P/serie-erreurs.gif)


## Un dispositif différent

Ce genre d'activité est résolument différent des vidéos dont j'ai l'habitude.
Elle nécessite davantage de planification et de vérification afin de m'assurer qu'elle est bien *fool-* et *idiot-proof*.

Les objectifs sont cependant différents ; il ne s'agit pas ici de présenter un nouveau concept ou de la nouvelle matière, mais bien de rendre l'utilisateur actif et de le pousser à se poser des questions.

H5P est une excellente boîte à outils et pourrait être utile pour rendre les tutoriels vidéos existant plus interactifs et peut-être plus accrocheurs.
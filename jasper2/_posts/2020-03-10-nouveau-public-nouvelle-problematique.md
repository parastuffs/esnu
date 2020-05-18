---
layout: post
current: post
cover: assets/images/stormtrooper-1343877_1280.jpg
navigation: True
title: Nouveau public, nouvelle problématique
date: 2020-03-10 10:18:00
tags: projet
class: post-template
subclass: 'post tag-projet'
author: quentin
---

Mise à jour des personas et de la problématique suite à la [réorientation du projet]({{site.baseurl}}{% link _posts/2020-03-01-reorientation-du-projet.md %}).


## Changement de public

Comme expliqué dans le billet parlant de mon choix de changer le projet, nous avons changé de public : il s'agit à présent d'une série d'étudiants de première année de master, à orientation biomédicale.
Quant au cours, il s'agit toujours d'électronique, mais analogique cette fois-ci.
Les laboratoires s'y déroulent en trois temps : des simulations numériques à l'aide d'un logiciel ([OrCAD](https://www.orcad.com/)), la conception d'un circuit imprimé à l'aide d'un autre ([KiCad](https://kicad-pcb.org/)), pour terminer avec l'assemblage et le test physique de leur réalisation.

Quelques échanges en fin de laboratoire avec des étudiants, en suivant le même canvas que pour les [premiers personas]({{site.baseurl}}{% link _posts/2019-11-10-construire-des-personas.md %}), ont permis de dresser un [persona représentant le groupe entier](assets/persona/elech402/export_canvas_personasesnu-elech402--camille.pdf).

Ce profil est fort similaire à ceux des étudiants de BA3 précédemment étudiés (ce qui est compréhensible).
L'un des changements notables est qu'ils ont un examen de laboratoire qu'ils se demandent comment préparer.


## Changement de projet

Le cours, le public et leurs besoins ayant changés, le projet doit aussi être mis jour.


### Définition du problème

Cette réflexion suit le même cheminement que la [première définition]({{site.baseurl}}{% link _posts/2019-11-15-definition-du-probleme.md %}) et en partage certains points.

#### Contradictions

* Ils veulent des corrigés détaillés des laboratoires, mais il ne prennent pas note de leur propres méthodes et développements.  
Des corrigés ont néanmoins été mis à disposition, principalement pour les réponses numériques finales. Certaines manipulations permettant d'y arriver ont aussi été ajoutées, mais l'essentiel est détaillé dans les vidéos d'explication du logiciel.

#### Révélations ou remarques intéressantes

* Très rares sont les étudiants allant chercher des ressources supplémentaires sur Internet pour mieux comprendre le fonctionnement du logiciel, des composants utilisés ou pour les aider à résoudre un message d'erreur.
* Ils regardent les vidéos avant ou pendant le laboratoire, mais n'en retiennent pas le contenu.
* Ils se contentent de regarder les vidéos une seule fois, généralement juste avant le premier laboratoire, mais n'y reviennent plus ensuite.


#### Difficultés, problèmes ou besoins vécus/ressentis par l’apprenant.e

* Identifier ses propres erreurs et en tirer des leçons.  
La majorité du temps, quand ils sont aidés pour résoudre un problème de manipulation du logiciel, ils ne notent nulle part comme ils ont résolu l'erreur.
* Ils ont globalement peur de l'examen de laboratoire.
Pas tant pour sa difficulté théorique, mais pour la maîtrise nécessaire du logiciel « qui bug tout le temps » selon eux, mais qui sont 99% du temps des erreurs de manipulation qui sont justement évaluées.


### Reformulation de la problématique

L'essentiel de leurs inquiétudes tournant autour de l'examen de laboratoire et du logiciel de simulation, la problématique pourrait être reformulée comme suit :

> Comment pourrais-je aider les étudiants à tester leur maîtrise du logiciel en vue de l'examen de laboratoire ?


### Matériel existant

Pour m'aider dans cette tâche, il existe déjà des ressources que j'ai developpées au cours des années.
Un [Wiki](https://github.com/BEAMS-EE/ELECH402/wiki/KiCad:-project) pour KiCad et surtout des [vidéos](https://www.youtube.com/playlist?list=PLOQHyfCR7VoDGZA_SN9r1AEn83DdWCXU0) pour OrCAD.

Ces dernières sont celles dont je parlais plus tôt : les étudiants les regardent généralement quelques jours avant le premier laboratoire pour se faire une idée de la manipulation du logiciel.

### Nouveau matériel à développer

Elles ne sont cependant pas suffisantes pour préparer correctement les étudiants, elles manquent d'interactivité afin de les engager dans leur apprentissage.
Il serait donc intéressant de développer un petit module d'auto-évaluation à l'utilisation du logiciel, mais ça, c'est pour un [autre billet]({{site.baseurl}}{% link _posts/2020-04-15-tester-maitrise-logiciel.md %}).
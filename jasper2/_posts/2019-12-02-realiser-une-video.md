---
layout: post
current: post
cover: assets/images/sony-1455032_1280.jpg
navigation: True
title: Réaliser une vidéo
date: 2019-12-02 10:18:00
tags: projet
class: post-template
subclass: 'post tag-projet'
author: quentin
---

Les vidéos c'est sympa, mais comment on fait ? Quelle marche suivre et quels outils utiliser ?

Ce billet présente les différentes étapes de réalisation d'une vidéo à destination des apprenants, en illustrant chacune avec ma réalisation pratique.


## Scénarisation

Avant de commencer à filmer quoi que ce soit, il faut savoir ce qu'on veut montrer.
La première étape consiste donc à *scénariser* la vidéo, écrire l'histoire qu'on veut raconter.

Le scénario peut prendre différentes formes : un *story board*, un texte construit de l'ensemble du contenu ou une simple liste des éléments à aborder et les points d'attention sur lesquels insister.


#### Application

Le but de cette vidéo est d'expliquer aux étudiants comment manipuler la matériel à leur disposition afin de réaliser une mesure particulière.
Pour être un peu technique, il s'agit de mesurer le temps de propagation d'un signal au sein d'un circuit logique à l'aide d'un oscilloscope.

Ma scénarisation a donc commencé par concevoir un montage intéressant et réaliser la manipulation en entier par moi-même.
Une fois terminée, j'ai pu la déconstruire pour mettre en évidence les **étapes clefs** par lesquelles les étudiants devront passer à leur tour.

Ce scénario a pris la forme d'une liste d'étapes, certaines illustrées par les schémas.


## Tournage

Le scénario terminé, il est temps de tourner les différents plans constituant l'histoire.
Il n'est pas encore essentiel de savoir ce qu'on va raconter ou d'enregistrer les voix en même temps. Il est même plus simple de séparer les deux étapes de vidéo et audio afin de les paufiner chacune de leur côté.

Cependant, cette manière de procéder nécessite de filmer des **scènes supplémentaires** « au cas où », afin d'avoir suffisamment de matériel.

Si le scénario est complet et qu'on est capable d'imaginer des plans supplémentaires pour compléter la trame principale, cette étape peut être réalisée en peu de temps, sans nécessiter de resortir la caméra par la suite.


#### Application

Je me suis filmé à l'aide d'un appareil photo de bonne qualité (Panasonic Lumix GX80) en séparant les différents plans, facilitant le montage pour la suite.
Chaque courte vidéo ne dure que quelques secondes, me permettant par la suite de trouver facilement une étape particulière.

La qualité du tournage aurait pu être drastiquement améliorée avec l'aide d'une autre personne pour manipuler la caméra ou avec la simple utilisation d'un trépied pour stabiliser l'image pendant les manipulations.

![Photo du montage non-utilisée dans la réalisation](assets/images/realisation-video/protoboard.JPG "Photo du montage non-utilisée dans la réalisation")


## Enregistrement des voix

Il ne sert à rien d'improviser l'entièreté de la vidéo.
Certes, lire un texte écrit à l'avance peut retirer l'effet naturel d'une explication, mais ne pas avoir de support est encore pire. Le discours sera ponctué d'hésitations qui ne feraient qu'ajouter du bruit.

Mais comment écrire un texte qui semble quand même naturel ?
Une méthode qui fonctionne assez bien est de complètement improviser la narration.
Étant donné le travail déjà effectué sur cette vidéo, ça ne devrait pas poser de problème.
Mais au lieu de directement utiliser cet enregistrement, on peut l'écouter et réécrire tout ce qu'on a raconté afin d'avoir un support propre pour un nouvel enregistrement.

Avant de se lancer pour de bon, il faut aussi bien **préparer l'introduction et la fin** de la vidéo.
* L'introduction devrait être courte et présenter clairement ce qui sera abordé dans la vidéo ainsi que les étapes de son déroulé.
* La conclusion peut servir de résumé en rappelant à nouveau les grandes étapes de la manipulation.


#### Application

J'ai utilisé un micro Bird UM1 et [Audacity](https://www.audacityteam.org/) pour enregistrer l'audio de la vidéo.

![Spectre Audacity](assets/images/realisation-video/audacity.png "Audacity")


## Montage

Une fois l'audio enregistré, il s'agit de piocher dans les plans tourner plus tôt et de les coller au bon endroit afin d'illustrer la narration.
Cette étape n'est pas compliquée avec un peu d'expérience, mais c'est celle qui impactera directement ce que regarderont les étudiants, c'est le moment où tout se joue.
Les scènes supplémentaires seront probablement utiles, ne serait-ce qu'en *[B-roll](https://fr.wikipedia.org/wiki/Bobine_B)* afin de combler les trous pendant l'introduction ou la conclusion.

Ajouter un écran d'accueil avec un titre clair et les logos de l'institution peut aussi s'avérer utile pour la publication à venir, mais aussi pour démarrer la vidéo en douceur pendant l'introduction.


#### Application
Il existe de nombreux logiciels gratuits et/ou libres permettant de monter ce genre de projet.

Du côté de le plus simple du spectre, [OpenShot](https://www.openshot.org/fr/download/) est une très bonne solution. Il permet des manipulations basiques du son et de l'image, rien de très élaboré, mais généralement suffisant pour une vidé sobre.

![Openshot timeline](assets/images/realisation-video/openshot.png "Openshot Timeline")

À l'autre extrémité se trouve [DaVinci Resolve](https://www.blackmagicdesign.com/products/davinciresolve/), un logiciel de montage non-linéaire extrêmement complet et plus difficile à prendre en main. Il permet pourtant de faire un montage particulièrement soigné une fois apprivoisé et vaut le détour.


## Publication

Le rendu terminé, il faut publier la vidéo pour que les étudiants puissent enfin la visioner.
Si on peut leur envoyer directement, une plate-forme de diffusion est beaucoup plus efficace et permet de suivre son impact.

[YouTube](https://studio.youtube.com/) est particulièrement approprié dans le cas présent.
La plate-forme permet de procéder à de nombreuses analyses : nombres de vues, quand, qui, où, la durée d'attention, etc.
Mais ça, c'est pour [un autre billet]({{site.baseurl}}{% link _posts/2019-12-10-premiere-diffusion-podcast.md %}).


#### Application

Le résultat de toute cette procédure est disponible [ici](https://youtu.be/5UpnbasZ3ng).

{% include youtube.html id="5UpnbasZ3ng" %}
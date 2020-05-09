---
layout: post
current: post
cover: assets/images/stadium-165406_1280.jpg
navigation: True
title: Distribuer des examens individuels
date: 2020-04-30 10:18:00
tags: experience
class: post-template
subclass: 'post tag-experience'
author: quentin
---
Comment automatiser la distribution d'un examen individuel à chaque étudiant ?

Cette question se pose dans le cadre des examens à distance.
Plusieurs solutions sont envisageables pour assurer ces évaluations, mais celle qui nous intéresse ici est de générer un examen différent pour chaque étudiant.
Le problème qui survient ensuite, c'est de donner accès à chaque étudiant à sa copie uniquement.

#### Utiliser Moodle pour distribuer un document automatiquement
C'est évidemment notre première idée : uploader tous les documents sur l'UV et les assigner automatiquement à chaque étudiant.
S'il est effectivement possible de limiter l'accès à un document à une personne en particulier via le menu « Restreindre l'accès », ce n'est pas automatisable.
La cohorte de l'examen en question étant composée de 200 personnes, ce n'est pas réaliste à la main.

#### Protéger le document par un mot de passe unique pour chaque étudiant
Reste le problème de distribuer les mots de passe à chaque étudiant.
On pourrait l'envoyer par email, mais il y a alors un problème de synchronisation de début de l'examen, il faut que le message arrive à tout le monde en même temps et surtout qu'il arrive tout court.

#### Envoyer le document par email à chaque étudiant
C'est une solution qui pourrait facilement être automatisée, mais nous avons alors le même problème de synchronisation et de fiabilité que précédemment.

#### Utiliser des groupes
Il s'agit de la réponse cryptique renseignée par le support Moodle de l'ULB, sans que nous comprenions comment exploiter cette information.


#### Combiner Moodle et un serveur externe
Une ressource de Moodle est paramétrisable à souhait : les URL.
Cette ressource fonctionne en deux parties :
1. URL externe  
Il s'agit de l'adresse de base vers laquelle renvoyer l'utilisateur.
Nous pouvons par exemple utiliser ```http://monsite.be```
2. Variables d'URL  
Une variable d'URL est un mot-clef ressemblant à ```mot-clef=valeur```.
La force de Moodle, c'est de permettre d'automatiser cette variable, par exemple en changeant la ```valeur``` par une info unique aux participants, par exemple leur matricule.

On peut ainsi générer une URL ressemblant à ```http://monsite.be?matricule=matricule_unique``` où ```matricule_unique``` est le matricule de l'étudiant.

L'URL ainsi générée sera unique pour chaque étudiant, reste à présent à lui envoyer le bon fichier lorsque qu'il y accède.

Pour ce faire, nous pouvons le rediriger vers un script qui analyse l'URL, récupère le numéro de matricule et envoie le fichier idoine à l'étudiant.
C'est exament ce que réalise le bout de code suivant :

```php
<?php
$mat = $_GET["matricule"];
$file_url = "examen_".$mat.".pdf";
header('Content-Type: application/octet-stream');
header("Content-Transfer-Encoding: Binary"); 
header("Content-disposition: attachment; filename=\"" . basename($file_url) . "\""); 
readfile($file_url); 
?>
```

Cette solution est donc utilisable sans effort particulier ou répétition de tâches identiques.

## Résumé de la mise en place

1. On crée une ressource « URL » sur Moodle comme expliqué ci-dessus.
2. On restreint l'accès à cette ressource aux heures de l'examen, ne la rendant accessible qu'au début de ce dernier.
3. Sur un serveur externe, on uploade tous les fichiers générés auparavant.
4. On crée le script décrit ci-dessus permettant de distribuer le fichier unique à l'étudiant.
5. On communique clairement sur le sujet.


## Scénario d'utilisation
Voici comment devrait se dérouler l'utilisation de cette ressource par les étudiants.

1. Ils seront prévenus à l'avance des modalités précises de distribution de la copie.  
Actuellement, ils sont déjà au courant qu'ils recevront une copie unique, a priori via Moodle.
2. À l'heure de l'examen, la ressource en question sera débloquée et ils pourront accéder à l'URL.
3. Ils seront automatiquement redirigés vers le serveur externe où ils recevront leur copie sans intervention supplémentaire de leur part.
4. Ils réalisent l'examen sur leur ordinateur.
5. Ils envoient leur réponse sur Moodle sous la forme d'une activité « devoir ».


## Limites
Cette solution n'est pas parfaite et possède ses propres limites.

#### Assurer la charge
Il faut être sûr que le serveur externe est capable de délivrer tous les fichiers en même temps lorsqu'ils seront tous téléchargés en l'intervalle d'une minute.
Si 200 fichiers pdf ne devraient pas poser de soucis, il est tout de même possible de mettre en place un service de *load balancing* afin de répartir la charge entre plusieurs serveurs si nécessaire.

#### Besoin d'un serveur externe
C'est le plus gros problème. Idéalement, on aimerait pouvoir envoyer tous les fichiers sur Moodle et permettre à l'URL de rediriger vers un fichier en particulier automatiquement, mais ce n'est malheureusement pas possible.

#### Tous les fichiers sont tout de même accessible par tout le monde
Certes, mais nous comptons sur la limite de temps pour nous assurer que chaque étudiant n'ait le temps de se concentrer uniquement sur son examen.
Pourquoi nous fatiguer à mettre ce système en place, dans ce cas ? Pourquoi ne pas simplement demander aux étudiants de récupérer leur copie dans un dossier les comprenant toutes ?

Tout simplement pour leur éviter le stress de récupérer la mauvaise copie.
Il faut aussi noter que le matricule « Moodle » n'est pas nécessaire le même que le matricule « étudiant », phénomène rencontré par exemple pour les étudiants de la VUB.
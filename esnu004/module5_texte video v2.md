Bonjour à tous et à toutes.
Au cours de cette vidéo, nous verrons ensemble comment utiliser le mode de déclenchement externe de l'oscilloscope.
Ce mode est par exemple utile pour observer le délais de propagation d'un signal au sein d'une porte logique lors de son changement d'état.

Prenons par exemple le circuit logique suivant.
*OBS sur l'écran avec le circuit logique*
Nous aimerions étudier le délais de propagation de la porte logique OR à la sortie du montage.

*Caméra protoboard*
Le circuit a été réalisé sur ce protoboard. Le package de gauche est composé de portes NAND, tandis que celui de droite est composé de portes OR.
Lorsque nous activons cet interrupteur correspondant à la variable A, la sortie connectée à la LED change aussi suite à un changement d'état de la porte OR qui nous intéresse.

Connectons à présent le premier canal de l'oscilloscope à l'entrée de notre porte OR et le second canal à la sortie de cette même porte.

*Caméra oscilloscope*
Dans son utilisation habituelle, l'oscilloscope acquiert des données en continu et rafraîchit sans arrêt son affichage à chaque fois que le signal passe par une certaine valeur qu'on peut lire en bas à droite de l'écran.
Nous aimerions changer son comportement pour qu'il remplisse son écran une seule fois à l'instant précis où nous activons l'interrupteur sur le protoboard.

Nous allons devoir utiliser l'entrée de déclenchement externe de l'oscilloscope, notée « EXT TRIG ». Connectons cette entrée à l'interrupteur du protoboard.
Dans le menu de déclenchement, le « trigger menu », sélectionnons d'abord la bonne entrée.
Le type de déclanchement sera sur un flanc montant si on décide d'activer l'interrupteur, ou un flanc descendant si on décide de le désactiver.
Enfin, nous pouvons régler le niveau de déclenchement.
Il ne reste plus qu'à presser le bouton « single seq » pour que l'oscilloscpe ne capture qu'une seule séquence et ne se rafraîchisse pas en continu.

En résumé, lorsque l'oscilloscope détectera une tension de 2.5 V lors d'une montée de tension sur l'interrupteur, il remplira sa fenêtre de données et puis se mettra en pause.

N'oubliez pas de bien régler les échelles de tension et de temps afin d'observer correctement votre signal.

Bon laboratoire.
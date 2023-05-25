# Script d'import de MIDI sur 3DS Max : note d'intention
Dans le cadre de la réalisation d'un court-métrage d'animation 3D, j'ai été amené à réaliser la partie musique d'un morceau joué au piano.
Il m'a alors fallu concevoir l'idée que le piano allait devoir être joué sur la scène 3D, et comme aucun outil actuel ne le permet, j'ai créé un script permettant d'exporter, puis de filtrer les données d'un fichier MIDI, afin de les importer dans un fichier du logiciel 3DS Max, les associer aux notes du piano et les jouer de façon automatique, en utilisant la bibliothèque MIDO de python.

## Overview du projet
La première partie consiste à récupérer le fichier midi, et de stocker les variables de vélocité, de note, de durée de note et de point de départ de la note, dans un tableau itératif.

La seconde étape, parfaitement optionnelle, et uniquement liée à mon projet, consistait à exporter la fichier en format txt, avec les informations du fichier midi.

La troisième étape correspond au mappage des notes, c'est-à-dire l'association de la numérotation des notes avec les objets 3DS Max. Là encore, le fichier est adapté à la terminologie de mon projet, mais peut être adapté sans le moindre soucis.

Finalement, la dernière étape consiste à lire les notes une par une, avec leurs informations, puis de les faire bougées en fonction de l'axe Z (qui permet d'avoir l'impression que la note s'enfonce dans le piano).


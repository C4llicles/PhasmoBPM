# PhasmoBPM

### Information
PhasmoBPM est un outil pour les joueurs de Phasmophobia, surtout ceux qui ont du mal pour définir la vitesse du phantome.
Il suffit d'appuyer sur la touche Espace pendant que le phantome chasse, en suivant le rythme de ses pas, et PhasmoBPM calcule sa vitesse en temps réel et propose la liste des phantomes avec la vitesse correspondante.
Il y a aussi un minuteur qui peut aider à voir si certains phantômes peuvent chasser à un moment précis.
Nous prévoyons également d'ajouter un calculateur de santé mentale, qui aurait aidé à éstimer le niveau approximatif de santé mentale du joueur.

### Outils
L'application est codé en Python avec PySide6 afin de permettre à PhasmoBPM d'être affiché au premier plan et de lire l'état de la barre Espace lorsque Phasmophobia a aussi le focus.

### Aperçu
<img width="2557" height="1437" alt="phasmo_preview" src="https://github.com/user-attachments/assets/40c99480-79a9-4eb9-b2da-e5695369a653" />
Voici l'interface utilisateur que nous voulons donner au produit final. Les éléments principaux sont :

- Un minuteur en haut à gauche, avec des icones du Démon et de l'Esprit, éventuellement en gris lorsque le joueur a communiqué le fait d'avoir utilisé un encens.
- Un calculateur de vitesse en haut à droite, avec une animation visuele lorsque l'utilisateur appuye sur l'espace, ainsi que le BPM et la vitesse en m/s affiché.
- Un calculateur de santé mentale en bas à gauche, affichant le niveau approximatif de santé mentale du joueur. Le calcul sera fait à partir des préréglages indiqués par le joueur, le temps du début de la partie, et les différents événements également signalés par le joueur.

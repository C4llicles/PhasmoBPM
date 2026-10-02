# PhasmoBPM

### Information
PhasmoBPM est un outil pour les joueurs de Phasmophobia, surtout pour ceux qui ont du mal à définir la vitesse du fantôme.  
Il suffit d'appuyer sur la touche **Espace** pendant que le fantôme chasse, en suivant le rythme de ses pas, et PhasmoBPM calcule sa vitesse en temps réel et propose la liste des fantômes avec la vitesse correspondante.  
Il y a aussi un minuteur qui peut aider à voir si certains fantômes peuvent chasser à un moment précis.  
Nous prévoyons également d'ajouter un calculateur de santé mentale, qui aiderait à estimer le niveau approximatif de santé mentale du joueur.

### Outils
L'application est codée en Python avec PySide6 pour l'interface et tournera dans un premier temps sous Windows, permettant à PhasmoBPM de s'afficher au premier plan et de détecter l'appui sur la barre Espace lorsque Phasmophobia est au premier plan.

### Aperçu
<img width="2557" height="1437" alt="phasmo_preview" src="https://github.com/user-attachments/assets/40c99480-79a9-4eb9-b2da-e5695369a653" />

Voici l'interface utilisateur que nous souhaitons pour le produit final. Les éléments principaux sont :

- Un minuteur en haut à gauche, avec les icônes du Démon et de l'Esprit, qui s'allumeront au bon moment après que le joueur a indiqué avoir utilisé un encens.
- Un calculateur de vitesse en haut à droite, avec une animation visuelle lorsque l'utilisateur appuie sur Espace, ainsi que le BPM et la vitesse en m/s affichés.
- Un calculateur de santé mentale en bas à gauche, affichant le niveau approximatif de santé mentale du joueur. Le calcul sera fait à partir des préréglages indiqués par le joueur, du temps écoulé depuis le début de la partie et des différents événements également signalés par le joueur.

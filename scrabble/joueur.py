from random import shuffle


class Joueur:
    """
    Cette classe permet de représenter un joueur.

    Attributes:
        taille_chevalet (int): Le nombre de jetons maximum qu'un joueur peut avoir
                            (Dans notre cas, cette valeur est fixée à 7).
        nom (str): Le nom du joueur (doit être non vide).
        points (int): Le nombre de points que le joueur détient.
        chevalet (list): Représente le chevalet (l'ensemble des jetons du joueur) du joueur. Cette liste devrait être en
                         tout temps de taille Joueur.taille_chevalet. À chaque position du chevalier on peut avoir un
                         jeton ou pas. Une position libre devra contenir None. Autrement elle devrait avoir un objet J
                         eton à cette position.
    """

    def __init__(self, nom):
        """
        *** Vous n'avez pas à coder cette méthode. ***

        Initialise un objet joueur avec le nom passé en argument.
        Le nombre de points d'un joueur devra être 0 à l'initialisation,
        et le chevalet devra être vide.
        Rappel: Un chevalet vide veut dire une liste contenant que des None.

        Args:
            nom (str): Le nom du joueur.

        Raises:
            AssertionError: Si le nom est vide.
        """
        # On valide les pré-conditions
        assert nom.strip() != '', 'Le nom doit être non vide.'

        # On initialise les différents attributs
        self.taille_chevalet = 7
        self.nom = nom
        self.points = 0
        self.chevalet = [None] * self.taille_chevalet

    def nb_a_tirer(self):
        """
        Méthode permet de trouver le nombre de places vides dans le chevalet.
        Rappel: Un chevalet vide veut dire une liste contenant que des None.

        Returns:
            int: Le nombre de places vides dans le chevalet.
        """
        # TODO: À compléter
        # Mettre votre code ici
        places_vides = 0

        # Si l'emplacement est vide, on incrémente le nombre de places vides
        for emplacement in self.chevalet:
            if emplacement is None:
                places_vides += 1
        return places_vides

    def position_est_valide(self, position):
        """
        Méthode permettant de vérifier si une position sur un chevalet est valide ou pas.
        Valide veut dire que la position est entre 0 (inclus) et la taille du chevalet (exclus)

        Args:
            position (int): La position à valider.

        Returns:
            bool: True si position valide, False sinon.
        """
        # TODO: À compléter
        # Mettre votre code ici

        # On retourne si la position est entre 0 (inclus) et la taille du chevalet (exclus)
        return 0 <= position < self.taille_chevalet

    def position_est_vide(self, position):
        """
        Étant donné une position sur le chevalet, cette méthode permet
        de savoir si la position est vide ou pas.
        Rappel: Une position vide ne contient pas de jeton, juste None.

        Args:
            position (int): La position à vérifier.

        Returns:
            bool: True si la position est vide et False sinon.
        """
        # TODO: À compléter
        # Mettre votre code ici
        return self.chevalet[position] is None

    def ajouter_jeton(self, jeton, position=None):
        """
        Étant donné un jeton et une position sur le chevalet, cette méthode permet d'ajouter le jeton au chevalet si la
        position mentionnée est vide.

        Si la position est vide (c'est-à-dire position est égal à None), le jeton est mis à la première position libre
        du chevalet en partant de la gauche.
        Rappel: Une position vide ne contient pas de jeton, juste None.

        Args:
            jeton (Jeton): le jeton à placer sur le chevalet.
            position (int, optionnel): Position où ajouter le jeton.
        """
        # TODO: À compléter
        # Mettre votre code ici

        # Si aucune position n'est spécifiée, on ajoute le jeton à la première position vide trouvée
        if position is None:
            for emplacement in range(self.taille_chevalet):
                if self.position_est_vide(emplacement):
                    self.chevalet[emplacement] = jeton
                    return
        # Sinon, on ajoute le jeton à la position spécifiée
        elif self.position_est_valide(position) and self.position_est_vide(position):
            self.chevalet[position] = jeton

    def retirer_jeton(self, position):
        """
        Cette méthode permet de retirer un jeton du chevalet. Autrement dit, le joueur prend un jeton de son chevalet.
        Donc, nous devons mettre la position à None et retourner le jeton qui était présent à cet emplacement.

        Args:
            position (int): Position du jeton à retirer.

        Returns:
            Jeton: Le jeton retiré.
        """
        # TODO: À compléter
        # Mettre votre code ici

        # On met la position du jeton à retirer à None (vide) puis on retourne le jeton retiré
        if self.position_est_valide(position) and not self.position_est_vide(position):
            jeton_retire = self.chevalet[position]
            self.chevalet[position] = None
        return jeton_retire

    def obtenir_jeton(self, position):
        """
        Cette méthode permet d'obtenir un jeton du chevalet. Autrement dit, le joueur regarde un jeton de son chevalet
        sans le retirer. Donc, nous devons simplement retourner le jeton à la position indiquée.

        Args:
            position (int): Position du jeton.

        Returns:
            Jeton: Le jeton à la position d'intérêt.
        """
        # TODO: À compléter
        # Mettre votre code ici
        if self.position_est_valide(position) and not self.position_est_vide(position):
            return self.chevalet[position]

    def ajouter_points(self, points):
        """
        Cette méthode permet d'ajouter des points à un joueur.

        Args:
            points (int): Le nombre de points à ajouter au joueur.
        """
        # TODO: À compléter
        # Mettre votre code ici
        self.points += points

    def melanger_jetons(self):
        """
        Cette méthode permet de mélanger au hasard le chevalet du joueur, c'est-à-dire mélanger les positions des
        éléments dans la liste représentant le chevalet.
        Pensez à utiliser la fonction shuffle du module random.
        """
        # TODO: À compléter
        # Mettre votre code ici

        # La méthode shuffle mélange les jetons du chevalet au hasard
        shuffle(self.chevalet)

    def __str__(self):
        """
        *** Vous n'avez pas à coder cette méthode. ***

        Formatage du joueur.
        Cette méthode est appelée lorsque vous faites str(v) où v est  un objet joueur.

        Returns
            str: Chaîne de caractères représentant un joueur.
        """
        s = '{}\n'.format(self.nom)
        s += 'Score: {}\n'.format(self.points)
        s += '            ' + ''.join(['{:<3s}'.format(str(x)) if x else '  ' for x in self.chevalet])
        s += '\nChevalet: \_' + '__'.join([chr(0x2080 + i + 1) for i in range(self.taille_chevalet)]) + '_/\n'
        return s

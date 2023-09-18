import tkinter as tk
import random
from unidecode import unidecode
from library import library_ES_FR



class TranslationGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Jeu de Traduction")

        self.category_label = tk.Label(root, text="Choisissez une catégorie :")
        self.category_label.pack()

        self.category_var = tk.StringVar(root)
        self.category_dropdown = tk.OptionMenu(root, self.category_var, *library_ES_FR.keys())
        self.category_dropdown.pack()

        self.translation_direction_label = tk.Label(root, text="Sens de traduction :")
        self.translation_direction_label.pack()

        self.translation_direction_var = tk.StringVar(root)
        self.translation_direction_dropdown = tk.OptionMenu(root, self.translation_direction_var, "es_fr", "fr_es")
        self.translation_direction_dropdown.pack()

        self.start_button = tk.Button(root, text="Start", command=self.start_game)
        self.start_button.pack()

        self.score_label = tk.Label(root, text="Score: 0")
        self.score_label.pack()

        self.category = None
        self.direction = None
        self.words = []
        self.score = 0
        self.current_word_index = 0

    def start_game(self):
        self.category = self.category_var.get()
        self.direction = self.translation_direction_var.get()
        self.words = list(library_ES_FR[self.category].keys())
        random.shuffle(self.words)
        self.score = 0
        self.current_word_index = 0
        self.score_label.config(text=f"Score: {self.score}")
        self.display_word()

    def display_word(self):
        # Détruire l'entrée de texte précédente s'il existe
        if hasattr(self, "answer_entry"):
            self.answer_entry.destroy()

        if self.current_word_index < len(self.words):
            word = self.words[self.current_word_index]
            if self.direction == "es_fr":
                self.word_label = tk.Label(self.root, text=word)
            else:
                self.word_label = tk.Label(self.root, text=library_ES_FR[self.category][word])
            self.word_label.pack()
            self.answer_entry = tk.Entry(self.root)
            self.answer_entry.bind("<Return>", self.check_answer)
            self.answer_entry.pack()
        else:
            self.score_label.config(text=f"Score final : {self.score}")
            self.words = []
            self.current_word_index = 0


    def check_answer(self, event):
        user_answer = self.answer_entry.get()
        if self.direction == "es_fr":
            correct_answer = library_ES_FR[self.category][self.words[self.current_word_index]]
        else:
            correct_answer = self.words[self.current_word_index]
        
        # Utilisez unidecode pour normaliser les réponses en retirant les accents
        user_answer_normalized = unidecode(user_answer).lower()
        correct_answer_normalized = unidecode(correct_answer).lower()
        
        if user_answer_normalized == correct_answer_normalized:
            self.score += 1
        else:
            # Si la réponse est incorrecte, affichez le mot correct et détruisez la correction précédente
            if hasattr(self, "correct_answer_label"):
                self.correct_answer_label.destroy()
            self.correct_answer_label = tk.Label(self.root, text=f"Correct : {correct_answer}")
            self.correct_answer_label.pack()
        
        self.current_word_index += 1
        self.score_label.config(text=f"Score: {self.score}")
        self.word_label.destroy()
        self.answer_entry.destroy()
        self.display_word()
        self.answer_entry.focus_set()





if __name__ == "__main__":
    root = tk.Tk()
    game = TranslationGame(root)


        # Obtenez la taille de l'écran
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculez les coordonnées pour positionner la fenêtre au milieu de l'écran
    window_width = 250  # Remplacez par la largeur souhaitée de la fenêtre
    window_height = 250  # Remplacez par la hauteur souhaitée de la fenêtre
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)

    # Définissez les dimensions et la position de la fenêtre
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")


        # Augmentez la largeur des menus déroulants
    menu_width = 17  # Vous pouvez ajuster cette valeur en fonction de vos besoins

    # Menu déroulant pour la catégorie
    game.category_dropdown.config(width=menu_width)

    # Menu déroulant pour le sens de la traduction
    game.translation_direction_dropdown.config(width=menu_width)

    start_button_width = 10  # Vous pouvez ajuster cette valeur en fonction de vos besoins
    start_button_height =1  # Vous pouvez ajuster cette valeur en fonction de vos besoins
    game.start_button.config(width=start_button_width, height=start_button_height)
    game.start_button.pack(pady=15)


    root.mainloop()













#     class TranslationGame:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Jeu de Traduction")

#         self.category_label = tk.Label(root, text="Choisissez une catégorie :")
#         self.category_label.pack()

#         self.category_var = tk.StringVar(root)
#         self.category_dropdown = tk.OptionMenu(root, self.category_var, *library_ES_FR.keys())
#         self.category_dropdown.pack()

#         self.translation_direction_label = tk.Label(root, text="Sens de traduction :")
#         self.translation_direction_label.pack()

#         self.translation_direction_var = tk.StringVar(root)
#         self.translation_direction_dropdown = tk.OptionMenu(root, self.translation_direction_var, "Español -> Français", "Français -> Español")
#         self.translation_direction_dropdown.pack()

#         self.start_button = tk.Button(root, text="START", command=self.start_game)
#         self.start_button.pack()

#         self.score_label = tk.Label(root, text="Score: 0/0")  # Score initial sous la forme "score/total_mots"
#         self.score_label.pack()

#         self.category = None
#         self.direction = None
#         self.words = []
#         self.score = 0
#         self.current_word_index = 0
#         self.total_words = 0  # Nombre total de mots
#         self.corrected_words = []  # Liste des mots corrigés
#         self.corrected_words_window = None  # Fenêtre pour afficher la correction

#     def start_game(self):
#         self.category = self.category_var.get()
#         self.direction = self.translation_direction_var.get()
#         self.words = list(library_ES_FR[self.category].keys())
#         random.shuffle(self.words)
#         self.score = 0
#         self.current_word_index = 0
#         self.total_words = len(self.words)
#         self.corrected_words = []  # Réinitialisez la liste des mots corrigés
#         self.score_label.config(text=f"Score: {self.score}/{self.total_words}")
#         self.display_word()

#     def display_word(self):
#         if hasattr(self, "answer_entry"):
#             self.answer_entry.destroy()

#         if self.current_word_index < len(self.words):
#             word = self.words[self.current_word_index]
#             if self.direction == "Español -> Français":
#                 self.word_label = tk.Label(self.root, text=word)
#             else:
#                 self.word_label = tk.Label(self.root, text=library_ES_FR[self.category][word])
#             self.word_label.pack()
#             self.answer_entry = tk.Entry(self.root)
#             self.answer_entry.bind("<Return>", self.check_answer)
#             self.answer_entry.pack()
#         else:
#             self.score_label.config(text=f"Score final : {self.score}/{self.total_words}")
#             self.words = []
#             self.current_word_index = 0

#     def check_answer(self, event):
#         user_answer = self.answer_entry.get()
#         if self.direction == "Español -> Français":
#             correct_answer = library_ES_FR[self.category][self.words[self.current_word_index]]
#         else:
#             correct_answer = self.words[self.current_word_index]

#         user_answer_normalized = unidecode(user_answer).lower()
#         correct_answer_normalized = unidecode(correct_answer).lower()

#         if user_answer_normalized == correct_answer_normalized:
#             self.score += 1
#         else:
#             self.corrected_words.append((self.words[self.current_word_index], correct_answer))

#         self.current_word_index += 1
#         self.score_label.config(text=f"Score: {self.score}/{self.total_words}")
#         self.word_label.destroy()
#         self.answer_entry.destroy()
#         self.display_word()
#         self.answer_entry.focus_set()

#     def show_correction(self):
#         if self.corrected_words:
#             self.corrected_words_window = tk.Toplevel(self.root)
#             self.corrected_words_window.title("Correction des Mots")

#             correction_label = tk.Label(self.corrected_words_window, text="Mots incorrects et leur correction:")
#             correction_label.pack()

#             for word, correct_answer in self.corrected_words:
#                 correction_text = f"{word} -> {correct_answer}"
#                 correction_display = tk.Label(self.corrected_words_window, text=correction_text)
#                 correction_display.pack()

# if __name__ == "__main__":
#     root = tk.Tk()
#     game = TranslationGame(root)

#         # Obtenez la taille de l'écran
#     screen_width = root.winfo_screenwidth()
#     screen_height = root.winfo_screenheight()

#     # Calculez les coordonnées pour positionner la fenêtre au milieu de l'écran
#     window_width = 250  # Remplacez par la largeur souhaitée de la fenêtre
#     window_height = 250  # Remplacez par la hauteur souhaitée de la fenêtre
#     x = (screen_width // 2) - (window_width // 2)
#     y = (screen_height // 2) - (window_height // 2)

#     # Définissez les dimensions et la position de la fenêtre
#     root.geometry(f"{window_width}x{window_height}+{x}+{y}")


#         # Augmentez la largeur des menus déroulants
#     menu_width = 17  # Vous pouvez ajuster cette valeur en fonction de vos besoins

#     # Menu déroulant pour la catégorie
#     game.category_dropdown.config(width=menu_width)

#     # Menu déroulant pour le sens de la traduction
#     game.translation_direction_dropdown.config(width=menu_width)

#     start_button_width = 10  # Vous pouvez ajuster cette valeur en fonction de vos besoins
#     start_button_height =1  # Vous pouvez ajuster cette valeur en fonction de vos besoins
#     game.start_button.config(width=start_button_width, height=start_button_height)
#     game.start_button.pack(pady=15)

#     root.mainloop()
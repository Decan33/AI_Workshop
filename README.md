# AI_Workshop

https://deepnote.com/workspace/ai-workshop-00bcbb34-42c8-4d83-a7ca-c6dbc20ed32f/project/material-project-373b239b-f978-44e3-a6c4-387718ef1571/notebook/material-project-6f0838106c524ecbb96f8d965a8cf9fe

# Autorzy

- Kacper Cygan (@decan33)
- Krzysztof Klimczyk (@bxo11)
- Krzysztof Kubit (@KrzQbt)

## Klasyfikacja materiałów jako izolator, ~~półprzewodnik~~, lub przewodnik bez użycia cechy "band gap"

### Realizacja Celów Projektowych

1. **Definicja Celów Projektu**  
    Głównym celem tego projektu jest stworzenie modelu sztucznej inteligencji, który może przewidywać, czy dany materiał jest izolatorem, półprzewodnikiem, czy przewodnikiem na podstawie dostępnych danych strukturalnych i chemicznych, bez bezpośredniego uwzględnienia wartości przerwy energetycznej (band gap). Celem jest przyspieszenie procesu identyfikacji właściwości materiałów.

2. **Określenie Wskaźników Sukcesu**  
    - Dokładność modelu w klasyfikowaniu materiałów jako izolatory, półprzewodniki lub przewodniki.  
    - Zdolność modelu do generalizacji na materiały nieobecne w danych treningowych.

3. **Wyznaczenie Zakresu Projektu**  
   - Zbieranie i przygotowanie danych z Materials Project.  
   - Rozwój i trening modelu AI do przewidywania właściwości materiałów.  
   - Walidacja i testowanie modelu na niezależnym zbiorze danych.  
   - Optymalizacja modelu dla lepszej wydajności i dokładności.

4. **Określenie Korzyści z Realizacji**  
   - Przyspieszenie charakteryzacji nowych materiałów.  
   - Zmniejszenie potrzeby eksperymentów fizycznych dzięki wstępnym przewidywaniom AI.
  
### Użyte technologie

- Python
- `pandas`
- `matplotlib`
- `sklearn`
- `FeatureWiz`
- TBA

### Obejrzenie danych oraz ustalenie celow projektowych
1. Sposób użycia danych będzie polegał na sprecyzowaniu wzoru chemicznego "composition" na podstawie którego model określi band gap materiału.
2. Z istniejących rozwiązań dostępnych jest niewiele prostych przykładów, które określają band gap na podstawie struktury materiału. Poza tym istnieje narzędzie "automatminer" - https://hackingmaterials.lbl.gov/automatminer/, które automatycznie dobiera cechy i tworzy model uczenia maszynowego do określania wybranej cechy.

## Struktura Projektu

### `utils`
- `save_to_file.py`: Skrypt do pobierania danych z Materials Project i zapisywania ich do pliku CSV.
- `google_colab_auto_feature_selection.ipynb`: Notebook Google Colab do automatycznego wyboru cech przy użyciu FeatureWiz.
- `google_colab_auto_feature_selection_with_structure.ipynb`: Notebook Google Colab do automatycznego wyboru cech z uwzględnieniem struktury materiałów.

### `ml`
- `random_forest_regression.ipynb`: Notebook do regresji z użyciem lasu losowego na podstawie wybranych cech.
- `random_forest_regression_with_structure.ipynb`: Notebook do regresji z użyciem lasu losowego z uwzględnieniem struktury materiałów.

### `wyniki`
-

# Zbiór danych

https://next-gen.materialsproject.org/

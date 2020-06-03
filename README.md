Hotfix branch: gałąź odpowiedzialna za najpilniejsze poprawki do programu.

Opisy wprowadzonych zmian w zależności od wersji:
- v0.1 - wprowadzono poprawki na podstawie punktów 1-7 z Uwag.
- v0.2 - utworzono funkcję check_which_button() działającą w zasugerowany sposób (punkt 8 Uwag).
- v0.3 - zapisano bibliotekę zewnętrzną pygame do pliku requirements.txt (punkt 9 Uwag), oraz wprowadzono kolejne poprawki do docstringów zgodnie z punktem 3 (rozbicie opisów na zwięzły opis i dopełnienie, weliminowanie skrótów).
- v0.4 - zmodyfikowano plik judge.py i dodano pętle for z enumerate() w windows.py zgodnie z Uwagami. Dodano poprawki na postawie Uwag drobiazgowych z pliku README.md. Utworzono plik na testy modułu game(na razie tylko szablon).
- v0.5 - poprawiono rozmiary niektórych elementów (klocków, piłki, okna gry).
- v0.6 - poprawiono zachowanie piłki po kolizji z klockami, rozbudowano szablony testów.
- v0.7 - zmieniono implementację kodu odpowiedzialnego za menu w grze (stworzono odzielną klasę).
- v0.7.1 - dalsze modyfikacje menusów: modyfikacja sposobu wywoływania menu w grze.
- v0.8 - poprawki do Uwag drobiazgowych z pliku README.md.
- v0.9 - rozbudowano testy dla głównych modułów
- v0.9.1 - zmieniono nazwy testów, usunięto docstringi, wymienione w Uwagach testy, oraz docstringi. Wprowadzono nazwane stałe. Dodano klasę Fonts w module constants ładującą czcionki. Zmieniono nazwę zmiennej przechowującą liczbę żyć.

Required_elements branch: gałąź z implementacjami wymaganych elementów do projektu

Opisy wprowadzonych zmian w zależności od wersji:
- v0.1 - utworzenie nowego modułu na klasy wyjątków i stworzenie klasy głównej wyjątków.
- v0.2 - zawarcie w programie mechanizm List comprehensions do tworzenia listy obiektów typu Block.
- v0.3 - usunięcie modułu na klasy wyjątków (skoro nie jest konieczna ich implementacja to nie dodaję ich na siłę).

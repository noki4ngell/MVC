\# System zarządzania cyfrową biblioteką (Projekt MVC)



\## Spis treści

1\. \[Opis projektu](#opis-projektu)

2\. \[Funkcjonalności](#funkcjonalności)

3\. \[Wykorzystane technologie](#wykorzystane-technologie)

4\. \[Instrukcja uruchomienia](#instrukcja-uruchomienia)

5\. \[Struktura architektoniczna MVC](#struktura-architektoniczna-mvc)



\---



\## Opis projektu

Projekt zaliczeniowy realizuje system zarządzania cyfrową biblioteką. Aplikacja została zbudowana w oparciu o wzorzec architektoniczny MVC (Model-View-Controller) za pomocą frameworka Django (w nomenklaturze Django: Model-Template-View). System pozwala na wygodne zarządzanie bazą książek oraz powiązanych z nimi autorów.



\## Funkcjonalności

Aplikacja została rozbudowana pod kątem wymagań na ocenę wyższą niż 3.0:

\* \*\*Zarządzanie książkami (Pełny CRUD):\*\* Możliwość przeglądania listy, podglądu szczegółów, dodawania oraz edycji książek.

\* \*\*Rozbudowana struktura modeli (Wymaganie na wyższą ocenę):\*\* Zamiast jednego modelu tekstowego wprowadzono relację powiązaną. Zaimplementowano modele `Book` (Książka), `Author` (Autor) oraz strukturę pod model `Loan` (Wypożyczenie) powiązane relacjami bazodanowymi typu ForeignKey.

\* \*\*Walidacja danych (Wymaganie na wyższą ocenę):\*\* Wdrożono walidację po stronie klienta (HTML5/Bootstrap) oraz zaawansowaną walidację biznesową po stronie serwera (np. skrypt blokuje możliwość wpisania roku wydania z przyszłości lub lat ujemnych).

\* \*\*Nowoczesny interfejs (Wymaganie na wyższą ocenę):\*\* Schludny, responsywny wygląd strony zrealizowany przy użyciu frameworka Bootstrap 5 (tabele, karty, ostylowane formularze).



\## Wykorzystane technologie

\* \*\*Backend:\*\* Python 3.12, Django Framework

\* \*\*Frontend:\*\* HTML5, Bootstrap 5

\* \*\*Baza danych:\*\* SQLite (wbudowana, plikowa)



\## Instrukcja uruchomienia



\### Wymagania wstępne

Upewnij się, że na komputerze zainstalowany jest Python w wersji 3.8 lub nowszej.



\### Kroki do uruchomienia:



1\. \*\*Sklonuj repozytorium na swój komputer:\*\*

&#x20;  ```bash

&#x20;  git clone \[https://github.com/TWOJ-LOGIN/TWOJE-REPO.git](https://github.com/TWOJ-LOGIN/TWOJE-REPO.git)

&#x20;  cd LibraryProject


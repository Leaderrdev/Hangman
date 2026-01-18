HANGMAN AUTOMATIZAT
MODUL DE RULARE

Proiectul este scris în Python și este format dintr-un singur fișier. Pentru a rula programul este suficient să fie instalat Python 3. Fișierul cu codul și fișierul jocuri.txt trebuie puse în același folder, după care programul se rulează dintr-un IDE sau din linia de comandă. La finalul rulării se generează fișierul rezultate.txt, în care sunt salvate rezultatele obținute.

CUM FUNCȚIONEAZĂ PROIECTUL

Programul citește jocurile din fișierul de intrare și verifică dacă fiecare linie respectă formatul cerut. Pentru fiecare joc se pornește de la un pattern inițial, unde literele necunoscute sunt marcate cu *. Pe parcurs, sunt reținute literele ghicite corect și cele greșite. Lista de cuvinte posibile este filtrată constant în funcție de informațiile cunoscute, iar la fiecare pas se alege litera care apare cel mai des în pozițiile încă necunoscute. După fiecare încercare, pattern-ul este actualizat și procesul continuă până când cuvântul este ghicit complet sau nu mai există variante valide.

FORMATUL FIȘIERULUI rezultate.txt

Fișierul de ieșire conține pentru fiecare joc: id-ul jocului, numărul de încercări făcute, cuvântul final obținut, statusul jocului (rezolvat sau nu) și lista literelor încercate în ordine.

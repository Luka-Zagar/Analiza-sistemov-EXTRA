## Analiza neznanega dinamičnega sistema (črna škatlica)

V nalogi pri predmetu **Analiza sistemov** je obravnavan neznan električni sistem (»črna škatlica«), ki vsebuje tuljavo, kondenzator, tri upornike ter konstantni tokovni in napetostni vir. Na podlagi podanih časovnih odzivov toka skozi tuljavo in napetosti na kondenzatorju po sklenitvi zunanjega stikala je bila izvedena identifikacija strukture in parametrov vezja.

Iz oblike odzivov je razvidno, da gre za **stabilen RLC sistem drugega reda z dušenimi oscilacijami**. Končne (asimptotske) vrednosti omogočajo določitev stacionarnega stanja, začetne vrednosti pa sklepanje o začetnih pogojih sistema. Na tej osnovi je bil izpeljan model v prostoru stanj, določen izbor elementov in njihove vrednosti ter preverjena skladnost s simulacijo.

Numerična simulacija sistema z izpeljanimi enačbami stanja potrjuje pravilnost izbrane konfiguracije, saj se simulirani odzivi ujemajo s podanimi grafi tako v prehodnem kot v stacionarnem delu.

### Simulirani odzivi sistema

![Simulacija sistema](vizualizacija.png)

## Orodja

- Python 3
- NumPy
- SciPy
- Matplotlib

## Avtor

Luka Žagar  
Fakulteta za elektrotehniko  
Predmet: Analiza sistemov

# Analiza neznanega dinamičnega sistema (črna škatlica)

## Opis naloge

Pri predmetu **Analiza sistemov** je bila podana dodatna naloga, v kateri obravnavamo t. i. *črno škatlico* z neznanim električnim vezjem. Vezje vsebuje:

- **1 tuljavo (L)**
- **1 kondenzator (C)**
- **3 upornike (R1, R2, R3)**
- **1 konstantni napetostni vir (u_g)**
- **1 konstantni tokovni vir (i_g)**

Topologija vezja je delno znana, vendar položaji elementov na mestih `a, b, c, d` niso vnaprej določeni. Na mestih `s1` in `s2` se nahajata vira, na mestu `e` pa je znan upor `R3`.  
Po sklenitvi zunanjega stikala sta bila izmerjena in podana grafa:

- tok skozi tuljavo \( i_L(t) \)
- napetost na kondenzatorju \( v_C(t) \)

Naloga je zahtevala:
- določitev **postavitve elementov**,
- identifikacijo **vrednosti elementov**,
- preverjanje **unikatnosti rešitve**,
- ter utemeljitev izločitve neustreznih konfiguracij.

---

## Razpoložljivi elementi

| Element | Možne vrednosti |
|-------|----------------|
| L | 0.5 H ali 1.5 H |
| C | 0.7 F ali 1.3 F |
| R1 | 2 Ω ali 4 Ω |
| R2 | 1.6 Ω ali 2.4 Ω |
| R3 | 1 Ω |
| \( i_g \) | 3 A |
| \( u_g \) | 5 V |

Pomemben namig pri nalogi je bil, da **zamenjava položajev R1 in R2 ne vpliva na začetne vrednosti odzivov**, kar bistveno zmanjša število smiselnih kombinacij.

---

## Analiza grafov in sklepanje

Iz podanih grafov je bilo možno razbrati naslednje lastnosti sistema:

- odziv je **oscilatoren z dušenjem**, kar jasno kaže na **RLC sistem 2. reda**,
- sistem je **stabilen** (lastne vrednosti imajo negativen realni del),
- iz končnih vrednosti je možno določiti **stacionarno stanje**,
- začetni pogoji niso ničelni → sistem je bil pred sklenitvijo stikala v drugem ravnotežju.

### Asimptotske vrednosti
Iz grafov:
- \( i_L(\infty) \approx -2.5 \, \text{A} \)
- \( v_C(\infty) \approx -5 \, \text{V} \)

Te vrednosti so bile uporabljene za preverjanje pravilnosti izbranih parametrov in strukture enačb stanja.

---

## Matematični model

Iz izbrane konfiguracije vezja je bil izpeljan **model v prostoru stanj**:

\[
\dot{x}(t) = A x(t) + B u
\]

kjer je:
\[
x(t) = 
\begin{bmatrix}
i_L(t) \\
v_C(t)
\end{bmatrix}, 
\quad
u =
\begin{bmatrix}
i_g \\
u_g
\end{bmatrix}
\]

### Izbrane vrednosti elementov

- \( L = 0.5 \, \text{H} \)
- \( C = 1.3 \, \text{F} \)
- \( R_1 = 2.0 \, \Omega \)
- \( R_2 = 2.4 \, \Omega \)
- \( i_g = 3 \, \text{A} \)
- \( u_g = 5 \, \text{V} \)

### Matrike sistema

\[
A =
\begin{bmatrix}
0 & -\frac{1}{L} \\
\frac{1}{C} & -\frac{1}{C(R_1+R_2)}
\end{bmatrix}
\quad
B =
\begin{bmatrix}
0 & -\frac{1}{L} \\
\frac{R_1}{C(R_1+R_2)} & 0
\end{bmatrix}
\]

Začetni pogoji so bili **odčitani neposredno iz grafov**:
\[
i_L(0) = -1.13 \, \text{A}, \quad v_C(0) = -5.0 \, \text{V}
\]

---

## Numerična simulacija

Za simulacijo je bila uporabljena funkcija `solve_ivp` iz knjižnice **SciPy**, ki numerično rešuje sistem navadnih diferencialnih enačb.

Simulacija potrdi:
- pravilno obliko prehodnega pojava,
- ujemanje dušenja in frekvence,
- pravilne asimptotske vrednosti.

---

## Rezultati

Spodaj je prikazan simuliran odziv sistema skupaj z označenimi asimptotami:

![Simulacija sistema](vizualizacija.png)

---

## Sklep

Z uporabo:
- analize prehodnih odzivov,
- stacionarnih vrednosti,
- znanja o RLC sistemih 2. reda,
- ter modeliranja v prostoru stanj,

je bilo možno **enolično določiti konfiguracijo in vrednosti elementov** neznanega vezja. Naloga se izogne popolni kombinatorični eksploziji z uporabo fizikalnega razumevanja sistema in danega namiga o zamenljivosti uporov R1 in R2.

Rešitev je bila potrjena tako analitično kot numerično s simulacijo.

---

## Orodja

- Python 3
- NumPy
- SciPy
- Matplotlib

---

## Avtor

Luka Žagar  
Fakulteta za elektrotehniko  
Predmet: Analiza sistemov

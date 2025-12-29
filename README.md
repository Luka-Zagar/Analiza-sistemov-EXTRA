# ANALIZA SISTEMOV: Identifikacija parametrov in topologije vezja "ČRNE ŠKATLICE"

Ta repozitorij vsebuje rešitev dodatne naloge pri predmetu **Analiza sistemov**. Projekt zajema "reverse engineering" (obratni inženiring) neznanega električnega vezja na podlagi vhodno-izhodnih podatkov, omejene topologije in delnih informacij o komponentah.

![Rezultat simulacije](vizualizacija.png)
*(Opomba: Zgornji graf prikazuje ujemanje simuliranega odziva z asimptotami sistema)*

## Opis problema

Naloga predstavlja "črno škatlico" z delno znano shemo, ki vsebuje:
*   **Elemente:** 1x kondenzator ($C$), 1x tuljava ($L$), 3x uporniki ($R_1, R_2, R_3$).
*   **Vire:** 1x tokovni vir ($i_g$), 1x napetostni vir ($v_g$).
*   **Neznanke:** Pozicije elementov $a, b, c, d$ ter virov $s1, s2$ niso določene.
*   **Odziv:** Sistem generira dva grafa časovnega poteka: tok skozi tuljavo $i_L(t)$ in napetost na kondenzatorju $v_C(t)$.

Cilj naloge je bil določiti točno postavitev elementov in njihove vrednosti iz končnega nabora možnih vrednosti, pri čemer so bile ključne informacije skrite v obliki prehodnega pojava in stabilnega stanja.

## 🔍 Metodologija reševanja

Reševanje je potekalo v treh fazah: topološka analiza, določitev parametrov in validacija s simulacijo.

### 1. Topološka analiza in izločanje
Na podlagi "skritega namiga" v navodilih (*če bi bila položaja $R_1$ in $R_2$ zamenjana, se grafi ne bi spremenili*), smo lahko drastično zmanjšali število možnih kombinacij. Ta simetrija nakazuje, da $R_1$ in $R_2$ nastopata v vezju na način, kjer njuna vsota ali produkt določa časovno konstanto oz. dušenje (npr. zaporedna vezava v isti zanki s kondenzatorjem).

Z analizo vezave smo postavili hipotezo:
*   **Zanka 1:** Vsebuje vir in RLC elemente, ki povzročajo nihanje.
*   **Zanka 2:** Vsebuje vir in upor $R_3$ (znana pozicija $e$).

### 2. Matematično modeliranje (Prostor stanj)
Za izbrano konfiguracijo smo zapisali enačbe vezja in jih prevedli v model prostora stanj oblike:

$$ \dot{\mathbf{x}}(t) = \mathbf{A}\mathbf{x}(t) + \mathbf{B}\mathbf{u}(t) $$
$$ \mathbf{y}(t) = \mathbf{C}\mathbf{x}(t) + \mathbf{D}\mathbf{u}(t) $$

Kjer je vektor stanj $\mathbf{x} = [i_L, v_C]^T$. Na podlagi Kirchhoffovih zakonov za končno vezje smo izpeljali sistemsko matriko $\mathbf{A}$:

$$
\mathbf{A} = \begin{bmatrix}
0 & -\frac{1}{L} \\
\frac{1}{C} & -\frac{1}{C(R_1+R_2)}
\end{bmatrix}
$$

Iz te matrike je razvidno, da vsota $R_1 + R_2$ določa realni del lastnih vrednosti (dušenje), kar potrjuje namig o simetriji zamenjave upornikov.

### 3. Identifikacija parametrov
S primerjavo karakterističnih lastnosti grafov (frekvenca nihanja, hitrost dušenja, končne vrednosti) in nabora dovoljenih vrednosti, smo določili optimalne parametre:
*   **Induktivnost:** $L = 0.5 \text{ H}$
*   **Kapacitivnost:** $C = 1.3 \text{ F}$
*   **Upornosti:** $R_1 = 2.0 \, \Omega, R_2 = 2.4 \, \Omega$ (vrstni red zamenljiv)
*   **Viri:** $v_g = 5 \text{ V}, i_g = 3 \text{ A}$

## Implementacija

Rešitev je implementirana v jeziku **Python** z uporabo knjižnic `NumPy` za matrične operacije in `SciPy` (`solve_ivp`) za numerično reševanje diferencialnih enačb.

Ključni del kode, ki definira dinamiko sistema:

```python
# Matrika sistema A
A = np.array([
    [0,  -1/L],
    [1/C,  -1/(C*(R1+R2))]
])

# Vektor vhodov B (vpliv virov)
B = np.array([
    [0,  -1/L],
    [R1/(C*(R1+R2)),  0]
])
```

## Rezultati

Končna simulacija (prikazana na vrhu dokumenta) kaže popolno ujemanje s pričakovanimi teoretičnimi lastnostmi:
1.  **Dušeno nihanje:** Sistem je stabilen, pod-dušen (konjugirano kompleksni pol).
2.  **Asimptote:**
    *   Tok tuljave konvergira k $-2.5 \text{ A}$.
    *   Napetost kondenzatorja konvergira k $-5.0 \text{ V}$.

## Navodila za pogon

Za zagon simulacije in izris grafov potrebujete nameščen Python in naslednje knjižnice:

```bash
pip install numpy scipy matplotlib
```

Zagon skripte:
```bash
python dodatna_naloga.py
```

---
**Avtor rešitve:** [Tvoje Ime]
**Predmet:** Analiza sistemov
**Leto:** 2025

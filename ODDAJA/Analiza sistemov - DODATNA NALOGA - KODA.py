import numpy as np
from scipy import integrate
from matplotlib import pyplot as pp
from matplotlib.font_manager import FontProperties

font = FontProperties(family='sans-serif', weight='bold', size=11)

# --- PARAMETRI NEZNANIH ELEMENTOV (L, C, R1, R2, R3, ig, ug) ---
# "a" - upor R1
# "b" - kondenzator C
# "c" - upor R2
# "d" - tuljava L
# "e" - upor R3 (določena vrednost)

# "s1" - napetostni vir ug (določena vrednost)
# "s2" - tokovni vir ig (določena vrednost)

L = 0.5 # H      
C = 1.3 # F  

R1 = 2.0  # Ω      
R2 = 2.4  # Ω

# --- MATRIKE ENAČBE STANJ ---
A = np.array([
    [0,  -1/L],
    [1/C,  -1/(C*(R1+R2))]
])

B = np.array([
    [0,  -1/L],
    [R1/(C*(R1+R2)),  0]
])

# --- VEKTOR VZBUJANJA (konstantna vira) ---
u_const = np.array([3.0, 5.0]) # [ig, ug] 

# --- ZAČETNI POGOJI (podatki odčitani iz grafa) ---
x0 = np.array([-1.13, -5.0]) # [iL(0), uC(0)]]

def model(t, x):
    return A @ x + B @ u_const

# --- SIMULACIJA ---
t_start = 0
t_stop = 30

t_eval = np.linspace(t_start, t_stop, 1000) # (start, stop, number of samples)
solve = integrate.solve_ivp(model, (t_start, t_stop), x0, t_eval=t_eval)

# --- VIZUALIZACIJA ---
fig, (ax1, ax2) = pp.subplots(2, 1, figsize=(10, 8), sharex=True, dpi=100)

# iL graf (Tok skozi tuljavo)
ax1.plot(solve.t, solve.y[0], color='navy', lw=2, label='simulacija $i_L(t)$')
ax1.axhline(-2.5, color='r', linestyle='--', label='asimptota (-2.5A)') # Teoretična vrednost
ax1.set_ylabel("tok $i_L$ [A]")
ax1.set_title("TOK SKOZI TULJAVO, KO SKLENEMO ZUNANJE STIKALO", fontproperties=font)
ax1.grid(True, linestyle=':', alpha=0.7)
ax1.legend(loc='upper right')

# vC graf (Napetost na kondenzatorju) [cite: 52]
ax2.plot(solve.t, solve.y[1], color='darkorange', lw=2, label='simulacija $v_C(t)$')
ax2.axhline(-5.0, color='r', linestyle='--', label='asimptota (-5V)')
ax2.set_ylabel("napetost $v_C$ [V]")
ax2.set_xlabel("čas $t$ [s]")
ax2.set_title("NAPETOST NA KONDEZATORJU, KO SKLENEMO ZUNANJE STIKALO", fontproperties=font)
ax2.grid(True, linestyle=':', alpha=0.7)
ax2.legend(loc='upper right')

pp.tight_layout()
pp.show()

# PREDHODNI TEST s KONFIGURACIJO
# "a" - upor R1
# "b" - tuljava L
# "c" - upor R2
# "d" - kondenzator C
# "e" - upor R3 (določena vrednost)

# "s1" - napetostni vir ug (določena vrednost)
# "s2" - tokovni vir ig (določena vrednost)

# --- MATRIKE ENAČBE STANJ ---
# A = np.array([
#    [0,  -1/L],
#    [1/C,  -1/(C*(R1+R2))]
# ])

# B = np.array([
#    [0,  -1/L],
#    [-R2/(C*(R1+R2)),  -1/(C*(R1+R2))]
# ])'''
import numpy as np
from scipy import linalg, integrate
from matplotlib import pyplot as pp
from matplotlib.font_manager import FontProperties

# Nastavitve pisave
font = FontProperties(family='sans-serif', weight='normal', size=11)

def numericna_resitev_ivp(A, B, u, x_0, t):
    """Numerična rešitev sistema DE 1. reda z uporabo solve_ivp."""
    f = lambda t, x: np.dot(A, x) + np.dot(B, u(t))
    solver = integrate.solve_ivp(f, (t[0], t[-1]), x_0, t_eval=t, method='RK45')
    return solver.y

def izris_loceno(t, x, naslov):
    """Izris toka in napetosti v dveh ločenih grafih, enega pod drugim."""
    fig, (ax1, ax2) = pp.subplots(2, 1, figsize=(10, 8), sharex=True, dpi=100)
    
    # Prvi graf: Tok skozi tuljavo
    ax1.plot(t, x[0,:], label=r"$i_L(t)$", color='#1f77b4', linewidth=2)
    ax1.set_ylabel("Tok [A]", fontproperties=font)
    ax1.set_title(naslov, fontproperties=font)
    ax1.grid(True, linestyle=':', alpha=0.6)
    ax1.legend(loc='upper right')
    
    # Drugi graf: Napetost na kondenzatorju
    ax2.plot(t, x[1,:], label=r"$v_C(t)$", color='#ff7f0e', linewidth=2)
    ax2.set_ylabel("Napetost [V]", fontproperties=font)
    ax2.set_xlabel("Čas [s]", fontproperties=font)
    ax2.grid(True, linestyle=':', alpha=0.6)
    ax2.legend(loc='upper right')
    
    pp.tight_layout()
    pp.show()

# --- PARAMETRI SISTEMA ---
L = 0.5  
C = 1.3  
R1 = 4.0  
R2 = 1.6  

# Matrike prostora stanj (izpeljane iz vezja)
A = np.array([[0, 1/L], 
              [-1/C, -1/(C * (R1 + R2))]])

B = np.array([[-1/L, 0], 
              [1/(C * (R1 + R2)), R1/(C * (R1 + R2))]])

# Začetni pogoji (prebrano iz grafov ob t=0)
# iL(0) je cca -1.2 A, vC(0) je -5.0 V
x_0 = np.array([-1.2, -5.0]) 

# Vzbujanje (v_g = 5V, i_g = 3A)
u = lambda t: np.array([5.0, 3.0])

# Časovni interval simulacije
t = np.linspace(0, 30, 1000)

# Izračun rešitve
x_resitev = numericna_resitev_ivp(A, B, u, x_0, t)

# Izris rezultatov
izris_loceno(t, x_resitev, "Časovni odziv stanja sistema (ločena prikaza)")
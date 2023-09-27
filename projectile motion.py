import numpy as np
import matplotlib.pyplot as plt

# Variabel dan Konstanta
m = 1    # Massa dalam kg
v0 = 10    # Kec. Awal dalam m/s
theta = 45    # Sudut peluncuran dalam derajat
g = 9.8    # Percepatan gravitasi dalam m/s^2

# Menghitung lintasan proyektil (Gerak Parabola)
theta = np.radians(theta)
t_max = 2*v0*np.sin(theta)/g    # Time of flight
t = np.linspace(0, t_max, 1000)    # Time array
x = v0*np.cos(theta)*t    # X position array
y = v0*np.sin(theta)*t - 0.5*g*t**2    # Y position array

# Plot grafik
fig, ax = plt.subplots()
ax.plot(x, y, label='Projectile Motion')
ax.set_xlabel('X Position (m)')
ax.set_ylabel('Y Position (m)')
ax.set_title('Projectile Motion')
ax.legend()
plt.show()

import numpy as np
import matplotlib.pyplot as plt

# Example altitude levels (in meters)
altitudes = np.linspace(0, 12000, 100)  # from surface to 12 km

# Example temperature profiles (in K)
T_parcel = 300 - 0.0065 * altitudes  # air parcel temperature decreases with altitude
T_env = 300 - 0.007 * altitudes      # environmental temperature (cooler at a higher rate)

# Calculate temperature difference (parcel - environment)
temp_diff = T_parcel - T_env

# Calculate buoyancy (CAPE where positive, CINH where negative)
g = 9.81  # gravity (m/s^2)
CAPE = np.maximum(g * temp_diff / T_env, 0)  # CAPE where temp_diff is positive
CINH = np.minimum(g * temp_diff / T_env, 0)  # CINH where temp_diff is negative

# Visualize the results
fig, ax1 = plt.subplots(figsize=(6, 8))

# Plot temperature profiles
ax1.plot(T_parcel, altitudes / 1000, 'r-', label='Parcel Temperature (K)')
ax1.plot(T_env, altitudes / 1000, 'b--', label='Environment Temperature (K)')
ax1.set_xlabel('Temperature (K)')
ax1.set_ylabel('Altitude (km)')
ax1.legend(loc='upper right')
ax1.grid(True)

# Twin axis for CAPE and CINH
ax2 = ax1.twiny()
ax2.plot(CAPE, altitudes / 1000, 'g-', label='CAPE (Buoyancy)')
ax2.plot(CINH, altitudes / 1000, 'm-', label='CINH (Inhibition)')
ax2.set_xlabel('CAPE / CINH (J/kg)')
ax2.legend(loc='lower right')

plt.title('Vertical Profile of CAPE and CINH')
plt.show()

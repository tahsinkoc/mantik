import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt
# Fren pedalı basma seviyesi
brake_pedal = ctrl.Consequent(np.arange(0, 101, 1), 'Fren Pedalı Basma Seviyesi')
brake_pedal['düşük'] = fuzz.trimf(brake_pedal.universe, [0, 0, 50])
brake_pedal['orta'] = fuzz.trimf(brake_pedal.universe, [25, 50, 75])
brake_pedal['yüksek'] = fuzz.trimf(brake_pedal.universe, [50, 100, 100])

# Gaz pedalı basma seviyesi
accelerator_pedal = ctrl.Consequent(np.arange(0, 101, 1), 'Gaz Pedalı Basma Seviyesi')
accelerator_pedal['düşük'] = fuzz.trimf(accelerator_pedal.universe, [0, 0, 50])
accelerator_pedal['orta'] = fuzz.trimf(accelerator_pedal.universe, [25, 50, 75])
accelerator_pedal['yüksek'] = fuzz.trimf(accelerator_pedal.universe, [50, 100, 100])

# Klima şiddeti
ac_intensity = ctrl.Consequent(np.arange(0, 101, 1), 'Klima Şiddeti')
ac_intensity['düşük'] = fuzz.trimf(ac_intensity.universe, [0, 0, 50])
ac_intensity['orta'] = fuzz.trimf(ac_intensity.universe, [25, 50, 75])
ac_intensity['yüksek'] = fuzz.trimf(ac_intensity.universe, [50, 100, 100])

# Far ayarı
headlight_setting = ctrl.Consequent(np.arange(0, 101, 1), 'Far Ayarı')
headlight_setting['düşük'] = fuzz.trimf(headlight_setting.universe, [0, 0, 50])
headlight_setting['orta'] = fuzz.trimf(headlight_setting.universe, [25, 50, 75])
headlight_setting['yüksek'] = fuzz.trimf(headlight_setting.universe, [50, 100, 100])

# Lastik basıncı uyarı göstergesi
tire_pressure_warning = ctrl.Consequent(np.arange(0, 31, 1), 'Lastik Basıncı Uyarı Göstergesi')
tire_pressure_warning['düşük'] = fuzz.trimf(tire_pressure_warning.universe, [0, 0, 15])
tire_pressure_warning['orta'] = fuzz.trimf(tire_pressure_warning.universe, [10, 15, 20])
tire_pressure_warning['yüksek'] = fuzz.trimf(tire_pressure_warning.universe, [15, 30, 30])

# Üyelik grafiği
fig, ((ax0, ax1), (ax2, ax3), (ax4, _)) = plt.subplots(nrows=3, ncols=2, figsize=(12, 12))

# Fren pedalı basma seviyesi grafiği
ax0.plot(brake_pedal.universe, fuzz.trimf(brake_pedal.universe, [0, 0, 50]), 'b', linewidth=1.5, label='Düşük')
ax0.plot(brake_pedal.universe, fuzz.trimf(brake_pedal.universe, [25, 50, 75]), 'g', linewidth=1.5, label='Orta')
ax0.plot(brake_pedal.universe, fuzz.trimf(brake_pedal.universe, [50, 100, 100]), 'r', linewidth=1.5, label='Yüksek')
ax0.fill_between(brake_pedal.universe, fuzz.trimf(brake_pedal.universe, [0, 0, 50]), color='blue', alpha=0.2)
ax0.fill_between(brake_pedal.universe, fuzz.trimf(brake_pedal.universe, [25, 50, 75]), color='green', alpha=0.2)
ax0.fill_between(brake_pedal.universe, fuzz.trimf(brake_pedal.universe, [50, 100, 100]), color='red', alpha=0.2)
ax0.set_title('Fren Pedalı Basma Seviyesi')
ax0.legend()

# Gaz pedalı basma seviyesi grafiği
ax1.plot(accelerator_pedal.universe, fuzz.trimf(accelerator_pedal.universe, [0, 0, 50]), 'b', linewidth=1.5, label='Düşük')
ax1.plot(accelerator_pedal.universe, fuzz.trimf(accelerator_pedal.universe, [25, 50, 75]), 'g', linewidth=1.5, label='Orta')
ax1.plot(accelerator_pedal.universe, fuzz.trimf(accelerator_pedal.universe, [50, 100, 100]), 'r', linewidth=1.5, label='Yüksek')
ax1.fill_between(accelerator_pedal.universe, fuzz.trimf(accelerator_pedal.universe, [0, 0, 50]), color='blue', alpha=0.2)
ax1.fill_between(accelerator_pedal.universe, fuzz.trimf(accelerator_pedal.universe, [25, 50, 75]), color='green', alpha=0.2)
ax1.fill_between(accelerator_pedal.universe, fuzz.trimf(accelerator_pedal.universe, [50, 100, 100]), color='red', alpha=0.2)
ax1.set_title('Gaz Pedalı Basma Seviyesi')
ax1.legend()

# Klima şiddeti grafiği
ax2.plot(ac_intensity.universe, fuzz.trimf(ac_intensity.universe, [0, 0, 50]), 'b', linewidth=1.5, label='Düşük')
ax2.plot(ac_intensity.universe, fuzz.trimf(ac_intensity.universe, [25, 50, 75]), 'g', linewidth=1.5, label='Orta')
ax2.plot(ac_intensity.universe, fuzz.trimf(ac_intensity.universe, [50, 100, 100]), 'r', linewidth=1.5, label='Yüksek')
ax2.fill_between(ac_intensity.universe, fuzz.trimf(ac_intensity.universe, [0, 0, 50]), color='blue', alpha=0.2)
ax2.fill_between(ac_intensity.universe, fuzz.trimf(ac_intensity.universe, [25, 50, 75]), color='green', alpha=0.2)
ax2.fill_between(ac_intensity.universe, fuzz.trimf(ac_intensity.universe, [50, 100, 100]), color='red', alpha=0.2)
ax2.set_title('Klima Şiddeti')
ax2.legend()

# Far ayarı grafiği
ax3.plot(headlight_setting.universe, fuzz.trimf(headlight_setting.universe, [0, 0, 50]), 'b', linewidth=1.5, label='Düşük')
ax3.plot(headlight_setting.universe, fuzz.trimf(headlight_setting.universe, [25, 50, 75]), 'g', linewidth=1.5, label='Orta')
ax3.plot(headlight_setting.universe, fuzz.trimf(headlight_setting.universe, [50, 100, 100]), 'r', linewidth=1.5, label='Yüksek')
ax3.fill_between(headlight_setting.universe, fuzz.trimf(headlight_setting.universe, [0, 0, 50]), color='blue', alpha=0.2)
ax3.fill_between(headlight_setting.universe, fuzz.trimf(headlight_setting.universe, [25, 50, 75]), color='green', alpha=0.2)
ax3.fill_between(headlight_setting.universe, fuzz.trimf(headlight_setting.universe, [50, 100, 100]), color='red', alpha=0.2)
ax3.set_title('Far Ayarı')
ax3.legend()

# Lastik basıncı uyarı göstergesi grafiği
ax4.plot(tire_pressure_warning.universe, fuzz.trimf(tire_pressure_warning.universe, [0, 0, 15]), 'b', linewidth=1.5, label='Düşük')
ax4.plot(tire_pressure_warning.universe, fuzz.trimf(tire_pressure_warning.universe, [10, 15, 20]), 'g', linewidth=1.5, label='Orta')
ax4.plot(tire_pressure_warning.universe, fuzz.trimf(tire_pressure_warning.universe, [15, 30, 30]), 'r', linewidth=1.5, label='Yüksek')
ax4.fill_between(tire_pressure_warning.universe, fuzz.trimf(tire_pressure_warning.universe, [0, 0, 15]), color='blue', alpha=0.2)
ax4.fill_between(tire_pressure_warning.universe, fuzz.trimf(tire_pressure_warning.universe, [10, 15, 20]), color='green', alpha=0.2)
ax4.fill_between(tire_pressure_warning.universe, fuzz.trimf(tire_pressure_warning.universe, [15, 30, 30]), color='red', alpha=0.2)
ax4.set_title('Lastik Basıncı Uyarı Göstergesi')
ax4.legend()

# Boş eksenlerin kaldırılması
plt.delaxes(ax=_)

plt.tight_layout()
plt.show()

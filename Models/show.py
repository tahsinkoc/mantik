import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# Hız
speed = ctrl.Antecedent(np.arange(0, 201, 1), 'Aracın hızı')
speed['çok_yavaş'] = fuzz.trimf(speed.universe, [0, 0, 100])
speed['orta'] = fuzz.trimf(speed.universe, [50, 100, 150])
speed['çok_hızlı'] = fuzz.trimf(speed.universe, [100, 200, 200])

# Nem
moisture = ctrl.Antecedent(np.arange(0, 101, 1), 'Nem %')
moisture['Az Nemli'] = fuzz.trimf(moisture.universe, [0, 0, 50])
moisture['Orta Nemli'] = fuzz.trimf(moisture.universe, [25, 50, 75])
moisture['Çok Nemli'] = fuzz.trimf(moisture.universe, [50, 100, 100])

# Sıcaklık
temperature = ctrl.Antecedent(np.arange(0, 51, 1), 'Sıcaklık Celcius')
temperature['Soğuk'] = fuzz.trimf(temperature.universe, [0, 0, 25])
temperature['Sıcak'] = fuzz.trimf(temperature.universe, [10, 25, 40])
temperature['Çok Sıcak'] = fuzz.trimf(temperature.universe, [25, 50, 50])

# Hava Işık
light = ctrl.Antecedent(np.arange(0, 10001, 1), 'Hava Işık')
light['az'] = fuzz.trimf(light.universe, [0, 0, 5000])
light['orta'] = fuzz.trimf(light.universe, [2000, 5000, 8000])
light['çok'] = fuzz.trimf(light.universe, [5000, 10000, 10000])

# Lastik Hava Basıncı
pressure = ctrl.Antecedent(np.arange(0, 31, 1), 'Lastik Hava Basıncı (bar)')
pressure['düşük'] = fuzz.trimf(pressure.universe, [0, 0, 15])
pressure['orta'] = fuzz.trimf(pressure.universe, [10, 15, 20])
pressure['yüksek'] = fuzz.trimf(pressure.universe, [15, 30, 30])


distance = ctrl.Antecedent(np.arange(0,101,1), 'Mesafe (Metre)')
distance['Yakın'] = fuzz.trimf(distance.universe, [0,0,50])
distance['Orta'] = fuzz.trimf(distance.universe, [25, 50, 75])
distance['Uzak'] = fuzz.trimf(distance.universe, [50, 100, 100])

# Çıkış 
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


def Enterence():
    fig, ((ax0, ax1), (ax2, ax3), (ax4, ax5), (ax6, ax7), (ax8, ax9), (ax10, _)) = plt.subplots(nrows=6, ncols=2, figsize=(10, 10), num="Üyelik Fonksiyon Grafikleri")

    # Hız grafiği
    ax0.plot(speed.universe, fuzz.trimf(speed.universe, [0, 0, 100]), 'b', linewidth=1.5, label='Çok Yavaş')
    ax0.plot(speed.universe, fuzz.trimf(speed.universe, [50, 100, 150]), 'g', linewidth=1.5, label='Orta')
    ax0.plot(speed.universe, fuzz.trimf(speed.universe, [100, 200, 200]), 'r', linewidth=1.5, label='Çok Hızlı')
    ax0.fill_between(speed.universe, fuzz.trimf(speed.universe, [0, 0, 100]), color='blue', alpha=0.2)
    ax0.fill_between(speed.universe, fuzz.trimf(speed.universe, [50, 100, 150]), color='green', alpha=0.2)
    ax0.fill_between(speed.universe, fuzz.trimf(speed.universe, [100, 200, 200]), color='red', alpha=0.2)
    ax0.set_title('Aracın Hızı')
    ax0.legend()

    # Nem grafiği
    ax1.plot(moisture.universe, fuzz.trimf(moisture.universe, [0, 0, 50]), 'b', linewidth=1.5, label='Az Nemli')
    ax1.plot(moisture.universe, fuzz.trimf(moisture.universe, [25, 50, 75]), 'g', linewidth=1.5, label='Orta Nemli')
    ax1.plot(moisture.universe, fuzz.trimf(moisture.universe, [50, 100, 100]), 'r', linewidth=1.5, label='Çok Nemli')
    ax1.fill_between(moisture.universe, fuzz.trimf(moisture.universe, [0, 0, 50]), color='blue', alpha=0.2)
    ax1.fill_between(moisture.universe, fuzz.trimf(moisture.universe, [25, 50, 75]), color='green', alpha=0.2)
    ax1.fill_between(moisture.universe, fuzz.trimf(moisture.universe, [50, 100, 100]), color='red', alpha=0.2)
    ax1.set_title('Nem %')
    ax1.legend()

    # Sıcaklık grafiği
    ax2.plot(temperature.universe, fuzz.trimf(temperature.universe, [0, 0, 25]), 'b', linewidth=1.5, label='Soğuk')
    ax2.plot(temperature.universe, fuzz.trimf(temperature.universe, [10, 25, 40]), 'g', linewidth=1.5, label='Sıcak')
    ax2.plot(temperature.universe, fuzz.trimf(temperature.universe, [25, 50, 50]), 'r', linewidth=1.5, label='Çok Sıcak')
    ax2.fill_between(temperature.universe, fuzz.trimf(temperature.universe, [0, 0, 25]), color='blue', alpha=0.2)
    ax2.fill_between(temperature.universe, fuzz.trimf(temperature.universe, [10, 25, 40]), color='green', alpha=0.2)
    ax2.fill_between(temperature.universe, fuzz.trimf(temperature.universe, [25, 50, 50]), color='red', alpha=0.2)
    ax2.set_title('Sıcaklık Celcius')
    ax2.legend()

    # Hava Işık grafiği
    ax3.plot(light.universe, fuzz.trimf(light.universe, [0, 0, 5000]), 'b', linewidth=1.5, label='Az')
    ax3.plot(light.universe, fuzz.trimf(light.universe, [2000, 5000, 8000]), 'g', linewidth=1.5, label='Orta')
    ax3.plot(light.universe, fuzz.trimf(light.universe, [5000, 10000, 10000]), 'r', linewidth=1.5, label='Çok')
    ax3.fill_between(light.universe, fuzz.trimf(light.universe, [0, 0, 5000]), color='blue', alpha=0.2)
    ax3.fill_between(light.universe, fuzz.trimf(light.universe, [2000, 5000, 8000]), color='green', alpha=0.2)
    ax3.fill_between(light.universe, fuzz.trimf(light.universe, [5000, 10000, 10000]), color='red', alpha=0.2)
    ax3.set_title('Hava Işık')
    ax3.legend()

    # Lastik Hava Basıncı grafiği
    ax4.plot(pressure.universe, fuzz.trimf(pressure.universe, [0, 0, 15]), 'b', linewidth=1.5, label='Düşük')
    ax4.plot(pressure.universe, fuzz.trimf(pressure.universe, [10, 15, 20]), 'g', linewidth=1.5, label='Orta')
    ax4.plot(pressure.universe, fuzz.trimf(pressure.universe, [15, 30, 30]), 'r', linewidth=1.5, label='Yüksek')
    ax4.fill_between(pressure.universe, fuzz.trimf(pressure.universe, [0, 0, 15]), color='blue', alpha=0.2)
    ax4.fill_between(pressure.universe, fuzz.trimf(pressure.universe, [10, 15, 20]), color='green', alpha=0.2)
    ax4.fill_between(pressure.universe, fuzz.trimf(pressure.universe, [15, 30, 30]), color='red', alpha=0.2)
    ax4.set_title('Lastik Hava Basıncı (bar)')
    ax4.legend()


    ax5.plot(brake_pedal.universe, fuzz.trimf(brake_pedal.universe, [0, 0, 50]), 'b', linewidth=1.5, label='Düşük')
    ax5.plot(brake_pedal.universe, fuzz.trimf(brake_pedal.universe, [25, 50, 75]), 'g', linewidth=1.5, label='Orta')
    ax5.plot(brake_pedal.universe, fuzz.trimf(brake_pedal.universe, [50, 100, 100]), 'r', linewidth=1.5, label='Yüksek')
    ax5.fill_between(brake_pedal.universe, fuzz.trimf(brake_pedal.universe, [0, 0, 50]), color='blue', alpha=0.2)
    ax5.fill_between(brake_pedal.universe, fuzz.trimf(brake_pedal.universe, [25, 50, 75]), color='green', alpha=0.2)
    ax5.fill_between(brake_pedal.universe, fuzz.trimf(brake_pedal.universe, [50, 100, 100]), color='red', alpha=0.2)
    ax5.set_title('Fren Pedalı Basma Seviyesi ÇIKIŞ')
    ax5.legend()

    # Gaz pedalı basma seviyesi grafiği
    ax6.plot(accelerator_pedal.universe, fuzz.trimf(accelerator_pedal.universe, [0, 0, 50]), 'b', linewidth=1.5, label='Düşük')
    ax6.plot(accelerator_pedal.universe, fuzz.trimf(accelerator_pedal.universe, [25, 50, 75]), 'g', linewidth=1.5, label='Orta')
    ax6.plot(accelerator_pedal.universe, fuzz.trimf(accelerator_pedal.universe, [50, 100, 100]), 'r', linewidth=1.5, label='Yüksek')
    ax6.fill_between(accelerator_pedal.universe, fuzz.trimf(accelerator_pedal.universe, [0, 0, 50]), color='blue', alpha=0.2)
    ax6.fill_between(accelerator_pedal.universe, fuzz.trimf(accelerator_pedal.universe, [25, 50, 75]), color='green', alpha=0.2)
    ax6.fill_between(accelerator_pedal.universe, fuzz.trimf(accelerator_pedal.universe, [50, 100, 100]), color='red', alpha=0.2)
    ax6.set_title('Gaz Pedalı Basma Seviyesi ÇIKIŞ')
    ax6.legend()

    # Klima şiddeti grafiği
    ax7.plot(ac_intensity.universe, fuzz.trimf(ac_intensity.universe, [0, 0, 50]), 'b', linewidth=1.5, label='Düşük')
    ax7.plot(ac_intensity.universe, fuzz.trimf(ac_intensity.universe, [25, 50, 75]), 'g', linewidth=1.5, label='Orta')
    ax7.plot(ac_intensity.universe, fuzz.trimf(ac_intensity.universe, [50, 100, 100]), 'r', linewidth=1.5, label='Yüksek')
    ax7.fill_between(ac_intensity.universe, fuzz.trimf(ac_intensity.universe, [0, 0, 50]), color='blue', alpha=0.2)
    ax7.fill_between(ac_intensity.universe, fuzz.trimf(ac_intensity.universe, [25, 50, 75]), color='green', alpha=0.2)
    ax7.fill_between(ac_intensity.universe, fuzz.trimf(ac_intensity.universe, [50, 100, 100]), color='red', alpha=0.2)
    ax7.set_title('Klima Şiddeti ÇIKIŞ')
    ax7.legend()

    # Far ayarı grafiği
    ax8.plot(headlight_setting.universe, fuzz.trimf(headlight_setting.universe, [0, 0, 50]), 'b', linewidth=1.5, label='Düşük')
    ax8.plot(headlight_setting.universe, fuzz.trimf(headlight_setting.universe, [25, 50, 75]), 'g', linewidth=1.5, label='Orta')
    ax8.plot(headlight_setting.universe, fuzz.trimf(headlight_setting.universe, [50, 100, 100]), 'r', linewidth=1.5, label='Yüksek')
    ax8.fill_between(headlight_setting.universe, fuzz.trimf(headlight_setting.universe, [0, 0, 50]), color='blue', alpha=0.2)
    ax8.fill_between(headlight_setting.universe, fuzz.trimf(headlight_setting.universe, [25, 50, 75]), color='green', alpha=0.2)
    ax8.fill_between(headlight_setting.universe, fuzz.trimf(headlight_setting.universe, [50, 100, 100]), color='red', alpha=0.2)
    ax8.set_title('Far Ayarı ÇIKIŞ')
    ax8.legend()

    # Lastik basıncı uyarı göstergesi grafiği
    ax9.plot(tire_pressure_warning.universe, fuzz.trimf(tire_pressure_warning.universe, [0, 0, 15]), 'b', linewidth=1.5, label='Düşük')
    ax9.plot(tire_pressure_warning.universe, fuzz.trimf(tire_pressure_warning.universe, [10, 15, 20]), 'g', linewidth=1.5, label='Orta')
    ax9.plot(tire_pressure_warning.universe, fuzz.trimf(tire_pressure_warning.universe, [15, 30, 30]), 'r', linewidth=1.5, label='Yüksek')
    ax9.fill_between(tire_pressure_warning.universe, fuzz.trimf(tire_pressure_warning.universe, [0, 0, 15]), color='blue', alpha=0.2)
    ax9.fill_between(tire_pressure_warning.universe, fuzz.trimf(tire_pressure_warning.universe, [10, 15, 20]), color='green', alpha=0.2)
    ax9.fill_between(tire_pressure_warning.universe, fuzz.trimf(tire_pressure_warning.universe, [15, 30, 30]), color='red', alpha=0.2)
    ax9.set_title('Lastik Basıncı Uyarı Göstergesi ÇIKIŞ')
    ax9.legend()

    ax10.plot(distance.universe, fuzz.trimf(distance.universe, [0, 0, 50]), 'b', linewidth=1.5, label='Yakın')
    ax10.plot(distance.universe, fuzz.trimf(distance.universe, [25, 50, 75]), 'g', linewidth=1.5, label='Orta')
    ax10.plot(distance.universe, fuzz.trimf(distance.universe, [50, 100, 100]), 'r', linewidth=1.5, label='Uzak')
    ax10.fill_between(distance.universe, fuzz.trimf(distance.universe, [0, 0, 50]), color='blue', alpha=0.2)
    ax10.fill_between(distance.universe, fuzz.trimf(distance.universe, [25, 50, 75]), color='green', alpha=0.2)
    ax10.fill_between(distance.universe, fuzz.trimf(distance.universe, [50, 100, 100]), color='red', alpha=0.2)
    ax10.set_title('Mesafe Giriş')
    ax10.legend()

    # Boş eksenlerin kaldırılması
    plt.delaxes(ax=_)

    plt.tight_layout()
    plt.show()


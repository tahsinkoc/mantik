import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# Lastik hava basıncı (input)
tire_pressure = ctrl.Antecedent(np.arange(0, 31, 1), 'Lastik hava basıncı')
tire_pressure['düşük'] = fuzz.trimf(tire_pressure.universe, [0, 0, 15])
tire_pressure['orta'] = fuzz.trimf(tire_pressure.universe, [10, 15, 20])
tire_pressure['yüksek'] = fuzz.trimf(tire_pressure.universe, [15, 30, 30])

# Lastik hava basıncı uyarı göstergesi (output)
pressure_warning = ctrl.Consequent(np.arange(0, 31, 1), 'Lastik hava basıncı uyarı göstergesi')
pressure_warning['düşük'] = fuzz.trimf(pressure_warning.universe, [0, 0, 15])
pressure_warning['orta'] = fuzz.trimf(pressure_warning.universe, [10, 15, 20])
pressure_warning['yüksek'] = fuzz.trimf(pressure_warning.universe, [15, 30, 30])

# Üyelik fonksiyonlarını görselleştirme
# tire_pressure.view()
# pressure_warning.view()

# plt.show()

# Bulanık kurallar
rule1 = ctrl.Rule(tire_pressure['düşük'], pressure_warning['düşük'])
rule2 = ctrl.Rule(tire_pressure['orta'], pressure_warning['orta'])
rule3 = ctrl.Rule(tire_pressure['yüksek'], pressure_warning['yüksek'])

# Kontrol sistemi oluşturma ve simülasyon
pressure_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
pressure_simulation = ctrl.ControlSystemSimulation(pressure_ctrl)

# Örnek bir lastik hava basıncı değeri için uyarı göstergesini hesaplama


# print(f"Lastik hava basıncı uyarı göstergesi: {pressure_simulation.output['Lastik hava basıncı uyarı göstergesi']}")


def ComputePressure(press):
    pressure_simulation.input['Lastik hava basıncı'] = press
    pressure_simulation.compute()
    pressure_warning.view(sim=pressure_simulation)
    plt.show()
    return pressure_simulation.output['Lastik hava basıncı uyarı göstergesi']

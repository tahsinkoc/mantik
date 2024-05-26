import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# Sıcaklık (input)
temperature = ctrl.Antecedent(np.arange(0, 51, 1), 'Sıcaklık')
temperature['soğuk'] = fuzz.trimf(temperature.universe, [0, 0, 25])
temperature['ılıman'] = fuzz.trimf(temperature.universe, [15, 25, 35])
temperature['sıcak'] = fuzz.trimf(temperature.universe, [25, 50, 50])

# Nem (input)
humidity = ctrl.Antecedent(np.arange(0, 101, 1), 'Nem')
humidity['düşük'] = fuzz.trimf(humidity.universe, [0, 0, 50])
humidity['orta'] = fuzz.trimf(humidity.universe, [25, 50, 75])
humidity['yüksek'] = fuzz.trimf(humidity.universe, [50, 100, 100])

# Klima şiddeti (output)
ac_power = ctrl.Consequent(np.arange(0, 101, 1), 'Klima şiddeti')
ac_power['düşük'] = fuzz.trimf(ac_power.universe, [0, 0, 50])
ac_power['orta'] = fuzz.trimf(ac_power.universe, [25, 50, 75])
ac_power['yüksek'] = fuzz.trimf(ac_power.universe, [50, 100, 100])

# Üyelik fonksiyonlarını görselleştirme
# temperature.view()
# humidity.view()
# ac_power.view()

plt.show()

# Bulanık kurallar
rule1 = ctrl.Rule(temperature['soğuk'] & humidity['düşük'], ac_power['düşük'])
rule2 = ctrl.Rule(temperature['soğuk'] & humidity['orta'], ac_power['düşük'])
rule3 = ctrl.Rule(temperature['soğuk'] & humidity['yüksek'], ac_power['orta'])

rule4 = ctrl.Rule(temperature['ılıman'] & humidity['düşük'], ac_power['düşük'])
rule5 = ctrl.Rule(temperature['ılıman'] & humidity['orta'], ac_power['orta'])
rule6 = ctrl.Rule(temperature['ılıman'] & humidity['yüksek'], ac_power['yüksek'])

rule7 = ctrl.Rule(temperature['sıcak'] & humidity['düşük'], ac_power['orta'])
rule8 = ctrl.Rule(temperature['sıcak'] & humidity['orta'], ac_power['yüksek'])
rule9 = ctrl.Rule(temperature['sıcak'] & humidity['yüksek'], ac_power['yüksek'])

# Kontrol sistemi oluşturma ve simülasyon
ac_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9])
ac_simulation = ctrl.ControlSystemSimulation(ac_ctrl)

# Örnek bir sıcaklık ve nem değeri için klima şiddetini hesaplama


# print(f"Klima şiddeti: {ac_simulation.output['Klima şiddeti']}")
# ac_power.view(sim=ac_simulation)


def ComputeAC(moui, temp):
    ac_simulation.input['Sıcaklık'] = temp
    ac_simulation.input['Nem'] = moui
    ac_simulation.compute()
    ac_power.view(sim=ac_simulation)
    plt.show()
    return ac_simulation.output['Klima şiddeti']
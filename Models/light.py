import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# Hava ışık şiddeti (input)
light_intensity = ctrl.Antecedent(np.arange(0, 10001, 1), 'Hava ışık şiddeti')
light_intensity['düşük'] = fuzz.trimf(light_intensity.universe, [0, 0, 5000])
light_intensity['orta'] = fuzz.trimf(light_intensity.universe, [2500, 5000, 7500])
light_intensity['yüksek'] = fuzz.trimf(light_intensity.universe, [5000, 10000, 10000])

# Far ayarı (output)
headlight_adjustment = ctrl.Consequent(np.arange(0, 101, 1), 'Far ayarı')
headlight_adjustment['düşük'] = fuzz.trimf(headlight_adjustment.universe, [0, 0, 50])
headlight_adjustment['orta'] = fuzz.trimf(headlight_adjustment.universe, [25, 50, 75])
headlight_adjustment['yüksek'] = fuzz.trimf(headlight_adjustment.universe, [50, 100, 100])

# Üyelik fonksiyonlarını görselleştirme
# light_intensity.view()
# headlight_adjustment.view()

# plt.show()

# Bulanık kurallar
rule1 = ctrl.Rule(light_intensity['düşük'], headlight_adjustment['yüksek'])
rule2 = ctrl.Rule(light_intensity['orta'], headlight_adjustment['orta'])
rule3 = ctrl.Rule(light_intensity['yüksek'], headlight_adjustment['düşük'])

# Kontrol sistemi oluşturma ve simülasyon
headlight_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
headlight_simulation = ctrl.ControlSystemSimulation(headlight_ctrl)

# Örnek bir hava ışık şiddeti değeri için far ayarını hesaplama


# print(f"Far ayarı: {headlight_simulation.output['Far ayarı']}")
# headlight_adjustment.view(sim=headlight_simulation)


def LightCompute(lux):
    headlight_simulation.input['Hava ışık şiddeti'] = lux
    headlight_simulation.compute()
    headlight_adjustment.view(sim=headlight_simulation)
    plt.show()
    return headlight_simulation.output['Far ayarı']

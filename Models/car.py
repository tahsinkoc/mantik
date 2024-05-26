import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# Hız (input)
speed = ctrl.Antecedent(np.arange(0, 201, 1), 'Aracın hızı')
speed['çok_yavaş'] = fuzz.trimf(speed.universe, [0, 0, 100])
speed['orta'] = fuzz.trimf(speed.universe, [50, 100, 150])
speed['çok_hızlı'] = fuzz.trimf(speed.universe, [100, 200, 200])

# Mesafe (input)
distance = ctrl.Antecedent(np.arange(0, 101, 1), 'Mesafe')
distance['yakın'] = fuzz.trimf(distance.universe, [0, 0, 50])
distance['orta'] = fuzz.trimf(distance.universe, [25, 50, 75])
distance['uzak'] = fuzz.trimf(distance.universe, [50, 100, 100])

# Fren kuvveti (output)
brake_force = ctrl.Consequent(np.arange(0, 101, 1), 'Fren kuvveti')
brake_force['düşük'] = fuzz.trimf(brake_force.universe, [0, 0, 50])
brake_force['orta'] = fuzz.trimf(brake_force.universe, [25, 50, 75])
brake_force['yüksek'] = fuzz.trimf(brake_force.universe, [50, 100, 100])

# Gaz pedalı (output)
throttle = ctrl.Consequent(np.arange(0, 101, 1), 'Gaz pedalı')
throttle['düşük'] = fuzz.trimf(throttle.universe, [0, 0, 50])
throttle['orta'] = fuzz.trimf(throttle.universe, [25, 50, 75])
throttle['yüksek'] = fuzz.trimf(throttle.universe, [50, 100, 100])

# Üyelik fonksiyonlarını görselleştirme
# speed.view()
# distance.view()
# brake_force.view()
# throttle.view()

# plt.show()

# Bulanık kurallar
rule1 = ctrl.Rule(speed['çok_yavaş'] & distance['uzak'], [brake_force['düşük'], throttle['yüksek']])
rule2 = ctrl.Rule(speed['orta'] & distance['orta'], [brake_force['orta'], throttle['orta']])
rule2 = ctrl.Rule(speed['orta'] & distance['yakın'], [brake_force['yüksek'], throttle['düşük']])
rule3 = ctrl.Rule(speed['çok_hızlı'] & distance['yakın'], [brake_force['yüksek'], throttle['düşük']])

# Kontrol sistemi oluşturma ve simülasyon
car_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
car_simulation = ctrl.ControlSystemSimulation(car_ctrl)

# Örnek bir hız değeri ve mesafe için fren kuvveti ve gaz pedalını hesaplama


# print(f"Fren kuvveti: {car_simulation.output['Fren kuvveti']}")
# print(f"Gaz pedalı: {car_simulation.output['Gaz pedalı']}")
# brake_force.view(sim=car_simulation)



def ComputeCar(dist, spd):
    car_simulation.input['Aracın hızı'] = spd
    car_simulation.input['Mesafe'] = dist
    car_simulation.compute()
    throttle.view(sim=car_simulation)
    brake_force.view(sim=car_simulation)
    plt.show()
    return {'acceleration': car_simulation.output['Gaz pedalı'], 'brake': car_simulation.output['Fren kuvveti']}

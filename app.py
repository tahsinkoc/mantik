import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt
from multiprocessing import Process
import sys
sys.path.append('./Models') 
from Models.light import LightCompute
from Models.ac import ComputeAC
from Models.car import ComputeCar
from Models.pressure import ComputePressure
from Models.show import Enterence

def let_show_begin():
    Enterence()

def compute_light():
    print(f"Far Ayarı {LightCompute(3000)}")

def compute_ac():
    print(f"Klima Şiddeti {ComputeAC(moui=20, temp=30)}")

def compute_car():
    print(f"Gaz Pedalı - Fren Pedalı {ComputeCar(dist=5, spd=80)}")

def compute_pressure():
    print(f"Lastik Basınç Göstergesi {ComputePressure(press=20)}")

if __name__ == "__main__":
    processes = []

    processes.append(Process(target=Enterence))
    processes.append(Process(target=compute_light))
    processes.append(Process(target=compute_ac))
    processes.append(Process(target=compute_car))
    processes.append(Process(target=compute_pressure))

    for process in processes:
        process.start()

    # Ensure all processes have finished
    for process in processes:
        process.join()

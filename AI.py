import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


windSpeed = ctrl.Antecedent(np.arange(0, 300, 1), 'windSpeed')
windSpeed.automf(3)
windSpeed.view()

AmountOfEngineUse = ctrl.Consequent(np.arange(0, 100, 1), 'AmountOfEngineUse')
AmountOfEngineUse['low'] = fuzz.trimf(AmountOfEngineUse.universe, [0, 0, 100])
AmountOfEngineUse['medium'] = fuzz.trimf(AmountOfEngineUse.universe, [0, 50, 100])
AmountOfEngineUse['high'] = fuzz.trimf(AmountOfEngineUse.universe, [50, 100, 100])
AmountOfEngineUse.view()


rule1 = ctrl.Rule(windSpeed['poor'], AmountOfEngineUse['low'])
rule2 = ctrl.Rule(windSpeed['average'], AmountOfEngineUse['medium'])
rule4 = ctrl.Rule(windSpeed['good'], AmountOfEngineUse['high'])

AmountOfEngineUsage_Logic = ctrl.ControlSystem([rule1, rule2, rule3, rule4])
AmountOfEngineUsage = ctrl.ControlSystemSimulation(AmountOfEngineUsage_Logic)


speedOfWingInString = input("Enter speed of windin string(low, medium, high):");
switch(speedOfWingInString) {
        case 'low':
            speed = 100;
        case 'medium':
            speed = 200;
        case 'high':
            speed = 300;
        default:
            raise Exception("Sorry, Please enter between low, medium, high.")

AmountOfEngineUsage.input['windSpeed'] = speed
AmountOfEngineUsage.compute()
print (AmountOfEngineUsage.output['AmountOfEngineUse'])
AmountOfEngineUse.view(sim=AmountOfEngineUsage)



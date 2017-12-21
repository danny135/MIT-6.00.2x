# 6.00.2x Problem Set 4

import numpy
import random
import pylab
from ps3b import *

#
# PROBLEM 1
#        
def simulationDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    def plot(populations):
        pylab.title("ResistantVirus simulations")
        
        i = 0
        for pops in populations:
            i += 1
            pylab.subplot(2, 2, i)
            pylab.hist(pops)
        pylab.show()
            
    populations = {}
    for insertionPoint in [300, 150, 75, 0]:
        populations[insertionPoint] = []
        for trial in range(numTrials):
            viruses = []
            for virus in range(100):
                viruses.append(ResistantVirus(0.1, 0.05, {"guttagonol": False}, 0.005))
            patient = TreatedPatient(viruses, 1000)
            for step in range(insertionPoint + 150):
                if step == insertionPoint:
                    patient.addPrescription("guttagonol")
                patient.update()
            populations[insertionPoint].append(patient.getTotalPop())        
    
    plot(populations.values())

#simulationDelayedTreatment(500)

#
# PROBLEM 2
#
def simulationTwoDrugsDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    def plot(populations):
        
        i = 0
        for point, pops in populations.items():
            i += 1
            pylab.subplot(2, 2, i)
            pylab.title(str(point))
            pylab.hist(pops)
        pylab.show()
            
    populations = {}
    for insertionPoint in [300, 150, 75, 0]:
        populations[insertionPoint] = []
        for trial in range(numTrials):
            viruses = []
            for virus in range(100):
                viruses.append(ResistantVirus(0.1, 0.05, {"guttagonol": False, "grimpex": False}, 0.005))
            patient = TreatedPatient(viruses, 1000)
            for step in range(insertionPoint + 300):
                if step == 150:
                    patient.addPrescription("guttagonol")
                elif step == 150 + insertionPoint:
                    patient.addPrescription("grimpex")
                patient.update()
            populations[insertionPoint].append(patient.getTotalPop())        
    
    plot(populations)
simulationTwoDrugsDelayedTreatment(500)
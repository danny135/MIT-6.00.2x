import random
import pylab

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 500
CURRENTFOXPOP = 30

def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP

    # TO DO
    for i in range(CURRENTRABBITPOP):
        if CURRENTRABBITPOP < MAXRABBITPOP and random.random() <= 1.0 - CURRENTRABBITPOP/float(MAXRABBITPOP):
            CURRENTRABBITPOP += 1
    
            
def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP

    # TO DO
    for i in range(CURRENTFOXPOP):
        if random.random() <= CURRENTRABBITPOP/float(MAXRABBITPOP):
            if CURRENTRABBITPOP > 10:
                CURRENTRABBITPOP -= 1
            if random.random() <= 1.0/3.0:
                CURRENTFOXPOP += 1
        else:
            if CURRENTFOXPOP > 10 and random.random() <= 0.1:
                CURRENTFOXPOP -= 1
            
def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """
    rabbit_populations = []
    fox_populations = []

    for i in range(numSteps):
        rabbitGrowth()
        rabbit_populations.append(CURRENTRABBITPOP)
        foxGrowth()
        fox_populations.append(CURRENTFOXPOP)
        
    pylab.figure(1)
    pylab.plot(range(numSteps), rabbit_populations, label = "Rabbits")
    pylab.plot(range(numSteps), fox_populations, label = "Foxes")
    pylab.title("Populations over Time")
    pylab.xlabel("Time step")
    pylab.ylabel("Population")
    pylab.legend()
    

    pylab.figure(2)
    
    coeff = pylab.polyfit(range(len(rabbit_populations)), rabbit_populations, 2)
    pylab.plot(pylab.polyval(coeff, range(len(rabbit_populations))), label = "Rabbits")
    coeff = pylab.polyfit(range(len(fox_populations)), fox_populations, 2)
    pylab.plot(pylab.polyval(coeff, range(len(fox_populations))), label = "Foxes")
    
    pylab.title("Coefficient")
    pylab.xlabel("Population")
    pylab.ylabel("Time Step")
    pylab.legend()
    
    return (rabbit_populations, fox_populations)
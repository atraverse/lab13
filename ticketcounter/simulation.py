# Implementation of the main simulation class.
import random
from array import Array
from llistqueue import Queue
from people import TicketAgent, Passenger

class TicketCounterSimulation :
    # Create a simulation object.
    def __init__( self, numAgents, numMinutes, betweenTime, serviceTime ):
    # Parameters supplied by the user.
        self._arriveProb = 1.0 / betweenTime
        self._serviceTime = serviceTime
        self._numMinutes = numMinutes

        # Simulation components.
        self._passengerQ = Queue()
        self._theAgents = Array( numAgents )
        for i in range( numAgents ) :
            self._theAgents[i] = TicketAgent(i+1)

        # Computed during the simulation.
        self._totalWaitTime = 0
        self._numPassengers = 0

    # Run the simulation using the parameters supplied earlier.
    def run( self ):
        for curTime in range(self._numMinutes + 1) :
            self._handleArrival(curTime)
            self._handleBeginService(curTime)
            self._handleEndService(curTime)

    # Print the simulation results.
    def printResults( self ):
        numServed = self._numPassengers - len(self._passengerQ)
        avgWait = float( self._totalWaitTime ) / numServed
        print( "" )
        print( "Number of passengers served = ", numServed )
        print( "Number of passengers remaining in line = %d" %
        len(self._passengerQ)
        print( "The average wait time was %4.2f minutes." % avgWait )

# The remaining methods that have yet to be implemented.

    def _handleArrive(self, curTime ):
        '''method determines if a passenger arrives during the current time step and handles that arrival.'''
        self.time = random.randint(0.0, 1.0)
        id_num = len(self._passengerQ)+1
        if self.time <= self._arriveProb:
            self._numPassengers += 1
            self._passengerQ.enqueue(Passenger(id_num,curTime))
        # Handles simulation rule #1.

    def _handleBeginService(self,curTime):
        '''determines if any agents are free and allows the next passenger(s)
        in line to begin their transaction'''
        id_num = len(self._theAgents)
        if TicketAgent(id_num).isFree() == True:
            self._numPassengers -=1
            self._passengerQ.dequeue()
        else:
            self._totalWaitTime +=curTime
        # Handles simulation rule #2.

    def _handleEndService(self, curTime):
        ''' determines
        which of the current transactions have completed, if any, and flags a passenger
        departure.'''
        id_num = len(self._theAgents)
        if TicketAgent(id_num).isFinished(curTime) == True:
            TicketAgent(id_num).stopService()
        # Handles simulation rule #3.

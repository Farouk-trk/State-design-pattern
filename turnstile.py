import time

class Turnstile():
    """
    The Context (a turnstile in a subway station) defines the interface of interest to clients. It also maintains
    a reference to an instance of a State subclass, which represents the current
    state of the Context.
    """


    def __init__(self):
        """
        defining the Context state attribute and initialize it with it's default state ClosedTurnstile
        """
        self.state = ClosedTurnstile(self) 

    def transition_to(self, state):
        """
        The Context allows changing the State object at runtime.
        """
        self.state = state

    """
    The Context delegates part of its behavior to the current State object.
    """
    def enter(self):
        self.state.enter()

    def pay(self):
        self.state.pay()
    
    def payOk(self):
        self.state.payOk()

    def payFailed(self):
        self.state.payFailed()


class TurnstileStates():
    """
    The base State class declares methods that all Concrete State should
    implement .
    """  
    
    def enter(self):
        pass

    def pay(self):
        pass

    def payOk(self):
        pass

    def payFailed(self):
        pass



"""
Concrete States implement various behaviors, associated with a state of the
Context.
"""
class ClosedTurnstile(TurnstileStates):

    def __init__(self,g):
        self.gate=g

    def enter(self) :
        print("client request: enter ")
        print("xxxx you must pay xxxx \n")

    def pay(self) :
        print("client request: pay ")
        self.gate.transition_to(ProcPaiment(self.gate))
        print("     State ---------> processing payment \n")
    
    def payOk(self) :
        pass
    
    def payFailed(self) :
        pass
    

class ProcPaiment(TurnstileStates):
    
    def __init__(self,g):
        self.gate=g

    def enter(self) :
        print("***procesing payment transaction, Please wait*** \n")

    def pay(self) :
        print("***procesing payment transaction, Please wait*** \n")
    
    def payOk(self) :
        print("payment successful, you can enter")
        self.gate.transition_to(OpenTurnstile(self.gate))
        print("     State ---------> Gate open \n")
    
    def payFailed(self) :
        print("payment failed!!!")
        self.gate.transition_to(ClosedTurnstile(self.gate))
        print("     State ---------> Gate closed \n")

class OpenTurnstile(TurnstileStates):
    
    def __init__(self,g):
        self.gate=g

    def enter(self) :
        print("client request: enter")
        print("client entred")
        self.gate.transition_to(ClosedTurnstile(self.gate))
        print("     State ---------> Gate closed \n")

    def pay(self) :
        print("client request: pay")
        print("You have already paid. You can enter \n")
    
    def payOk(self) :
        pass
    
    def payFailed(self) :
        pass

    



gateA = Turnstile()

gateA.enter()
time.sleep(2)
gateA.pay()
time.sleep(2)
gateA.payFailed()
time.sleep(2)
gateA.pay()
time.sleep(2)
gateA.payOk()
time.sleep(2)
gateA.enter()
time.sleep(2)

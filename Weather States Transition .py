import numpy as np
class WeatherSimulation:
    state='sunny'
    def __init__(self,transition_probabilities,holding_times):
        for i,j in transition_probabilities.items():
            sumP=0
            for k,p in j.items():
                sumP+=p
            if sumP!=1:
                raise RuntimeError("The Transition probabilities for %s are invalid i.e sum not equal to 1"%(i))
            else:
                self.transition_probabilities=transition_probabilities
                self.holding_times=holding_times
                self.time_remaining=holding_times["sunny"]
    def get_states(self):
        return [i for i,j in self.transition_probabilities.items()]
    def current_state(self):
        return self.state
    def next_state(self):
        states=[x for x in self.transition_probabilities.keys()]
        if self.time_remaining > 0:
            self.time_remaining -= 1
        else:
            probabilities = self.transition_probabilities[self.state]
            self.state = np.random.choice(states, p=list(probabilities.values()))
            self.time_remaining = self.holding_times[self.state]
            self.time_remaining -= 1
            return self.state
    def set_state(self,new_state):
        if new_state not in get_states():
            raise ValueError("Invalid State Name")
        else:
            state=new_state
    def current_state_remaining_hours(self):
        for i,j in self.holding_times.items():
                if i==self.state:
                    return j
    def iterable(self):
        while 1:
            yield self.current_state()
            self.next_state()
    def simulate(self,hours):
        lstP=[0,0,0,0]
        time=hours
        states=self.get_states()
        while hours>0:
            self.next_state()
            lstP[states.index(self.state)]+=1
            hours-=1
        return [x*100/time for x in lstP]

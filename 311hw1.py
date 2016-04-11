__author__ = 'Hsuan-Chih, Chen'

import json

class DFA:
    states = None
    alphabet = None
    description = None
    start_state = None
    accept_states = None
    transitions = None
    strings = None
    current_state = None

    

    def __init__(self, file_name):
        self.states = json.load(open(file_name))["states"]        
        self.alphabet = json.load(open(file_name))["alphabet"]
        self.description = json.load(open(file_name))["description"]
        self.start_state = json.load(open(file_name))["start"]
        self.current_state = ""
        self.accepted_states = json.load(open(file_name))["accept"]
        self.transitions = json.load(open(file_name))["transitions"]
        self.strings = json.load(open(file_name))["inputs"]


    
    def get_string(self):
        return self.strings


    
    def display_title(self):
        print("DFA: ",self.description)


        
    def run_dfa(self, input_str):
        self.current_state = self.start_state
        print("\nInput string: ", input_str)
        for letter in input_str:
            if(letter not in self.alphabet): #and letter != ""):
                return False
            des_state = self.transitions[self.current_state][letter]
            print("input(",letter,")",self.current_state," -> ",des_state)
            self.current_state = des_state


            
    def accepted_or_not(self):
        if(self.current_state in self.accepted_states):
            return True
        else:
            return False

    

    def display_result(self):
        print("\nFinal state: ", self.current_state)
        print("\nAccepted state(s): ")
        for i in self.accepted_states:
            print(i," ")


            
    def reset_current_state(self):
        self.current_state = ""


if __name__ == "__main__":

    dfa_object = DFA("test2.json")
    input_strings = dfa_object.get_string()
    dfa_object.display_title()
    for s in input_strings:
        if(dfa_object.run_dfa(s)== False):
            print("\ninvaild input!")
        else:
            dfa_object.display_result()
            if(dfa_object.accepted_or_not() == True):
                print("\n",s," is accepted. ")
            else:
                print("\n",s," is rejected. ")    
    user = input("\nUser Input: ")
    if(dfa_object.run_dfa(user)==False):
        print("\ninvaild input!")
    else:
        dfa_object.display_result()
        if(dfa_object.accepted_or_not() == True):
                print("\n",user," is accepted. ")
        else:
                print("\n",user," is rejected. ")


            

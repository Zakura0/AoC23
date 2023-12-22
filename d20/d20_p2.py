from collections import deque
import numpy as np
class Module:
    def __init__(self, label, symbol, targets):
        self.label = label
        self.symbol = symbol
        self.targets = targets
        if symbol == "%":
            self.status = "off"
        else: 
            self.status = {}
    def __repr__(self):
        return "(label = " + self.label + " | symbol = " + self.symbol + " | targets = " + ",".join(self.targets) + " | status = " + str(self.status) + ")"

modules = {}
starting_targets = []

for line in open("input.txt"):
    key, value = line.strip().split(" -> ")
    targets = value.split(", ")
    if key == "broadcaster":
        starting_targets = targets
    else:
        symbol = key[0]
        label = key[1:]
        modules[label] = Module(label, symbol, targets)

for label, module in modules.items():
    for target in module.targets:
        if target in modules and modules[target].symbol == "&":
            modules[target].status[label] = "low"

button_presses = 0
kk = mr = bb = gl = 0
circles_found = False
while not circles_found:
    button_presses += 1
    queue = deque([("broadcaster", t, "low") for t in starting_targets])
    while queue:
        sender, target, pulse = queue.popleft()
        if target not in modules:
            continue        
        module = modules[target]
        if sender == 'kk':
            if pulse == "high":
                kk = button_presses
                if kk and mr and bb and gl:
                    circles_found = True
        if sender == 'mr':
            if pulse == "high":
                mr = button_presses
                if kk and mr and bb and gl:
                    circles_found = True
        if sender == 'bb':
            if pulse == "high":
                bb = button_presses
                if kk and mr and bb and gl:
                    circles_found = True
        if sender == 'gl':
            if pulse == "high":
                gl = button_presses
                if kk and mr and bb and gl:
                    circles_found = True
        elif target != "rx":
            if module.symbol == "%":
                if pulse == "low":
                    module.status = "on" if module.status == "off" else "off"
                    pulse_out = "high" if module.status == "on" else "low"
                    for t in module.targets:
                        queue.append((module.label, t, pulse_out))
            else:
                module.status[sender] = pulse
                pulse_out = "low" if all(inputs == "high" for inputs in module.status.values()) else "high"
                for t in module.targets:
                    queue.append((module.label, t, pulse_out))
print(np.lcm.reduce([kk, mr, bb, gl], dtype='int64'))
    



G = {} #ou dict() mais plus coûteux
G["France"] = ["Bresil","Suriname"]
G["Argentine"] = ["Bolivie","Bresil","Chili","Paraguay","Uruguay"]
G["Bolivie"] = ["Argentine","Bresil","Chili","Paraguay","Perou"]
G["Bresil"] = ["Argentine","Bolivie","Colombie","France","Guyana","Paraguay","Perou","Suriname","Uruguay","Venezuela"]
G["Chili"]=["Argentine","Bolivie","Perou"]
G["Colombie"] = ["Bresil","Equateur","Perou","Venezuela"]
G["Equateur"] = ["Colombie","Perou"]
G["Guyana"] = ["Bresil","Suriname","Venezuela"]
G["Paraguay"] = ["Argentine","Bolivie","Bresil"]
G["Perou"] = ["Bolivie","Bresil","Chili","Colombie","Equateur"]
G["Suriname"] = ["Bresil","France","Guyana"]
G["Uruguay"] = ["Argentine","Bresil"]
G["Venezuela"] = ["Bresil","Colombie","Guyana"]

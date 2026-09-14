web_development = ["Arun", "Meera", "Rahul"]
data_science = ["Anu", "Vivek", "Priya"]
ui_ux_design = ["Asha", "Neha", "Kiran"] 
all_participants = [web_development, data_science, ui_ux_design]
web_development.append("Sanjay")
data_science.insert(1, "Divya")
ui_ux_design.pop()
data_science_copy = data_science.copy()
data_science.clear()
print("First two Web Development participants:", web_development[:2])
name_lengths = [len(name) for name in data_science_copy]
print("Name lengths:", name_lengths)
asha_present = (
    "Asha" in web_development
    or "Asha" in data_science_copy
    or "Asha" in ui_ux_design
)
print("Is Asha in any workshop list?", asha_present)
first_participants = (
    web_development[0],
    data_science_copy[0],
    ui_ux_design[0])
print("First participants tuple:", first_participants)
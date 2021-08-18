programmincg_terms = { 
    "Bug": "kinda error",
    "Function": "callable piece of code",
     }

# Key must be a string. This won't work: { Bug: "..." }

one_term = programmincg_terms["Bug"]        # ...["Bog"] --> KeyError

programmincg_terms["Loop"] = "Do over and over again"

empty = {}
empty["first"] = "FIRST"

# to wipe
empty = {}

programmincg_terms["Bug"] = "changed description"

# loop to bring keys
for key in programmincg_terms:
    print(key)

# loop values
for key in programmincg_terms:
    print(programmincg_terms[key])




# Nesting
capitals = {
    "France" : "Paris",
    "Germany" : "Berlin"
}
travel_log_simple = {
    "France" : ["Paris", "Grenoble", "Lille"]
}
travel_log = [
    {
        "country": "France",
        "visited": ["Paris", "Grenoble", "Lille"],
        "capital": "Paris"
    }
]


["A", "B", ["C", "D"]]


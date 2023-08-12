#!/usr/bin/env python

# Define variables
gamers = {
    "Anthony": {
        "console": "Playstation",
        "snack": "Munchos"
    },
    "April": {
        "console": "Nintendo",
        "snack": "Cheez-It"
    }
}

# Print gamer info
for person in gamers.keys():
    print(person + " is a gamer who eats " + gamers[person]["snack"] + " while playing games on " + gamers[person]["console"] + ".")

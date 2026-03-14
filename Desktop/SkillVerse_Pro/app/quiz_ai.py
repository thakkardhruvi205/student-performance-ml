import random

def generate_questions(skill):

    questions = {

        "Cricket":[
        ("How many players in a cricket team?", ["11","9","8","10"], "11"),
        ("What does LBW mean?", ["Leg Before Wicket","Long Ball Win","Left Bat Wide","Low Bounce"], "Leg Before Wicket"),
        ("Who invented T20?", ["England","India","Australia","Pakistan"], "England")
        ],

        "Python":[
        ("Python is?", ["Language","Snake","Game","Compiler"], "Language"),
        ("Which loop exists?", ["for","repeat","loop","again"], "for"),
        ("Which datatype?", ["int","run","go","jump"], "int")
        ]

    }

    return random.sample(questions.get(skill, []),3)
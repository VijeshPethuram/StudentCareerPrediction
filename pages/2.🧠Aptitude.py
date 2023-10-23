import streamlit as st

# Define a list of 10 questions and their corresponding options and correct answers
logical_questions = [
    
        
        {
            "category": "Logical",
            "question": "If all Zips are Zaps, and some Zaps are Zops, can we conclude that some Zips are definitely Zops?",
            "options": ["A) Yes", "B) No"],
            "correct_answer": "A) Yes"
        },
        {
            "category": "Logical",
            "question": "If John is twice as old as Alice, and Alice is 10 years old, how old is John?",
            "options": ["A) 5 years", "B) 10 years", "C) 20 years", "D) 30 years"],
            "correct_answer": "C) 20 years"
        },
        {
            "category": "Logical",
            "question": "If all cats have tails, and Fluffy is a cat, can we conclude that Fluffy has a tail?",
            "options": ["A) Yes", "B) No"],
            "correct_answer": "A) Yes"
        },
        {
            "category": "Logical",
            "question": "If the train departs at 2:30 PM and arrives at 4:45 PM, how long is the train journey?",
            "options": ["A) 1 hour 45 minutes", "B) 2 hours", "C) 2 hours 15 minutes", "D) 3 hours 15 minutes"],
            "correct_answer": "A) 1 hour 45 minutes"
        },
        {
            "category": "Logical",
            "question": "If A implies B, and B implies C, can we conclude that A implies C?",
            "options": ["A) Yes", "B) No"],
            "correct_answer": "A) Yes"
        },
        {
            "category": "Logical",
            "question": "If all squares are rectangles, and some rectangles are not circles, can we conclude that some squares are not circles?",
            "options": ["A) Yes", "B) No"],
            "correct_answer": "A) Yes"
        },
        {
            "category": "Logical",
            "question": "If today is Monday, and two days from now will be a Wednesday, what day was it yesterday?",
            "options": ["A) Saturday", "B) Sunday", "C) Monday", "D) Tuesday"],
            "correct_answer": "B) Sunday"
        },
        {
            "category": "Logical",
            "question": "If all birds can fly, and penguins cannot fly, can we conclude that penguins are not birds?",
            "options": ["A) Yes", "B) No"],
            "correct_answer": "B) No"
        },
        {
            "category": "Logical",
            "question": "If 3 people can paint 3 rooms in 3 hours, how many people are needed to paint 6 rooms in 6 hours?",
            "options": ["A) 3 people", "B) 6 people", "C) 9 people", "D) 12 people"],
            "correct_answer": "A) 3 people"
        },
        {
        "category": "Logical",
        "question": "In a town, there are two barbers. One barber has a neatly trimmed beard, while the other barber is clean-shaven. Each day, every man in the town must visit one of the barbers to get a haircut. The rule is that if a man arrives at a barber's shop and the barber has a neatly trimmed beard, he must leave and go to the clean-shaven barber. If the barber is clean-shaven, he must leave and go to the barber with a neatly trimmed beard. Given this scenario, can such a situation exist in the town?",
        "options": ["A) Yes", "B) No"],
        "correct_answer": "B) No"
        },

        {
            "category": "Logical",
            "question": "If all roses are flowers, and some flowers are red, can we conclude that some roses are red?",
            "options": ["A) Yes", "B) No"],
            "correct_answer": "A) Yes"
        },
        {
            "category": "Logical",
            "question": "If Peter is taller than Mary, and Mary is taller than Sarah, who is the shortest among them?",
            "options": ["A) Peter", "B) Mary", "C) Sarah"],
            "correct_answer": "C) Sarah"
        },
        {
            "category": "Logical",
            "question": "If no mammals can fly, and bats are mammals, can we conclude that bats cannot fly?",
            "options": ["A) Yes", "B) No"],
            "correct_answer": "B) No"
        },
        {
            "category": "Logical",
            "question": "If the train travels at a speed of 60 mph and covers a distance of 120 miles, how long does the journey take?",
            "options": ["A) 1 hour", "B) 2 hours", "C) 3 hours", "D) 4 hours"],
            "correct_answer": "B) 2 hours"
        },
        {
            "category": "Logical",
            "question": "If all squares have four sides, and this shape has four sides, can we conclude that it is a square?",
            "options": ["A) Yes", "B) No"],
            "correct_answer": "B) No"
        },
        {
            "category": "Logical",
            "question": "If Jack is older than Jill, and Jill is older than Tom, who is the youngest among them?",
            "options": ["A) Jack", "B) Jill", "C) Tom"],
            "correct_answer": "C) Tom"
        },
        {
            "category": "Logical",
            "question": "If 5 books cost $25, how much do 8 books cost?",
            "options": ["A) $40", "B) $45", "C) $50", "D) $55"],
            "correct_answer": "A) $40"
        },
        {
            "category": "Logical",
            "question": "If no reptiles can swim, and turtles are reptiles, can we conclude that turtles cannot swim?",
            "options": ["A) Yes", "B) No"],
            "correct_answer": "A) Yes"
        },
        {
            "category": "Logical",
            "question": "If it is rainy and John has an umbrella, will John use the umbrella?",
            "options": ["A) Yes", "B) No"],
            "correct_answer": "A) Yes"
        },
        {
            "category": "Logical",
            "question": "If all fruits are healthy, and some fruits are delicious, can we conclude that some healthy things are delicious?",
            "options": ["A) Yes", "B) No"],
            "correct_answer": "A) Yes"
        },

        {
            "category": "Logical",
            "question": "If all birds can fly, and penguins are birds, can we conclude that penguins can fly?",
            "options": ["A) Yes", "B) No"],
            "correct_answer": "B) No"
        },
        {
            "category": "Logical",
            "question": "If every student in the class passed the math exam, and John is a student, can we conclude that John passed the math exam?",
            "options": ["A) Yes", "B) No"],
            "correct_answer": "A) Yes"
        },
        {
            "category": "Logical",
            "question": "If all triangles have three sides, and this shape has three sides, can we conclude that it is a triangle?",
            "options": ["A) Yes", "B) No"],
            "correct_answer": "A) Yes"
        },
        {
            "category": "Logical",
            "question": "If it is snowing, and Mary has a snowball, can we conclude that Mary made the snowball?",
            "options": ["A) Yes", "B) No"],
            "correct_answer": "A) Yes"
        },
        {
            "category": "Logical",
            "question": "If every apple is a fruit, and some fruits are red, can we conclude that some apples are red?",
            "options": ["A) Yes", "B) No"],
            "correct_answer": "A) Yes"
        },
        {
            "category": "Logical",
            "question": "If all dogs have tails, and Fido is a dog, can we conclude that Fido has a tail?",
            "options": ["A) Yes", "B) No"],
            "correct_answer": "A) Yes"
        },
        {
            "category": "Logical",
            "question": "If it is daytime and the sun is shining, can we conclude that it is not nighttime?",
            "options": ["A) Yes", "B) No"],
            "correct_answer": "A) Yes"
        },
        {
            "category": "Logical",
            "question": "If no insects have fur, and bees are insects, can we conclude that bees do not have fur?",
            "options": ["A) Yes", "B) No"],
            "correct_answer": "A) Yes"
        },
        {
            "category": "Logical",
            "question": "If it is raining and Mary has an umbrella, can we conclude that Mary will use the umbrella?",
            "options": ["A) Yes", "B) No"],
            "correct_answer": "A) Yes"
        },
        {
            "category": "Logical",
            "question": "If all planets orbit the sun, and Earth is a planet, can we conclude that Earth orbits the sun?",
            "options": ["A) Yes", "B) No"],
            "correct_answer": "A) Yes"
        },





        # Add more questions here...
    
    # Add more questions here...
]
verbal_questions = [
    {
     "category": "Verbal",
     "question": "What is the synonym of 'Ubiquitous'?",
     "options": ["A) Rare", "B) Pervasive", "C) Limited", "D) Scarce"],
     "correct_answer": "B) Pervasive"
 },
 {
     "category": "Verbal",
     "question": "What is the antonym of 'Innocuous'?",
     "options": ["A) Harmless", "B) Dangerous", "C) Safe", "D) Mild"],
     "correct_answer": "B) Dangerous"
 },
 {
     "category": "Verbal",
     "question": "Which word means 'a brief and decisive statement or expression'?",
     "options": ["A) Elusive", "B) Facetious", "C) Ephemeral", "D) Epigram"],
     "correct_answer": "D) Epigram"
 },
 {
     "category": "Verbal",
     "question": "What is the synonym of 'Voracious'?",
     "options": ["A) Hungry", "B) Satisfied", "C) Ravenous", "D) Starving"],
     "correct_answer": "C) Ravenous"
 },
 {
     "category": "Verbal",
     "question": "What is the antonym of 'Ubiquitous'?",
     "options": ["A) Rare", "B) Pervasive", "C) Limited", "D) Scarce"],
     "correct_answer": "A) Rare"
 },
 {
     "category": "Verbal",
     "question": "Which word means 'lasting for a very short time'?",
     "options": ["A) Eternal", "B) Fleeting", "C) Permanent", "D) Lasting"],
     "correct_answer": "B) Fleeting"
 },
 {
     "category": "Verbal",
     "question": "What is the antonym of 'Innocuous'?",
     "options": ["A) Harmless", "B) Dangerous", "C) Safe", "D) Mild"],
     "correct_answer": "B) Dangerous"
 },
 {
     "category": "Verbal",
     "question": "Which word means 'lack of interest, enthusiasm, or concern'?",
     "options": ["A) Apathy", "B) Enthusiasm", "C) Detachment", "D) Passivity"],
     "correct_answer": "A) Apathy"
 },
 {
     "category": "Verbal",
     "question": "What is the antonym of 'Serene'?",
     "options": ["A) Calm", "B) Peaceful", "C) Turbulent", "D) Tranquil"],
     "correct_answer": "C) Turbulent"
 },
 {
     "category": "Verbal",
     "question": "Which word means 'a state of being pleasantly lost in one's thoughts; a daydream'?",
     "options": ["A) Reverie", "B) Nightmare", "C) Reality", "D) Fantasy"],
     "correct_answer": "A) Reverie"
 },
    {
       "category": "Verbal",
       "question": "What is the synonym of 'Ephemeral'?",
       "options": ["A) Lasting", "B) Fleeting", "C) Permanent", "D) Eternal"],
       "correct_answer": "B) Fleeting"
   },
   {
       "category": "Verbal",
       "question": "What is the antonym of 'Obfuscate'?",
       "options": ["A) Clarify", "B) Confuse", "C) Complicate", "D) Mystify"],
       "correct_answer": "A) Clarify"
   },
   {
       "category": "Verbal",
       "question": "Which word means 'a person who is new to a subject or activity'?",
       "options": ["A) Expert", "B) Veteran", "C) Novice", "D) Master"],
       "correct_answer": "C) Novice"
   },
   {
       "category": "Verbal",
       "question": "What is the synonym of 'Eloquent'?",
       "options": ["A) Fluent", "B) Inarticulate", "C) Charming", "D) Brief"],
       "correct_answer": "A) Fluent"
   },
   {
       "category": "Verbal",
       "question": "What is the antonym of 'Voracious'?",
       "options": ["A) Hungry", "B) Satisfied", "C) Ravenous", "D) Starving"],
       "correct_answer": "B) Satisfied"
   },
   {
       "category": "Verbal",
       "question": "Which word means 'intentionally exaggerated to emphasize a point or create humor'?",
       "options": ["A) Literal", "B) Hyperbolic", "C) Understated", "D) Accurate"],
       "correct_answer": "B) Hyperbolic"
   },
   {
       "category": "Verbal",
       "question": "What is the antonym of 'Precarious'?",
       "options": ["A) Stable", "B) Dangerous", "C) Secure", "D) Unsteady"],
       "correct_answer": "A) Stable"
   },
   {
       "category": "Verbal",
       "question": "Which word means 'a person who loves or is strongly attracted to something'?",
       "options": ["A) Apathetic", "B) Repellent", "C) Enthusiast", "D) Skeptic"],
       "correct_answer": "C) Enthusiast"
   },
   {
       "category": "Verbal",
       "question": "What is the synonym of 'Serene'?",
       "options": ["A) Calm", "B) Peaceful", "C) Turbulent", "D) Tranquil"],
       "correct_answer": "D) Tranquil"
   },
   {
       "category": "Verbal",
       "question": "What is the antonym of 'Eloquent'?",
       "options": ["A) Fluent", "B) Inarticulate", "C) Charming", "D) Brief"],
       "correct_answer": "B) Inarticulate"
   },
    {
     "category": "Verbal",
     "question": "What is the synonym of 'Ephemeral'?",
     "options": ["A) Lasting", "B) Fleeting", "C) Permanent", "D) Eternal"],
     "correct_answer": "B) Fleeting"
 },
 {
     "category": "Verbal",
     "question": "What is the antonym of 'Obfuscate'?",
     "options": ["A) Clarify", "B) Confuse", "C) Complicate", "D) Mystify"],
     "correct_answer": "A) Clarify"
 },
 {
     "category": "Verbal",
     "question": "Which word means 'a person who is new to a subject or activity'?",
     "options": ["A) Expert", "B) Veteran", "C) Novice", "D) Master"],
     "correct_answer": "C) Novice"
 },
 {
     "category": "Verbal",
     "question": "What is the synonym of 'Eloquent'?",
     "options": ["A) Fluent", "B) Inarticulate", "C) Charming", "D) Brief"],
     "correct_answer": "A) Fluent"
 },
 {
     "category": "Verbal",
     "question": "What is the antonym of 'Voracious'?",
     "options": ["A) Hungry", "B) Satisfied", "C) Ravenous", "D) Starving"],
     "correct_answer": "B) Satisfied"
 },
 {
     "category": "Verbal",
     "question": "Which word means 'intentionally exaggerated to emphasize a point or create humor'?",
     "options": ["A) Literal", "B) Hyperbolic", "C) Understated", "D) Accurate"],
     "correct_answer": "B) Hyperbolic"
 },
 {
     "category": "Verbal",
     "question": "What is the antonym of 'Precarious'?",
     "options": ["A) Stable", "B) Dangerous", "C) Secure", "D) Unsteady"],
     "correct_answer": "A) Stable"
 },
 {
     "category": "Verbal",
     "question": "Which word means 'a person who loves or is strongly attracted to something'?",
     "options": ["A) Apathetic", "B) Repellent", "C) Enthusiast", "D) Skeptic"],
     "correct_answer": "C) Enthusiast"
 },
 {
     "category": "Verbal",
     "question": "What is the synonym of 'Serene'?",
     "options": ["A) Calm", "B) Peaceful", "C) Turbulent", "D) Tranquil"],
     "correct_answer": "D) Tranquil"
 },
 {
     "category": "Verbal",
     "question": "What is the antonym of 'Eloquent'?",
     "options": ["A) Fluent", "B) Inarticulate", "C) Charming", "D) Brief"],
     "correct_answer": "B) Inarticulate"
 }
    # Add more verbal questions here...
]
st.title("Aptitude")


 
st.header('🧠QUESTIONS ON LOGICAL!!!')
    # Create a dictionary to store user responses for Logical quiz
user_responses1 = {}
st.title("Logical Quiz")
    
    # Loop through 10 logical questions
for i in range(10):
    question_data = logical_questions[i]
    st.subheader(f"Question {i + 1}:")
    st.write(question_data["question"])  
        # Display multiple choice options and store user's choice with a unique key
    user_response1 = st.radio(f"Select an option {i}:", question_data["options"], key=f"radio_logical_{i}")
    user_responses1[i] = user_response1
    st.markdown('~~~~~~~~~~~~~~~~~~~~~~') 

    # Check answers and display results for Logical quiz


st.markdown('--------------------')
st.header('🔠QUESTIONS ON VERBAL!!!')
    # Create a dictionary to store user responses for Verbal quiz
user_responses = {}
    
st.title("Verbal Quiz")
    
    # Loop through 10 verbal questions
for i in range(10):
    question_data = verbal_questions[i]
    st.subheader(f"Question {i + 1}:")
    st.write(question_data["question"])
        
        # Display multiple choice options and store user's choice with a unique key
    user_response = st.radio(f"Select an option {i}:", question_data["options"], key=f"radio_verbal_{i}")
    user_responses[i] = user_response

    # Check answers and display results for Verbal quiz
if st.button("Submit "):
    st.subheader("Results for Logical Quiz:")
    correct_answers1 = 0
    for i in range(10):
         user_response1 = user_responses1[i]
         correct_answer1 = logical_questions[i]["correct_answer"]
         st.write(f"Question {i + 1}: {logical_questions[i]['question']}")
         st.write(f"Your Answer: {user_response1}")
         st.write(f"Correct Answer: {correct_answer1}")
         if user_response1 == correct_answer1:
             correct_answers1 += 1
    st.write(f"You got {correct_answers1} out of 10 questions correct for the Logical quiz.")
    st.subheader("Results for Verbal Quiz:")
    correct_answers = 0
    for i in range(10):
        user_response = user_responses[i]
        correct_answer = verbal_questions[i]["correct_answer"]
        st.write(f"Question {i + 1}: {verbal_questions[i]['question']}")
        st.write(f"Your Answer: {user_response}")
        st.write(f"Correct Answer: {correct_answer}")
        if user_response == correct_answer:
            correct_answers += 1
    st.write(f"You got {correct_answers} out of 10 questions correct for the Verbal quiz.")
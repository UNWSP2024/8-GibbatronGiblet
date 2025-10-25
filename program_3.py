# Program #3: Capital Quiz
# Write a program that creates a dictionary containing the U.S. states as keys, 
# and their capitals as values.  
# The program should then randomly quiz the user by displaying the name of a state 
# and asking the user to enter the state's capital.  
# The program should count of the number of correct and incorrect responses.  
# (You could alternatively use another country and provinces, 
# or countries of the world and capitals).

def main():
    quiz_logic(*get_states())

def get_states():
    states_list = {}
    state_number = int(input("Enter the number of states you want to be quizzed on: "))
    count = 1
    while count <= state_number:
        state = input(f"Enter the name of state {count}: ")
        capital = input(f"Enter the capital of state {count}: ")
        states_list[state.strip()] = capital.strip()
        count +=1
    return states_list, count

def quiz_logic(states_list, count):
    import random
    correct_answers = 0
    wrong_answers = 0
    attempt = "GO!"
    q_ask = int(input("How many practice questions would you like?"))
    q_answered = 0
    while attempt != "STOP" and q_ask > q_answered:
        state = random.choice(list(states_list))
        user_input = input(f"""What is the capital of {state}? 
        (Enter 'STOP' to quit):""")
        attempt = user_input.strip()
        if str(states_list[state]) == attempt:
            print("Correct!")
            correct_answers += 1
        elif attempt == "STOP":
            print("You stopped your quiz early.")
            break
        else:
            print(f"Incorrect! The answer is {str(states_list[state])}.")
            wrong_answers += 1
        q_answered += 1
    print(f"Your score is {correct_answers}/{q_answered}. You had {wrong_answers} wrong answers.")

main()

#This program was written by Logan Gibson on 10/23/25
#Its name is "State Capitals Quizzer"
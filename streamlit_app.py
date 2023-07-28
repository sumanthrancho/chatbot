import streamlit as st

bot_responses = {
    
                 "Good evening" : ['good','evening'],            
                  "Good Morning ! " : ["good", "morning"],        
                  "good afternoon " :["good","afternoon","student"],  
                  "I am young and dashing. " : ["how","old","you"],   
                  "I don't know. " : ["how", "she","old"],             
                  "Fine! Thank You.": ["how","are","you",'good','student'],  
                  "I don't know movies":["movies"],                          
                  'nothing' :["what" , 'doing'],                             
                  "Hi! What can I help you with?" :['hello','hai','hi'],     
                  "I don't have knowledge on it ": ['vegetables', 'fruits'], 
    
}

def get_response(user_input):
    # ... (existing get_response function code)

    if maxx < 10:
        response = "Bot: I am sorry but I'm not able to understand: " + str(user_input)
    else:
        response = "Bot: " + correct_response

    st.write(response)
    st.write(Matches)

def main():
    st.sidebar.title("Chatbot")
    st.sidebar.write("Hello! I am your Service manager bot. How can I help you?")

    user_input = st.text_input("You:", "")

    if user_input:
        user_input = user_input.lower()
        if user_input in ["bye", "goodbye", "takecare"]:
            st.write("Bot: Goodbye, Have a nice day.")
        else:
            get_response(user_input)

if __name__ == "__main__":
    main()

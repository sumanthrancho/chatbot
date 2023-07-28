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




def get_response():
  user_words = User_input.split()   
  Matches = {}

  for response in bot_responses:
    count = 0
    for word in bot_responses[response]:   
      if word in user_words:
        count = count+1                         

    percentage_match = (count / len(bot_responses[response])) * 100    

    Matches[response] = percentage_match

  maxx = 0
  for keys in Matches:
    if Matches[keys] > maxx:    
      maxx = Matches[keys]    
      Correct_response = keys

  if maxx < 10:
      response = "Bot: I am sorry but I'm not able to understand: " + str(user_input)
  else:
      response = "Bot: " + correct_response

  st.write(response)
  st.write(Matches)


st.sidebar.title("Chatbot")
st.write("Bot : Hello! I am your Service manager bot. How can I help you?")  
User_input = st.text_input("You : ")
while True:
  
  User_input=User_input.lower()  

  if(User_input == "bye" or User_input=='goodbye' or User_input == 'takecare'):
    st.error("Bot : Goodbye, Have a nice day. ")
    break
  if(User_input):
    get_response()
    User_input = st.text_input("You : ")


    # user_input = st.text_input("You:", "")

    # if user_input:
    #     user_input = user_input.lower()
    #     if user_input in ["bye", "goodbye", "takecare"]:
    #         st.write("Bot: Goodbye, Have a nice day.")
    #     else:
    #         get_response(user_input)


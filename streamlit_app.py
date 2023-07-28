# !pip install streamlit
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

#step 1 : it is comparing with the dictionary values.
#step 2 : find the percentage of the noof matches.( checking each word is matching or not)
#step 3 : Find the max of the percentage value going to display it.






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
    st.warning("Bot : I am sorry but I'm not able to understand :   "+str(User_input))
    st.write(Matches)

  else:
    st.success("Bot : ", Correct_response)
    st.write(Matches)



st.write("Bot : Hello! I am your Service manager bot. How can I help you?")  

while True:
  User_input = st.text_input("You : ")
  User_input=User_input.lower()  

  if(User_input == "bye" or User_input=='goodbye' or User_input == 'takecare'):
    st.error("Bot : Goodbye, Have a nice day. ")
    break
  else:
    get_response()


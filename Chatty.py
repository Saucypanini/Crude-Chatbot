###Chatbot

import sys
import random
import datetime

computer_greetings = [ "How are you?", "What are you doing?", "Can I help you?"]

computer_replies = ["Oh I don t know how to answer that","That sounds like something that I can agree on", "Who knows?","I must know what the meaning of life is first","Do you know the answer? Clearly not","Sometimes not knowing is better","I m on my break", "I haven t been outside before", "I don t plan on telling you anytime soon","Could you be more specific?","Dunno. You tell me","This is not fair Why can't I ask you questions?","I m on my break","I m on another break", "I m on my last break", "I m on my break after my break", "I m going home now Siri Where is home?"]

name = (raw_input)

print "Hello " + name("what is your name?")




print "what can I do for you"

while True:
  
  user_demands = raw_input(">")
 
 
  if user_demands == "hello":
    print "Hello, I don't usually do this, but have a nice day"
 
 
  elif user_demands == "bye":                                           ### this statement closes the program
    print "I didn't want to talk to you anyways"
    sys.exit()
    
    
  elif user_demands == "what is the weather?":
    print "I dont know, havent been outside before"
  
  
  elif user_demands == "can I ask a question?":
    print "No. Absolutely Not." 
  
  
  elif user_demands == "what is the date?":                             ### this statement brings up date/time
    print datetime.datetime.now()                                       ###this line had to be found via wiki.python.org
    
    
  elif user_demands == "what is the time?":
    print datetime.datetime.now()                                      ###this line had to be found via wiki.python.org
    
    
  elif user_demands =="what is the meaning of life?":
    print "The meaning of life, or the answer to the question 'What is the meaning of life?', pertains to the significance of living or existence in general. Many other related questions include 'Why are we here?', 'What is life all about', or 'What is the purpose of existence?' \nThere have been a large number of proposed answers to these questions from many different cultural and ideological backgrounds. The search for life's meaning has produced much philosophical, scientific, theological, and metaphysical speculation throughout history. Different people and cultures believe different things for the answer to this question.\nThe meaning of life as we perceive it is derived from philosophical and religious contemplation of, and scientific inquiries about existence, social ties, consciousness, and happiness. \nMany other issues are also involved, such as symbolic meaning, ontology, value, purpose, ethics, good and evil, free will, the existence of one or multiple gods, conceptions of God, the soul, and the afterlife. Scientific contributions focus primarily on describing related empirical facts about the universe, exploring the context and parameters concerning the 'how' of life. \nScience also studies and can provide recommendations for the pursuit of well-being and a related conception of morality. An alternative, humanistic approach poses the question, 'What is the meaning of my life?'"
                        
                                                ###__________LINE 45-46  is for laughs, no actual meaning or point is to be made___________###
                            
  elif user_demands == "can you sing?":
    print "I might say I can sing a couple of tunes, wanna hear? ......OHHHHHH!  Ummm....are you there?"
    sys.exit()
    print " Ummm....are you there?"
  
  
  else:
    print random.choice(computer_replies) + (" try asking another question")
                                                                        ### if none of the requirements are met
                                                                        ### program outputs random array from computer_replies
  
 
##################################




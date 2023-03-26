def newgame(questions, options):
 guesses = []
 correct_guess = 0
 ques_num = 1
 
 for key in questions :
 print("--------------------")
 print(key)
 for i in options[ques_num-1]:
 print(i)
 guess = input("Enter (A , B or C): ") 
 guess = guess.upper()
 guesses.append(guess)
 correct_guess += checkanswer(questions.get(key),guess)
 
 ques_num += 1
 
 displayscore(correct_guess,guesses) 
def checkanswer(answer , guess):
 if answer == guess :
 print("CORRECT!!!")
 return 1
 else :
 print("WRONG!!!")
 return 0
 
 
def displayscore(correct_guess,guesses):
 print("--------------------")
 print("RESULTS")
 print("--------------------")
 print("Answers : ",end=" ")
 for i in questions:
 print(questions.get(i),end=" ")
 print()
 print("Guesses : ",end=" ")
 for i in guesses:
 print(i,end=" ")
 print()
 
 score = (int)((correct_guess/len(questions))*100)
 print("Your score is : "+str(score)+ "%")
 
 if score<=50:
 print("You need to enhance your GENERAL KNOWLEDGE!!!! ")
 elif score>50 and score<100:
 print("GOOD!!!!")
 elif score==100:
 print("BRAVO!!!!!!!")
 
 print("--------------")
 
 print("Now returning back to the original game!!!!!")
 print("--------------")
 if colour == "RED":
 li1 = [3 , 4 , 7 ,8]
 print(li1)
 elif colour == "BLUE":
 li2 = [1 , 2 , 5 , 6]
 print(li2)
 elif colour == "YELLOW":
 li3 = [3 , 4, 7 ,8]
 print(li3)
 elif colour == "GREEN":
 li4 = [1 , 2 , 5 ,6]
 print(li4)
 else :
 print("--------------")
 
 n = int(input("Tipi Tipi Tap Which Number Do You Want? "))
 a = "QUEEN"
 b = "PRINCE"
 c = "PRINCESS"
 d = "KING"
 e = "BLESSING"
 f = "GREAT"
 g = "COMPUTER"
 h = "INTELLIGENT"
 if n == 1:
 print("Congratulations you are a",a,"!!!")
 elif n == 2:
 print("Congratulations you are a",b,"!!!")
 elif n == 3:
 print("Congratulations you are a",c,"!!!")
 elif n == 4:
 print("Congratulations you are a",d,"!!!")
 elif n == 5:
 print("Congratulations you are a",e,"!!!")
 elif n == 6:
 print("Congratulations you are",f,"!!!")
 elif n == 7:
 print("Congratulations you are a",g,"!!!")
 elif n == 8:
 print("Congratulations you are",h,"!!!")
questions = {
 "Who is the Prime Minister of India?":"B",
 "Which is the national flower of India?":"A",
 "Which is the national fruit of India?":"B",
}
options = [["A : Dr.Manmohan Singh","B : Narendra Modi","C : Arvind Kejriwal"],
 ["A : Lotus","B : Rose","C : Tulip"],
 ["A : Apple","B : Mango","C : Pineapple"]]
questions1 = {
 "Who is the father of personal computer?":"A",
 "What converts a high-level language source program into a machine language object 
program":"C",
 "What is the number of different charcters in ASCII coding system?":"A",
}
options1 = [["A : Edward Robert","B : Charles Babbage","C : Isaac Newton"],
 ["A : Converter","B : Encryption","C : Compiler"],
 ["A : 1024","B : 1023","C : 1099"]]
questions2 = {
 "What is the full form of CU?":"B",
 "Who is the father of computer science?":"A",
 "What is the scrambling of code known as?":"B",
}
options2 = [["A: Compound Unit ", "B : Control Unit", "C : Communication Unit"],
 ["A : Charles Babbage","B : Isaac Newton ","C : Edward Robert"],
 ["A : Converter","B : Encryption","C : Compiler"]]
questions3 = {
 "What is the full form of CPU?":"A",
 "First Page of website is termed as?":"B",
 "Which command is used to select the entire document?":"B",
}
options3 = [["A : Central Processing Unit","B : Central Programming Unit","C : Central processor 
Unit"],
 ["A : Desktop","B : Homepage","C : Open Page"],
 ["A : Ctrl+C","B : Ctrl+A","C : Ctrl+X"]]
questions4 = {
 "Which element is said to keep the bones strong?":"B",
 "How many rings is the Olympic ring said to have?":"C",
 "The logo for luxury car maker Porsche features which animal?":"A",
}
options4 = [["A : Phosphorus","B : Calcium","C : Sodium"],
 ["A : 7","B : 8","C : 5"],
 ["A : Horse","B : Cheetah","C : Jaguar"]]
questions5 = {
 "Which English City is known as steel city?":"B",
 "How many lives a cat is said to have?":"C",
 "How many wisdom teeth an average adult have?":"A",
}
options5= [["A :England","B : Sheffield","C : Scotland"],
 ["A : 8","B : 1","C : 9"],
 ["A : 4","B : 5","C : 6"]]
print("Colour Options: ")
li1 = ["RED", "BLUE", "GREEN", "YELLOW"]
for ele in li1:
 print (ele)
 
colour = input("Tipi Tipi Tap Which Colour Do You Want? ")
colour = colour.upper()
print("Chosen Colour: ",colour)
print("--------------------")
if colour not in li1:
 print("Please enter a valid colour!")
 pass
else:
 print("Now you'll have to answer some questions. Please enter level (easy/medium/hard)!!!")
level = input()
if colour == "RED":
 if level == "easy":
 newgame(questions,options)
 elif level == "medium":
 newgame(questions2,options2)
 elif level == "hard":
 newgame(questions1,options1)
 else:
 print("------------")
 
if colour == "BLUE":
 if level == "easy":
 newgame(questions,options)
 elif level == "medium":
 newgame(questions2,options2)
 elif level == "hard":
 newgame(questions1,options1)
 else:
 print("------------")
 
if colour == "GREEN":
 if level == "easy":
 newgame(questions3,options3)
 elif level == "medium":
 newgame(questions4,options4)
 elif level == "hard":
 newgame(questions5,options5)
 else:
 print("------------")
 
if colour == "YELLOW":
 if level == "easy":
 newgame(questions3,options3)
 elif level == "medium":
 newgame(questions4,options4)
 elif level == "hard":
 newgame(questions5,options5)
 else:
 print("------------")
 
print("------------")
print("Thankyou for playing!!!!!!!!!")
print("------------")

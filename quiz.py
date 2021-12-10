from flask import Blueprint, render_template, request

quiz = Blueprint('quiz', __name__)


questions = [
    {
        "id": "1",
        "question": "Is talkative"
    },
    {
        "id": "2",
        "question": "Tends to find fault with others"
    },
    {
        "id": "3",
        "question": "Does a thorough job"
    },
    {
        "id": "4",
        "question": "Is depressed, blue "
    },
    {
        "id": "5",
        "question": "Is original, comes up with new ideas"
    },
    {
        "id": "6",
        "question": "Is reserved"
    },
    {
        "id": "7",
        "question": "Is helpful and unselfish with others"
    },
    {
        "id": "8",
        "question": "Can be somewhat careless"
    },
    {
        "id": "9",
        "question": "Is relaxed, handles stress well"
    },
    {
        "id": "10",
        "question": "Is curious about many different things"
    },
    {
        "id": "11",
        "question": "Is full of energy"
    },
    {
        "id": "12",
        "question": "Starts quarrels with others "
    },
    {
        "id": "13",
        "question": "Is a reliable worker"
    },
    {
        "id": "14",
        "question": "Can be tense"
    },
    {
        "id": "15",
        "question": "Is ingenious, a deep thinker "
    },
    {
        "id": "16",
        "question": "Generates a lot of enthusiasm "
    },
    {
        "id": "17",
        "question": "Has a forgiving nature   "
    },
    {
        "id": "18",
        "question": "Tends to be disorganized "
    },
    {
        "id": "19",
        "question": "Worries a lot "
    },
    {
        "id": "20",
        "question": "Has an active imagination   "
    },
    {
        "id": "21",
        "question": "Tends to be quiet   "
    },
    {
        "id": "22",
        "question": "Is generally trusting   "
    },
    {
        "id": "23",
        "question": "Tends to be lazy   "
    },
    {
        "id": "24",
        "question": "Is emotionally stable, not easily upset  "
    },
    {
        "id": "25",
        "question": "Is inventive   "
    },
    {
        "id": "26",
        "question": "Has an assertive personality  "
    },
    {
        "id": "27",
        "question": "Can be cold and aloof   "
    },
    {
        "id": "28",
        "question": "Perseveres until the task is finished   "
    },
    {
        "id": "29",
        "question": "Can be moody  "
    },
    {
        "id": "30",
        "question": "Values artistic, aesthetic experiences  "
    },
    {
        "id": "31",
        "question": "Is sometimes shy, inhibited   "
    },
    {
        "id": "32",
        "question": "Is considerate and kind to almost everyone"
    },
    {
        "id": "33",
        "question": "Does things efficiently "
    },
    {
        "id": "34",
        "question": "Remains calm in tense situations   "
    },
    {
        "id": "35",
        "question": "Prefers work that is routine  "
    },
    {
        "id": "36",
        "question": "Is outgoing, sociable "
    },
    {
        "id": "37",
        "question": "Is sometimes rude to others  "
    },
    {
        "id": "38",
        "question": "Makes plans and follows through with them  "
    },
    {
        "id": "39",
        "question": "Gets nervous easily"
    },
    {
        "id": "40",
        "question": "Likes to reflect, play with ideas   "
    },
    {
        "id": "41",
        "question": "Has few artistic interests "
    },
    {
        "id": "42",
        "question": "Likes to cooperate with others   "
    },
    {
        "id": "43",
        "question": " Is easily distracted   "
    },
    {
        "id": "44",
        "question": "Is sophisticated in art, music, or literature"
    }
]

@quiz.route("/quiz", methods=['POST', 'GET'])
def personalityTest():

    if request.method == 'GET':
        return render_template("quiz.html", data=questions)
    if request.method == 'POST':
        ans1=0
        ans2=0
        ans3=0
        ans4=0
        ans5=0
        per1=0
        per2=0
        per3=0
        per4=0
        per5=0
        new_list=[]

        for question in questions:
            result=request.form.to_dict()

        new_list=list(result.values())

        counter=0
        while (counter<6):
            for element in range(counter,44,5):
                if(counter==0):
                    if(element==5 or element==20 or element==30 ):
                        if(new_list[element]=='1'):
                            ans1=ans1+5
                        elif(new_list[element]=='2'):
                            ans1=ans1+4
                        elif(new_list[element]=='4'):
                            ans1=ans1+2
                        elif(new_list[element]=='5'):
                            ans1=ans1+1
                        elif(new_list[element]=='3'):
                            ans1=ans1+3
                    else:
                        ans1=ans1+int(new_list[element])
               
                elif(counter==1):
                    if(element==1 or element==11 or element==26 or element==36 ):
                        if(new_list[element]=='1'):
                            ans2=ans2+5
                        elif(new_list[element]=='2'):
                            ans2=ans2+4
                        elif(new_list[element]=='4'):
                            ans3=ans3+2
                        elif(new_list[element]=='5'):
                            ans4=ans4+1
                        elif(new_list[element]=='3'):
                            ans5=ans5+3
                    else:
                        ans2=ans2+int(new_list[element])
                
                
                elif(counter==2):
                    if(element==7 or element==17 or element==22 or element==42 ):
                        if(new_list[element]=='1'):
                            ans3=ans3+5
                        elif(new_list[element]=='2'):
                            ans3=ans3+4
                        elif(new_list[element]=='4'):
                            ans3=ans3+2
                        elif(new_list[element]=='5'):
                            ans3=ans3+1
                        elif(new_list[element]=='3'):
                            ans3=ans3+3
                    else:
                        ans3=ans3+int(new_list[element])
                
                
                elif(counter==3):
                    if(element==8 or element==23 or element==33):
                        if(new_list[element]=='1'):
                            ans4=ans4+5
                        elif(new_list[element]=='2'):
                            ans4=ans4+4
                        elif(new_list[element]=='4'):
                            ans4=ans4+2
                        elif(new_list[element]=='5'):
                            ans4=ans4+1
                        elif(new_list[element]=='3'):
                            ans4=ans4+3
                    else:
                        ans4=ans4+int(new_list[element])
                
                
                elif(counter==4):
                    if(element==34 or element==40):
                        if(new_list[element]=='1'):
                            ans5=ans5+5
                        elif(new_list[element]=='2'):
                            ans5=ans5+4
                        elif(new_list[element]=='4'):
                            ans5=ans5+2
                        elif(new_list[element]=='5'):
                            ans5=ans5+1
                        elif(new_list[element]=='3'):
                            ans5=ans5+3
                    else:
                        ans5=ans5+int(new_list[element])
            counter=counter+1
        per1=((ans1-1)/40)*100
        per2=(ans2/45)*100
        per3=(ans3/45)*100
        per4=(ans4/40)*100
        per5=((ans5+6)/50)*100
        
        per1= round(per1, 2)
        per2= round(per2, 2)
        per3= round(per3, 2)
        per4= round(per4, 2)
        per5= round(per5, 2)
    
    return render_template('submittest.html', result=new_list, ans1=per1, ans2=per2, ans3=per3, ans4=per4, ans5=per5)

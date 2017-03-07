from flask import Flask,render_template,url_for,request,redirect
from functions1 import *
from collections import OrderedDict

user=""
print dataset
dataset=update_dataset(dataset)
print dataset
dataset2={}
dataset3={}
movies_added=[]

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("login_page.html")

@app.route('/home',methods=['GET','POST'])
def login():

    error=None
    if request.method == 'POST':
        if request.form['username']!="":
            username=request.form['username']
            fo=open("test.txt","w")
            fo.truncate()
            fo.write(username)

            return render_template("home.html",username=username)

        else:
            error="You have not entered a correct username"
            return render_template("error.html",error=error)


    else:
        return render_template("login_page.html")


@app.route('/rating',methods=['GET','POST'])
def rating():

    if request.method == 'POST':
        lf=request.form['lf']
        m1=float(request.form['m1'])
        m2=float(request.form['m2'])
        m3=float(request.form['m3'])
        m4=float(request.form['m4'])
        m5=float(request.form['m5'])
        m6=float(request.form['m6'])
        m7=float(request.form['m7'])
        m8=float(request.form['m8'])
        m9=float(request.form['m9'])
        m10=float(request.form['m10'])

        checkboxes=request.form.getlist('check')
        test_arr=[]
        for check in checkboxes:
            test_arr.append(str(check))
        user_set=set(test_arr)

        if lf == 'A':
            names=['Avengers','Avatar','Fury','Twilight','Justlikeheaven','Fightclub','Bridewar','Hugo','Kungfupanda','Matrix']

        elif lf == 'B':
            names=['Dilwale','Barfi','Fukrey','Housefull','Kika','Neerja','Nh10','Raajneeti','Ready','Shaandaar']

        elif lf == 'C':
            names=['Pancharangi','Bombat','Mungarumale','Manasaare','Shivalinga','Ranna','Hudugaru','Rangitaranga','Annabond','Galaate']

        fo=open("test.txt","rb")
        user=fo.read()
        fo.close()
        movies=[m1,m2,m3,m4,m5,m6,m7,m8,m9,m10]

        for (mov,val) in zip(names,movies):
            if user in dataset:
                dataset[user].update({mov:val})
            else:
                dataset.update({user:{mov:val}})





        update_csv(dataset)


        sim_scores=similarity_scores(user)
        print sim_scores
        sim_scores2=dict.copy(sim_scores)

        final_op=OrderedDict()

        while(sim_scores):
            max_person=fetch_max(sim_scores)
            print max_person

            movie_scores=get_movie_score(dataset,user,max_person,user_set)

            if max_person in final_op:
                final_op[max_person].update(movie_scores)
            else:
                final_op.update({max_person:movie_scores})

            sim_scores.pop(max_person)

            print final_op

        return render_template("rating.html",usr=user,scr=sim_scores2,m_list=final_op)

if __name__ == '__main__':
    app.run(debug=True)

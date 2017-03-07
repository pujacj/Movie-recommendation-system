from math import sqrt
import csv
import os.path

dataset={}
movies_added=[]

def update_dataset(dataset):
    f=open("user_ratings.csv","rb")
    reader=csv.reader(f)

    for row in reader:
        usr=row[0]
        mov=row[1]
        val=float(row[2])

        if usr in dataset:
            dataset[usr].update({mov:val})
        else:
            dataset.update({usr:{mov:val}})

    f.close()
    return dataset

def update_csv(dataset):
    f=open("user_ratings.csv","wb")
    writer=csv.writer(f)

    for user,movie_value in dataset.items():
        for movie,value in movie_value.items():
            writer.writerow([user,movie,value])

    f.close()




def common_count(set,person1,person2):
    both_viewed=[]
    for item in set[person1]:

        if item in set[person2]:

            if item in both_viewed:
                continue
            else:
                both_viewed.append(item)

    return both_viewed



def sim_compute(person1,person2):
    sum_of_eclidean_distance=[]

    both_viewed=common_count(dataset,person1,person2)
    if len(both_viewed) == 0:
        return 0

    for movie in both_viewed:
        sum_of_eclidean_distance.append(pow(dataset[person1][movie] - dataset[person2][movie],2))
    sum_of_eclidean_distance = sum(sum_of_eclidean_distance)

    return 1/(1+sqrt(sum_of_eclidean_distance))





def similarity_scores(person):
    sim_scores={}
    for other in dataset:
        if other==person:
            continue
        sim_scores[other]=round(sim_compute(person,other),4)

    return sim_scores


def fetch_max(sim_scores):
    max=-1
    max_person=''

    for person in sim_scores.keys():
        if sim_scores[person]>max:
            max=sim_scores[person]
            max_person=person

    return max_person


def get_movie_score(dataset,user,max_person,user_set):

    global movies_added
    movie_scores={}
    f1=open("features.csv","rb")
    reader=csv.reader(f1)

    for row in reader:

        for movie in dataset[max_person]:
            if movie not in dataset[user]:

                if row[0]==movie:
                    if movie not in movies_added:

                        feature_set=set()
                        for i in row:
                            if i!=row[0]:
                                if i not in feature_set:
                                    feature_set.add(i)

                        p=feature_set.intersection(user_set)
                        q=feature_set.union(user_set)
                        result=len(p)/float(len(q))

                        movie_scores.update({movie:result})
                        movies_added.append(movie)

    f1.close()
    return movie_scores

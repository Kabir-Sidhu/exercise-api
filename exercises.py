import os, json, operator

def getExercise(exercise_id: str = None):
    exercise_json = open(f"exercises/{exercise_id}/exercise.json", "r")

    exercise = json.load(exercise_json)

    images = []

    for i in os.listdir(f"exercises/{exercise_id}/images"):
        images.append(i)

    exercise["images"] = images

    exercise_json.close()

    return exercise

def searchExercises(query: str):
    results = []

    _query = query

    query = query.split(" ")

    for i in os.listdir("exercises"):
        name = i.replace("_", " ")

        score = 0

        if _query.lower() == name.lower() or _query.lower() == i.lower():
            score += 100

        for j in query:
            if j.lower() in name.lower() or j.lower() in i.lower():
                score += 1
        
        if score > 0:
            results.append({"id": i, "name": name, "score": score})
    
    # sorted_results = dict(sorted(results.items(), key=lambda item: item[1]['score'], reverse=True))
    results.sort(key=operator.itemgetter('score'))

    results.reverse()

    return results


if __name__ == "__main__":
    results = searchExercises("reverse barbell curl")

    for i in results:
        print((i["id"], i["name"], i["score"]))
    print(results[0])
    
    exercise = getExercise("Reverse_Barbell_Curl")

    print(exercise)
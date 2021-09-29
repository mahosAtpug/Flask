from flask import Flask , jsonify , request

app = Flask(__name__)

tasks = [{
            "id": 1,
            "title" : u"buy groceries",
            "description" : u"milk , cheese , pizza , biscuits",
            "done" : False
        },
        {
            "id": 2,
            "title": u"Buy clothes",
            "description" : u"t-shirts , jeans , shorts , pants",
            "done" : False
        }

    ]

@app.route("/get-tasks")
def get_tasks():
    return jsonify({
        "data" : tasks
    })

@app.route("/add-tasks" , methods = ["POST"])
def add_tasks():
    if not request.json:
        return jsonify({
            "status" : "ERROR",
            "message": "Please Provide Data"

        }, 400)

    task = {"id":tasks[-1]["id"]+1,
            "title" : request.json["title"],
            "description" : request.json.get("description" , ""),
            "done" : False}

    tasks.append(task)
    return jsonify({
        "status" : "Success",
        "message": "Task added Successfully!!!"
    })

if(__name__ == "__main__"):
    app.run(debug = True)


from flask import Flask, jsonify, request

app  = Flask(__name__)
users = []
??

@app.route('/register', methods=['POST'])
def regi():
    jj = request.get_json()
    first = jj.get("first")
    second = jj.get("second")
    email = jj.get("email")
    password = jj.get("password")
   
    if not (first, second, email):
        return jsonify({"errMsg": "you must have them fields!!!"})
    
    
    additional_user = {
        "id": len(users)+1,
        "first":first,
        "second":second,
        "email":email,
        "password":password
    }
    users.append(additional_user)
    return jsonify(additional_user), 200
@app.route("/users", methods=["GET"])
def getem():
    return jsonify(users), 200

@app.route("/login", methods=["POST"])
def log():
    jj = request.get_json()
    email = jj.get("email")
    passy = jj.get("password")
    if not email:
        return jsonify({"we mzee": "register firest"})
    for aloo in users:
        if aloo["email"] == email:
            if aloo["password"] == passy:
                return jsonify({"congrats":"youve logged in succesfully!!!",
                                "my Buddy": aloo})
            else:
                return jsonify({"prob":"there was a problem"})
        return jsonify({"err" : "not that password or email "})

    
@app.route("/users/<int:id>", methods=["PUT"]) 
def aptd(id):
    jj = request.get_json()
    for u in users:
      if u["id"] == id:
        u["first"] = jj.get("first", u["first"])
        u["second"] = jj.get("second", u["second"])
        u["email"] = jj.get("email", u["email"])
        u["password"] = jj.get("password", u["password"])
        return jsonify(u), 200
    return jsonify({"erro":"the user is not here"})

@app.route("/users/<int:id>", methods=["DELETE"])
def rem(id):
    
    for u in users:
        if u["id"] == id:
             users.remove(u)
             return jsonify({"msg":"Removed succesfully!!!"})
        
    return jsonify({"err":"error"})
    
if __name__=="__main__":
    app.run(debug=True)
from main import app,db
from flask import request,jsonify
from main.models import Friend



#Get all friends
@app.route("/api/friends",methods=["GET"])
def get_friends():
    friends = Friend.query.all()
    result = [friend.to_json() for friend in friends]
    return jsonify(result)

#Get a single friend
@app.route("/api/friends/<int:id>",methods=["GET"])
def get_friend(id):
    friend = Friend.query.get(id)

    if friend is None:
        return jsonify({"error":f"{id} not found"}),404
    
    result = friend.to_json()
    return jsonify(result)


#create a friend
@app.route("/api/friends",methods=["POST"])
def create_friends():
    try:

        data=request.json

        required_fields=['name','role','gender','description']

        for field in required_fields:
            if field not in data:
                return jsonify({"error":f"Missing required field {field}"}),400

        name=data.get('name')
        role=data.get('role')
        gender=data.get('gender')
        description=data.get('description')

        #fetch the image_url
        if gender.lower() == 'male':
            img_url=f"https://avatar.iran.liara.run/public/boy?username={name}"
        elif gender.lower() == 'female':
            img_url=f"https://avatar.iran.liara.run/public/girl?username={name}"
        else:
            img_url=None
        
        #create a new friend object
        new_friend = Friend(
            name=name,
            role=role,
            gender=gender,
            description=description,
            img_url=img_url
        )

        db.session.add(new_friend)
        db.session.commit()
        return jsonify({"msg":"new friend created successfully"}),201

    except Exception as e:
       db.session.rollback()
       return jsonify({"error":str(e)}),500
    
#Delete a friend
@app.route("/api/friends/<int:id>",methods=['DELETE'])
def delete_friend(id):
    try:
       del_frd=Friend.query.get(id)
       if del_frd is None:
           return jsonify({"error":f"{id} not found"}),404
       db.session.delete(del_frd)
       db.session.commit()
       return jsonify({"Msg":f"{id} deleted successfully"})
    except Exception as e:
        db.session.rollback()
        return jsonify({"error":str(e)}),500
    
#Update a friend
@app.route("/api/friends/<int:id>",methods=['PATCH'])
def update_friend(id):
    try:
       upd_frd=Friend.query.get(id)
       if upd_frd is None:
           return jsonify({"error":f"{id} not found"}),404
       
       upd_frd.name=request.json.get('name',upd_frd.name)
       upd_frd.role=request.json.get('role',upd_frd.role)
       upd_frd.description=request.json.get('description',upd_frd.description)
       upd_frd.gender=request.json.get('gender',upd_frd.gender)

       #fetch the image_url
       if upd_frd.gender.lower() == 'male':
            upd_frd.img_url=f"https://avatar.iran.liara.run/public/boy?username={upd_frd.name}"
       elif upd_frd.gender.lower() == 'female':
            upd_frd.img_url=f"https://avatar.iran.liara.run/public/girl?username={upd_frd.name}"
       else:
            upd_frd.name.img_url=None

       

       db.session.commit()
       
       return jsonify({"msg":f"{id} updated successfully"})
    except Exception as e:
        db.session.rollback()
        return jsonify({"error":str(e)}),500
       


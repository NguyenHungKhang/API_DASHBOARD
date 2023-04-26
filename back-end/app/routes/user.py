from fastapi import APIRouter, HTTPException, status
from app.models.user import User
from app.config.db import db
from app.schemas.user import userEntity, usersEntity
from app.utils.utils import (
    get_hashed_password,
    verify_password,
    create_access_token,
    create_refresh_token,
)
from bson import ObjectId
from datetime import datetime, date

app_router = APIRouter()


@app_router.get("/")
async def main():
    return {"message": "Hello World"}


# RETRIEVE ALL ACCOUNT
@app_router.get("/users")
async def find_all_users():
    result = usersEntity(db.find())
    listUsers = []
    for r in result:
        r["image"] = ""
        if r["role"] != 0:
            length = len(r["accessed_at"])
            dtAcc = ["NaN", "NaN"]
            if length > 0:
                time = datetime.fromisoformat(str(r["accessed_at"][length - 1]))
                dtAcc = time.strftime("%Y/%m/%d %H:%M:%S").split(" ")
            time = datetime.fromisoformat(str(r["created_at"]))
            dtCre = time.strftime("%Y/%m/%d %H:%M:%S").split(" ")
            listUsers.append(
                {
                    "id": r["id"],
                    "email": r["email"],
                    "status": r["status"],
                    "role": r["role"],
                    "accessed_at": {"date": dtAcc[0], "time": dtAcc[1]},
                    "created_at": {"date": dtCre[0], "time": dtCre[1]},
                }
            )

    return {"status": "success", "data": listUsers}


# RETRIEVE ACCOUNT BY ID
@app_router.get("/user/{id}")
async def find_user_by_id(id: str):
    result = userEntity(db.find_one({"_id": ObjectId(id)}))
    return {"status": "success", "data": result}


# REGISTER ACCOUNT
@app_router.post("/user/register")
async def register(user: User):
    # check existed email
    check = usersEntity(db.find({"email": str(user.email.lower())}))

    if len(check) != 0:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Can't create account with email: {user.email.lower()}",
        )
    elif int(user.role) == 0 or int(user.role) > 2 or int(user.role) < 0:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Can't create account"
        )
    elif user.email.lower() == "" or user.password == "":
        raise HTTPException(status_code=406, detail="Not Acceptable")
    else:
        user.password = get_hashed_password(user.password)
        user.created_at = datetime.now()
        user.email = user.email.lower()
        _id = db.insert_one(dict(user))
        result = userEntity(db.find_one({"_id": _id.inserted_id}))
        return {
            "message": "Successfully created user: " + result["email"],
        }


# UPDATE ACCOUNT BY ID
@app_router.put("/user/{id}")
async def update_user(id: str, user: User):
    try:
        # check existed email
        findUser = userEntity(db.find_one({"_id": ObjectId(id)}))

        # if email's existed return status 409 (admin's role is 1)
        # if role = 0 or out range[0;2] return status 401
        # else return status 200

        if findUser["email"] != user.email.lower():
            check = usersEntity(db.find({"email": user.email.lower()}))
            if len(check) != 0:
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail=f"Can't update email: {user.email.lower()}",
                )
            elif (
                int(user.role) == 0
                or int(user.role) > 2
                or int(user.role) < 0
                or findUser["role"] == 0
            ):
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Can't update account",
                )
        if user.password == "":
            user.password = findUser["password"]
        if user.email == "":
            user.email = findUser["email"]
        if user.status == 0:
            user.status == findUser["status"]
        user.accessed_at = findUser["accessed_at"]
        user.created_at = findUser["created_at"]
        user.image = findUser["image"]
        db.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(user)})
        return {"status": "success"}
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Can't update account"
        )


# DELETE ACCOUNT BY ID
@app_router.delete("/user/{id}")
async def delete_user(id: str):
    try:
        check = userEntity(db.find_one({"_id": ObjectId(id)}))
        if check["role"] != 0:
            db.find_one_and_delete({"_id": ObjectId(id)})
            return {"status": "success"}
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="You can delete this account!",
            )
    except:
        raise HTTPException(status_code=400, detail="Not found")


# LOGIN USER
@app_router.post("/user/login")
async def user_login(user: User):
    try:
        print(user.password)
        result = userEntity(db.find_one({"email": str(user.email.lower())}))

        if not verify_password(user.password, result["password"]):
            raise HTTPException(status_code=400, detail="Incorrect email or password")

        acc = result["accessed_at"]
        length = len(acc)

        if length > 0:
            if acc[length - 1].date() != date.today():
                result["accessed_at"].append(datetime.now())
                db.find_one_and_update(
                    {"_id": ObjectId(result["id"])}, {"$set": dict(result)}
                )

        else:
            result["accessed_at"].append(datetime.now())
            db.find_one_and_update(
                {"_id": ObjectId(result["id"])}, {"$set": dict(result)}
            )
        return {
            "data": {
                "id": result["id"],
                "email": result["email"],
                "role": result["role"],
            },
            "access_token": create_access_token(result["email"]),
            "refresh_token": create_refresh_token(result["email"]),
        }
        # return {"status": "success"}
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Login failed"
        )

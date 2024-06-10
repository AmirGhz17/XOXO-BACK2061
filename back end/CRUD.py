from typing import List
from sqlalchemy.orm import Session
import models, schemas


def get_user(db: Session, name: str):
    return db.query(models.User).filter(models.User.name == name).first()

def get_users(db: Session):
    return db.query(models.User).all()

def change_user_score(db: Session,name: str,change: int):
    db.query(models.User).filter(models.User.name == name).update({'score' : models.User.score + change})
    db.commit()
    changedUser = db.query(models.User).filter(models.User.name == name).first()
    return changedUser
# def change_user_scores(db: Session,items : List[schemas.Item]):
#     changedUsers = []
#     for item in items:
#         if (item.status == "Win"):
#             db.query(models.User).filter(models.User.name == item.name).update({'score' : models.User.score + 1 })
#             db.commit()
#             changedUser = db.query(models.User).filter(models.User.name == item.name).first()
#             changedUsers.append(changedUser)
#         elif (item.status == "Lose") :
#             db.query(models.User).filter(models.User.name == item.name).update({'score' : models.User.score - 1 })
#             db.commit()
#             changedUser = db.query(models.User).filter(models.User.name == item.name).first()
#             changedUsers.append(changedUser) 
       
#     return changedUsers


def get_top_users(db: Session , limit = None):
    if(limit == None):
       return db.query(models.User).order_by(models.User.score.desc()).all() 
    else:
        return db.query(models.User).order_by(models.User.score.desc()).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(name= user.name, score=user.score)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
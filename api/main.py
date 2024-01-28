from fastapi import FastAPI
import models #database structure
from database import engine #db configuration
from routers import users,login,weightdata

app=FastAPI()

app.include_router(users.router)
app.include_router(login.router)
app.include_router(weightdata.router)

#convert models to db table
models.Base.metadata.create_all(engine)
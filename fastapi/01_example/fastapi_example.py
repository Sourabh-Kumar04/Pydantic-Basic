from fastapi import Fastapi, Depends
from pydantic import BaseModel, EmailStr

app = FastAPI()

class UserSignUp(BaseModel):
    username: str
    email: EmailStr
    password: str

class Settings(BaseModel):
    app_name: str = "Pydantic App"
    admin_email: str = 'admin@example.com'

def get_settings():
    return Settings

@app.post('/signup')
def signup(user: UserSignUp):
    return {'message': f"{user.username} signup successfully"}

@app.get('/Settings')
def get_settings_endpoint(settings: Settings = Depends(get_settings)):
    return settings

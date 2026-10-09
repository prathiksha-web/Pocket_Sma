from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi import Request
from app.database import create_user,get_user_by_email
from app.models import RegisterRequest,LoginRequest
from app.security import hash_password,verify_password,set_auth_cookie,clear_auth_cookie,get_current_user
router=APIRouter()
@router.post('/register')
def register(p:RegisterRequest):
 if get_user_by_email(p.email): return JSONResponse({'detail':'An account with this email already exists.'},status_code=409)
 u=create_user(p.email,p.name,hash_password(p.password)); r=JSONResponse({'message':'Registration successful','user':{'id':u['id'],'name':u['name'],'email':u['email']}}); set_auth_cookie(r,u['id']); return r
@router.post('/token')
def token(p:LoginRequest):
 u=get_user_by_email(p.email)
 if not u or not verify_password(p.password,u['password_hash']): return JSONResponse({'detail':'Incorrect email or password.'},status_code=401)
 r=JSONResponse({'access_token':'httpOnly-cookie','token_type':'bearer'}); set_auth_cookie(r,u['id']); return r
@router.post('/login')
def login(p:LoginRequest): return token(p)
@router.post('/logout')
def logout(): r=JSONResponse({'message':'Logged out'}); clear_auth_cookie(r); return r
@router.get('/session-info')
def session_info(request:Request):
 u=get_current_user(request); return {'logged_in':True,'user':{'id':u['id'],'name':u['name'],'email':u['email']}}
@router.get('/session-data')
def session_data(request:Request):
 u=get_current_user(request); return {'user_id':u['id'],'name':u['name'],'email':u['email']}

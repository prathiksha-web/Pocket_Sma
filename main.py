from pathlib import Path
from fastapi import FastAPI,Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.config import get_settings
from app.database import init_db
from app.routes.auth import router as auth_router
from app.routes.planners import router as planner_router
s=get_settings(); base=Path(__file__).resolve().parent; templates=Jinja2Templates(directory=str(base/'templates'))
app=FastAPI(title=s.app_name,version='1.0.0')
app.add_middleware(CORSMiddleware,allow_origins=s.frontend_origins,allow_credentials=True,allow_methods=['*'],allow_headers=['*'])
@app.on_event('startup')
def startup(): init_db()
app.include_router(auth_router); app.include_router(planner_router)
@app.get('/health')
def health(): return {'status':'ok','service':s.app_name,'ai_model':s.gemini_model}
@app.get('/',response_class=HTMLResponse)
def home_page(request:Request): return templates.TemplateResponse('index.html',{'request':request})
@app.get('/login',response_class=HTMLResponse)
def login_page(request:Request): return templates.TemplateResponse('login.html',{'request':request})
@app.get('/register',response_class=HTMLResponse)
def register_page(request:Request): return templates.TemplateResponse('register.html',{'request':request})
@app.get('/dashboard',response_class=HTMLResponse)
def dashboard(request:Request): return templates.TemplateResponse('dashboard.html',{'request':request})
@app.get('/planner/{planner}',response_class=HTMLResponse)
def planner_page(request:Request,planner:str):
 if planner not in {'home','party','jewelry'}: planner='home'
 return templates.TemplateResponse(f'{planner}.html',{'request':request,'planner':planner})
@app.get('/history',response_class=HTMLResponse)
def history_page(request:Request): return templates.TemplateResponse('history.html',{'request':request})
@app.get('/recommendation/{recommendation_id}',response_class=HTMLResponse)
def recommendation_page(request:Request,recommendation_id:int): return templates.TemplateResponse('recommendation.html',{'request':request,'recommendation_id':recommendation_id})
if __name__=='__main__':
 import uvicorn; uvicorn.run('app.main:app',host='127.0.0.1',port=8000,reload=True)

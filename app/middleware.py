from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware import Middleware

from .middlewares.redirect_recources import RedirectsMiddleware

# docs:  https://www.starlette.io/middleware/

######################## Cors Setup ########################
# UPDATE CORS Setup
origins = [
    "*",  # replace  "http://localhost:3000",
]

MyCustomCORSMiddleware = Middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
    allow_credentials=True,
)
#############################################################

redirections = {
    "/docs": "/",
    # "/login": "/auth/login",
    # "/sign-up": "/auth/register",
}


middlewareStack = [
    MyCustomCORSMiddleware,
    Middleware(RedirectsMiddleware, path_mapping=redirections),
]

from fastapi import FastAPI
from presentation.product_routes import routes
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(description = "API for inventory management")
app.include_router(routes,prefix='/api')

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


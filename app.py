from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from agent import build_weather_agent, ask_agent
from starlette.middleware.base import BaseHTTPMiddleware

import uuid

weather_agent = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    global weather_agent

    weather_agent = build_weather_agent()

    yield

    weather_agent = None


app = FastAPI(
    title="Weather Agent API",
    version="1.0.0",
    lifespan=lifespan
)


class WeatherRequest(BaseModel):
    question: str


class WeatherResponse(BaseModel):
    response: str


class SessionMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next):

        session_id = request.cookies.get("session_id")

        if not session_id:
            session_id = str(uuid.uuid4())

        request.state.session_id = session_id

        response = await call_next(request)

        response.set_cookie(
            key="session_id",
            value=session_id,
            httponly=True,
            secure=False,  # True behind HTTPS
            samesite="lax"
        )

        return response

app.add_middleware(SessionMiddleware)

@app.get("/")
def health_check():
    return {
        "status": "healthy",
        "agent": "weather-agent"
    }


@app.post("/ask", response_model=WeatherResponse)
def ask_weather(
    request: Request,
    payload: WeatherRequest
):

    try:
        
        session_id = request.state.session_id
        
        answer = ask_agent(
            weather_agent,
            session_id,
            payload.question
        )


        return WeatherResponse(
            response=answer
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
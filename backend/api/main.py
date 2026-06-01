"""
Quant Platform API - Main Application Module

This module contains the FastAPI application setup and core endpoints
for the Quant Platform API.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

# Initialize FastAPI application
app = FastAPI(
    title="Quant Platform API",
    version="1.0.0",
    description="A comprehensive quantitative trading platform API",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

# Configure CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)


@app.get("/", tags=["root"])
async def root() -> JSONResponse:
    """
    Root endpoint - Returns API information.
    
    Returns:
        JSONResponse: API name, version, and status
    """
    return JSONResponse(
        status_code=200,
        content={
            "name": "Quant Platform API",
            "version": "1.0.0",
            "status": "running"
        }
    )


@app.get("/health", tags=["health"])
async def health_check() -> JSONResponse:
    """
    Health check endpoint - Verifies API is responsive.
    
    Returns:
        JSONResponse: Health status
    """
    return JSONResponse(
        status_code=200,
        content={
            "status": "healthy"
        }
    )


if __name__ == "__main__":
    import uvicorn
    
    # Run the application using Uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )

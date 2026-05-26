"""FastAPI application entrypoint."""
from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference
from app.api.router import router

app = FastAPI()
app.include_router(router)


@app.get("/scalar", include_in_schema=False)
def get_scalar_docs():
    """Return the Scalar API reference."""
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Scalar API",
    )

"""LCS web app."""
from pathlib import Path
from typing import List, Sequence

from fastapi import FastAPI
from pydantic import BaseModel, Field, validator
from starlette.applications import Starlette
from starlette.responses import RedirectResponse
from starlette.staticfiles import StaticFiles

from lcs.main import matches


API = FastAPI(title="LCS", description="Longest Common String")
APP = Starlette()


class String(BaseModel):
    """Individual string item."""

    value: str = Field(
        min_length=1, max_length=1024,
    )


class SetOfStrings(BaseModel):
    """Set of strings to query for LCS."""

    setOfStrings: List[String] = Field(min_items=2, max_items=1024)

    @validator("setOfStrings")
    def _check_and_convert(cls, values):
        strs = [x_.value for x_ in values]
        if len(strs) != len(set(strs)):
            raise ValueError("strings must be unique.")
        return strs


class LCSResults(BaseModel):
    """Longest common substring results."""

    lcs: Sequence[String]


@API.post("/", response_model=LCSResults, tags=["Query"])
async def query(strings: SetOfStrings):
    """Endpoint to search for LCS."""
    return LCSResults(lcs=[String(value=x_) for x_ in matches(strings.setOfStrings)])


@API.get("/", tags=["Redirect"])
async def to_docs():
    """Redirects from API root to OpenAPI documention."""
    return RedirectResponse(url="/lcs/docs")


def main():
    """Attach mounts and routes."""
    web_dir = Path(__file__).parent.joinpath("html")
    APP.add_route("/", StaticFiles(directory=web_dir, html=True), name="home")
    APP.mount("/css", StaticFiles(directory=web_dir.joinpath("css")), name="css")
    APP.mount("/lcs", API, name="api")


if __name__ == "__main__":
    raise RuntimeError("These aren't the droids you're looking for.")

main()

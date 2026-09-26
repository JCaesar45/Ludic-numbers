"""
AURELIS backend — FastAPI service exposing the Ludic engine
and the product catalog for the storefront.
"""

from __future__ import annotations
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field
from typing import List
import time
import os

from ludic import ludic  # local module

app = FastAPI(title="AURELIS API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)


class LudicResponse(BaseModel):
    bound: int
    count: int
    elapsed_ms: float
    values: List[int]


class Product(BaseModel):
    id: str
    name: str
    artisan: str
    origin: str
    ludic_index: int = Field(..., alias="ludicIndex")
    price_eur: int = Field(..., alias="priceEUR")
    cert: bool
    technique: str

    class Config:
        populate_by_name = True


CATALOG: List[Product] = [
    Product(id="AUR-001", name="Filigree Drop Earrings", artisan="Amadou Diallo",
            origin="Dakar, SN", ludicIndex=2, priceEUR=1240, cert=True, technique="Filigree"),
    Product(id="AUR-002", name="Cascade Signet Ring", artisan="Yuki Tanaka",
            origin="Kyoto, JP", ludicIndex=3, priceEUR=2180, cert=True, technique="Mokume-gane"),
    Product(id="AUR-003", name="Meridian Cuff", artisan="Ines Moreau",
            origin="Paris, FR", ludicIndex=5, priceEUR=3420, cert=True, technique="Repoussé"),
    Product(id="AUR-004", name="Seventh Cycle Pendant", artisan="Amadou Diallo",
            origin="Dakar, SN", ludicIndex=7, priceEUR=1680, cert=True, technique="Granulation"),
    Product(id="AUR-005", name="Undecim Chain", artisan="Yuki Tanaka",
            origin="Kyoto, JP", ludicIndex=11, priceEUR=2890, cert=False, technique="Chain weave"),
    Product(id="AUR-006", name="Tertius Brooch", artisan="Ines Moreau",
            origin="Paris, FR", ludicIndex=13, priceEUR=4120, cert=True, technique="Enamel"),
]


@app.get("/api/ludic", response_model=LudicResponse)
def api_ludic(n: int = Query(26, ge=1, le=100_000)):
    t0 = time.perf_counter()
    values = ludic(n)
    t1 = time.perf_counter()
    return LudicResponse(
        bound=n,
        count=len(values),
        elapsed_ms=round((t1 - t0) * 1000, 4),
        values=values,
    )


@app.get("/api/products", response_model=List[Product])
def api_products():
    return CATALOG


@app.get("/api/products/{pid}", response_model=Product)
def api_product(pid: str):
    for p in CATALOG:
        if p.id == pid:
            return p
    raise HTTPException(status_code=404, detail="Product not found")


@app.get("/api/health")
def

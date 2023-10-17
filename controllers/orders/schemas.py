from pydantic import BaseModel


class GetOrdersRequestSchema(BaseModel):
    startDate: str
    endDate: str
    recordLimit: int
    offset: int
    statuses: list[str]


class Product(BaseModel):
    amount: int
    name: str


class OfferDetails(BaseModel):
    currencyCode: str
    description: str
    price: int
    products: list[Product]


class Results(BaseModel):
    acOfferId: str
    acOrderId: str
    acPaymentId: str
    amountTotal: str
    createdAt: str
    currency: str
    currencySymbol: str
    offerDetails: OfferDetails
    offerName: str
    playerId: str
    publisherOfferId: str
    reason: str | None
    state: str


class GetOrdersResponseSchema(BaseModel):
    results: list[Results]
    totalCount: int

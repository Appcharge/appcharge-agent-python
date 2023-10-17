from pydantic import BaseModel


class PlayerInfoSyncRequest(BaseModel):
    playerId: str


class PlayerUpdateBalanceRequest(BaseModel):
    appChargePaymentId: str
    purchaseDateAndTimeUtc: str
    gameId: str
    playerId: str
    bundleName: str
    bundleId: str
    sku: str
    priceInCents: int
    currency: str
    priceInDollar: int
    action: str
    actionStatus: str
    tax: int
    subTotal: int
    products: list

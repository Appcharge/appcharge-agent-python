from pydantic import BaseModel


class Interval(BaseModel):
    startDate: str
    endDate: str


class Product(BaseModel):
    publisherProductId: str
    productId: str
    quantity: int


class ProductsSequenceItem(BaseModel):
    index: int
    products: list[Product]
    priceInUsdCents: int
    playerAvailability: int


class DynamicOfferUi(BaseModel):
    badges: list


class CreateOfferRequest(BaseModel):
    publisherOfferId: str
    name: str
    type: str
    intervals: list[Interval]
    offerUiId: str
    active: bool
    segments: list[str]
    productsSequence: list[ProductsSequenceItem]
    createdBy: str
    dynamicOfferUi: DynamicOfferUi


class UpdateOfferRequest(BaseModel):
    publisherOfferId: str
    name: str
    type: str
    intervals: list[Interval]
    offerUiId: str
    active: bool
    segments: list[str]
    productsSequence: list
    createdBy: str

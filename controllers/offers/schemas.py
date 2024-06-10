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


class DynamicOfferUi(BaseModel):
    badges: list


class Triggers(BaseModel):
    type: str
    eventName: str
    every: int


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


class CreatePopUpOfferRequest(BaseModel):
    publisherOfferId: str
    name: str
    type: str
    subType: str
    startOver: bool
    priority: int
    showAfter: str
    intervals: list[Interval]
    offerUiId: str
    active: bool
    segments: list[str]
    productsSequence: list[ProductsSequenceItem]
    createdBy: str
    dynamicOfferUi: DynamicOfferUi
    triggers: Triggers


class UpdatePopUpOfferRequest(BaseModel):
    publisherOfferId: str
    name: str
    type: str
    subType: str
    startOver: bool
    priority: int
    showAfter: str
    intervals: list[Interval]
    offerUiId: str
    active: bool
    segments: list[str]
    productsSequence: list[ProductsSequenceItem]
    createdBy: str
    dynamicOfferUi: DynamicOfferUi
    triggers: Triggers


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

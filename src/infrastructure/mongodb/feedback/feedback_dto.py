from typing import TypedDict

from bson import ObjectId


class FeedbackDto(TypedDict):
    _id: ObjectId
    name: str
    address: str
    content: str

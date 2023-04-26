from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor
HIDING: StatusEnum
PENDING: StatusEnum
PUBLISHING: StatusEnum

class CreateCommentsRequest(_message.Message):
    __slots__ = ["content", "status", "user_id"]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    content: str
    status: StatusEnum
    user_id: int
    def __init__(self, user_id: _Optional[int] = ..., status: _Optional[_Union[StatusEnum, str]] = ..., content: _Optional[str] = ...) -> None: ...

class CreateCommentsResponse(_message.Message):
    __slots__ = ["success"]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...

class StatusEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

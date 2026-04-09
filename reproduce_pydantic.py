from pydantic import BaseModel
from resolute import Result, Ok, Option, Some, Nothing
from typing import Any

class UserProfile(BaseModel):
    status: Result[str, str]
    bio: Option[str] = Nothing

try:
    p = UserProfile(status=Ok("active"), bio=Some("hey"))
    print("Pydantic success:", p)
    print("status type:", type(p.status))
    print("bio type:", type(p.bio))
except Exception as e:
    print("Pydantic failure:")
    print(e)

# Test with dict
try:
    p2 = UserProfile(status={"ok": "active"}, bio=None)
    print("Pydantic dict success:", p2)
except Exception as e:
    print("Pydantic dict failure:")
    print(e)

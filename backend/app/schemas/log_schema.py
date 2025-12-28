from pydantic import BaseModel

class cloudflarelog(BaseModel):
    ip_address: str
    request_path: str
    status_code: int
    bytes_sent: int
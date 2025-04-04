from pydantic import BaseModel

# {
#   "success": true,
#   "estimate_id": "EST-20250328-001",
#   "status": "received",
#   "timestamp": "2025-03-28T14:30:05Z",
#   "validation_results": {
#     "passed": true,
#     "warnings": [
#       {
#         "code": "WRN-101",
#         "message": "Unit price differs from standard by more than 10%",
#         "line_item_index": 2
#       }
#     ]
#   }
# }
#
class ImportResponse(BaseModel):
    success: bool
    estimate_id: str
    status: str
    timestamp: str
    validation_results: dict | None = None

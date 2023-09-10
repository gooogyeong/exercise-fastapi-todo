from pydantic import BaseModel

# every todo you create has to follow this data model
# and fastapi has built-in validation to do that
class Todo(BaseModel):
  id: int
  item: str

# print('validate Todo', Todo.model_validate({ 'id': 1, 'item': 'do laundry'}))
# validate Todo id=1 item='do laundry'
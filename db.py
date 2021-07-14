
import json
from copy import copy

class DB:

  data:dict = []

  def __init__(self, path:str):
    self.data = self.read_file(path)


  def read_file(self,path:str) -> dict:
    try:
      f = open(path, "r")
      file = f.read()
      res = json.loads(file)
    except Exception as e:
      raise ValueError(f"File {path} does not exist. Please check. Error: {e}")
    return res
    

  def list_to_dict(self, data:list, key) -> dict:
    hash_tab = dict()
    for d in data:
      hash_tab[d[key]] = d
    return hash_tab


  def join_left_hash(self, left_db, key:str):
    hash_tab = self.list_to_dict(left_db.data, "user_id")
    data = self.data.copy()
    join_result = []
    for row in data:
      join_val = hash_tab[row[key]]
      row = {**row, **join_val}
      join_result.append(row)
    
    result = copy(self)
    result.data = join_result
    return result


  def filter(self, field:str, eq_type:str, val:str):
    res = []
    for row in self.data:
      if eval(f"row['{field}'] {eq_type} '{val}'"):
        res.append(row)
    
    result = copy(self)
    result.data = res
    return result
    
class Problem(NamedTuple):
  name: str
  content: str
  question: str
  answer: str

def parse_problem_from_file(file_path: str): # -> some Problem object (I guess?)
  return Problem.new()
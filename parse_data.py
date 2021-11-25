import sys
import json
import os.path

def read_json(file_path: str) -> dict:
  if os.path.exists(file_path):
    f = open(file_path, 'r')
    json_dict = json.load(f)
    f.close()
    return json_dict
  else:
    return None

def get_contributors(path: str) -> str:
  file_path = f"{path}.contributors.json"
  contributors = read_json(file_path)
  if contributors is None:
    return ''

  return len(contributors)

def get_repodata(path: str) -> dict:
  dir_path = path.split('/')[:-1]
  dir_path = '/'.join(dir_path)
  file_path = f"{dir_path}/repodata.json"
  temp = read_json(file_path)
  repo_data = dict()
  if temp is None:
    repo_data['owner_type'] = ''
    repo_data['language'] = ''
    repo_data['size'] = ''
    return repo_data
  else:
    repo_data['owner_type'] = temp['owner']['type']
    repo_data['language'] = temp['language']
    repo_data['size'] = temp['size']
    return repo_data

def get_year(path: str) -> str:
  file_path = f"{path}.lastCommit.json"
  last_commit = read_json(file_path)
  if last_commit is None:
    return ""

  if len(last_commit) == 0:
    return ""
  else:
    return last_commit[0]['commit']['committer']['date'][:4]

def get_smells(path: str) -> list:
  file_path = f"{path}.hadolint.json"
  smell_list = read_json(file_path)
  if smell_list is None:
    return []

  smells = []
  for smell in smell_list:
    temp = dict()
    temp['code'] = smell['code']
    temp['level'] = smell['level']
    temp['type'] = smell['code'][:2]
    if temp['level'] in ['error', 'warning']:
      smells.append(temp)

  return smells

def get_name(path: str) -> str:
  author_repo = path.split('/')[2:4]
  return '/'.join(author_repo)

def parse_to_csv(paths: list[str]) -> list[str]:
  rows = []
  for path in paths:
    name = get_name(path)
    smells = get_smells(path)
    year = get_year(path)
    repo_data = get_repodata(path)
    contributors = get_contributors(path)
    for smell in smells:
      row = f"{name},{smell['code']},{smell['type']},{smell['level']},{year},{repo_data['owner_type']},{repo_data['language']},{repo_data['size']},{contributors}"
      rows.append(row)
  return rows

def read_input() -> list[str]:
  return [line.strip() for line in sys.stdin]

def main():
  # reads paths to dockerfile dirs from stdin
  # in the following format: /path/to/dockerfile/dir/
  paths = read_input()
  rows = parse_to_csv(paths)
  print('repo_name,smell_code,type,level,year,owner_type,language,size,contributors')
  print('\n'.join(rows))

if __name__ == '__main__':
  main()
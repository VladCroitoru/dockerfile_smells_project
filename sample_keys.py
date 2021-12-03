import sys


YEARS = { '2014': 0, '2015': 0 , '2016': 0, '2017': 0, '2018': 0, '2019': 0, '2020': 0, '2021': 0}
YEARS_SAMPLE_SIZE = 1300
OWNERS = {'User': 0, 'Organization': 0}
OWNERS_SAMPLE_SIZE = 14000
LANGUAGES = {'Rust': 0, 'Java': 0, 'Jupyter Notebook': 0, 'C#': 0, 'C++': 0, 'C': 0, 'TypeScript': 0, 'JavaScript': 0, 'PHP': 0, 'Ruby': 0, 'Go': 0, 'Python': 0, 'Shell': 0}
LANGUAGES_SAMPLE_SIZE = 330
LANGUAGES_2 = {'Ruby': 0, 'Java': 0, 'TypeScript': 0, 'JavaScript': 0, 'Go': 0, 'Python': 0, 'Shell': 0}
LANGUAGES_SAMPLE_SIZE_2 = 1500


def read_csv(filename):
  f = open(filename, 'r')
  return f

def sample_by_year(csv_file, debug):
  repo_names = []
  for line in csv_file.readlines():
    values = line.split(',')
    year = values[1]
    if year in YEARS and YEARS[year] < YEARS_SAMPLE_SIZE:
      repo_name = values[0].rstrip()
      if repo_name not in repo_names:
        repo_names.append(repo_name)
        YEARS[year] += 1
  if debug:
    print(YEARS)
  return repo_names

def sample_by_owner(csv_file, debug):
  repo_names = []
  for line in csv_file.readlines():
    values = line.split(',')
    owner_type = values[2].rstrip()
    if owner_type in OWNERS and OWNERS[owner_type] < OWNERS_SAMPLE_SIZE:
      repo_name = values[0]
      if repo_name not in repo_names:
        repo_names.append(repo_name)
        OWNERS[owner_type] += 1
  if debug:
    print(OWNERS)
  return repo_names

def sample_by_language(csv_file, debug):
  repo_names = []
  for line in csv_file.readlines():
    values = line.split(',')
    language = values[3].rstrip()
    if language in LANGUAGES and LANGUAGES[language] < LANGUAGES_SAMPLE_SIZE:
      repo_name = values[0]
      if repo_name not in repo_names:
        repo_names.append(repo_name)
        LANGUAGES[language] += 1
  if debug:
    print(LANGUAGES)
  return repo_names

def sample_by_language2(csv_file, debug):
  repo_names = []
  for line in csv_file.readlines():
    values = line.split(',')
    language = values[3].rstrip()
    if language in LANGUAGES_2 and LANGUAGES_2[language] < LANGUAGES_SAMPLE_SIZE_2:
      repo_name = values[0]
      if repo_name not in repo_names:
        repo_names.append(repo_name)
        LANGUAGES_2[language] += 1
  if debug:
    print(LANGUAGES_2)
  return repo_names

def main():
  filename = sys.argv[1]
  if not filename or not filename.endswith('.csv'):
    print('Please provide a valid csv filename')
    sys.exit(1)

  csv_file = read_csv(filename)
  type = sys.argv[2]
  if len(sys.argv) > 3:
    debug = sys.argv[3]
  else:
    debug = False
  if type == 'year':
    repos = sample_by_year(csv_file, debug)
  elif type == 'owner':
    repos = sample_by_owner(csv_file, debug)
  elif type == 'language':
    repos = sample_by_language(csv_file, debug)
  elif type == 'language2':
    repos = sample_by_language2(csv_file, debug)

  if not debug:
    for repo in repos:
      print(f"merged_dockerfiles/{repo}/Dockerfile")

if __name__ == '__main__':
  main()
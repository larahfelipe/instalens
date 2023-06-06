from os import name, path, remove, sep, system
from sys import argv


class Util:
  @staticmethod
  def get_os():
    common_os = {
      'nt': 'Windows',
      'posix': 'Linux',
      'mac': 'MacOS'
    }
    return common_os[name]


  @staticmethod
  def clear_screen():
    system('cls' if Util.get_os() == 'Windows' else 'clear')


  @staticmethod
  def get_dir_path():
    return path.dirname(path.realpath(__file__)) + sep

  @staticmethod
  def check_dir_exists(target_dir: str, current_dir=True):
    if not current_dir:
      return path.isdir(target_dir)

    abs_path = Util.get_dir_path()
    return path.isdir(abs_path + target_dir)


  @staticmethod
  def check_file_exists(target_file: str, current_dir=True):
    if not current_dir:
      return path.isfile(target_file)

    abs_path = Util.get_dir_path()
    return path.isfile(abs_path + target_file)


  @staticmethod
  def get_flags():
    FLAG_PREFIX = '--'
    flags = argv[1:]
    fmt_flags = {}

    if not len(flags) and FLAG_PREFIX not in flags:
      return fmt_flags

    for f in flags:
      [k, v] = f.removeprefix(FLAG_PREFIX).split('=')
      fmt_flags[k] = v

    return fmt_flags


  @staticmethod
  def create_dir(dir_name: str):
    dir_exists = Util.check_dir_exists(dir_name, current_dir=False)

    if not dir_exists:
      abs_path = Util.get_dir_path()
      system(f'mkdir {abs_path}{dir_name}')


  @staticmethod
  def write_to_file(filename: str, content: str, mode='w'):
    data_dir_exists = Util.check_dir_exists('data')
    if not data_dir_exists:
      Util.create_dir('data')

    fmt_file_path = Util.get_dir_path() + f'data/{filename}'

    file_exists = Util.check_file_exists(fmt_file_path, current_dir=False)
    if file_exists:
      remove(fmt_file_path)

    with open(fmt_file_path, mode) as f:
      for i, l in enumerate(content, 1):
        f.write(f'{i}. {l}\n')
      f.close()

    file_created = Util.check_file_exists(fmt_file_path, current_dir=False)
    if file_created:
      print(f'> {filename} created and saved to data directory\n')

import engine.enums.errors as error_nums

def handle_error(error_code: error_nums.gui_error):
  print(f"got error {error_code}")
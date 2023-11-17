import os

# Define the directories and files
directories = ['src', 'tests', 'docs']
files = ['physical_layer.py', 'data_link_layer.py', 'network_layer.py', 'transport_layer.py', 'session_layer.py', 'presentation_layer.py', 'application_layer.py']
test_files = ['physical_layer_tests.py', 'data_link_layer_tests.py', 'network_layer_tests.py', 'transport_layer_tests.py', 'session_layer_tests.py', 'presentation_layer_tests.py', 'application_layer_tests.py']

# Create the directories
for directory in directories:
  os.makedirs(directory, exist_ok=True)

# Create the files
for file in files:
  with open(f'src/{file}', 'w') as f:
      pass

for file in test_files:
  with open(f'tests/{file}', 'w') as f:
      pass

# Create the README file
with open('docs/README.md', 'w') as f:
  pass

# Create the main file
with open('main.py', 'w') as f:
  pass

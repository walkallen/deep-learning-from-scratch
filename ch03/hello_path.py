
import os

current_path = os.path.dirname(os.path.abspath(__file__))

project_path = os.path.abspath(os.path.join(current_path, os.pardir))


print(current_path)

print(project_path)
import os

root_path = os.path.dirname(__file__).replace("utilities", "")
resources_path = os.path.join(root_path, "resources")


def get_resource(file_name):
    file_path = os.path.join(resources_path, file_name)
    assert os.path.exists(file_path), f"File does not exist: {file_path}"

    return file_path
import os
import importlib.util
import sys
from craftext.environment.scenarious.checkers.relevant import place_object_relevant_to

def count_dict_elements(module, dict_names):
    """
    Counts the number of elements in specified dictionaries within a module.
    """
    dict_counts = {}
    for dict_name in dict_names:
        if hasattr(module, dict_name):
            dictionary = getattr(module, dict_name)
            if isinstance(dictionary, dict):
                dict_counts[dict_name] = len(dictionary)
    return dict_counts

def import_module_from_path(module_name, file_path):
    """
    Dynamically imports a module from a given file path.
    """
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module

def process_folders(base_folder):
    """
    Processes folders starting with 'jax', imports specific files,
    and counts elements in dictionaries.
    """
    results = {}

    for folder_name in os.listdir(base_folder):
        if folder_name.startswith("jax"):
            folder_path = os.path.join(base_folder, folder_name)

            if os.path.isdir(folder_path):
                results[folder_name] = {}

                # Import instructions.py
                instructions_path = os.path.join(folder_path, "instructions.py")
                if os.path.exists(instructions_path):
                    module_name = f"{folder_name}_instructions"
                    instructions_module = import_module_from_path(module_name, instructions_path)
                    dict_names = ["one", "easy", "medium"]
                    results[folder_name]["instructions"] = count_dict_elements(instructions_module, dict_names)

                # Import test.py
                test_path = os.path.join(folder_path, "test.py")
                if os.path.exists(test_path):
                    module_name = f"{folder_name}_test"
                    test_module = import_module_from_path(module_name, test_path)
                    dict_names = [
                        "easy_test_paraphrased",
                        "easy_test_other_params",
                        "medium_test_parafrased",
                        "medium_test_other_paramets",
                    ]
                    results[folder_name]["test"] = count_dict_elements(test_module, dict_names)

    return results

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Count elements in dictionaries from Python files in 'jax' folders.")
    parser.add_argument("--base_folder", type=str, help="Path to the base folder containing 'jax' subfolders.")
    args = parser.parse_args()

    results = process_folders(args.base_folder)
    total_goals = 0
    total_instructions = 0
    # Print the results
    for folder, data in results.items():
        print(f"Folder: {folder}")
        for file_type, counts in data.items():
            print(f"  {file_type}:")
            for dict_name, count in counts.items():
                print(f"    {dict_name}: {count} * 6 = {count*6}")
                total_goals += count
            print()
    
    print("---"*60)
    print("TOTAL_GOALS = ", total_goals)
    print("TOTAL_INSTRUCTIONS = ", total_goals*6)

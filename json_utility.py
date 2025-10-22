import json
import os

# Define the path for the configuration file
CONFIG_FILE = 'app_config.json'

def create_default_config():
    """Creates a basic default configuration dictionary."""
    return {
        "app_name": "Hacktoberfest Utility Tool",
        "version": "1.0",
        "settings": {
            "logging_level": "INFO",
            "max_retries": 5,
            "theme": "dark"
        },
        "file_paths": ["/tmp/data", "/var/logs"]
    }

def load_config(file_path=CONFIG_FILE):
    """Loads configuration data from a JSON file."""
    if not os.path.exists(file_path):
        print(f"Configuration file not found at {file_path}. Creating default config.")
        config_data = create_default_config()
        save_config(config_data, file_path) # Save the default config
        return config_data
        
    try:
        with open(file_path, 'r') as f:
            # json.load() deserializes the file content into a Python dictionary
            return json.load(f)
    except json.JSONDecodeError:
        print("Error: Config file is corrupted (invalid JSON). Returning default.")
        return create_default_config()
    except Exception as e:
        print(f"An unexpected error occurred while loading: {e}")
        return create_default_config()

def save_config(config_data, file_path=CONFIG_FILE):
    """Saves a Python dictionary to a JSON file."""
    try:
        with open(file_path, 'w') as f:
            # json.dump() serializes the dictionary to the file
            # indent=4 makes the file human-readable (pretty-printed)
            json.dump(config_data, f, indent=4)
        print(f"Configuration saved successfully to {file_path}")
    except Exception as e:
        print(f"Error saving configuration: {e}")

# --- Example Usage ---

# 1. Load the current configuration (will create default if file doesn't exist)
app_config = load_config()
print("\n--- Initial Config ---")
print(json.dumps(app_config, indent=2)) # Print using dumps for formatted display

# 2. Modify a setting
print("\n--- Modifying Config ---")
app_config['settings']['theme'] = 'light'
app_config['settings']['max_retries'] = 10
print(f"Changed theme to: {app_config['settings']['theme']}")

# 3. Add a new setting or path
app_config['file_paths'].append('/home/user/new_data')
app_config['new_feature_enabled'] = True

# 4. Save the modified configuration
save_config(app_config)

# 5. Verify the save by loading it again
reloaded_config = load_config()
print("\n--- Reloaded Config Verification ---")
print(f"New max_retries: {reloaded_config['settings']['max_retries']}")
print(f"New feature enabled: {reloaded_config['new_feature_enabled']}")

# Clean up the generated file (optional)
# os.remove(CONFIG_FILE)

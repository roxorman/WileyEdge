import json
config_file_path = r"C:\Users\marno\Wiley Edge\Code\Week 2\day2\config.json"

try:
    with open(config_file_path,"r") as config_file:
        config_data = json.load(config_file)
        
    database_setting = config_data.get("database",{})
    api_key = config_data.get("api_key","")
    debug_mode = config_data.get("debug_mode",False)
    
    print(database_setting.get("host","N/A"))
    print(api_key)
    print(debug_mode)
    
    config_data["new_setting"] = "new value"
    
    with open(config_file_path,"w") as config_file:
        json.dump(config_data,config_file, indent=4)
    
except FileNotFoundError:
    print(f"Config file not found {config_file_path}")
except json.JSONDecodeError as e:
    print("Error parsing JSON",e.msg)
except Exception as e:
    print("Unknown error occurred",e)
    
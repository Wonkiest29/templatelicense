import datetime
import os
import json

# Загружаем основные данные из config.json
config_json_path = "config.json"
with open(config_json_path, "r", encoding="utf-8") as f:
    base_config = json.load(f)

# Получаем и увеличиваем номер договора из config.json
numberid = int(base_config.get("numberid", "1"))
new_numberid = numberid + 1
base_config["numberid"] = f"{new_numberid:03d}"

# Сохраняем новый номер обратно в config.json
with open(config_json_path, "w", encoding="utf-8") as f:
    json.dump(base_config, f, ensure_ascii=False, indent=2)

today = datetime.datetime.now()
contract_end_date = today + datetime.timedelta(days=30)



config = base_config.copy()
config.update({
    "current_date": today.strftime("%d.%m.%Y"),
    "contract_end": contract_end_date.strftime("%d.%m.%Y"),
    "contract_title": f"КЛИШЕ - ДОГОВОР – {base_config['numberid']}"
})

name_parts = config["client_name"].split()
if len(name_parts) >= 2:
    config["client_sign"] = name_parts[0][0] + name_parts[1][0]
else:
    config["client_sign"] = config["client_name"][:2]

lawyer_name_parts = config["lawyer_name"].split()
if len(lawyer_name_parts) >= 2:
    config["lawyer_sign"] = lawyer_name_parts[0][0] + lawyer_name_parts[1][0]
else:
    config["lawyer_sign"] = config["lawyer_name"][:2]

# Проверяем наличие картинки подписи адвоката
lawyer_sign_image = "lawyer_sign.png"
if os.path.exists(lawyer_sign_image):
    config["lawyer_sign"] = lawyer_sign_image
else:
    config["lawyer_sign"] = "".join([part[0] for part in lawyer_name_parts if part])  # инициалы как строка
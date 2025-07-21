import os
import json

CONFIG_PATH = "config.json"
DEFAULT_CONFIG = {
  "numberid": "000",
  "lawyer_name": "имя адвоката",
  "lawyer_id": "статик адвоката",
  "lawyer_licenseid": "номер лицензии адвоката",
  "client_name": "имя клиента",
  "client_id": "статик клиента",
  "client_discord": "",
  "client_phone": "номер телефона клиента",
  "client_bank": "номер банковского счета клиента",
  "lawyer_discord": "дискорд адвоката",
  "lawyer_phone": "номер телефона адвоката",
  "lawyer_bank": "номер банковского счета адвоката",
  "cost": "100000"
}

print("[DEBUG] Проверка наличия config.json...")
if not os.path.exists(CONFIG_PATH):
    with open(CONFIG_PATH, "w", encoding="utf-8") as f:
        json.dump(DEFAULT_CONFIG, f, ensure_ascii=False, indent=4)
    print(f"[DEBUG] Создан файл конфига: {CONFIG_PATH}")
    print("[DEBUG] Пожалуйста, заполните config.json перед запуском.")
    exit(1)  # Завершаем выполнение, если файл не найден
else:
    print(f"[DEBUG] Файл конфига найден: {CONFIG_PATH}")

# Теперь можно импортировать config
from config import config
from template import generate_contract_from_template

print("[DEBUG] Генерация контракта из шаблона...")
output_path = generate_contract_from_template("template.docx", config)
print(f"[DEBUG] Контракт сохранён: {output_path}")
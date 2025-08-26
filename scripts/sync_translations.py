# scripts/sync_translations.py
#!/usr/bin/env python3
import os
import shutil
from pathlib import Path

def sync_po_files():
    # Пути к .po файлам
    ru_po_dir = Path('docs/locale/ru/LC_MESSAGES/')
    en_po_dir = Path('ksenia-sandbox-eng/docs/locale/en/LC_MESSAGES/')
    
    # Синхронизируем .po файлы
    for po_file in ru_po_dir.glob('*.po'):
        en_po_file = en_po_dir / po_file.name
        if en_po_file.exists():
            print(f"Syncing {po_file} with {en_po_file}")
            
if __name__ == '__main__':
    sync_po_files()
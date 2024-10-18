import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import json
import os
from collections import defaultdict

def flatten_dict(d, parent_key='', sep='.'):
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

def unflatten_dict(flat_dict, sep='.'):
    result_dict = {}
    for key, value in flat_dict.items():
        parts = key.split(sep)
        d = result_dict
        for part in parts[:-1]:
            d = d.setdefault(part, {})
        d[parts[-1]] = value
    return result_dict

def convert_json_to_excel():
    json_files = filedialog.askopenfilenames(
        title='Select JSON Files',
        filetypes=[('JSON Files', '*.json')]
    )
    if not json_files:
        return

    data = defaultdict(dict)
    try:
        for json_file in json_files:
            lang_code = os.path.splitext(os.path.basename(json_file))[0]
            with open(json_file, 'r', encoding='utf-8') as f:
                json_data = json.load(f)
            flat_data = flatten_dict(json_data)
            for key, value in flat_data.items():
                data[key][lang_code] = value

        all_keys = sorted(data.keys())
        all_langs = sorted({lang for values in data.values() for lang in values.keys()})

        rows = []
        for key in all_keys:
            row = {'Key': key}
            for lang in all_langs:
                row[lang] = data[key].get(lang, '')
            rows.append(row)

        df = pd.DataFrame(rows)
        df = df[['Key'] + all_langs]

        save_path = filedialog.asksaveasfilename(
            defaultextension='.xlsx',
            filetypes=[('Excel Files', '*.xlsx')],
            title='Save Excel File'
        )
        if save_path:
            df.to_excel(save_path, index=False)
            messagebox.showinfo('Success', f"Excel file '{os.path.basename(save_path)}' has been created successfully.")
    except Exception as e:
        messagebox.showerror('Error', f"An error occurred: {e}")

def convert_excel_to_json():
    excel_file = filedialog.askopenfilename(
        title='Select Excel File',
        filetypes=[('Excel Files', '*.xlsx'), ('Excel Files', '*.xls')]
    )
    if not excel_file:
        return

    try:
        df = pd.read_excel(excel_file)

        if 'Key' not in df.columns:
            messagebox.showerror('Error', "The Excel file must contain a 'Key' column.")
            return

        lang_cols = [col for col in df.columns if col != 'Key']

        if not lang_cols:
            messagebox.showerror('Error', "The Excel file must contain at least one language column.")
            return

        for lang in lang_cols:
            flat_dict = {}
            for index, row in df.iterrows():
                key = row['Key']
                value = row[lang]
                if pd.isna(value):
                    continue  
                flat_dict[key] = value

            nested_dict = unflatten_dict(flat_dict)

            json_file = f"{lang}.json"
            save_path = filedialog.asksaveasfilename(
                defaultextension='.json',
                initialfile=json_file,
                filetypes=[('JSON Files', '*.json')],
                title=f'Save JSON File for {lang}'
            )
            if save_path:
                with open(save_path, 'w', encoding='utf-8') as f:
                    json.dump(nested_dict, f, ensure_ascii=False, indent=4)
                messagebox.showinfo('Success', f"JSON file '{os.path.basename(save_path)}' has been created successfully.")
    except Exception as e:
        messagebox.showerror('Error', f"An error occurred: {e}")

root = tk.Tk()
root.title('Language File Converter')

root.geometry('400x200')

btn_json_to_excel = tk.Button(root, text='Convert JSON to Excel', command=convert_json_to_excel, width=30, height=2)
btn_excel_to_json = tk.Button(root, text='Convert Excel to JSON', command=convert_excel_to_json, width=30, height=2)

btn_json_to_excel.pack(pady=20)
btn_excel_to_json.pack(pady=10)

root.mainloop()

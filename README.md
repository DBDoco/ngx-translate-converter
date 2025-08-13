# ngx-translate-converter

A simple and beautiful UI tool to convert translation JSON files (used by [ngx-translate](https://github.com/ngx-translate/core)) to Excel files and back. This makes it easy for developers and clients to collaborate on translations.

## What is this?

**ngx-translate-converter** is a user-friendly application that helps you:
- Convert your `ngx-translate` JSON translation files to Excel (`.xlsx`) format.
- Share the Excel file with clients or translators for easy review and editing.
- Convert the updated Excel file back to JSON for use in your Angular project.

## Why use it?
- **For Developers:** Simplifies the process of sharing translations with non-technical stakeholders.
- **For Clients/Translators:** Allows easy editing and review of translations in Excel, a familiar format.
- **For Teams:** Reduces errors and streamlines the translation workflow.

## How does it work?
1. **Convert JSON to Excel:**
   - Upload your `ngx-translate` JSON file.
   - The app generates an Excel file with all translation keys and values.
2. **Client/Translator Review:**
   - The client or translator edits the Excel file as needed.
   - They send the updated Excel file back to the developer.
3. **Convert Excel to JSON:**
   - Upload the updated Excel file.
   - The app converts it back to the JSON format required by `ngx-translate`.

## Usage

1. **Clone the repository:**
   ```sh
   git clone https://github.com/DBDoco/ngx-translate-converter.git
   cd ngx-translate-converter
   ```
2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
3. **Run the app:**
   ```sh
   python converter.py
   ```
4. **Follow the UI instructions:**
   - Choose to convert JSON to Excel or Excel to JSON.
   - Upload your file and download the result.

## Example Workflow
1. Developer exports translations to Excel and sends to client.
2. Client reviews and updates translations in Excel.
3. Client sends Excel file back to developer.
4. Developer converts Excel back to JSON and uses it in the Angular app.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
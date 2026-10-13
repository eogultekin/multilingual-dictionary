# multilingual-dictionary
A Python command-line dictionary that translates words between Turkish, English and French using JSON data.

# 🌍 Multilingual Dictionary – Turkish · English · French

A command-line dictionary app written in Python that translates words between **Turkish, English and French**. Languages and words are stored in JSON files, so the dictionary can be extended without changing the code.

## ✨ Features

- Translate words in any direction between Turkish, English and French (6 language pairs)
- Menu-based, easy-to-use console interface
- Languages and vocabulary loaded from JSON files (`config.json`, `words.json`)
- Case-insensitive search that ignores extra spaces
- Input validation for menu choices
- Prevents choosing the same language as source and target
- Option to search again or exit after each translation

## 🛠️ Tech Stack

- **Python 3**
- **JSON** for data storage
- Standard libraries: `json`, `os`, `sys`

## 📁 Project Structure

```
├── translator.py   # Main program
├── config.json     # List of supported languages
├── words.json      # Word list with Turkish, English and French translations
└── README.md
```

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/USERNAME/multilingual-dictionary.git
   cd multilingual-dictionary
   ```
2. Run the program:
   ```bash
   python translator.py
   ```

> No external libraries are required. The program uses `cls` to clear the screen, so it is designed for the Windows terminal.

## 💡 Example Usage

```
Ana Menü
1- Dil Seçin
2- Kelime Arayın
3- Çıkış
> 1

Başlangıç dilinizi seçiniz
1- Türkçe
2- İngilizce
3- Fransızca
> 1

Hedef dilinizi seçiniz
> 3

Aradığınız kelimeyi giriniz: bilgisayar
Sonuç: ordinateur
```

## ➕ Adding New Words

Open `words.json` and add a new entry in the same format:

```json
{
  "Türkçe": "kitap",
  "Ingilizce": "book",
  "Fransizca": "livre"
}
```

## 🔮 Future Improvements

- Add more words and languages
- Build a graphical interface (e.g. Tkinter)
- Suggest similar words when a word is not found

## 👤 Author

**Ezgi Oğultekin** – Computer Engineering student at Piri Reis University


# ibus_rime_flypy

## Project Description
This project contains configuration files for the IBus Rime input method, specifically tailored for the Flypy input scheme. It includes custom settings for common characters, symbols, and phrases, as well as a Japanese kana shortcut dictionary.

## Key Features
*   Custom encoding for common characters (e.g., "u" for "是, 事, 时, 十").
*   Ctrl+Space for toggling English/Chinese mode.
*   Addition of frequently used characters and phrases.
*   Removal of less common phrases.
*   Pinyin character support for quick retrieval (e.g., "ofpya", "ofpyo").
*   Reverse lookup support using "`" (backtick).
*   Japanese kana shortcuts (optional user dictionary).

## Installation (Linux)
1.  Install `ibus-rime`.
2.  Navigate to `~/.config/ibus`.
3.  Clone the repository: `git clone https://github.com/walterclozet/ibus_rime_flypy.git rime`.
4.  Redeploy Rime.

## Installation (Windows)
1.  Install Rime (Xiaolanghao).
2.  Open the user folder.
3.  Download and extract the latest code, then copy all files to the user folder.
4.  Redeploy Rime.
*   Alternatively, use Git to clone and pull updates similar to Linux.

## Updating
1.  Navigate to the project directory: `cd ~/.config/ibus/rime`.
2.  Pull the latest changes: `git pull`.

## Python Scripts
The project includes Python scripts (`check4wc.py`, `getwc.py`) for managing the reverse lookup dictionary (`wc.txt`). When new Chinese characters are added to the dictionary, their full codes should be added to `wc.txt`, and `getwc.py` should be run to update the reverse lookup dictionary.

## Important Note
This configuration is based on an older public version of the Flypy dictionary and does not update with the official version. It is primarily tested on Linux, and official versions are recommended for other platforms.

# 🧠 BrutaList 🔓 Not Just Brute. Brutal. ⚔️💥  
Welcome to BrutaList — the cyber crowbar for cracking chaos. 🦾💻  
BrutaList is a weaponized wordlist generator built for hackers who don’t ask permission. 🚫🔐  
You throw in characters — it returns every possible valid permutation, filtered by logic and forged in entropy. 🧬🛠️

No bloat. No guesswork. Just raw, optimized brute-force ammo. 🔥🔫⚡

---

🧿 “One charset to rule them all — one list to breach them.” ⚡  
– BrutaList Philosophy 🧠💣

---

### 🐍 Built with Python | 💣 Designed for Bruteforce | 🧪 Crafted for Recon

---

## ⚙️ Features 🔥🛠️

- 🔡 Input any custom charset (e.g., `abc123@#!`) 💻🎛️  
- 📏 Control the minimum length of combinations 📐🔢  
- 🔁 Generates **valid permutations** without repeating characters more than available 🔒🔄  
- 🎲 Shuffles combinations for randomness 🎰♻️  
- 📄 Outputs to `BrutaList.txt` 💾🧾

---

## 🧰 Installation (Kali Linux)

Make sure Python 3 is installed. Kali usually ships with Python 3 pre-installed.

🧰 `sudo apt update` 🔄⚙️ <br>
🧰 `sudo apt install python3 python3-pip -y` 🐍📦 <br>
🔽 `git clone https://github.com/Error2k25/BrutaList.git` 🧬💣 <br>
📂 `cd BrutaList` 🚪🗂️ <br>
⚙️💻 `python3 brutalist.py` 🔓🎯 <br>

---

💾 All combinations will be saved in a file called: 🗃️🧠 <br>
📝 BrutaList.txt 📂📄

---

⚔️ Use this file with your favorite tools like: 🛠️💀

`hydra -L users.txt -P BrutaList.txt ssh://target` 🐉🔐  <br>
or

`wfuzz -w BrutaList.txt --hc 404 http://target.com/login.php?user=FUZZ` 🌐🎯  <br>

---

⚠️ **Legal Disclaimer** 🕵️‍♂️🔐  
🛡️ This tool is intended only for educational and authorized testing purposes. 🎓✅  
🚫 Do NOT use it against systems you don’t have permission to test. ❌🛑  
🧷 You are fully responsible for your actions. 👁️‍🗨️⚖️

---

🧠 Made with caffeine & curiosity ☕👨‍💻  
🔑 Remember  
💡 Tools don't hack — Hackers do. 💻💀

---
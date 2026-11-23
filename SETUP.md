# Setup – do this before the workshop (about 5 minutes)

## 1. Accounts
- A **GitHub** account: <https://github.com/signup>

## 2. Install
| Tool | Check it works | Get it |
|---|---|---|
| Python 3.10+ | `python --version` (or `python3 --version`) | <https://www.python.org/downloads/> – on Windows tick **"Add Python to PATH"** |
| Git | `git --version` | <https://git-scm.com/downloads> |
| VS Code | opens | <https://code.visualstudio.com/> |

## 3. Get the project
1. Click **Fork** on this repository's GitHub page to copy it to your account.
2. Clone **your fork** and install the one dependency:

```bash
git clone https://github.com/YOUR-USERNAME/StegoLab.git
cd StegoLab
python -m pip install -r requirements.txt
```

## 4. Check
```bash
python main.py --help
python -m unittest discover -s tests -t .
```

The first command should print the help text. The second should **fail** with lots of `NotImplementedError: TODO` messages – that is correct, you will fix them in the workshop.

## No laptop, or install problems?
Come anyway. You can pair with someone, and helpers will be there 15 minutes before the start to sort out installs. You can also use **GitHub Codespaces** (Code → Codespaces → Create) to run everything in the browser.

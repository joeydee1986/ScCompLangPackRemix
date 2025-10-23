# Extraction Tools (BETA)

This folder contains utilities for extracting and processing Star Citizen game files.

**⚠️ BETA STATUS:** These tools are currently in beta testing and have not been tested with a live Star Citizen patch yet.

**📦 NOT INCLUDED IN RELEASES:** This folder is excluded from release ZIP files - it's for developers and advanced users only.

---

## Contents

### extract-global-ini.py

Extracts the stock `global.ini` localization file from Star Citizen's `Data.p4k` archive.

**Features:**
- 🔍 Auto-detects LIVE, PTU, EPTU, and HOTFIX installations
- 🎯 Interactive mode with step-by-step guidance
- ⚡ Non-interactive mode for automation
- 📝 Saves with versioned filenames (e.g., `global-4.3.4-LIVE.ini`)

---

## Prerequisites

### 1. Download unp4k.exe

You need the `unp4k.exe` tool to extract files from Star Citizen's Data.p4k archive.

**Download:**
- Visit: https://github.com/dolkensp/unp4k/releases
- Download the latest `unp4k-suite-vX.X.X.zip`
- Extract `unp4k.exe` to this `tools/` folder

**File Structure:**
```
tools/
├── extract-global-ini.py
├── unp4k.exe          ← Place it here
└── README.md          ← You are here
```

### 2. Python 3

The script requires Python 3.6 or newer (already installed if you're using Claude Code in WSL).

---

## Usage

### Interactive Mode (Guided Walkthrough)

Run without arguments for a step-by-step walkthrough:

```bash
python tools/extract-global-ini.py
```

**The script will:**
1. ✓ Check for unp4k.exe
2. 🔍 Scan for Star Citizen installations
3. ❓ Ask you which installation (LIVE, PTU, etc.)
4. ❓ Ask you what version it is
5. ⚙️ Extract global.ini
6. 💾 Save to `stock-global-ini/global-VERSION-BRANCH.ini`
7. 📋 Show you the command to skip prompts next time

**Example session:**
```
Found installations:
  [1] LIVE    - C:\Program Files\...\LIVE\Data.p4k
  [2] PTU     - C:\Program Files\...\PTU\Data.p4k

Which installation? [1]: 1
What version is this? (e.g., 4.3.2): 4.3.2

Extracting global.ini from LIVE (v4.3.2)...
✓ Extracted global.ini successfully!
  Saved to: stock-global-ini/global-4.3.2-LIVE.ini

Next time, skip the prompts by running:
  python tools/extract-global-ini.py --branch LIVE --version 4.3.2
```

### Non-Interactive Mode (Automation)

Skip all prompts by providing branch and version:

```bash
python tools/extract-global-ini.py --branch LIVE --version 4.3.4
```

**Arguments:**
- `--branch` or `-b`: Installation branch (LIVE, PTU, EPTU, HOTFIX)
- `--version` or `-v`: Star Citizen version (e.g., 4.3.4, 4.4.0)

**Examples:**
```bash
# Extract from LIVE version 4.3.4
python tools/extract-global-ini.py --branch LIVE --version 4.3.4

# Extract from PTU version 4.4.0
python tools/extract-global-ini.py -b PTU -v 4.4.0

# Extract from EPTU
python tools/extract-global-ini.py --branch EPTU --version 4.4.1
```

---

## Output

Extracted files are saved to `stock-global-ini/` with this naming format:

```
global-{VERSION}-{BRANCH}.ini
```

**Examples:**
- `global-4.3.4-LIVE.ini`
- `global-4.4.0-PTU.ini`
- `global-4.4.1-EPTU.ini`

This makes it easy to track which version and branch each file came from.

---

## Troubleshooting

### "unp4k.exe not found"

**Solution:** Download unp4k.exe from https://github.com/dolkensp/unp4k/releases and place it in the `tools/` folder.

### "No Star Citizen installations found"

**Possible causes:**
- Star Citizen is not installed
- Installed in a non-standard location
- Running from a drive that's not mounted in WSL

**Solution:** Check if Data.p4k exists at:
- `C:\Program Files\Roberts Space Industries\StarCitizen\LIVE\Data.p4k`
- Or your custom installation path

### "Extraction timed out"

**Possible causes:**
- Slow hard drive (use SSD if possible)
- System under heavy load
- Data.p4k is corrupted

**Solution:**
- Close other applications
- Verify game files through RSI Launcher
- Try again

### "LIVE installation not found" (non-interactive mode)

**Solution:** The specified branch doesn't exist. Run in interactive mode to see available installations:
```bash
python tools/extract-global-ini.py
```

---

## For Developers

### Running from WSL

The script automatically handles WSL/Windows path conversions when:
- Running the script from WSL (Linux)
- Calling unp4k.exe (Windows executable)
- Accessing Windows drives (/mnt/c/, /mnt/d/, etc.)

### Integration with Claude Code

Claude Code can run this tool automatically:

```bash
# From Claude Code in WSL:
python tools/extract-global-ini.py --branch LIVE --version 4.3.4
```

See `.claude/claude.md` for the complete workflow.

---

## Credits

- **unp4k**: https://github.com/dolkensp/unp4k
- **Star Citizen**: Cloud Imperium Games

This tool is not affiliated with or endorsed by Cloud Imperium Games.

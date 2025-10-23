# ScCompLangPackRemix - Claude Code Project Guidelines

## Release Process

### ZIP File Naming Convention
When creating new releases, **always** use this exact naming format:
```
ScCompLangPackRemix-v[VERSION].zip
```

**Examples:**
- `ScCompLangPackRemix-v4.zip`
- `ScCompLangPackRemix-v5.zip`
- `ScCompLangPackRemix-v10.zip`

### Release ZIP Contents
The release ZIP file should contain **ONLY**:
- `data/` folder (with all localization files)
- `user.cfg` file

### What NOT to Include in Release ZIP
**DO NOT** include the following in release ZIP files:
- `.claude/` directory or `claude.md` file
- `.git/` directory
- `.gitignore` file
- `README.md`
- Any existing ZIP files
- Any development/project files
- **`tools/` directory** (extraction utilities - for developers only)
- **`stock-global-ini/` directory** (vanilla game files - for development only)

### Creating Release ZIP
Use this command to create the release ZIP:
```bash
powershell.exe -Command "Compress-Archive -Path data,user.cfg -DestinationPath ScCompLangPackRemix-v[VERSION].zip -Force"
```

## Component Naming Convention

This project uses a compact naming format for Star Citizen ship components:

**Format:** `[Type][Size][Quality] ComponentName`

### Type Abbreviations
- **M** = Military
- **I** = Industrial
- **C** = Civilian
- **R** = Racing (Competition renamed to avoid conflict with Civilian)
- **S** = Stealth

### Size
- **0-4** = Component size

### Quality Grades
- **A** = Best
- **B** = Good
- **C** = Average
- **D** = Basic

### Example Transformations
- `QuadraCell MT S2 Military A` → `M2A QuadraCell MT`
- `Eco-Flow S1 Industrial B` → `I1B Eco-Flow`
- `Cryo-Star S1 Civilian B` → `C1B Cryo-Star`
- `AbsoluteZero S2 Competition B` → `R2B AbsoluteZero`
- `NightFall S2 Stealth A` → `S2A NightFall`

## Component Verification

When verifying components, use these authoritative sources in order of preference:
1. **erkul.games** (most up-to-date, but requires JavaScript)
2. **finder.cstone.space** (reliable alternative)
3. **starcitizen.tools** (wiki, may have outdated data)

Always verify: Size, Grade, Type, and Component Name spelling.

## File Locations

- Component definitions: `data/Localization/english/global.ini`
- Game configuration: `user.cfg`
- Stock game files: `stock-global-ini/` (vanilla, not modified)
- Extraction tools: `tools/` (development utilities)

---

## Updating for New Star Citizen Patches (BETA)

When a new Star Citizen patch is released, follow this workflow to update the component language pack:

### Step 1: Extract Stock global.ini

Use the extraction tool to get the vanilla global.ini from the latest patch:

```bash
python tools/extract-global-ini.py --branch LIVE --version X.X.X
```

**Replace X.X.X with the actual version (e.g., 4.3.4)**

**Branch options:**
- `LIVE` - Stable release (most common)
- `PTU` - Public Test Universe
- `EPTU` - Evocati early access
- `HOTFIX` - Rare hotfix branch

**Example:**
```bash
python tools/extract-global-ini.py --branch LIVE --version 4.3.4
```

**Output:** `stock-global-ini/global-4.3.4-LIVE.ini`

### Step 2: Copy Stock File to Working Location

```bash
cp stock-global-ini/global-4.3.4-LIVE.ini data/Localization/english/global.ini
```

### Step 3: Apply Component Renaming

Apply the compact naming format to all components:

**Components to rename:**
- **Coolers** (COOL_*)
- **Power Plants** (POWR_*)
- **Quantum Drives** (QDRV_*)
- **Shields** (SHLD_*)

**Format:** `[Type][Size][Quality] ComponentName`

**Important:** Rename BOTH uppercase and lowercase entries:
- `item_Name[Component]` (capital N)
- `item_name[Component]` (lowercase n)

**Excluded components (DO NOT rename):**
- Size 4 bespoke/capital ship components (Algid, Serac, Stellate, Allegro, etc.)
- Alien components (Vanduul, Xi'an)
- Placeholder components ([PH] markers)
- Generic shields (BEHR Small, SECO Small/Medium, etc.)

### Step 4: Verify Changes

Run verification checks:

1. **Count renamed components:**
   ```bash
   grep -E "^item_Name(COOL|POWR|QDRV|SHLD)_.*=[MICRS][0-4][A-D] " data/Localization/english/global.ini | wc -l
   ```
   Expected: ~192 (uppercase entries)

2. **Check lowercase entries:**
   ```bash
   grep -E "^item_name(COOL|POWR|QDRV|SHLD)_.*=[MICRS][0-4][A-D] " data/Localization/english/global.ini | wc -l
   ```
   Expected: ~14 (lowercase entries)

3. **Total should be ~206 renamed components**

### Step 5: Test In-Game

1. Copy `data/` folder and `user.cfg` to Star Citizen LIVE folder
2. Launch game
3. Check component names in:
   - Mobiglas vehicle manager
   - Ship customization screens
   - Component shops

### Step 6: Create Release

Once verified:

```bash
# Create release ZIP
powershell.exe -Command "Compress-Archive -Path data,user.cfg -DestinationPath ScCompLangPackRemix-vX.zip -Force"

# Create git tag
git tag vX && git push origin vX

# Create GitHub release
gh release create vX ScCompLangPackRemix-vX.zip --repo joeydee1986/ScCompLangPackRemix --title "vX - [Description]" --notes "[Release notes]"
```

---

## Extraction Tool Details (BETA)

### Prerequisites

**1. unp4k.exe**
- Download: https://github.com/dolkensp/unp4k/releases
- Place in `tools/` directory
- Required to extract files from Star Citizen's Data.p4k

**2. Python 3**
- Already available in WSL/Linux
- Required for running extraction script

### Interactive Mode (For Manual Use)

Run without arguments for guided walkthrough:

```bash
python tools/extract-global-ini.py
```

The script will:
1. Auto-detect Star Citizen installations
2. Ask which branch (LIVE, PTU, etc.)
3. Ask what version
4. Extract and save with versioned filename
5. Show the command to skip prompts next time

### Non-Interactive Mode (For Automation)

Skip all prompts:

```bash
python tools/extract-global-ini.py --branch LIVE --version 4.3.4
```

**This is the recommended mode for Claude Code automation.**

### Output Files

Extracted files are saved as:
```
stock-global-ini/global-{VERSION}-{BRANCH}.ini
```

**Examples:**
- `global-4.3.4-LIVE.ini`
- `global-4.4.0-PTU.ini`

### Troubleshooting

See `tools/README.md` for detailed troubleshooting guide.

**Common issues:**
- Missing unp4k.exe → Download and place in `tools/`
- No installations found → Check Star Citizen is installed
- Extraction timeout → Close other applications, try again

---

## Project Structure

```
ScCompLangPackRemix/
├── .claude/
│   └── claude.md              (This file - project guidelines)
├── tools/                     (NOT in releases - development only)
│   ├── extract-global-ini.py  (Extraction script)
│   ├── unp4k.exe              (Download separately)
│   └── README.md              (Tool documentation)
├── stock-global-ini/          (NOT in releases - vanilla files)
│   └── global-X.X.X-BRANCH.ini (Extracted stock files)
├── data/
│   └── Localization/english/
│       └── global.ini         (Modified with component renames)
├── user.cfg                   (Game configuration)
└── README.md                  (User documentation)
```

**Release ZIP contains ONLY:**
- `data/` folder
- `user.cfg` file

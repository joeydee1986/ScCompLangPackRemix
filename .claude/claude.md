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

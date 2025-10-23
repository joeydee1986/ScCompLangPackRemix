# ⚙️ Component Language Pack - Remix Edition

> **📢 IMPORTANT:** This is a modified fork of the original [Component Language Pack by ExoAE](https://github.com/ExoAE/ScCompLangPack).
> **All credit for the original language pack goes to [ExoAE](https://github.com/ExoAE).**
> This remix was created using [Claude Code](https://claude.com/claude-code) to provide an alternative compact naming format.

## 🎯 What's Different in This Remix?

This version uses a **compact naming format** that puts the important stats first:

**Original format:**
`XL-1` → `XL-1 S2 Military A`

**Remix format:**
`XL-1` → `M2A XL-1`

The format is: **[Type][Size][Quality] [Component Name]**

**Type abbreviations:**
- **M** = Military
- **I** = Industrial
- **C** = Civilian
- **R** = Racing (Competition renamed to avoid conflict with Civilian)
- **S** = Stealth

**More examples:**
- `QuadraCell MT` → `M2A QuadraCell MT` (Military, Size 2, Quality A)
- `Eco-Flow` → `I1B Eco-Flow` (Industrial, Size 1, Quality B)
- `Cryo-Star` → `C1B Cryo-Star` (Civilian, Size 1, Quality B)
- `AbsoluteZero` → `R2B AbsoluteZero` (Racing, Size 2, Quality B)
- `NightFall` → `S2A NightFall` (Stealth, Size 2, Quality A)

This makes it easier to quickly scan and sort components by their stats at a glance!

## ⬇️ Download and install

**Download the latest version from the [Releases Page](https://github.com/joeydee1986/ScCompLangPackRemix/releases)**

**Want the original format instead?** Check out [ExoAE's original pack](https://github.com/ExoAE/ScCompLangPack)

🔧 How to Install:

1. Extract the ZIP file.
2. Copy the data folder and the user.cfg file into your game's LIVE folder root.
3. Launch the game.

**Note for manual downloads:** If you download files directly from the repository instead of using a release ZIP, **only copy the `data` folder and `user.cfg` file**. Do not include the `.claude` folder - it's only used for project maintenance and future updates.

## 🚧 Found an Error or Issue?

If you notice any incorrectly formatted component names, missing conversions, or other issues, please let us know!

**How to report:**
- Open an issue on [GitHub Issues](https://github.com/joeydee1986/ScCompLangPackRemix/issues)
- Include the component name and what's wrong
- Screenshots are super helpful!

We appreciate your help in making this pack better for everyone. Feel free to submit pull requests with fixes too!

## Developer Tools (Beta)

This repository includes extraction tools for developers and advanced users in the `tools/` folder. These tools allow you to:

- Extract fresh `global.ini` files directly from Star Citizen's game files
- Update the language pack when new patches are released
- Maintain independence from third-party localization sources

**📁 Additional Folders (Not in Releases):**

- **`tools/`** - Extraction utilities and scripts (see `tools/README.md`)
- **`stock-global-ini/`** - Vanilla game files extracted from Star Citizen

**⚠️ These folders are NOT included in release downloads** - they're for development purposes only. Release ZIPs contain only `data/` and `user.cfg`.

For more information, see:
- `tools/README.md` - How to use the extraction tools
- `.claude/claude.md` - Complete developer workflow

---

## Notes

- This project is not affiliated with Cloud Imperium Games.
- Using language packs is currently intended by Cloud Imperium Games.
https://robertsspaceindustries.com/spectrum/community/SC/forum/1/thread/star-citizen-community-localization-update

## ☕ Support the Original Creator

If you'd like to support the original creator ExoAE, you can use their Star Citizen referral code when buying the game:

**STAR-4JD7-RZT4**

Thank you to ExoAE for creating the original pack!

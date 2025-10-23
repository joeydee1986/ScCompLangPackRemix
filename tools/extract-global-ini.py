#!/usr/bin/env python3
"""
Star Citizen global.ini Extractor (BETA)

Extracts the stock global.ini file from Star Citizen's Data.p4k archive.
Supports both interactive (guided) and non-interactive (automated) modes.

Usage:
    Interactive:  python extract-global-ini.py
    Automated:    python extract-global-ini.py --branch LIVE --version 4.3.4
"""

import argparse
import os
import platform
import subprocess
import sys
from pathlib import Path
import shutil

# ANSI color codes
class Color:
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    GRAY = '\033[90m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    END = '\033[0m'

def print_header(text):
    print(f"\n{Color.CYAN}{'='*60}{Color.END}")
    print(f"{Color.CYAN}{Color.BOLD}{text}{Color.END}")
    print(f"{Color.CYAN}{'='*60}{Color.END}\n")

def print_success(text):
    print(f"{Color.GREEN}✓ {text}{Color.END}")

def print_error(text):
    print(f"{Color.RED}✗ ERROR: {text}{Color.END}")

def print_warning(text):
    print(f"{Color.YELLOW}⚠ {text}{Color.END}")

def print_info(text):
    print(f"{Color.WHITE}{text}{Color.END}")

def print_gray(text):
    print(f"{Color.GRAY}{text}{Color.END}")

def find_unp4k():
    """Find unp4k.exe in the tools directory."""
    script_dir = Path(__file__).parent
    unp4k_path = script_dir / "unp4k.exe"

    if not unp4k_path.exists():
        return None
    return unp4k_path

def convert_wsl_path(path):
    """Convert WSL path to Windows path if running in WSL."""
    if platform.system() == "Linux" and "microsoft" in platform.uname().release.lower():
        # Running in WSL
        try:
            result = subprocess.run(
                ["wslpath", "-w", str(path)],
                capture_output=True,
                text=True,
                check=True
            )
            return result.stdout.strip()
        except subprocess.CalledProcessError:
            return str(path)
    return str(path)

def convert_windows_path(path):
    """Convert Windows path to WSL path if running in WSL."""
    if platform.system() == "Linux" and "microsoft" in platform.uname().release.lower():
        # Running in WSL
        try:
            result = subprocess.run(
                ["wslpath", "-u", str(path)],
                capture_output=True,
                text=True,
                check=True
            )
            return Path(result.stdout.strip())
        except subprocess.CalledProcessError:
            return Path(path)
    return Path(path)

def find_star_citizen_installations():
    """Find all Star Citizen installation folders (LIVE, PTU, EPTU, HOTFIX)."""
    installations = []

    # Common installation paths (Windows)
    common_roots = [
        "C:/Program Files/Roberts Space Industries/StarCitizen",
        "D:/Program Files/Roberts Space Industries/StarCitizen",
        "E:/Program Files/Roberts Space Industries/StarCitizen",
        "C:/Games/Roberts Space Industries/StarCitizen",
        "D:/Games/Roberts Space Industries/StarCitizen",
        "E:/Games/Roberts Space Industries/StarCitizen",
    ]

    # Convert to WSL paths if needed
    if platform.system() == "Linux" and "microsoft" in platform.uname().release.lower():
        common_roots = [
            "/mnt/c/Program Files/Roberts Space Industries/StarCitizen",
            "/mnt/d/Program Files/Roberts Space Industries/StarCitizen",
            "/mnt/e/Program Files/Roberts Space Industries/StarCitizen",
            "/mnt/c/Games/Roberts Space Industries/StarCitizen",
            "/mnt/d/Games/Roberts Space Industries/StarCitizen",
            "/mnt/e/Games/Roberts Space Industries/StarCitizen",
        ]

    branches = ["LIVE", "PTU", "EPTU", "HOTFIX"]

    for root in common_roots:
        root_path = Path(root)
        if root_path.exists():
            for branch in branches:
                data_p4k = root_path / branch / "Data.p4k"
                if data_p4k.exists():
                    installations.append({
                        "branch": branch,
                        "path": data_p4k,
                        "root": root_path
                    })

    return installations

def extract_global_ini(data_p4k_path, unp4k_path, output_dir, branch, version):
    """Extract global.ini from Data.p4k using unp4k.exe."""
    print_info(f"Extracting global.ini from {branch} (v{version})...")
    print_gray("This may take 30-120 seconds depending on your system...\n")

    # Create temp directory
    temp_dir = output_dir / "temp_extraction"
    temp_dir.mkdir(parents=True, exist_ok=True)

    try:
        # Convert paths for unp4k.exe (needs Windows paths)
        data_p4k_win = convert_wsl_path(data_p4k_path)
        temp_dir_win = convert_wsl_path(temp_dir)
        unp4k_win = convert_wsl_path(unp4k_path)

        # Run unp4k.exe
        cmd = [
            unp4k_win,
            data_p4k_win,
            "*global.ini"
        ]

        result = subprocess.run(
            cmd,
            cwd=temp_dir_win,
            capture_output=True,
            text=True,
            timeout=300  # 5 minute timeout
        )

        if result.returncode != 0:
            raise Exception(f"unp4k.exe failed with exit code {result.returncode}\n{result.stderr}")

        # Find the extracted global.ini
        extracted_files = list(temp_dir.rglob("global.ini"))
        if not extracted_files:
            raise Exception("global.ini was not found in extracted files")

        extracted_file = extracted_files[0]

        # Save with versioned filename
        output_filename = f"global-{version}-{branch}.ini"
        output_path = output_dir / output_filename

        shutil.copy2(extracted_file, output_path)

        # Get file size
        file_size_mb = output_path.stat().st_size / (1024 * 1024)

        print_success(f"Extracted global.ini successfully!")
        print_info(f"  Saved to: {output_path.relative_to(Path.cwd())}")
        print_info(f"  File size: {file_size_mb:.2f} MB")

        return output_path

    except subprocess.TimeoutExpired:
        print_error("Extraction timed out after 5 minutes")
        return None
    except Exception as e:
        print_error(str(e))
        return None
    finally:
        # Cleanup temp directory
        if temp_dir.exists():
            shutil.rmtree(temp_dir, ignore_errors=True)

def interactive_mode():
    """Run the tool in interactive mode with user prompts."""
    print_header("Star Citizen global.ini Extractor (BETA)")

    # Check for unp4k.exe
    unp4k_path = find_unp4k()
    if not unp4k_path:
        print_error("unp4k.exe not found in tools/ directory!")
        print_info("\nPlease download unp4k from:")
        print_info("  https://github.com/dolkensp/unp4k/releases")
        print_info("\nExtract unp4k.exe to the tools/ folder and try again.")
        return 1

    print_success("Found unp4k.exe\n")

    # Find installations
    print_info("Scanning for Star Citizen installations...\n")
    installations = find_star_citizen_installations()

    if not installations:
        print_error("No Star Citizen installations found!")
        print_info("\nPlease ensure Star Citizen is installed in one of these locations:")
        print_gray("  C:\\Program Files\\Roberts Space Industries\\StarCitizen\\LIVE")
        print_gray("  D:\\Program Files\\Roberts Space Industries\\StarCitizen\\LIVE")
        print_gray("  C:\\Games\\Roberts Space Industries\\StarCitizen\\LIVE")
        return 1

    # Show found installations
    print_info("Found installations:")
    for i, inst in enumerate(installations, 1):
        print_info(f"  [{i}] {inst['branch']:8} - {inst['path']}")

    # Select installation
    print()
    while True:
        try:
            choice = input(f"{Color.YELLOW}Which installation? [1]: {Color.END}").strip()
            if not choice:
                choice = "1"
            choice_num = int(choice)
            if 1 <= choice_num <= len(installations):
                selected = installations[choice_num - 1]
                break
            print_error(f"Please enter a number between 1 and {len(installations)}")
        except ValueError:
            print_error("Please enter a valid number")
        except KeyboardInterrupt:
            print("\n\nCancelled by user")
            return 1

    # Get version
    print()
    while True:
        try:
            version = input(f"{Color.YELLOW}What version is this? (e.g., 4.3.2): {Color.END}").strip()
            if version:
                # Basic validation (X.X.X format)
                parts = version.split('.')
                if len(parts) >= 2 and all(p.isdigit() for p in parts):
                    break
            print_error("Please enter a valid version (e.g., 4.3.2)")
        except KeyboardInterrupt:
            print("\n\nCancelled by user")
            return 1

    print()

    # Extract
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "stock-global-ini"
    output_dir.mkdir(exist_ok=True)

    result_path = extract_global_ini(
        selected['path'],
        unp4k_path,
        output_dir,
        selected['branch'],
        version
    )

    if result_path:
        print()
        print_header("SUCCESS!")
        print_info("The stock global.ini has been extracted.\n")
        print_info(f"{Color.BOLD}Next time, skip the prompts by running:{Color.END}")
        print(f"  {Color.GREEN}python tools/extract-global-ini.py --branch {selected['branch']} --version {version}{Color.END}\n")
        return 0
    else:
        print()
        print_header("FAILED")
        print_error("Extraction failed. See errors above.")
        return 1

def main():
    parser = argparse.ArgumentParser(
        description="Extract global.ini from Star Citizen Data.p4k",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  Interactive mode:
    python extract-global-ini.py

  Automated mode:
    python extract-global-ini.py --branch LIVE --version 4.3.4
    python extract-global-ini.py -b PTU -v 4.4.0
        """
    )

    parser.add_argument(
        "-b", "--branch",
        choices=["LIVE", "PTU", "EPTU", "HOTFIX"],
        help="Star Citizen branch (LIVE, PTU, EPTU, HOTFIX)"
    )

    parser.add_argument(
        "-v", "--version",
        help="Star Citizen version (e.g., 4.3.4)"
    )

    args = parser.parse_args()

    # If no arguments, run interactive mode
    if not args.branch and not args.version:
        return interactive_mode()

    # Non-interactive mode - both arguments required
    if not args.branch or not args.version:
        print_error("Both --branch and --version are required for automated mode")
        print_info("Use interactive mode by running without arguments:")
        print_info("  python extract-global-ini.py")
        return 1

    # Non-interactive extraction
    print_header(f"Extracting global.ini from {args.branch} (v{args.version})")

    # Check for unp4k.exe
    unp4k_path = find_unp4k()
    if not unp4k_path:
        print_error("unp4k.exe not found in tools/ directory!")
        print_info("\nDownload from: https://github.com/dolkensp/unp4k/releases")
        return 1

    # Find the specified installation
    installations = find_star_citizen_installations()
    selected = None
    for inst in installations:
        if inst['branch'] == args.branch:
            selected = inst
            break

    if not selected:
        print_error(f"{args.branch} installation not found!")
        print_info("\nAvailable installations:")
        for inst in installations:
            print_info(f"  - {inst['branch']}")
        return 1

    # Extract
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "stock-global-ini"
    output_dir.mkdir(exist_ok=True)

    result_path = extract_global_ini(
        selected['path'],
        unp4k_path,
        output_dir,
        args.branch,
        args.version
    )

    print()
    return 0 if result_path else 1

if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\n\nCancelled by user")
        sys.exit(1)

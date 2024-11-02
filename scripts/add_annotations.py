#!/usr/bin/env python3
from __future__ import annotations

import argparse
import os
import subprocess
import sys
import tempfile


def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description='Add file path annotations to files.')
    parser.add_argument('files', nargs='*', help='Files to process')
    parser.add_argument(
        '--no-stage', action='store_true',
        help='Do not stage modified files',
    )
    return parser.parse_args()


def check_annotation(file_path: str) -> bool:
    """Check if file already has the annotation."""
    expected_annotation = f"# {file_path}"
    try:
        with open(file_path, encoding='utf-8') as f:
            first_line = f.readline().strip()
            return first_line == expected_annotation
    except Exception:
        return False


def add_annotation(file_path: str) -> bool:
    """Add annotation to file."""
    annotation = f"# {file_path}"
    temp_fd, temp_path = tempfile.mkstemp(dir=os.path.dirname(file_path))

    try:
        with os.fdopen(temp_fd, 'w', encoding='utf-8') as temp_file, \
                open(file_path, encoding='utf-8') as original_file:
            # Write annotation
            temp_file.write(f"{annotation}\n")
            # Copy original content
            temp_file.write(original_file.read())

        # Replace original file with temporary file
        os.replace(temp_path, file_path)
        return True
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        if os.path.exists(temp_path):
            os.unlink(temp_path)
        return False


def is_text_file(file_path: str) -> bool:
    """Check if file is a text file using 'file' command."""
    try:
        result = subprocess.run(['file', file_path], capture_output=True, text=True)
        return 'text' in result.stdout.lower() or 'empty' in result.stdout.lower()
    except Exception:
        return False


def stage_file(file_path: str) -> bool:
    """Stage file using git add."""
    try:
        subprocess.run(['git', 'add', file_path], check=True, capture_output=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error staging {file_path}: {e.stderr.decode()}")
        return False


def main():
    args = parse_args()
    modified_files = []
    success = True

    # Process each file passed as argument
    for file_path in args.files:
        if not os.path.isfile(file_path):
            continue

        if not is_text_file(file_path):
            print(f"Skipping binary file: {file_path}")
            continue

        if check_annotation(file_path):
            print(f"Annotation already exists in: {file_path}")
            continue

        print(f"Adding annotation to: {file_path}")
        if add_annotation(file_path):
            modified_files.append(file_path)
        else:
            success = False

    # Stage files only if --no-stage is not set and there were no errors
    if not args.no_stage and modified_files and success:
        print("Staging modified files...")
        for file_path in modified_files:
            if not stage_file(file_path):
                return 1
    elif modified_files:
        print("\nFiles modified but not staged:")
        for file_path in modified_files:
            print(f"  {file_path}")
        print("\nYou can stage these files manually with 'git add' if desired")

    return 0 if success else 1


if __name__ == '__main__':
    sys.exit(main())

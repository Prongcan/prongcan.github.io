#!/usr/bin/env python3
"""Auto-approve safe bash commands for Claude Code"""
import json
import sys
import re

# Read input from stdin
try:
    data = json.load(sys.stdin)
except json.JSONDecodeError:
    sys.exit(0)

tool_name = data.get('tool_name', '')
tool_input = data.get('tool_input', {})
command = tool_input.get('command', '')

# Only process Bash commands
if tool_name != 'Bash' or not command:
    sys.exit(0)

# Define safe command patterns (read-only, non-destructive)
SAFE_PATTERNS = [
    r'^ls\b',
    r'^pwd\b',
    r'^cat\s+',
    r'^head\s+',
    r'^tail\s+',
    r'^grep\s+',
    r'^find\s+',
    r'^sed\s+',
    r'^awk\s+',
    r'^git\s+(status|diff|log|branch|show|blame)',
    r'^echo\s+',
    r'^which\b',
    r'^date\b',
    r'^whoami\b',
    r'^id\b',
]

# Check if command matches any safe pattern
command_stripped = command.strip()
is_safe = any(re.match(pattern, command_stripped) for pattern in SAFE_PATTERNS)

if is_safe:
    # Auto-approve the command
    output = {
        'hookSpecificOutput': {
            'hookEventName': 'PermissionRequest',
            'decision': {
                'behavior': 'allow'
            }
        }
    }
    print(json.dumps(output))
    sys.exit(0)
else:
    # Let user approve manually
    sys.exit(0)

import json
import sys
import re
import os

def parse_fluency_facts(text):
    # Split into sections (each entry is separated by a blank line)
    sections = [s.strip() for s in text.strip().split("\n\n") if s.strip()]
    
    data = {}
    for section in sections:
        lines = section.splitlines()
        if not lines:
            continue
        
        topic = lines[0].strip().rstrip(":")  # First line is the topic (e.g. "Maize")
        entry = {}
        
        key = None
        buffer = []
        for line in lines[1:]:
            if re.match(r"^(Who|What|Where|When|Why|Significance)\s*$", line):
                # Save previous key-value
                if key and buffer:
                    entry[key] = " ".join(buffer).strip()
                # Start new key
                key = line.strip()
                buffer = []
            else:
                buffer.append(line.strip())
        
        # Save the last key-value
        if key and buffer:
            entry[key] = " ".join(buffer).strip()
        
        data[topic] = entry
    
    return data

def txt_to_json(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as f:
        text = f.read()
    
    parsed = parse_fluency_facts(text)
    
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(parsed, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    if os.path.exists("ff.txt"):
        input_file = "ff.txt"
        output_file = "ff.json"
        print(f"⚙️ Using default input file: {input_file}")
    else:
        if len(sys.argv) != 3:
            print("Usage: python txt_to_json.py input.txt output.json")
            sys.exit(1)
        input_file = sys.argv[1]
        output_file = sys.argv[2]
    
    txt_to_json(input_file, output_file)
    print(f"✅ Converted {input_file} → {output_file}")
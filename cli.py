import argparse
import textwrap
from humanizer import humanize_text

def main():
    parser = argparse.ArgumentParser(
        description="Humanizer AI CLI - Make your text sounf more natural and human-like."
    )
    parser.add_argument(
        "--input",
        "-i",
        type=str,
        help="Path to input text file. If omitted, you can text manually."
    )
    parser.add_argument(
        "--output",
        "-o",
        type=str,
        help="Optional path to save the humanized text.",
    )
    parser.add_argument(
        "--tone",
        "-t",
        type=str,
        default="natural",
        help="Tone of the rewritten text (e.g. 'friendly', 'formal', 'storytelling', 'professional').",
    )
    
    args = parser.parse_args()
    
    # Read input text
    if args.input:
        try:
            with open(args.input, "r", encoding="utf-8") as f:
                text = f.read()
        except FileNotFoundError:
            print("Error: Input file not found.")
            return
    else:
        print("Paste your text below (press Enter twice to finish):\n")
        lines = []
        while True:
            line = input()
            if line.strip() == "":
                break
            lines.append(line)
        text = "\n".join(lines)
        
    print("\n Processing with Gemini... Please wait...\n")
    result = humanize_text(text, args.tone)
    
    print("=== Humanized Output ===\n")
    print(textwrap.fill(result, width=100))
    
    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(result)
        print(f"\n Saved humanized text to {args.output}")
        

if __name__ == "__main__":
    main()
    
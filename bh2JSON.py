import json
import re

def parse_bh_file(file_content):
    results = []
    current_entry = None
    
    for line in file_content.split('\n'):
        if line.startswith('[ MATCHED ]'):
            if current_entry:
                results.append(current_entry)
            current_entry = {
                'matched': line.split('[ MATCHED ]')[1].strip(),
                'behavior': {},
                'explained': '',
                'prevalence': '',
                'detections': []
            }
        elif line.startswith('[ BH'):
            parts = line.split('/')
            current_entry['behavior'] = {
                'code': parts[0].strip(),
                'category': parts[1].strip() if len(parts) > 1 else '',
                'count': parts[2].strip() if len(parts) > 2 else '',
                'description': parts[3].strip() if len(parts) > 3 else ''
            }
        elif line.startswith('Explained:'):
            current_entry['explained'] = line.split('Explained:')[1].strip()
        elif line.startswith('Prevalence'):
            prevalence_lines = []
            for prevalence_line in file_content.split('\n')[file_content.split('\n').index(line) + 1:]:
                if prevalence_line.strip() and not prevalence_line.startswith('Detections'):
                    prevalence_lines.append(prevalence_line.strip())
                else:
                    break
            current_entry['prevalence'] = ' '.join(prevalence_lines).strip()
        elif line.startswith('Detections'):
            detections_start = file_content.split('\n').index(line)
            detections = []
            for detection_line in file_content.split('\n')[detections_start + 1:]:
                if detection_line.strip() and not detection_line.startswith('----------------'):
                    detections.append(detection_line.strip())
                elif detection_line.startswith('----------------'):
                    break
            current_entry['detections'] = detections

    if current_entry:
        results.append(current_entry)

    return results

def main():
    with open('bh.txt', 'r') as file:
        content = file.read()

    parsed_data = parse_bh_file(content)
    json_output = json.dumps(parsed_data, indent=2)

    with open('bh.json', 'w') as outfile:
        outfile.write(json_output)

    print("Conversion completed. Output saved to bh_output.json")

if __name__ == "__main__":
    main()

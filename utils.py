# import the necessary packages
import os
import json
import numpy as np



def get_all_virus_total_reports(reports_dir):
    reports = []
    for root, dirs, files in os.walk(reports_dir):
        apt_group = os.path.basename(root)
        
        # Skip processing for any files located in the 'virustotal' subdirectory
        if apt_group == 'virustotal': continue
        
        for file in files:
            # Process only JSON files
            if file.endswith('.json'):
                with open(os.path.join(root, file), 'r') as f:
                    json_data = json.load(f)
                    # Add APT group and file name to each JSON data
                    json_data['apt_group'] = apt_group
                    json_data['file_name'] = file
                    reports.append(json_data)
    
    return reports



def get_all_cuckoo_reports(reports_path):
    # Initialize a list to store parsed cuckoo report data.
    cuckoo_reports = []

    # Iterate over each item in the reports directory.
    for task_id_name in os.listdir(reports_path):
        # Skip non-directory items.
        if not os.path.isdir(os.path.join(reports_path, task_id_name)):
            print(f"Skipping {task_id_name} as it is not a folder")
            continue

        # Skip directories missing a JSON report.
        if not os.path.exists(os.path.join(reports_path, task_id_name, 'reports', 'report.json')):
            print(f"Skipping {task_id_name} as it does not have a report.json file")
            continue
        
        # Load and parse the JSON report.
        with open(os.path.join(reports_path, task_id_name, 'reports', 'report.json')) as f:
            report = json.loads(f.read())
        
        # Extract relevant information from the report.
        cuckoo_report = {
            'task_id': task_id_name,
            'score': report['info']['score'],
            'signatures_count' : len(report['signatures']),
            'signature_mark_call_count': sum(sum(len([y for y in x if 'call' in x.keys()]) for x in sig['marks'] if 'marks' in sig.keys()) for sig in report['signatures']),
            'category': report['info']['category'],
            'package': report['info']['package'],
            'strings_count' : len(set(report['strings'])),
        }
        
        # Include optional details if available
        for key in ['static', 'fileops']:
            if key in report:
                cuckoo_report[key] = report[key]
        
        # Include behavior details if available
        if 'behavior' in report:
            bevariour = report['behavior']
            cuckoo_report['generic_behavior'] = bevariour['generic']
            cuckoo_report['apistats'] = np.nan if 'apistats' not in bevariour.keys() else bevariour['apistats']
            cuckoo_report['processes'] = bevariour['processes']
            cuckoo_report['summary'] = {} if 'summary' not in bevariour.keys() else bevariour['summary']

        # Check for suricata analysis and include it if present.
        if os.path.exists(os.path.join(reports_path, task_id_name, 'suricata', 'eve.json')):
            with open(os.path.join(reports_path, task_id_name, 'suricata', 'eve.json')) as f:
                eve = json.loads('[' + ','.join(f.readlines()) + ']')
            
            cuckoo_report['suricata'] = eve[:-1]
            cuckoo_report['suricata_summary'] = eve[-1]

        # Add the parsed report to the list.
        cuckoo_reports.append(cuckoo_report)
    
    return cuckoo_reports
# Import necessary libraries.
from appscript import *
import time
import os
import pandas as pd

# Load and sort CSV data by 'cuckoo_id'.
df = pd.read_csv('cuckoo_task_ids_to_download.csv').sort_values(by='cuckoo_id')

# Filter data for 'Gorgon Group' only.
filtered_df = df[df['apt'] == 'Gorgon Group']

# Loop through the filtered IDs to manage report downloads.
for cuckoo_task_id in filtered_df['cuckoo_id']:
    # Initialize Safari for web navigation.
    safari = app("Safari")

    # Open a new Safari tab with the specific report URL.
    safari.make(new=k.document, with_properties={k.URL: f"https://cuckoo.cert.ee/analysis/{cuckoo_task_id}/export/"})

    # AppleScript to focus Safari.
    osascript_bring_to_front = '''
    tell application "Safari"
        activate
    end tell
    '''

    # Run the AppleScript, wait for 5 seconds.
    os.system(f"osascript -e '{osascript_bring_to_front}'")
    time.sleep(5)

    # Close the active Safari tab after operations.
    safari.windows.first.current_tab.close()
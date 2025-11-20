import json
import time
def convert_test_to_main(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            source_data = json.load(f)
    except FileNotFoundError:
        print(f"Error: {input_file} not found.")
        return
    output_data = {
        "backupManga": [],
        "backupSources": [
            {
                "name": "MangaDex",
                "sourceId": "2499283573021220400" 
            }
        ]
    }
    status_map = {
        "ONGOING": 1,
        "COMPLETED": 2,
        "HIATUS": 6
    }
    current_time_ms = str(int(time.time() * 1000))
    for entry in source_data:
        manga_details = entry.get('manga', {})        
        tags = [tag['title'] for tag in manga_details.get('tags', [])]
        state_str = manga_details.get('state', 'ONGOING')
        status_int = status_map.get(state_str, 1) 
        new_manga = {
            "source": "2499283573021220400", 
            "url": f"/manga/{manga_details.get('url', '')}",
            "title": manga_details.get('title', ''),
            "artist": manga_details.get('author', ''), 
            "author": manga_details.get('author', ''),
            "description": "Imported from backup.", 
            "genre": tags,
            "status": status_int,
            "thumbnailUrl": manga_details.get('cover_url', ''),
            "dateAdded": current_time_ms,
            "viewerFlags": 0,
            "chapters": [] 
        }

        output_data["backupManga"].append(new_manga)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)
    
    print(f"Successfully converted {len(source_data)} entries to {output_file}")

convert_test_to_main('history.json', 'converted_main.json')
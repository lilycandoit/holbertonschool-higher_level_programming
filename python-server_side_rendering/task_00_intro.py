import os

def generate_invitations(template, attendees):
    # Input type validation
    if not isinstance(template, str):
        print("Error: template must be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: attendees must be a list of dictionaries.")
        return

    # Empty content checks
    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Ensure output directory exists
    output_dir = "output_invitations"
    try:
        os.makedirs(output_dir, exist_ok=True)
    except PermissionError:
        print(f"Error: Permission denied to create directory '{output_dir}'.")
        return

    # Process each attendee
    for i, person in enumerate(attendees, start=1):
        content = template
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = person.get(key)
            content = content.replace(f"{{{key}}}", value if value else "N/A")

        # Write to output_i.txt
        output_filename = os.path.join(output_dir, f"output_{i}.txt")
        try:
            with open(output_filename, "w") as f:
                f.write(content)
        except Exception as e:
            print(f"Failed to write file {output_filename}: {e}")

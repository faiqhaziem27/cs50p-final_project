import sys
import re
import csv

class ContactManager:
    def __init__(self):
        self.contacts = []

    def load_csv(self, file_path):
        with open(file_path, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                row["name"] = row["name"].strip()
                row["email"] = row["email"].strip()
                row["phone"] = row["phone"].strip()
                self.contacts.append(row)

    @property
    def get_valid_contacts(self):
        name_pattern = r"[a-zA-Z]+(?:\s[a-zA-Z]+)+"
        email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        phone_pattern = r"^\+?\d[\d\s-]{5,13}\d$"
        valid_rows = []

        for row in self.contacts:
            is_valid_name = re.match(name_pattern, row["name"])
            is_valid_email = re.match(email_pattern, row["email"])
            is_valid_phone = re.match(phone_pattern, row["phone"])

            if is_valid_name or is_valid_email or is_valid_phone:
                valid_rows.append(row)

        return valid_rows

    def export_to_csv(self, rows, output_filename):
        if not rows:
            return False

        with open(output_filename, "w", newline="") as new_file:
            writer = csv.DictWriter(new_file, fieldnames=["name", "email", "phone"])
            writer.writeheader()
            writer.writerows(rows)

        return True

    def load_txt(self, file_path):
        name_pattern = r"(?:[Nn]ame:[ \t]*)([a-zA-Z]+(?:[ \t]+[a-zA-Z]+)*)"
        email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
        phone_pattern = r"\+?\d[\d\s-]{5,13}\d"

        with open(file_path, "r") as file:
            content = file.read()
            contact_blocks = re.split(r"(?=[Nn]ame:[ \t]*)", content)

            for block in contact_blocks:
                name_match = re.search(name_pattern, block)
                if not name_match:
                    continue

                email_match = re.search(email_pattern, block)
                phone_match = re.search(phone_pattern, block)

                self.contacts.append({
                    "name": name_match.group(1).strip(),
                    "email": email_match.group(0) if email_match else "Unknown",
                    "phone": phone_match.group(0) if phone_match else "N/A"
                })

def main():

    contact_manager = ContactManager()

    if len(sys.argv) > 3:
        sys.exit("Too many command-lines")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-lines")

    file_path = sys.argv[1]
    try:
        if sys.argv[1].endswith(".csv"):
            contact_manager.load_csv(file_path)

            clean_rows = contact_manager.get_valid_contacts

            export = contact_manager.export_to_csv(clean_rows, sys.argv[2])

            print(export)
            print("File has successfully been exported")

        elif sys.argv[1].endswith(".txt"):
            contact_manager.load_txt(file_path)

            clean_rows = contact_manager.get_valid_contacts

            export = contact_manager.export_to_csv(clean_rows, sys.argv[2])

            print(export)
            print("File has successfully been exported")

        else:
            print("Unsupported file extension not supported. Please utilize .csv or .txt")

    except FileNotFoundError:
        sys.exit(f"Error: File {file_path} not found")

if __name__ == "__main__":
    main()

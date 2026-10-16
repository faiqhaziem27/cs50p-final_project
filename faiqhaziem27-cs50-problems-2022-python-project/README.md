# Polymorphic Object-Oriented Contact & Artifact Harvester

#### Video Demo: https://youtu.be/kOqqnzP5RWw

#### Description:

## Comprehensive Project Overview
The Polymorphic Object-Oriented Contact & Artifact Harvester is a production-ready, command-line utility engineered in Python. This tool programmatically aggregates, normalizes, standardizes, and parses contact profile information from fluctuating, unstructured data streams. The core application engine solves a ubiquitous real-world problem: processing completely loose communication artifacts (such as automated server log entries, chat transcripts, raw terminal dumps, and conversational text notes) alongside structured database spreadsheets.

Unlike primitive text scripts that only loop through specific characters or scan lines sequentially, this system deploys an architecture that dynamically inspects and routes data bundles based on their file extensions. Once incoming records penetrate the application's processing pipeline, they are instantly sanitized of superficial layout noise and converted into uniform, encapsulated Python memory dictionaries. The application maintains rigid data integrity using layered regular expression testing structures, isolating clean profile models before exporting the compilation down into an external comma-separated asset list. This software serves as an exceptional automation utility for data analysts, system administrators, or software engineers who need to quickly harvest clean identity metrics out of messy operational environments.

---

## Architectural & Technical Design Considerations
This utility was built on solid software engineering principles, prioritizing object encapsulation, structural consistency, and runtime error isolation.

### 1. Object-Oriented State Isolation (OOP)
Instead of executing functional routines or mutating loose global tracking lists, the application manages all localized data boundaries within a central database container class: `ContactManager`. This class manages state internally via `self.contacts`, exposing safe entry modification channels while completely hiding extraction complexities away from the user interface loop in `main()`.

### 2. Streamlined Property Abstraction
To demonstrate structural mastery over advanced Python capabilities, the auditing filter layer utilizes the `@property` decorator pattern. This converts the operational logic of data verification into a clean attribute abstraction layer. When `contact_manager.get_valid_contacts` is referenced inside the file execution loop, it evaluates existing state lists dynamically without needing a parenthetical function call expression. This structure minimizes syntax clutter, an approach highly valued in professional micro-framework production.

### 3. Asymmetric Text Data Alignment
When reading unstructured `.txt` communication logs via unstructured regular expressions, names, emails, and phone digits rarely match up in equal counts. To eliminate array indexing exceptions (`IndexError`) when parsing uneven datasets, the class implements an automatic alignment mapping mechanism (`max_len`). It processes records using fallback placeholders (`"Unknown"` and `"N/A"`) to build a uniform internal list of dictionaries that perfectly mirrors a pristine corporate spreadsheet layout.

### 4. Contextual Token Guard rails
To counter conversational text noise (such as phrases like "Hello Team", "Good Morning", or "Dear Customer") from corrupting the identity rows, the text processing regular expression engine implements explicit non-capturing boundaries `(?:[Nn]ame:\s*)`. This structure forces the system to look for an explicit contextual identifier prefix, isolating the literal name string group securely while throwing away the surrounding prefix noise automatically.

---

## Technical File Blueprint Breakdown

### 1. `project.py`
The execution core of the utility containing class properties, regex patterns, and command-line interfaces:
*   `__init__(self)`: Instantiates a clean, independent list array to serve as the application's internal data staging environment.
*   `load_csv(self, file_path)`: Opens tabular records using `csv.DictReader` and strips trailing white space from columns.
*   `load_txt(self, file_path)`: Parses raw text string contents, applies non-capturing prefix regular expressions, and deploys structural bounds tracking loops.
*   `get_valid_contacts(self)`: Decorating as a `@property`, it runs character validation rules (`re.match`) on internal rows using a logical `or` boundary to keep partially populated entries.
*   `export_to_csv(self, rows, output_filename)`: Opens a fresh target file path and uses `csv.DictWriter` to compile rows under exact header field layouts.
*   `main()`: Coordinates argument length check logic (`sys.argv`), wraps file exceptions gracefully inside `try/except` statements, and handles terminal print loops.

### 2. `test_project.py`
The verification module executed via the `pytest` engine framework. It isolates target logic branches through test functions prefixed with `test_`. The script handles file environment sandboxing by testing reading and writing loops across isolated files using virtual directory paths (`tmp_path`).

### 3. `requirements.txt`
Documents application dependencies. It specifies the configuration baseline (`pytest`) needed to support local unit verification test workflows.

---

## Installation & Deployment Guide

### Prerequisites
Ensure your local terminal machine is running **Python 3.8+** or higher.

### Step 1: Navigate to Project Directory
Ensure your required project files are organized inside a single workspace directory:
```bash
cd path/to/your/project_directory
```

### Step 2: Install Testing Dependencies
Install the required unit tracking tools documented in your dependency file:
```bash
pip install -r requirements.txt
```

---

## Execution Instructions & Examples

Execute the script through your system terminal by passing exactly two command-line file arguments:
```bash
python project.py <input_file_path> <output_file_path>
```

### Example A: Scraping Unstructured Text Logs
To extract and standardize contacts hidden inside unstructured notes:
```bash
python project.py sample.txt parsed_output.csv
```

### Example B: Auditing Tabular Databases
To filter completely clean records out of messy spreadsheet inputs:
```bash
python project.py sample.csv filtered_output.csv
```

### Example C: Invoking the Verification Suite
To execute internal unit tests and verify code architecture stability:
```bash
pytest test_project.py
```

SEP 8 PROJECT STATEMENT 
Job Tracker — Reusable Python Package
1. Project Goal
Turn the existing JobApplication domain model into a small reusable Python package called job_tracker.
Separate:
•	domain data and behavior 
•	reusable normalization/validation helpers 
•	tracker behavior 
•	statistics 
•	package exports 
•	application startup 
into clear modules.
The main purpose of this version is to practice:
OOP + dataclasses + modules + packages + imports + namespaces + typing + virtual environments + clean responsibility separation.
Exceptions, logging, exception-focused testing, and pytest are postponed to later roadmap chapters.
 
2. Concepts Tested
Python fundamentals
Practice:
•	functions 
•	parameters 
•	return values 
•	loops 
•	conditionals 
•	lists 
•	dictionaries 
•	type hints 
Do not assess exception handling in this version.
 
Classes and objects
Practice:
•	instance state 
•	methods 
•	self 
•	class attributes 
•	mutation vs read-only queries 
•	interfaces 
•	invariants 
•	encapsulation 
 
Composition
JobTracker owns a collection of JobApplication objects.
JobTracker
    has
     ↓
list[JobApplication]
Do not use inheritance between these classes.
 
Responsibility separation
Different modules should have different responsibilities:
application.py → one job application's state/behavior
validation.py  → normalization/validation helpers
stats.py       → collection calculations
tracker.py     → manages applications
__init__.py    → package public interface
main.py        → application entry point/orchestration
 
Dataclasses
Practice:
•	@dataclass 
•	fields 
•	defaults 
•	default_factory 
•	__post_init__ 
•	generated __repr__ 
•	generated equality 
•	ClassVar 
 
Modules and packages
Practice:
•	modules 
•	module namespaces 
•	package structure 
•	__init__.py 
•	relative imports 
•	public package interface 
•	import execution 
•	import safety 
•	__name__ 
•	__main__ entry-point guard 
 
Virtual environments
Practice:
python3 -m venv .venv
source .venv/bin/activate
python -m pip list
Understand:
•	why .venv exists 
•	what activation changes 
•	why .venv is not committed 
•	why dependencies should not be installed globally 
 
3. Required Project Structure
job_tracker_project/
│
├── .gitignore
├── README.md
├── requirements.txt
├── main.py
│
└── job_tracker/
    ├── __init__.py
    ├── application.py
    ├── tracker.py
    ├── validation.py
    └── stats.py
Removed from this version
manual_tests.py
You will revisit testing after learning exceptions and then pytest.
 
4. Functional Requirements
4.1 application.py — JobApplication
Create:
@dataclass
class JobApplication:
    ...
Required instance fields:
company
role
status
notes
Requirements:
•	status defaults to "applied". 
•	Every object must receive its own notes list using default_factory. 
•	Allowed statuses are: 
applied
interview
rejected
offer
•	Store allowed statuses as class-level configuration, not instance data. 
•	Use ClassVar. 
•	Normalize surrounding whitespace from company and role. 
•	Normalize status consistently. 
•	Use __post_init__() for normalization/validation after dataclass initialization. 
•	Provide: 
change_status(new_status)
add_note(note)
get_summary()
•	change_status() should validate/normalize before assigning the new status. 
•	add_note() should normalize the note before storing it. 
•	get_summary() must be a read-only query. 
Exception note
Your implementation may currently use:
raise ValueError(...)
That is acceptable, but exception mechanics are not assessed in this version.
You are not required yet to explain:
•	exception propagation 
•	try/except 
•	exception hierarchies 
•	handling strategies 
Those belong to the next chapter.
 
4.2 validation.py
Move reusable normalization/validation logic here.
Provide small functions such as:
normalize_text(...)
validate_status(...)
Each function should have one clear responsibility.
validation.py must:
•	normalize values 
•	validate status against supplied allowed statuses 
•	return normalized usable values 
•	avoid mutating JobApplication 
•	remain independent of JobApplication to avoid circular imports 
For example, dependency flow should remain:
application.py
      ↓
validation.py
not:
application.py
      ↕
validation.py
Exception behavior inside these helpers is not part of the current assessment.
 
4.3 tracker.py — JobTracker
Create:
class JobTracker:
    ...
Each tracker owns its own:
self.applications: list[JobApplication]
Provide:
add_application(application)
total_applications()
find_by_status(status)
get_status_counts()
add_application()
Adds a JobApplication to the collection.
Your current runtime type protection may remain, but exception behavior is not tested in this project version.
total_applications()
Read-only query returning:
int
find_by_status()
Normalize the requested status and return:
list[JobApplication]
containing only matching applications.
Do not mutate applications during the search.
get_status_counts()
Delegate counting work to:
stats.py
Do not duplicate the counting algorithm in tracker.py.
 
4.4 stats.py
Provide:
total_applications(applications)
returning:
int
And:
counts_by_status(applications)
returning:
dict[str, int]
Use a normal loop and dictionary:
counts: dict[str, int] = {}
Do not use collections.Counter yet.
Do not mutate supplied applications.
Do not print from stats.py.
 
4.5 __init__.py
Expose the package's public interface.
At minimum:
from .application import JobApplication
from .tracker import JobTracker
Stats functions may also be exposed deliberately:
from .stats import counts_by_status, total_applications
Keep __init__.py small.
Do not put:
•	demo code 
•	object creation 
•	printing 
•	application execution 
inside it.
 
4.6 Import Safety
This should be safe:
python -c "import job_tracker"
It should not:
•	print application output 
•	start the program 
•	create demo objects 
•	modify files 
•	perform unrelated work 
Importing the package should primarily establish definitions and package names.
 
4.7 main.py — Application Entry Point
Requirements:
•	Define: 
def main() -> None:
•	Use: 
if __name__ == "__main__":
    main()
•	Import through the package interface: 
from job_tracker import JobApplication, JobTracker
Do not import from internal modules such as:
from job_tracker.application import ...
Create at least:
4 JobApplication objects
covering at least:
3 different statuses
Add all four to one:
JobTracker
Perform:
•	at least one valid status change 
•	at least one add_note() 
Print:
•	useful application summaries 
•	total application count 
•	grouped status counts 
Do not put validation or class definitions in main.py.
 
5. Testing — Deferred
Remove the previous manual_tests.py requirement entirely.
For this project version:
No formal manual-test script is required.
You only need to run:
python main.py
once and confirm that the package imports and the valid demonstration path executes.
You do not need to test yet:
blank company
blank role
invalid status
invalid status transition
wrong object passed to tracker
expected ValueError
expected TypeError
try/except behavior
Those cases will be revisited after studying Exceptions + Logging, and later converted into proper automated tests when you reach pytest.
 
6. Environment Requirements
Create:
python3 -m venv .venv
Activate on macOS/Linux:
source .venv/bin/activate
Verify:
which python
python -m pip list
The project currently uses only the Python standard library, so:
requirements.txt
may remain empty.
Do not install packages merely to make it non-empty.
 
7. .gitignore
Include:
.venv/
__pycache__/
*.pyc
Do not commit the virtual environment.
 
8. README Requirements
Keep the README relatively short.
Explain:
•	project purpose 
•	project structure 
•	responsibility of each module 
•	how to create/activate .venv 
•	how to run main.py 
•	why .venv is not committed 
•	why requirements.txt can currently be empty 
•	what __init__.py exposes 
•	why package-relative imports are used internally 
•	why JobTracker uses composition rather than inheritance 
•	one example of delegation 
•	== vs is 
•	__str__ vs __repr__ 
•	why default_factory=list is needed 
Remove from README for now
You do not need to explain:
try/except
exception propagation
exception handling strategies
logging
pytest
 
9. Definition of Done
The project is complete when:
•	✅ package structure exists 
•	✅ modules have clear responsibilities 
•	✅ JobApplication uses @dataclass 
•	✅ ALLOWED_STATUSES is class-level configuration 
•	✅ default_factory=list is used correctly 
•	✅ __post_init__() is used 
•	✅ validation/normalization is delegated 
•	✅ JobTracker uses composition 
•	✅ stats.py uses loop + dictionary 
•	✅ internal imports are package-relative 
•	✅ __init__.py defines a deliberate public interface 
•	✅ main.py imports from that public interface 
•	✅ main() exists 
•	✅ __main__ guard exists 
•	✅ four applications / three statuses demonstrated 
•	✅ state change demonstrated 
•	✅ note addition demonstrated 
•	✅ summaries/counts print correctly 
•	✅ .venv works 
•	✅ .venv is ignored by Git 
•	✅ requirements.txt exists 
•	✅ package import has no application side effects 
•	✅ code is pushed to GitHub 
Explicitly NOT required yet
manual_tests.py
try/except exercises
exception-focused testing
logging
pytest
JSON/files
HTTP
SQL
FastAPI
Updated scope in one line
Your current project is now:
OOP + dataclasses + modules + packages + imports + namespaces + typing + environments + responsibility separation — without assessing exceptions, logging, or testing yet.
That is the version I would use for where you are in the roadmap now.


SEP 9 FINAL PROJECT STATEMENT
Robust Job Tracker CLI
Exceptions + Logging Confidence Project
A one-day build focused on failure handling, exception flow, invariants, and useful operational logs.
Primary goal
Build a small CLI that remains usable after expected user mistakes, never corrupts valid application state, raises failures from the correct layer, and logs enough context to understand what happened.
Item	Specification
Required features	Add application • Update status • List applications • Exit
Main focus	try/except • raise • propagation • custom exceptions • boundaries • logging
Revision used naturally	Dataclass • invariants • composition • modules/package • relative imports
Out of scope	JSON/files for app data • HTTP • SQL • pytest • FastAPI • GUI • advanced logging
Target build time	About 4–5 focused hours; one day comfortably
Scope rule: Do not add features merely to make the project look bigger. The difficulty must come from correct contracts, control flow, exception boundaries, and logging decisions.
1. What This Project Must Prove
Concept	How it is demonstrated
Expected exceptions	You can predict what may fail and use specific handlers for failures you understand.
raise + invariants	Invalid construction or status changes are rejected before state is mutated.
Propagation	Lower layers detect/raise; higher layers catch only when they can respond meaningfully.
Custom exception	A missing application is represented by a domain-specific exception.
else / finally	Use else when it clarifies successful continuation; use finally only if real cleanup exists. If no cleanup exists, explain why no finally is needed.
Re-raising	Unexpected failures may be logged at the outer boundary and re-raised so bugs are not disguised.
Logging	Use sensible levels, module loggers, useful context, and traceback logging for unexpected failures.
Earlier Python concepts	Dataclass, __post_init__, composition, methods, lists, loops, package imports, and main entry-point pattern appear only where natural.
2. Required Project Structure
robust-job-tracker/
├── README.md
└── job_tracker/
    ├── __init__.py
    ├── application.py
    ├── tracker.py
    ├── exceptions.py
    └── main.py
Run the program from the outer project directory with:
python3 -m job_tracker.main
•	Use package-relative imports between files inside job_tracker/.
•	Keep __init__.py simple. No business logic belongs there.
•	Do not create extra modules unless a new responsibility genuinely needs one.
Architecture
User → CLI (main.py) → JobTracker → JobApplication. Domain objects own rules and raise failures. The CLI is the main user-facing exception boundary.
3. Domain Model
3.1 JobApplication
•	Use @dataclass.
•	Fields: company: str, role: str, status: str = "applied".
•	Allowed statuses: applied, interview, rejected, offer.
•	Keep ALLOWED_STATUSES as class-level configuration, not instance state.
•	Use __post_init__ to establish valid construction-time state.
•	Normalize company and role with strip(); reject blank values with ValueError.
•	Normalize status with strip().lower(); reject unsupported status with ValueError.
•	Provide change_status(new_status). Validate first; mutate only after validation succeeds.
•	Invariant: status must always be one of ALLOWED_STATUSES.
Required failure behavior: If change_status() receives an invalid status, it must raise and leave the previous valid status unchanged.
3.2 JobTracker
•	Own a private-by-convention application collection such as self._applications.
•	add_application(application): accept only JobApplication objects; wrong object type should raise TypeError.
•	list_applications(): return/read the current applications without changing them.
•	get_application(number): use the 1-based number shown to the CLI user.
•	If the number does not exist, raise ApplicationNotFoundError.
•	update_status(number, new_status): retrieve the application, then delegate the state change to JobApplication.change_status().
Important delegation rule
JobTracker must not directly assign application.status. JobApplication owns the status invariant, so JobTracker delegates the mutation to change_status().
4. Custom Exception Requirement
Create one meaningful domain-specific exception in exceptions.py:
class ApplicationNotFoundError(Exception):
    pass
•	Use it only when a requested application number does not exist.
•	Do not create extra custom exception classes unless they represent a genuinely different domain failure.
•	Use built-in ValueError for invalid text/status values and TypeError for wrong object types.
You must be able to explain
Why ApplicationNotFoundError improves clarity over a generic ValueError, and how a custom exception still participates in normal Python exception matching.
5. Required CLI Behavior
=== Job Tracker ===
1. Add application
2. Update application status
3. List applications
4. Exit
•	The menu repeats until the user explicitly chooses Exit.
•	Recoverable user mistakes must not terminate the program.
•	Use print() for user-facing CLI messages.
•	Do not print user-facing error messages from JobApplication or JobTracker.
Action	Required behavior
Add application	Ask for company and role. Successful creation is added to tracker and logged at INFO.
Update status	Ask for application number and new status. Missing number and invalid status are handled differently.
List applications	Display a 1-based number plus company, role, and status. Empty list should be handled cleanly.
Exit	Log normal shutdown and end the loop.
6. Exception Boundary Rules
•	Keep try blocks narrow enough that you know which operation failed.
•	Catch expected failures only where the program can recover, translate, or meaningfully respond.
•	Order handlers from more specific exception types to broader ones.
•	Do not wrap every function in try/except.
•	Do not use except: or broad except Exception inside ordinary menu operations just to keep the loop alive.
•	Do not use except/pass to hide failures.
lower layer: detect → raise
CLI layer:   catch → log → user-friendly message → continue
7. Exception Concepts That Must Appear
Concept	Project requirement
try / except	Handle expected runtime failures at the CLI boundary.
Multiple handlers	Handle ApplicationNotFoundError separately from ValueError where both can arise.
Specific before broad	Specific expected exceptions must appear before any broader outer handler.
raise	Domain/tracker code rejects invalid operations explicitly.
Propagation	Do not catch an error in the layer that cannot meaningfully handle it.
else	Use at least once only if it makes a successful path clearer; otherwise explain why you chose not to force it.
finally	Do not force it. In README, explain what finally is for and why this CLI has no mandatory cleanup resource.
Re-raising	At the outermost unexpected-failure boundary, log traceback and re-raise rather than converting a bug into a normal validation message.
Outer unexpected-failure boundary
It is acceptable to use a broad Exception handler only at the outermost application boundary for diagnostic logging, provided you do not pretend the failure was recovered. Log it with traceback information and re-raise.
8. Logging Requirements
Use Python's standard logging module. Keep the configuration simple and write operational logs to job_tracker.log so the CLI remains readable.
•	Configure logging once in main.py.
•	Default level: INFO.
•	Include at least timestamp, level, logger name, and message in the format.
•	Use logger = logging.getLogger(__name__) in any module that actually logs.
•	Never use logging as a replacement for user-facing print() messages.
•	Do not log passwords/secrets. This project has none, but keep the habit.
8.1 Required logging events
Level	Use in this project
DEBUG	At least one useful diagnostic detail, e.g. application count after a successful add. It may be hidden at INFO level.
INFO	Application start/exit, successful add, successful status update.
WARNING	Recoverable bad user input, unsupported menu choice, blank text, invalid status, missing application number.
ERROR	Unexpected operation failure that prevents completion.
CRITICAL	Not required. Be able to explain why this small CLI has no normal CRITICAL event.
9. Expected vs Unexpected Failures
Category	Required treatment
Expected / recoverable	Non-integer menu choice; unsupported menu option; blank company/role; invalid status; nonexistent application number.
Expected response	Specific handler → friendly print → WARNING log → menu continues.
Unexpected	Programming defect or runtime condition outside the known domain rules.
Unexpected response	logger.exception(...) with traceback at outer boundary → short user message → re-raise / fail visibly.
10. Required Manual Scenarios
1.	Start the program: INFO log records startup.
2.	Enter letters where the menu expects an integer: program does not crash.
3.	Enter an unsupported menu number such as 99: warning + friendly message; menu continues.
4.	Try to add a blank company: no object is added.
5.	Try to add a blank role: no object is added.
6.	Add a valid application: tracker count/state changes and INFO log is written.
7.	List applications: numbering begins at 1 and state is readable.
8.	Update a valid application to INTERVIEW with mixed case/spaces: stored state becomes normalized.
9.	Try an invalid status: ValueError path is handled and previous status remains unchanged.
10.	Request an application number that does not exist: ApplicationNotFoundError path is handled separately.
11.	Trigger or temporarily simulate one unexpected exception during development: logger.exception records traceback information.
12.	Exit normally: INFO log records shutdown.
Success standard
Do not count a scenario as passed merely because the program printed something. Verify state: invalid operations must leave the tracker and JobApplication objects unchanged.
11. README Requirements
•	Project purpose and four CLI features.
•	How to run: python3 -m job_tracker.main.
•	One short failure-flow explanation: where a failure is detected, raised, propagated, caught, logged, and shown to the user.
•	Why ApplicationNotFoundError is custom while invalid status uses ValueError.
•	Why validation happens before mutation.
•	Why print() and logging have different responsibilities.
•	Why finally and CRITICAL are not forced into this project.
12. Definition of Done
•	☐ CLI runs until the user explicitly exits.
•	☐ Valid add/update/list operations work.
•	☐ Recoverable user mistakes do not terminate the program.
•	☐ JobApplication always preserves a valid status invariant.
•	☐ Invalid status change leaves previous status untouched.
•	☐ JobTracker delegates status mutation to JobApplication.
•	☐ ApplicationNotFoundError is raised from tracker logic and handled at the CLI boundary.
•	☐ Expected exceptions are handled with specific handlers.
•	☐ No exception is silently swallowed.
•	☐ A broad unexpected-error handler exists only at the outermost boundary, if used.
•	☐ Unexpected failures retain traceback information via logger.exception.
•	☐ INFO/WARNING/ERROR usage is semantically reasonable; one useful DEBUG event exists.
•	☐ User-facing print output is separate from developer/operator logs.
•	☐ All 12 manual scenarios have been exercised.
•	☐ README explains the failure path and the design decisions.
•	☐ No later-roadmap technology has been added.
13. Recommended Build Order + One-Day Timebox
Build sequence: follow these steps in order. The sequence tells you what to build next, not how to implement it.
1.  Create the package/files and confirm the project starts from the intended entry point.
2.  Build JobApplication first: construction validation, allowed-status invariant, and change_status() with validate-before-mutate behavior.
3.  Define ApplicationNotFoundError as the single required custom domain exception.
4.  Build JobTracker: add, list, retrieve by 1-based application number, and update status by delegating to JobApplication.
5.  Before building the CLI, manually trigger the domain/tracker failure paths and confirm exceptions propagate rather than being swallowed.
6.  Build the four-option CLI loop: Add, Update Status, List, Exit.
7.  Add narrow, specific exception handlers at the CLI boundary so expected failures produce friendly messages and the menu continues.
8.  Configure logging and add semantically appropriate DEBUG, INFO, WARNING, and unexpected-failure traceback logging.
9.  Run all required manual scenarios and verify state after every failed operation, not just printed output.
10.  Write the README, complete the Confidence Gate without notes, inspect Git status, and commit only the intended project files.
Time	Focus
0–30 min	Create package/files; build JobApplication and its invariant.
30–75 min	Build JobTracker + ApplicationNotFoundError; verify failure contracts.
75–150 min	Build the four-option CLI and expected exception handlers.
150–210 min	Configure logging; add INFO/WARNING/DEBUG and unexpected traceback logging.
210–270 min	Run every manual scenario; fix state-corruption or exception-boundary mistakes.
270–300 min	Write concise README, explain failure flow aloud, final Git check/commit.
Timebox rule: The build order is intentionally high-level and contains no implementation solution. Five hours is a target, not a deadline. If debugging takes longer, continue until you can explain the failure flow confidently.
14. Confidence Gate - Explain Without Notes
1.  What is the difference between raising an exception and catching one?
2.  Why should JobApplication validate a new status before assigning it?
3.  Why does ApplicationNotFoundError belong in tracker/domain logic rather than main.py?
4.  Why should that exception propagate to the CLI instead of being caught immediately inside JobTracker?
5.  What is the practical reason for specific exception handlers before broader handlers?
6.  When does a try/except else block run, and when is it useful?
7.  What guarantee does finally provide, and why is it not automatically required here?
8.  What is the difference between logging.warning(), logging.error(), and logger.exception()?
9.  Why are print() and logging not interchangeable in this CLI?
10.  If an unexpected bug occurs, why is catching Exception and pretending the program recovered dangerous?
11.  How does a custom exception improve the behavioral contract of get_application()?
12.  Trace one invalid-status request from user input all the way back to the next menu prompt.
Project complete when
You can run the CLI, deliberately trigger each expected failure, predict which exception is raised, identify where it is caught, explain what gets logged, prove valid state was preserved, and answer the confidence-gate questions without a tutorial.
15. Scope Boundaries - Do Not Add Yet
•	JSON or application-data file persistence
•	HTTP/API calls
•	SQLite/PostgreSQL
•	pytest or mocking
•	FastAPI
•	argparse
•	GUI
•	advanced logging handlers/rotation/structured logs
•	LLM APIs, RAG, agents, deployment
Final engineering intent: This is not a feature project. It is a reliability project. Keep the domain small enough that you can see every failure path end-to-end and reason about it with confidence.

from job_application import JobApplication


#Test1 - Valid construction
job = JobApplication("OpenAI", "AI Engineer")

assert job.company == "OpenAI"
assert job.role == "AI Engineer"
assert job.status == "applied"
assert job.notes == []

#Test2 - Company whitespace is normalized

job = JobApplication("  OpenAI ", "AI Engineer")

assert job.company == "OpenAI"

#Test3 - Role whitespace is normalized

job = JobApplication("OpenAI", " AI Engineer  ")

assert job.role == "AI Engineer"

#Test4 - Default status is "applied"

job = JobApplication("Facebook","Software Engineer")

assert job.status == "applied"

#Test5 - 	A custom valid status works.

job = JobApplication("Facebook","Software Engineer","interview")

assert job.status == "interview"

#Test6 - Blank company raises ValueError

try:
    JobApplication("", "Software Engineer")
    assert False, "Expected ValueError for blank company."

except ValueError:
    pass


#Test 7 -  Blank role raises ValueError

try:
    JobApplication("Facebook","")
    assert False, "Expected ValueError for blank role."

except ValueError:
    pass


# 8.	Invalid status raises ValueError.

try:
    JobApplication("Facebook", "Software Engineer","not interested")
    assert False, "Expected ValueError for invalid status."

except ValueError:
    pass



# 9.	change_status() accepts a valid status.

job = JobApplication("Facebook","Software Engineer")

job.change_status("interview")

assert job.status == "interview"



# 10.	change_status() rejects an invalid status.

job = JobApplication("Facebook","Software Engineer")

try:
    job.change_status("not_interested")
    assert False, "Expected ValueError for invalid status."

except ValueError:
    pass



# 11.	add_note() stores a normalized note.

job = JobApplication("Facebook","Software Engineer")

job.add_note(" Applied walk-in ")

assert job.notes == ["Applied walk-in"]

# 12.	Blank note raises ValueError.

job = JobApplication("Facebook","Software Engineer")

try:
    job.add_note("")
    assert False, "Expected ValueError for blank note."

except ValueError:
    pass
    

# 13.	Two instances have independent notes lists.

job1 = JobApplication("Facebook","Software Engineer")
job2 = JobApplication("Apple","Software Engineer")

job1.add_note("I am the CEO.")

assert job1.notes == ['I am the CEO.']
assert job2.notes == []


# 14.	repr(job) provides a useful dataclass representation.

job = JobApplication("Facebook","Software Engineer")

assert repr(job) == "JobApplication(company='Facebook', role='Software Engineer', status='applied', notes=[])"



# 15.	Generated equality behavior is tested and explained.

job1 = JobApplication("Facebook","Software Engineer")
job2 = JobApplication("Facebook","Software Engineer")

assert job1 == job2

job2.add_note("Who is the CEO")

assert job1 != job2




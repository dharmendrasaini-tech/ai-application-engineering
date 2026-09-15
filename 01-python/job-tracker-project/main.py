from job_tracker import JobApplication, JobTracker

def main() -> None:
    tracker = JobTracker()

    job1 = JobApplication(company="microsoft", role= "designer",status="applied")
    job2 = JobApplication(company="apple", role= "swe", status="interview")
    job3 = JobApplication(company="cred", role= "ceo", status="rejected")
    job4 = JobApplication(company="phonepe", role= "ceo",status="applied")

    tracker.add_application(job1)
    tracker.add_application(job2)
    tracker.add_application(job3)
    tracker.add_application(job4)

    job1.change_status("rejected")
    job2.add_note("Candidate not worthy.")

    print(job1.get_summary())

    print(tracker.total_applications())

    print(tracker.get_status_counts())




    








if __name__ == "__main__":
    main()











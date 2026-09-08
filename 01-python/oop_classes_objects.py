# Sep 5 — 5 Class & Object Exercises

# Do these without inheritance, composition, polymorphism, dataclasses, or advanced dunder methods. Stay strictly inside Part 1.

# Exercise 1 — Student
# Goal

# Practice:

# class creation
# __init__
# instance attributes
# independent object state
# simple mutation
# Requirements

# Create a class:

# Student

# Each student must have:

# name
# score
# Methods
# add_score(points)

# Rules:

# points must be positive.
# If points <= 0, raise ValueError.
# Otherwise add the points to the student's score.
# get_summary()

# Returns:

# "<name>: <score>"
# Test scenario

# Create:

# s1 = Student("A", 50)
# s2 = Student("B", 70)

# Then:

# s1.add_score(10)

# Verify that:

# s1.score → 60
# s2.score → 70
# Engineering concept

# Explain in a comment:

# Why does mutating s1.score not affect s2.score?


class Student:

    def __init__(self,name,score):
        self.name = name
        self.score = score


    def add_score(self,points):

        if points <= 0:
            raise ValueError("Points must be positive.")

        self.score += points


    def get_summary(self):
        return f"{self.name} : {self.score}"

        

s1 = Student("A",50)
s2 = Student("B",70)

s1.add_score(10)

print(s1.get_summary())
print(s2.get_summary())

# Mutating s1.score does not affect s2.score because s1 and s2 are two seperate instances of class Student and they have their seperate object attributes.




# Exercise 2 — Book
# Goal

# Practice:

# parameters vs instance attributes
# class-controlled initial state
# read methods vs mutation methods
# invariants
# Requirements

# Create:

# Book

# Each book must have:

# title
# author
# pages
# current_page

# The caller provides:

# title
# author
# pages

# But every new book must automatically start with:

# current_page = 0
# Methods
# read(pages_to_read)

# Rules:

# value must be positive
# cannot read beyond the total number of pages
# invalid operations raise ValueError
# validate before mutation
# pages_remaining()

# Returns:

# pages - current_page

# This method must not mutate state.

# Example
# book = Book("Python", "Author A", 300)

# book.read(50)

# Expected state:

# current_page = 50
# pages_remaining() = 250
# Engineering concept

# Add a comment explaining:

# read() → command/mutation
# pages_remaining() → query/read

class Book:

    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages

        self.current_page = 0


    def read(self,pages_to_read):

        if pages_to_read <= 0:
            raise ValueError("Value must be positive.")

        if self.current_page + pages_to_read > self.pages:
            raise ValueError("Cannot read beyound the total number of pages.")
        
        self.pages_to_read = pages_to_read

        self.current_page += self.pages_to_read


    def pages_remaining(self):
        return self.pages - self.current_page


book = Book("Python", "Author A", 300)

book.read(50)


print(book.current_page)
print(book.pages_remaining())


# read() - read() first validates the objects buiness validation rules and then mutates the object state

# pages_remaining() - it just reads the object state and answers pages remaining
    



# Exercise 3 — BankAccount
# Goal

# Practice:

# encapsulation
# validation
# invariants
# controlled mutation
# Requirements

# Create:

# BankAccount

# Instance attributes:

# owner
# balance
# Methods
# deposit(amount)

# Rules:

# amount must be positive
# otherwise raise ValueError
# withdraw(amount)

# Rules:

# amount must be positive
# amount cannot exceed balance
# otherwise raise ValueError
# balance must never become negative
# get_balance()

# Returns the current balance without modifying anything.

# Test cases

# Test at least:

# deposit valid amount
# deposit 0
# deposit negative amount

# withdraw valid amount
# withdraw too much
# withdraw negative amount
# Important invariant

# Your class should preserve:

# balance >= 0
# Engineering question

# Write a short comment answering:

# Why is account.withdraw(500) safer than directly writing account.balance -= 500 throughout a program?

class BankAccount():
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance


    def deposit_amount(self,amount):

        if amount <= 0:
            raise ValueError("Amount must be positive.")

        self.balance += amount

    def withdraw_amount(self,amount):

        if amount <= 0:
            raise ValueError("Amount must be positive.")

        if amount > self.balance:
            raise ValueError("Insufficient balance.")


        self.balance -= amount


    def get_balance(self):
        return self.balance



account1 = BankAccount("dharm",1000)
account1.deposit_amount(500)
account1.deposit_amount(0)
account1.deposit_amount(-100)

print(account1.get_balance())


account1.withdraw_amount(500)
account1.withdraw_amount(10000)
account1.withdraw_amount(-12324)

print(account1.get_balance())




# Exercise 4 — Player
# Goal

# Practice:

# class attributes
# instance attributes
# attribute lookup
# shadowing
# mutable instance state
# Requirements

# Create:

# Player

# Class attribute:

# game = "Chess"

# Instance attributes:

# name
# score
# badges

# Each new player must get its own:

# badges = []
# Methods
# add_score(points)

# Positive points only.

# add_badge(badge)

# Adds a badge to that player's list.

# get_summary()

# Returns something like:

# A | Chess | Score: 20 | Badges: 2
# Test this behavior
# p1 = Player("A", 10)
# p2 = Player("B", 20)

# p1.add_badge("Winner")
# p1.game = "Football"

# Verify:

# p1.game → Football
# p2.game → Chess

# p1.badges → ["Winner"]
# p2.badges → []
# Engineering comments

# Explain both:

# Why p1.game does not modify Player.game

# and:

# Why badges belongs in __init__ instead of being a mutable class attribute


class Player():

    game = "Chess"

    def __init__(self,name,score):
        self.name = name
        self.score = score
        self.badges = []

    def add_score(self,points):

        if points <= 0:
            raise ValueError("Positive points only.")

        self.score += points

    def add_badge(self,badge):

        self.badges.append(badge)

    def get_summary(self):

        return f"{self.name} | {self.game} | Score: {self.score} | Badges: {len(self.badges)}"


p1 = Player("A",10)
p2 = Player("B",20)

p1.add_badge("Winner")
p1.game = "Football"

print(p1.game)
print(p2.game)
print(p1.badges)
print(p2.badges)


# Why p1.game does not modify Player.game

#Because p1.game is seperate instance attribute and Player.game is class attribute . In attribute lookup instance attribute shadows class attribute 


# Why badges belongs in __init__ instead of being a mutable class attribute

# Because if it is a mutuable class attribute then it will be referred by all the instances . if defined in init__ then each instance will have its own mutable instance attribute badges.




# Exercise 5 — Task

# This is the most important one. It combines almost all of Sep 5.

# Goal

# Build a small but clean object with:

# state
# behavior
# validation
# invariants
# mutation
# read-only methods
# class attributes
# clear interface
# Requirements

# Create:

# Task

# Class attribute:

# category = "general"

# Instance attributes:

# title
# priority
# completed

# Initial state:

# completed = False

# The caller provides:

# title
# priority

# Allowed priorities:

# ("low", "medium", "high")
# Initialization rules

# Reject:

# blank title
# unsupported priority

# Use:

# ValueError
# Methods
# mark_complete()

# Changes:

# completed → True
# change_priority(new_priority)

# Validate before mutation.

# Only allow:

# low
# medium
# high
# is_complete()

# Returns the completion state.

# Must not mutate anything.

# get_summary()

# Example result:

# Fix login bug | high | completed=False
# Required tests

# Create at least two tasks.

# Demonstrate that:

# task1 and task2 have independent state

# Then test:

# valid priority change
# invalid priority change
# mark complete
# blank title
# different category through instance shadowing

# For example:

# task1.category = "backend"

# Then reason about:

# task1.category
# task2.category
# Task.category


class Task:
    category = "general"

    def __init__(self,title,priority):

        if not title.strip():
            raise ValueError("Blank Title not allowed.")
        
        self.title = title

        

        if priority not in ("low","medium","high"):
            raise ValueError("Unsupported priority.")


        self.priority = priority


        self.completed = False


    def mark_complete(self):
        self.completed = True

    def change_priority(self,new_priority):

        if new_priority not in ("low","medium","high"):
            raise ValueError("Invalid priority")

        self.priority = new_priority


    def is_complete(self):
        return self.completed


    def get_summary(self):
        return f" {self.title} | {self.priority} | Completed = {self.completed}"


task1 = Task("Bug", "low")
task2 = Task("Upgrade", "high")

task1.completed = True

print(task1.completed)
print(task2.completed)

# I changed completed attribute of task1 it did not change task2 completed attribute hence proved they have independent state

print(task1.change_priority("low"))

print(task1.change_priority("ultra"))

print(task2.mark_complete())

task3 = Task("", "high")

task2.category = "high"





#Variation 2


# Exercise 1 - Student
# Goal: practice class creation, initialization, independent object state, controlled mutation, validation, and a simple read-only summary method.
# •	Class: Student
# •	Instance state: name, score
# •	Method: add_score(points)
# •	Method: get_summary()
# Rules:
# •	name must not be blank after trimming whitespace.
# •	score must not be negative.
# •	add_score(points) accepts only positive points; otherwise raise ValueError.
# •	get_summary() returns: "<name>: <score>".
# Minimum tests: two independent students; valid score increase; zero points; negative points; blank name; negative initial score.
# Design questions before coding
# •	Which attributes are instance attributes?
# •	What invariant should always hold for score?
# •	Does get_summary mutate the object?

class Student:
    def __init__(self,name,score):

        if not name.strip():
            raise ValueError("Name cannot be blank.")
        
        
        self.name = name.strip()

        if score < 0:
            raise ValueError("Score cannot be negative.")
        
        self.score = score

    def add_score(self,points):

        if points <= 0:
            raise ValueError("Points must be positive.")
     
        self.score += points

    def get_summary(self):
        return f"{self.name}:{self.score}"


student1 = Student("Dharm",100)
student2 = Student("Ravi", 99)
student3 = Student("", 23)
student4 = Student("Rohit", -12)

student1.add_score(23)

student2.add_score(0)

student1.add_score(-12)


# Design questions before coding
# •	Which attributes are instance attributes?
# •	What invariant should always hold for score?
# •	Does get_summary mutate the object?




















# Exercise 2 - BankAccount
# Goal: practice state transitions and preserving invariants during mutation.
# •	Class: BankAccount
# •	Instance state: owner, balance
# •	Methods: deposit(amount), withdraw(amount), get_balance()
# Rules:
# •	owner must not be blank.
# •	initial balance must be >= 0.
# •	deposit amount must be positive.
# •	withdraw amount must be positive and cannot exceed the current balance.
# •	Invalid operations must not change the balance.
# Minimum tests: deposit; full-balance withdrawal; over-withdrawal; zero/negative deposit; zero/negative withdrawal; two accounts with independent balances.
# Design questions before coding
# •	What is the balance invariant?
# •	Which checks must happen before balance mutation?
# •	Should get_balance change any state?


class BankAccount:
    def __init__(self,owner,balance):

        if not owner.strip():
            raise ValueError("Ower cannot be blank.")

        if balance < 0:
            raise ValueError("Balance must be positive.")

        
        self.owner = owner.strip()
        self.balance = balance

    def deposit_amount(self,deposit_amount):

        if self.deposit_amount < 0:
            raise ValueError("Deposit_amount must be positive")
        self.balance += deposit_amount

    def withdraw_amount(self,withdraw_amount):

        if withdraw_amount < 0:
            raise ValueError("Withdraw amount must be positive.")

        if withdraw_amount < self.balance:
            raise ValueError("Insufficient balance")


        self.balance -= withdraw_amount

    def get_balance(self):
        return self.balance

                        

owner1 = BankAccount("Ajay",1000)
owner2 = BankAccount("Robin", 2000)


owner1.deposit_amount(1000)

owner2.withdraw_amount(2000)

owner2.withdraw_amount(4000)

owner1.deposit_amount(0)
owner1.deposit_amount(-1)




























# Exercise 3 - Book
# Goal: model progress while protecting a boundary invariant.
# •	Class: Book
# •	Instance state: title, author, pages, current_page
# •	Methods: read(page_count), get_progress()
# Rules:
# •	title and author must not be blank.
# •	pages must be a positive integer.
# •	current_page starts at 0.
# •	read(page_count) requires a positive integer.
# •	current_page must never exceed pages.
# •	Choose and document one policy for reading beyond the final page: reject the operation or cap at the final page. Be consistent.
# •	get_progress() should return useful current progress without mutating the book.
# Minimum tests: new book; partial reading; reading to final page; attempt beyond final page; zero/negative page count; independent books.
# Design questions before coding
# •	Write the current_page invariant as an inequality.
# •	What happens to state when an invalid read is attempted?
# •	Why is your beyond-final-page policy part of the method contract?


class Book:
    def __init__(self,title,author,pages):

        if not title.strip():
            raise ValueError("Title cannot be blank.")

        if not author.strip():
            raise ValueError("Author cannot be blank.")

        
        if not isinstance(pages,int):
            raise ValueError("Pages must be an integer")

        if pages <= 0:
            raise ValueError("Pages must be positive number.")


        self.title = title.strip()
        self.author = author.strip()
        self.pages = pages

        self.current_page = 0


    def read(self,page_count):

        if not isinstance(page_count,int):
            raise ValueError("Page count must be an integer.")

        if page_count <= 0:
            raise ValueError("Page count must be a positive number.")





        #Reject the operation beyond book pages.

        if page_count + self.current_page > self.pages:
            raise ValueError("Total pages exceeded.")

        self.current_page += page_count


    def get_progress(self):

        return self.current_page



book1 = Book("Fountainhead","Ayn Rand",700)
book2 = Book("The Scam", "Sucheta Dalal", 400)
book3 = Book("Rich Dad Poor Dad","Robert Kiyosaki",0)


book1.read(300)
book2.read(400)

book2.read(700)

































# Exercise 4 - Task
# Goal: model a small stateful domain object with a constrained set of values.
# •	Class: Task
# •	Instance state: title, priority, completed
# •	Methods: mark_complete(), change_priority(new_priority), get_summary()
# Rules:
# •	title must not be blank.
# •	priority must be one of: "low", "medium", "high".
# •	completed starts as False.
# •	mark_complete() changes completed to True.
# •	change_priority(new_priority) validates before mutation.
# •	get_summary() reports title, priority, and completion state.
# Minimum tests: valid priorities; unsupported priority at creation; priority change; invalid priority change preserving the old value; completion; two independent tasks.
# Design questions before coding
# •	Which attribute has a class-wide allowed-value policy but per-instance state?
# •	Should mark_complete return anything? State your chosen contract.
# •	How will you prove an invalid priority change does not partially mutate the object?








class Task:

    ALLOWED_PRIORITIES = {"low", "medium", "high"}

    def __init__(self,title,priority):


        if not title.strip():
            raise ValueError("Title cannot be blank.")

        title = title.strip()

        if not priority.strip():
            raise ValueError("Priority cannot be blank.")

        priority = priority.strip()

        if priority not in self.ALLOWED_PRIORITIES:
            raise ValueError("Invalid priority value.")


        self.title = title
        self.priority = priority


        self.completed = False


    def mark_complete(self):
        self.completed = True


    def change_priority(self,new_priority):

        if not new_priority.strip():
            raise ValueError("new_priority cannot be empty.")

        new_priority = new_priority.strip()

        if new_priority not in self.ALLOWED_PRIORITIES:
            raise ValueError("Invalid priority value.")

        self.priority = new_priority

    def get_summary(self):

        return f"Title: {self.title} | Priority: {self.priority} | Completed: {self.completed}"

#mark completed need not return anything

task1 = Task("gym","high")
task2 = Task("college", "low")
task3 = Task("dance", "medium")

task4 = Task("sing","ultra")

task2.change_priority("medium")

task3.change_priority("super ultra")

task2.mark_complete()




        























# Exercise 5 - JobApplication
# Goal: create the first small model that connects directly to the later Job Tracker CLI project.
# •	Class: JobApplication
# •	Instance state: company, role, status
# •	Methods: change_status(new_status), get_summary()
# Rules:
# •	company and role must not be blank.
# •	status defaults to "applied".
# •	Allowed statuses: "applied", "interview", "offer", "rejected".
# •	change_status(new_status) validates before changing status.
# •	get_summary() returns a clear one-line summary.
# Minimum tests: default status; explicit valid status; valid transition; invalid status preserving the previous value; blank company; blank role; multiple independent applications.
# Design questions before coding
# •	Is the set of allowed statuses instance state or a class-level policy?
# •	What invariant must status satisfy?
# •	Which part of this class could later become a dataclass on Day 3, and what behavior would still need explicit methods?


class JobApplication:

    ALLOWED_STATUSES = {"applied", "interview", "offer", "rejected"}

    def __init__(self,company,role):

        if not company.strip():
            raise ValueError("Company cannot be blank.")

        company = company.strip()

        if not role.strip():
            raise ValueError("Role cannot be blank.")

        role = role.strip()

        self.status = "applied"

        
        self.company = company
        self.role = role

        


    def change_status(self,new_status):

        if new_status not in self.ALLOWED_STATUSES:
            raise ValueError("Invalid status")

        self.status = new_status

    def get_summary(self):
        return f"Company: {self.company}, Role: {self.role}, Status: {self.status}"



application1 = JobApplication("OpenAI","CEO","offer")
application2 = JobApplication("Microsoft","CTO")

application1 = JobApplication("","CEO","offer")
application2 = JobApplication("Microsoft","")


application1.change_status("rejected")

application1.change_status("terminated")










    
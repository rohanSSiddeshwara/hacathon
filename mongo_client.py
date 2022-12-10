import pymongo
import json
import os
import pandas as pd


#how to store dictionary in .csv file

resume ={
    "basic_info": {
        "first_name": "G",
        "last_name": "Sai Charan",
        "full_name": "G Sai Charan",
        "email": "gsaicharan152020@gmail.com",
        "phone_number": "9482283105",
        "location": "",
        "portfolio_website_url": "",
        "linkedin_url": "linkedin.com/in/Sai Charan",
        "github_main_page_url": "github.com/PsyCharan17",
        "university": "New Horizon College of Engineering",
        "education_level": "Bachelor of Engineering",
        "graduation_year": "2024",
        "graduation_month": "June",
        "majors": "Artificial Intelligence and ML",
        "GPA": "9.17"
    },
    "work_experience": [
        {
            "job_title": "Secretary",
            "company": "Brainiacs(AIML Technical Club)",
            "location": "NHCE",
            "duration": "Oct 2022- Present",
            "job_summary": "Promoted to the position of Secretary in the Technical Club of AIML department in the college. Responsible for leading a team of board members and ensure smooth conduction of events. Delegating the tasks to be completed by the members as well as guiding junior members with the club processes"
        },
        {
            "job_title": "Board Member",
            "company": "Brainiacs(AIML Technical Club)",
            "location": "NHCE",
            "duration": "Sep 2021- Sep 2022",
            "job_summary": "Conducted several events in the college along with the other core and board members. Promoted the events and managed the registration of participants. Updated the Club website and reported the Event details to the department post every event"
        }
    ],
    "project_experience": [
        {
            "project_name": "Task Manager App",
            "project_discription": "A web app built using MongoDB, Express, ReactJS and NodeJs. Developed a Task Manager web app which can be used by the user to create and keep track of their tasks. Implemented the CRUD functionality using MongoDB NoSQL database. Created Log In and Sign Up functionality to efficiently manage their tasks"
        },
        {
            "project_name": "Crime Analysis and Visualizer",
            "project_discription": "An interactive Webapp dashboard to visualize and understand the geography of various types of crimes reported. Used the Real dataset of crimes reported in Lucknow to perform Data analysis and enable the law the enforcement officials. Plotted various crimes reported on an interactive map and enabled Filters to gain further insights"
        }
    ],
    "skills": [
        {
            "skill_name": "Languages",
            "skill_level": "C++,JavaScript,Python,Java, HTML,CSS"
        },
        {
            "skill_name": "Technologies/Frameworks",
            "skill_level": "React, NodeJS,Express, MongoDB,Pandas,Numpy"
        },
        {
            "skill_name": "Developer Tools",
            "skill_level": "VS Code, Git, Netlify, Streamlit"
        }
    ]
}



class mongo_connector:
    def __init__(self):
        self.client = pymongo.MongoClient("mongodb+srv://admin:admin@cluster0.4gj0znt.mongodb.net/?retryWrites=true&w=majority")
        self.db = self.client["resume"]
        self.collection = self.db["resume"]

    def add_resume(self,resume):
        self.collection.insert_one(resume)

    def get_resume(self):
        return self.collection.find_one()

    #get all the resumes which have any one given skill 
    def get_resume_by_skill(self,skill_name,skill_level):
        return self.collection.find({"skills.skill_name":skill_name,"skills.skill_level":skill_level})
         
        
   
    #given a job description, return all the resumes which have the most matching job requirements
    def get_resume_by_job_description(self,job_description):
        return self.collection.find({"work_experience.job_summary":job_description})

    #given a project description, return all the resumes which have the most matching project requirements
    def get_resume_by_project_description(self,project_description):
        return self.collection.find({"project_experience.project_discription":project_description})


if __name__ == "__main__":
    mongo = mongo_connector()
    mongo.add_resume(resume)
    mongo.get_resume_by_skill("Languages","JavaScript")

   

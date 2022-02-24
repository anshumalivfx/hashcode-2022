import os
import skills
class Contributors:
    contributors = {}
    def __init__(self, N, M, name, number_skills):
        self.number_of_contributors = N
        self.number_pf_projects = M
        self.contributor_name = name
        self.number_of_skills = number_skills
        self.myskills = skills
    
    def addContri(self, filename):
           file = open(filename, 'r')
           for i in file.readlines():
                self.contributors = {}
                self.name, self.number_skills = i.split()
                self.number_skills = int(self.number_skills)
                for j in range(self.number_skills):
                     self.myskills.Skills(skill_name, level)
                     self.level = self.myskills.level
                     self.skill[self.myskills.skill_name] = self.myskills.level
                self.contributors[name] = self.skill
               
           
    def addContributor(self):
        self.number_of_members, self.number_of_projects = N, M
        self.number_of_members = int(self.number_of_members)
        self.number_of_projects = int(self.number_of_projects)
        
        for i in range(self.number_of_members):
            self.skill = {}
            
            self.name, self.number_skills = name, number_skills
            self.number_skills = int(self.number_skills)
            for j in range(self.number_skills):
                self.myskills.Skills(skill_name, level)
                self.level = self.myskills.level
                self.skill[self.myskills.skill_name] = self.myskills.level
            self.contributors[name] = self.skill
        
    
    

        
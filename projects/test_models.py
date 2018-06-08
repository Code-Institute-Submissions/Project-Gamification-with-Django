from django.test import TestCase
from .models import *
from django.contrib.auth.models import User

class TestProjectModel(TestCase):

    def create_project(self, name="Create a Test"):
        user = User.objects.create_user(username='username', password='password')
        return Project.objects.create(name=name,
                                      proposed_by = user)
                                      
    def test_create_project(self):
        a = self.create_project()
        self.assertTrue(isinstance(a, Project))

    def test_project_status_defaults_to_proposed(self):
        user = User.objects.create_user(username='username', password='password')
        self.client.login(username='username', password='password')
        project = Project(name="Create a Test", proposed_by = user)
        project.save()
        self.assertEqual(project.name, "Create a Test")
        self.assertEqual(project.status, "proposed")
        
    def test_project_as_a_string(self):
        user = User.objects.create_user(username='username', password='password')
        self.client.login(username='username', password='password')
        project = Project(name="Create a Test", proposed_by = user)
        self.assertEqual("Create a Test", str(project) )
        
        
class TestIssueModel(TestCase):        
    
    def create_issue(self, name="Create a Test", description = "Test"):
        user = User.objects.create_user(username='username', password='password')
        project = Project(name="Create a Test", proposed_by = user)
        project.save()
        
        return Issue.objects.create(name=name,
                                    description = description,
                                    project = project,
                                    assigned_to = user)
                                    
    def test_create_issue(self):
        a = self.create_issue()
        self.assertTrue(isinstance(a, Issue))                               
    
    def test_issue_cost_defaults_to_proposed(self):
        a = self.create_issue()
        self.assertEqual(a.cost, 0)
        self.assertEqual(a.project.name, "Create a Test")    
        
    def test_project_as_a_string(self):
        a = self.create_issue()
        self.assertEqual("Create a Test", str(a.project) )    
        
        
class TestRequiredSkillsModel(TestCase):  
    
    def create_requiredskills(self):
        user = User.objects.create_user(username='username', password='password')
        project = Project(name="Create a Test", proposed_by = user)
        project.save()
        return RequiredSkills.objects.create(project=project)
         
    def test_create_requiredskills(self):
        a = self.create_requiredskills()
        self.assertTrue(isinstance(a, RequiredSkills))    
        
    def test_html_defaults_to_zero(self):
        a = self.create_requiredskills()
        self.assertEqual(a.html, 0)
        
    def test_requiredskills_as_a_string(self):
        a = self.create_requiredskills()
        self.assertEqual("Create a Test", str(a.project))       
        
class TestCommitSkillModel(TestCase): 
    
    def create_commitskill(self):
        user = User.objects.create_user(username='username', password='password')
        project = Project(name="Create a Test", proposed_by = user)
        project.save()
        return CommitSkill.objects.create(project=project, user=user)
        
    def test_create_commitskill(self):
        a = self.create_commitskill()
        self.assertTrue(isinstance(a, CommitSkill))        
        
    def test_skill_defaults_to_html(self):
        a = self.create_commitskill()
        self.assertEqual(a.skill, 'html') 
        
class TestProjectMessageModel(TestCase):      
    
    def create_projectmessage(self):
        user = User.objects.create_user(username='username', password='password')
        project = Project(name="Create a Test", proposed_by = user)
        project.save()
        return ProjectMessage(project=project, message = "test")
        
    def test_create_projectmessage(self):
        a = self.create_projectmessage()
        self.assertTrue(isinstance(a, ProjectMessage))     
        
    def test_projectmessage_as_a_string(self):
        a = self.create_projectmessage()
        self.assertEqual("Create a Test", str(a.project))      


class TestGamificationAdvice(TestCase):

    def create_advice(self, name="test", advice="test"):
        return GamificationAdvice(name=name, advice = advice)        
        
    def test_create_advice(self):
        a = self.create_advice()
        self.assertTrue(isinstance(a, GamificationAdvice)) 

    def test_create_advice_as_a_string(self):
        a = self.create_advice()
        self.assertEqual("test", str(a))           
        
        
        
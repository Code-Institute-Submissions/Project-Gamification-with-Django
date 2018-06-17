# PROJECT GAMIFICATION DASHBOARD

#### LINK:
https://github.com/

#### TLDR:
Project management Dashboard made with Django. Register new profile or use one of existing ones (password for all of them: adminadmin). Explore & Enjoy!


## PROJECT CASE

*“I want to implement gamification in my workplace.”* 

While having this kind of idea on a management level 10 years ago could get ridiculed almost instantly, in today's software project environment gamification rewards companies with a greater employee involvement and productivity. 

This Project is a simulation of work environment, where more traditional agile techniques are blended with key gamification concepts of "reward" and "role".

## PROJECT REQUIREMENTS:

1. The project must be a brand new Django project, composed of multiple apps
2. The project should include an authentication mechanism, allowing a user to register and log in
3. At least one of your Django apps should contain some e-commerce functionality using Stripe
4. Include at least one form with validation that will allow users to create and edit models in the backend (in addition to the authentication mechanism).
5. The project will need to connect to a database (e.g., sqlite or Postgres) using Django’s ORM
6. The UI should be responsive, use either media queries or a responsive framework such as Bootstrap to make sure that the site looks well on all commonly-used devices.
7. As well as having a responsive UI, the app should have a great user experience.
8. The frontend should contain some JavaScript logic to enhance the user experience.

## MAIN CONCEPTS:

#### PROJECT ROLES:

![roles](https://user-images.githubusercontent.com/26208598/41512090-40f3a3c8-727b-11e8-9ed4-dfd7f0c13d5a.JPG)


#### PLAYER TYPES:

![playertypes](https://user-images.githubusercontent.com/26208598/41512114-96dca320-727b-11e8-88a1-c24960f9b8b1.JPG)

#### PROJEC TEAM TYPES:

![teamtypes](https://user-images.githubusercontent.com/26208598/41512116-a100590a-727b-11e8-83b9-118ace92f85a.JPG)

#### REWARDS:

![rewardsy](https://user-images.githubusercontent.com/26208598/41512129-f4d0f990-727b-11e8-8038-f7a01565377d.JPG)

#### KANBAN: 

![kanban](https://user-images.githubusercontent.com/26208598/41512132-ff04108c-727b-11e8-8455-22e1e9ed5a0d.JPG)

## APP STRUCTURE

#### Login View with two forms:

![login](https://user-images.githubusercontent.com/26208598/41512134-0a356adc-727c-11e8-9002-fac32073edc2.JPG)

1. Login Form
2. Registry Form 
3. While user's log out, side menu is not active


#### Kanban Dashboard:

![dashboard](https://user-images.githubusercontent.com/26208598/41512135-147f2082-727c-11e8-88e7-663e293e60d1.JPG)

1. Dropdown menu
2. Project search bar 
3. Standard navbar functions
4. Status Card - provides information about project status and current project count
5. Project Card - provides project details - title, PM photo & description
6. Enter Button - leads to Project Details page
7. On Hold (ADMIN ONLY) - projects that current status is "on hold"


#### Project Details(Status "PROPOSED") - Coder Perspective:

![coderdetails](https://user-images.githubusercontent.com/26208598/41512144-5338c774-727c-11e8-99eb-db13ecf59120.JPG)

1. Team Requirements Card  - allows Coder to apply for a team
2. & 3. - Join/Leave Team buttons


#### Project Details(Status "non-PROPOSED") - Coder Perspective:

![coderview2](https://user-images.githubusercontent.com/26208598/41512146-5f1536d6-727c-11e8-8e96-7fa6e1d8ef8f.JPG)

1. Current Project Team - separated by skill provided
2. Current Project Bugs & Issue - with an issue details and offered reward 
3. Assign to Me button - Assign issue to the Coder


#### Project Details(Status "PROPOSED") - PM Perspective:

![pmdetails](https://user-images.githubusercontent.com/26208598/41512150-6e4d53d6-727c-11e8-8e83-153b5f682774.JPG)

1. Define Skillset - Allows PM to define what kind of skillset Project requires
2. Team Requirements Card - detailed information regarding current skill coverage applications
3. X - allows PM to reject applicant
4. Team Analysis Button - brings up Team Analysis Modal 
5. Project Description Card- project description provided by PM
6. Project Plan Card - project schedule 


#### Project Details(Status "non-PROPOSED") - PM Perspective:

![1](https://user-images.githubusercontent.com/26208598/41512232-43aaf27c-727d-11e8-8396-635e838f904d.JPG)

1. Side Bar Menu - navigation shortcuts
2. Projec Details Card - information regarding current budget status, project state & project team
3. Team Analysis Button - brings up Team Analysis Modal
4. Current Project Bugs & Issue - with an issue details and offered reward  
5. Raise an Issue Button - allows PM to raise an project issue and offer reward
6. Project Log - list of automatically generated project messages (issue fix, status change etc..)


#### Project Details - Admin Perspective:

![2](https://user-images.githubusercontent.com/26208598/41512239-4e734b32-727d-11e8-84b6-b714672c00b8.JPG)

1. Project Status button(ADMIN ONLY) - allows Program Manager(admin) to launch/advance/complete project (depends on project status)



#### Team Analysis Modal: 

![3](https://user-images.githubusercontent.com/26208598/41512244-561a55a6-727d-11e8-9f1a-a3e29cdd8c5f.JPG)

1. Team Breakdown Chart - chartjs doughnut. Gives a personalities breakdown of currently applied Coder
2. Team Type - after analyzing personalities blend, algorithm provides matching team preset
3. Team Type Characteristics - some advice for PM to take in account when constructing a team.<br>
<br>
*View doesn't provide detailed information regarding Coder's personalities, so PM cannot discriminate any personalities group. "Team Analytics" provides just an advice and it's not determining fate of a Project.*


#### User Profile - New User Perspective:

![4](https://user-images.githubusercontent.com/26208598/41512246-60485e7e-727d-11e8-85c6-429c233a3624.JPG)

1. User Card - generic portrait along with generic profile details
2. Edit Button - allows User to provide information
3. Take Test - which player type are you?
4. Gamification Test - based on Bartle player taxonomy:
https://en.wikipedia.org/wiki/Bartle_taxonomy_of_player_types

#### User Profile - PM Perspective:

![5](https://user-images.githubusercontent.com/26208598/41512250-65f9c470-727d-11e8-8d10-abbd2451e4c6.JPG)

1. User Card - photo and information provided by user, along with current leancoin wallet
2. My Projects Card - Project currently managed by PM
3. New Project Button - if wallet > 450lc button allows to propose a new project
4. Support Charity - allows user to donate some money to the good cause

#### User Profile - Coder Perspective:

![6](https://user-images.githubusercontent.com/26208598/41512253-6bb4572c-727d-11e8-9dca-fa60ed925235.JPG)

1. Joined Teams Card - Project currently joined by Coder
2. Assigned Issue - Issues currently being fixed by Coder
3. Fixed Button - report issue being fixed. Automatically adds reward to the Coder's wallet


#### Charities View:

![7](https://user-images.githubusercontent.com/26208598/41512254-70191276-727d-11e8-9f63-32e46ba8f822.JPG)

1. New Charity(VISIBLE TO ADMIN ONLY) - allows Program Manager to propose new charities every month
2. Charity Card - provides information regarding charity cause 
3. Donate Button - allows User to donate money
4. Remove Button(VISIBLE TO ADMIN ONLY) - allows Program Manager to remove old charities every month


#### My Donations View:

![8](https://user-images.githubusercontent.com/26208598/41512256-7acdcd4c-727d-11e8-8dea-a374061a52a5.JPG)

1. Remove Button - removes charity donation before proceeding to payment
2. Proceed Button - Proceed to payment view

#### Donation Payment View:

![9](https://user-images.githubusercontent.com/26208598/41512257-7fea8766-727d-11e8-8f70-3ebff96f0867.JPG)

1. List of chosen donations
2. Stripe Payment form

#### Various Forms:

![10](https://user-images.githubusercontent.com/26208598/41512259-86052e44-727d-11e8-9789-0c709e1a35ee.JPG)

#### Admin View:

![11](https://user-images.githubusercontent.com/26208598/41512260-8d212598-727d-11e8-9ef2-0467f1b6d763.JPG)

## TEST SUITE


### Travis CI:

(swap settings and disable env in settings.py in order to pass integration test)<br>
[![Build Status](https://travis-ci.org/LukaszMalucha/Project-Gamification-with-Django.svg?branch=master)](https://travis-ci.org/LukaszMalucha/Project-Gamification-with-Django)
<br>
![travis](https://user-images.githubusercontent.com/26208598/41512542-c7a7a832-7281-11e8-93dc-bee6360a536f.JPG)

### Test Files:

* */test_forms.py
* */test_views.py
* */test_models.py 

### Manual Tests:

#### Login/Signin Form Test:

*  Is data properly saved in database?
*  Are different templates properly routing to signup and login urls
*  Are form fields values properly validated (example: email field)

#### Main Dashboard:

*  Is database populating dashboard/cards correctly?
*  Button functionality (edit/delete/download/routing)
*  Github repo projects displaying properly. Repos searchability

#### Add template/Edit template:

* Fields properly connected to the database
* Forms are populating database correctly
* Accepted input file
* Missing input test

#### App Responsivity:

* Done with Inspect element tool as a last part of the test suite


## TOOLS, MODULES & TECHNIQUES

#### Python – web development:

Django 

#### Database Development:

MySQL

#### Web Development:

HTML | CSS | Bootstrap | Materialize | JavaScript | JQuery | ChartJS


## CREDITS & INSPIRATIONS

#### Login/Register form: 

Danny Santos:

https://codepen.io/THEORLAN2/pen/MyedKo

#### Error 404 template:

Robin Selmer:

https://codepen.io/robinselmer/pen/vJjbOZ

#### Team Members Portraits:

https://www.pexels.com

<br>

Thank you,

Lukasz Malucha 














